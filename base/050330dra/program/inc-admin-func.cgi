# 管理機能下請け 2003/09/25 由來

my $functionname=$Q{mode};
OutError("不正なリクエストです") if !defined(&$functionname);
&$functionname;

sub menteon
{
	if(-d "$DATA_DIR/lock")
		{push(@log,'現在メンテモードです');}
	elsif(mkdir("$DATA_DIR/lock",$DIR_PERMISSION))
		{push(@log,'メンテモードに入りました');}
	else
		{push(@log,'メンテモードに移行できませんでした',$checkdatadir);}
}

sub menteoff
{
	if(!-d "$DATA_DIR/lock")
		{push(@log,'現在メンテモードではありません');}
	elsif(rmdir("$DATA_DIR/lock"))
		{push(@log,'メンテモードを解除しました');}
	else
		{push(@log,'メンテモードの解除に失敗しました',$checkdatadir);}
}

sub errdel
{
	unlink("$DATA_DIR/error.log");
	push(@log,'エラー情報を削除しました。');
}

sub init
{
	CheckLock();
	#各種ディレクトリ＆ダミーindex.html 作成
	foreach my $dir ($COMMON_DIR,$DATA_DIR,$SESSION_DIR,$COTEMP_DIR,$TEMP_DIR,$LOG_DIR,$SUBDATA_DIR,$BACKUP_DIR)
	{
		if(!-d $dir)
		{
			if(mkdir($dir,$DIR_PERMISSION))
				{push(@log,'ディレクトリ '.$dir.' を作成しました');}
			else
			{
				push(@log,'ディレクトリ '.$dir.' は作成出来ませんでした');
				push(@log,' 設定を見直すか、手動で作成してください');
			}
		}
		if(!-e "$dir/index.html")
		{
			if(open(OUT,">$dir/index.html"))
			{
				print OUT "<html></html>";
				close(OUT);
				push(@log,'ディレクトリ '.$dir.' へダミーのindex.htmlを作成しました');
			}
			else
			{
				push(@log,'ディレクトリ '.$dir.' へのダミーindex.html作成に失敗しました');
				push(@log,' ディレクトリ '.$dir.' のパーミッションを見直してください');
			}
		}
	}
	
	#ロックファイル作成
	if(!GetFileList($DATA_DIR,"^$LOCK_FILE"))
	{
		if(open(DATA,">$DATA_DIR/$LOCK_FILE"))
		{
			print DATA 'ロックファイルです。削除してはいけません。';
			close(DATA);
			push(@log,'ロックファイルを作成しました');
		}
		else
		{
			push(@log,'ロックファイルの作成に失敗しました');
		}
	}
	if(!GetFileList($COMMON_DIR,"^$LOCK_FILE"))
	{
		if(open(DATA,">$COMMON_DIR/$LOCK_FILE"))
		{
			print DATA 'ロックファイルです。削除してはいけません。';
			close(DATA);
			push(@log,'共有ロックファイルを作成しました');
		}
		else
		{
			push(@log,'共有ロックファイルの作成に失敗しました');
		}
	}
	
	#タウンデータ作成
	MakeTownFile();
	
	#新規ゲームデータ作成
	if(!-e "$DATA_DIR/$DATA_FILE$FILE_EXT")
	{
		if(open(DATA,">$DATA_DIR/$DATA_FILE$FILE_EXT"))
		{
			print DATA time()."\n500000,100,,0,0:0:0:0:5001:0:5001:0:0:2000:0\n\n\n//\n"; #初期状態
			close(DATA);
			unlink(map{"$DATA_DIR/$_$FILE_EXT"}grep($_ ne $DATA_FILE,@BACKUP_FILES)); #関連ファイルを消去初期化
			push(@log,'ゲームデータを新規作成しました');
		}
		else
			{push(@log,'ゲームデータの新規作成に失敗しました',$checkdatadir);}
	}
	
	#最終更新時刻検査用ファイル作成
	MakeFile("$DATA_DIR/$LASTTIME_FILE$FILE_EXT",'最終更新時刻検査用ファイル','');
	#ギルド定義ファイルベース作成
	MakeFile("$DATA_DIR/$GUILD_FILE$FILE_EXT",'ギルド定義ファイル','1;');
	
	sub MakeFile
	{
		if(!-e $_[0])
		{
			if(open(DATA,">$_[0]"))
			{
				print DATA $_[2];
				close(DATA);
				utime(1,1,$_[0]);
				push(@log,$_[1].'を作成しました');
			}
			else
				{push(@log,$_[1].'作成に失敗しました',$checkdatadir);}
		}
	}
	push(@log,'初期化/修復の必要はありませんでした。') if !scalar(@log);
}

