# 全体管理 2004/01/20 由來

CheckUserPass();
OutError("") if !$MASTER_USER;

$NOMENU=1;
$Q{bk}="none";

if($Q{log})
{
	GetLog();
	OutSkin();
}
elsif($Q{mode} eq "delitem")
{
	$num=CheckCount($Q{num1},$Q{num2},0,$MAX_MONEY);
	OutError('消去するアイテムを指定してください。') if !$num;

	Lock();
	DataRead();
	foreach my $DT (@DT)
	{
	$DT->{item}[$num-1]="";
		for(my $cnt=0; $cnt<$DT->{showcasecount}; $cnt++)
		{
		$DT->{showcase}[$cnt]=0 if ($DT->{showcase}[$cnt] == $num);
		}
	delete $DT->{exp}{$num};
	delete $DT->{itemtoday}{$num};
	delete $DT->{itemyesterday}{$num};
	}
	DataWrite();
	DataCommitOrAbort();
	UnLock();
	$disp.="アイテムNo.".$num."をプレイデータの中から消去しました。";
	OutSkin();
}
elsif ($Q{ecode})
{
	$Q{tlyear}-=1900 if $Q{tlyear}>=2000;
	$time=0;
	$time=GetTimeLocal($Q{tlsec},$Q{tlmin},$Q{tlhour},$Q{tlday},$Q{tlmon}-1,$Q{tlyear});
	OutError('日付時刻設定が不正です。') if !$time;
	Lock();
	DataRead();
	require (GetPath($ITEM_DIR,"event"));
	my $key=$Q{ecode};
	OutError('正しいイベントコードを指定してください。') if !defined($EVENT{$key});
	$DTevent{$key}=$time;
	DataWrite();
	DataCommitOrAbort();
	UnLock();
	$disp.="イベントコード".$Q{ecode}."を発生させました。";
	OutSkin();
}
else
{
	GetMember();
	OutSkin();
}
1;

sub GetFileList
{
	my($dir,$file)=@_;
	opendir(DIR,$dir);
	my @list=map{$dir."/".$_}sort grep(/$file/ && !/^\.\.?$/,readdir(DIR));
	closedir(DIR);

	return @list;
}

