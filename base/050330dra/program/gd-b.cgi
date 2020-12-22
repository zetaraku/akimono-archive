# ギルド設立処理 2004/01/20 由來

CoLock();
DataRead();
CheckUserPass();
ReadGuild();
ReadGuildData();
$image[0]=GetTagImgKao("ギルド受付","guild");
$Q{er}='gd-f';

$disp.="<BIG>●ギルド公館</BIG><br><br>";

$Q{url}="http://" if $Q{url} eq "";
$Q{leadt}=$MYDIR;
$Q{leader}=$DT->{id};
@GLIST=(name,shortname,dealrate,feerate,member,comment,appeal,needed,leadt,leader,url);
@MAX=(30,12,4,4,6,30,120,120,10,10,60);
foreach my $i(0..$#GLIST)
	{
	OutError('記入されていない項目があります - '.$GLIST[$i]) if (!$Q{$GLIST[$i]});
	$Q{$GLIST[$i]}=CutStr(jcode::sjis($Q{$GLIST[$i]},$CHAR_SHIFT_JIS&&'sjis'),$MAX[$i]);
	$Q{$GLIST[$i]}=~s/&/&amp;/g;
	$Q{$GLIST[$i]}=~s/>/&gt;/g;
	$Q{$GLIST[$i]}=~s/</&lt;/g;
	}
$Q{url}="" if $Q{url} eq "http://";
OutError('会費率や割引増率に使用できない文字が含まれています') if ($Q{dealrate} =~ /([^0-9])/)||($Q{feerate} =~ /([^0-9])/);
OutError('割引増率は10～500の間の数値で指定してください') if ($Q{dealrate} > 500) || ($Q{dealrate} < 10);
OutError('会費率は10～500の間の数値で指定してください') if ($Q{feerate} > 500) || ($Q{feerate} < 10);
OutError('ギルドコードに使用できない文字が含まれています') if ($Q{code} =~ /([^a-z])/);
OutError('ギルド設立に画像ファイルは必須です') if (!$Q{upfile})&&($Q{mode} ne "edit");

OutError('同じギルドコードがすでに存在しています') if (-e $COMMON_DIR."/".$Q{code}.".pl")&&($Q{mode} ne "edit");

GuildImgUp() if ($Q{upfile});
BuildGuild();
CoUnLock();

if ($Q{mode} ne "edit")
{
	Lock();
	DataRead();
	CheckUserPass();
	$DT->{guild}=$Q{code};
	DataWrite();
	DataCommitOrAbort();
	UnLock();
}

$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
ギルド受付：手続が完了しました。数分後に反映されると思います。<br>
楽しいギルドになっていくといいですね。頑張ってください。
$TRE$TBE
HTML
OutSkin();
1;


sub GuildImgUp
{
	if ($MIMETYPE{upfile} =~ /gif/i)
	{
	my $ImgFile = $COMMON_DIR."/".$Q{code}.".gif";
	my $upfile=$Q{upfile};
	open(OUT,"> $ImgFile");
	binmode(OUT);
	binmode(STDOUT);
	print OUT $upfile;
	close(OUT);
	chmod (0666,$ImgFile);
	}
	else
	{
	OutError('gif画像ファイルではないようです。'.$MIMETYPE{upfile});
	}
}

sub BuildGuild
{
	my @MESSAGE=();
	push(@GLIST, @OtherDir);
	foreach my $i(0..$#GLIST)
		{
		$MESSAGE[$i]=$GLIST[$i]."=".$Q{$GLIST[$i]}."\n";
		}
	OpenAndCheck($COMMON_DIR."/".$Q{code}.".pl");
	print OUT @MESSAGE;
	close(OUT);
}