sub delunit
{
	CheckLock();
	delete_dir($DATA_DIR);
	push(@log,'削除すべきデータがありませんでした。') if !scalar(@log);
}

sub piece
{
	CheckLock();
	delete_evt();
	delete_dir($LOG_DIR,1);
	delete_dir($ITEM_DIR,1);
	delete_dir($SESSION_DIR,1);
	delete_dir($TEMP_DIR,1);
	delete_dir($SUBDATA_DIR,1);
	push(@log,'削除すべきデータがありませんでした。') if !scalar(@log);
}

sub mini
{
	CheckLock();
	delete_evt();
	delete_dir($ITEM_DIR,1);
	push(@log,'削除すべきデータがありませんでした。') if !scalar(@log);
}

sub timeedit
{
	CheckLock();
	$Q{tlyear}-=1900 if $Q{tlyear}>=2000;
	$time=0;
	$time=GetTimeLocal($Q{tlsec},$Q{tlmin},$Q{tlhour},$Q{tlday},$Q{tlmon}-1,$Q{tlyear});
	if(!$time) { push(@log,'日付時刻設定が不正です');}
	elsif(open(IN,"$DATA_DIR/$DATA_FILE$FILE_EXT"))
	{
		my @data=<IN>;
		close(IN);
		$data[0]=$time."\n";
		open(OUT,">$DATA_DIR/$DATA_FILE$FILE_EXT");
		print OUT @data;
		close(OUT);
		my($s,$min,$h,$d,$m,$y)=gmtime($time+$TZ_JST);
		my $timestr=sprintf("%04d-%02d-%02d %02d:%02d:%02d",$y+1900,$m+1,$d,$h,$min,$s);
		push(@log,'最終更新時刻を['.$timestr.']に設定しました');
	}
	else
	{
		push(@log,'データファイルを変更出来ませんでした');
	}
}

sub backup
{
	CheckLock();
	#バックアップを現役に復元
	my @files=map{"$_$FILE_EXT"}@BACKUP_FILES;
	my @errorfiles=grep(!-e $_,map{"$Q{backup}/$_"}@files);
	
	if(scalar(@errorfiles))
	{
		push(@log,map{$_.' が存在しませんでした'}@errorfiles);
		push(@log,'バックアップデータが不完全なので処理を中止しました');
	}
	else
	{
		my $time=(stat("$Q{backup}/$DATA_FILE$FILE_EXT"))[9];
		my($s,$min,$h,$d,$m,$y)=gmtime($time+$TZ_JST);
		my $timestr=sprintf("%04d-%02d-%02d %02d:%02d",$y+1900,$m+1,$d,$h,$min);
		
		foreach my $file (@files)
		{
			my $inok=open(IN,"$Q{backup}/$file");
			my $outok=open(OUT,">$DATA_DIR/$file");
			if($inok && $outok)
			{
				my @data=<IN>;
				close(IN);
				if($file eq $DATA_FILE.$FILE_EXT)
				{
					#play.cgiの場合は更新時刻を現在に
					$data[0]=time()."\n";
					push(@log,'最終更新時刻を現在に設定しました');
				}
				if($file eq $LOG_FILE."-s0".$FILE_EXT || $file eq $PERIOD_FILE.$FILE_EXT)
				{
					#period.cgiとlog-s0.cgiの場合はバックアップ復元アナウンスを付加
					unshift(@data,time().",1,0,0,バックアップデータ復元のため[$timestr]時点に戻りました\n");
				}
				print OUT @data;
				close(OUT);
				push(@log,$file.' の復元に成功しました');
			}
			else
			{
				close(IN) if $inok;
				push(@log,$file.' の復元に失敗しました',' 再度処理を行ってください');
			}
		}
	}
}