sub GetLog
{
	$disp.=GetTagA("[loglist]","action.cgi?key=admin-sub2&log=.&$USERPASSURL")." ";
	foreach(GetFileList($LOG_DIR,"\\$FILE_EXT\$"))
	{
		/([\w\-]+)$FILE_EXT$/;
		$disp.=GetTagA("[$1 ".GetTime2FormatTime((stat($_))[9]+0,1)."]","action.cgi?key=admin-sub2&log=$1&$USERPASSURL")." ";
	}

	if($Q{log}eq'.')
	{
		$disp.="<hr>上記タブより閲覧したいログを選択してください<br>";
		$disp.="[$LOG_DELETESHOP_FILE] 閉店/移転した店舗のログ<br>";
		$disp.="[$LOG_ERROR_FILE] 各種エラーのログ<br>";
		$disp.="[$LOG_MOVESHOP_FILE] 移転受け入れのログ<br>";
		$disp.="[$LOG_DEBUG_FILE] デバッグログ<br>";
		$disp.="[$LOG_GLOBAL_MSG_FILE] 広域掲示板ログ<br>";
		$disp.="[$LOG_MARK_FILE] マークログ<br>";
		$disp.="<hr>なお、表\示される内容には生のパスワードが含まれる可能\性もありますので、注意してください。";
	}
	else
	{
		open(IN,GetPath($LOG_DIR,$Q{log})) or OutError('存在しません '.$Q{log});
		my @data=reverse(<IN>);
		close(IN);

		my($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
			=GetPage($Q{pg},30,scalar(@data));
		my $pagecontrol=GetPageControl($pageprev,$pagenext,"&log=$Q{log}","pg",$pagemax,$page);

		$disp.="<hr>$Q{log}<br>".$pagecontrol;
		$disp.="<table width=\"100%\">";
		$disp.="<tr><th>time<th>user<th>message<th>script<th>remoteaddr<th>remotehost<th>trueip</tr>";
		my $buf="";
		foreach(@data[$pagestart..$pageend])
		{
			chop;
			if(/^\d+\t/)
			{
				/^(\d+)\t.*\/(.+\.cgi)\t(.*?)\t(.*?)\t(.*?)\t(.*?)\t(.*)$/;
				my $msg=$7;
				if(index($msg,"\t")!=-1)
				{
					$msg=~s/\t/<BR>/g;
				}
				$disp.="<tr><td>".GetTime2FormatTime($1)."<td>$6<td>$msg<td>$2<td>$3<td>$4<td>$5</tr>";
				$disp.="<tr><td colspan=\"20\"><small>$buf</small></tr>" if $buf ne '';
				$buf="";
			}
			else
			{
				$buf="$_<br>$buf";
			}
		}
		$disp.="</table>";
		$disp.="<hr>".$pagecontrol;
	}
}

sub GetMember
{
	DataRead();
	if(open(IN,GetPath("user")))
	{
		while(<IN>)
		{
			chop;
			@_=split(/\t/);
			my $DT=$DT[$id2idx{$_[2]}];
			$DT->{remoteaddr}=$_[4];
			$DT->{last}=$_[3];
			$DT->{ua}=$_[5];
		}
		close(IN);
	}

	$disp.=$TB;
	$disp.=$TR;
	foreach(qw(IP No ID 名前 店名 創業 最終login 資金 ごみ 行動time 人気 売上 支出 平均 棚数 凍結 IP重複許可))
	{
		$disp.=$TD.$_;
	}
	$disp.=$TRE;
	$cnt=1;

	foreach my $DT (@DT)
	{
		$count{$DT->{remoteaddr}}++ if $DT->{remoteaddr};
		open(SESS,"$SESSION_DIR/$DT->{name}.cgi");
		$DT->{clientinfo}=[<SESS>];
		close(SESS);
		shift(@{$DT->{clientinfo}});

		undef %sameAcount;
		undef %sameBcount;
		undef %sameCcount;
		undef %sameDcount;
		%samecount=();
		foreach(@{$DT->{clientinfo}})
		{
			chop;
			last if $_ eq "";
			my($date,$ip,$agent,$referer,$accept)=split(/\t/);
			$sameA{"$ip\t$agent\t$referer\t$accept"}++ if !($samecount{"$ip\t$agent\t$referer\t$accept"}++);
			$sameB{"$ip\t$agent\t$accept"}++           if !($samecount{"$ip\t$agent\t$accept"}++);
			$sameC{"$ip\t$agent"}++                    if !($samecount{"$ip\t$agent"}++);
			$sameD{"$ip"}++                            if !($samecount{"$ip"}++);
		}
	}

	foreach my $DT (@DT)
	{
		$disp.=$TR;

		$disp.=$TD.$DT->{remoteaddr};
		if($Q{host}ne'')
		{
			foreach(split(/!/,$DT->{remoteaddr}))
			{
				$disp.="[".gethostbyaddr(pack("C4",split(/\./)),2)."]";
			}
		}
		$disp.=$TD.$cnt++;
		$disp.=$TD.$DT->{id};
		$disp.=$TD.$DT->{name};
		$disp.=$TD.qq|<a href="#$DT->{id}">$DT->{shopname}</a>|;
		$disp.=$TD.GetTime2FormatTime($DT->{foundation});
		#$disp.=$TD.GetTime2FormatTime($DT->{lastlogin});
		$disp.=$TD.$DT->{last};
		$disp.=$TD.$DT->{money};
		$disp.=$TD.$DT->{trush};
		$disp.=$TD.GetTime2FormatTime($DT->{time});
		$disp.=$TD.$DT->{rank};
		$disp.=$TD.$DT->{saletoday};
		$disp.=$TD.$DT->{paytoday};
		$disp.=$TD.$DT->{profitstock};
		$disp.=$TD.$DT->{showcasecount};
		$disp.=$TD.$DT->{blocklogin};
		$disp.=$TD.($DT->{nocheckip} ? '重複許可':'');
		#$disp.=$TD.$DT->{comment};
		$disp.=$TRE;

		#my $warning=$DT->{ua}."<br>";
		my $warning="";
		undef %sameAcount;
		undef %sameBcount;
		undef %sameCcount;
		undef %sameDcount;
		%samecount=();
		foreach(@{$DT->{clientinfo}})
		{
			last if $_ eq "";
			my($date,$ip,$agent,$referer,$accept)=split(/\t/);
			if($sameA{"$ip\t$agent\t$referer\t$accept"}>1 && !$samecount{"$ip\t$agent\t$referer\t$accept"})
			{
				$warning.="●IP[$ip]&AGENT&ACCEPT&REFERER重複　";
			}
			elsif($sameB{"$ip\t$agent\t$accept"}>1 && !$samecount{"$ip\t$agent\t$accept"})
			{
				$warning.="●IP[$ip]&AGENT&ACCEPT重複　";
			}
			elsif($sameC{"$ip\t$agent"}>1 && !$samecount{"$ip\t$agent"})
			{
				$warning.="●IP[$ip]&AGENT重複　";
			}
			elsif($sameD{"$ip"}>1 && !$samecount{"$ip"})
			{
				$warning.="●IP[$ip]重複　";
			}
			$samecount{"$ip\t$agent\t$referer\t$accept"}++;
			$samecount{"$ip\t$agent\t$accept"}++;
			$samecount{"$ip\t$agent"}++;
			$samecount{"$ip"}++;
		}
		if($count{$DT->{remoteaddr}}>1)
		{
			$warning.="●TRUE IP[$DT->{remoteaddr}]重複　";
		}

		if($warning ne '')
		{
			#$list=~s/\t/<br>/g;
			$disp.=$TR."<td colspan=\"20\"><a href=\"#$DT->{id}\">↑".$warning."</a>";
			$disp.="".$TRE;
		}
		my $list=join("<br>",grep($_ ne "\n",@{$DT->{clientinfo}}));
		$detail.="<pre><hr><a name=\"$DT->{id}\">●$DT->{shopname} $DT->{name}<hr>$list</pre>";
	}
	$disp.=$TBE;
	$disp.=$detail if (!$Q{only});
}

# 簡易timelocal関数（日付=>秒数変換)
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