sub CheckLock
{
	return if -e "./lock" or -e "$DATA_DIR/lock";
	if(mkdir("$DATA_DIR/lock",$DIR_PERMISSION))
		{
		return;
		}
		else
		{
		OutError('この操作はメンテモードでしか行えません','noerror');
		}
}

sub GetTimeLocal {
    my($Sec, $Min, $Hour, $Date, $Mon, $Year) = @_;
    my($sec, $min, $hour, $date, $mon, $year, $day, $yday, $isdst);

    my($cnt) = 0;
    my($Now) = time;
    while($cnt < 20) {
        ($sec, $min, $hour, $date, $mon, $year, $day, $yday, $isdst) = gmtime($Now+$TZ_JST);
        if ($year != $Year) {
            $Now -= ($year - $Year) * 31536000;
        } elsif ($mon != $Mon) {
            $Now -= ($mon - $Mon) * 2592000;
        } elsif ($date != $Date) {
            $Now -= ($date - $Date) * 86400;
        } elsif ($hour != $Hour) {
            $Now -= ($hour - $Hour) * 3600;
        } elsif ($min != $Min) {
            $Now -= ($min - $Min) * 60;
        } elsif ($sec != $Sec) {
            $Now -= ($sec - $Sec);
        } else {
            last;
        }
        $cnt++;
    }
    $Now = 0 if $cnt == 20;

    return $Now;
}

sub delete_evt
{
	if(open(IN,"$DATA_DIR/$DATA_FILE$FILE_EXT"))
	{
	my @data=<IN>;
	close(IN);
	$data[3]="\n";
	open(OUT,">$DATA_DIR/$DATA_FILE$FILE_EXT");
	print OUT @data;
	close(OUT);
	push(@log,$DATA_FILE.$FILE_EXT.'内のイベントデータを削除しました');
	}
	else
	{
	push(@log,' '.$DATA_FILE.$FILE_EXT.'内イベントデータ削除に失敗しました');
	}
}

sub delete_dir
{
	my($dir,$owndelete)=@_;
	
	return if !-d $dir;
	
	opendir(DIR,$dir);
	my @filelist=grep(!/^\.\.?$/,readdir(DIR));
	closedir(DIR);
	foreach my $file (@filelist)
	{
		$file="$dir/$file";
		if(-f $file)
		{
			if(unlink($file))
				{push(@log,$file.' を削除しました');}
			else
				{push(@log,' '.$file.' の削除に失敗しました');}
		}
		delete_dir($file,1) if -d $file;
	}
	if($owndelete)
	{
		if(rmdir($dir))
			{push(@log,'ディレクトリ '.$dir.' を削除しました');}
		else
			{push(@log,' ディレクトリ'.$dir.' の削除に失敗しました');}
	}
}

sub MakeTownFile
{
my $townfile="$COMMON_DIR/towndata$FILE_EXT";
require $townfile if -e $townfile;

return if ($Tname{$MYDIR} eq $TOWN_TITLE);

	if(open(OUT,">".$townfile))
		{
		$Tname{$MYDIR}=$TOWN_TITLE;
		undef @OtherDir;
		@OtherDir=keys(%Tname);
		print OUT '@OtherDir=("',join('","',@OtherDir),'");',"\n";
		foreach(keys(%Tname))
			{
			print OUT '$Tname{',$_,'}="',$Tname{$_},'";',"\n";
			}
			close(OUT);
			push(@log,'街リストを作成しました');
		}
		else
		{
			push(@log,'街リストの作成に失敗しました'.$townfile);
		}
}
1;
