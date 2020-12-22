#店内掲示板

$NOITEM=1;
Lock();
DataRead();
CheckUserPass();
return ('','対象を選択してください<br>') if !$Q{dts};
$i=$id2idx{$Q{dts}};
$DTS=$DT[$i];

return ('','ゲストユーザーの使用は禁止です<br>') if $GUEST_USER;
return ('','対象を選択してください<br>') if !$DTS;

	$disp.=GetMenuTag('subbbs',	'[自店掲示板'.GetTime2FormatTime((stat($SUBDATA_DIR."/$DT->{id}-bbs.cgi"))[9]+0,1).']','&dts='.$DT->{id}.'&'.$USERPASSURL)
		.GetMenuTag('bbslist',	'[店内掲示板一覧]');

	$disp.="<hr width=500 noshade size=1>";

	$disp.="<BIG>●$DTS->{shopname}店内掲示板</BIG><br><br>";

if ($Q{use})
	{
	$DT->{user}->{subbbs}=$Q{use}-1;
	}
elsif ($Q{del})
	{
	DeleteBoard($Q{del});
	}
elsif ($Q{msg})
	{
	($Q{msg},$errormsg)=WriteGBBS($Q{msg},180);
	}

ReadBoard();

my %printed=();

if($DT==$DTS)
	{
$disp.=<<STR;
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=hidden NAME=key VALUE=subbbs>
<INPUT TYPE=hidden NAME=code VALUE="$code">
<INPUT TYPE=hidden NAME=dts VALUE="$Q{dts}">
$USERPASSFORM
<SPAN>掲示板使用設定</SPAN>：
<SELECT NAME=use>
<OPTION value=1>使用しない</OPTION>
<OPTION value=2>使用する</OPTION>
</SELECT> 
<INPUT TYPE=SUBMIT VALUE="変更する">
</FORM>
<hr width=500 noshade size=1>
STR
	}

if(!$DTS->{user}->{subbbs})
{
$disp.="現在この掲示板は使用されていません";
}
else
{
$RANKING_PAGE_ROWS=20;
my($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
	=GetPage($Q{lpg},$RANKING_PAGE_ROWS,scalar(@MESSAGE));

$disp.=<<"STR";
<FORM ACTION="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=hidden NAME=code VALUE="$code">
<INPUT TYPE=hidden NAME=dts VALUE="$Q{dts}">
$errormsg
<INPUT TYPE=TEXT NAME=msg SIZE=50 VALUE="$Q{msg}">
<INPUT TYPE=SUBMIT VALUE="書込">
</FORM>
STR

my $pagecontrol=GetPageControl($pageprev,$pagenext,"","lpg",$pagemax,$page);
$disp.=$pagecontrol;

$disp.="<BR>";
$disp.=$TB;
$disp.=$TR;
$disp.='<td width=48>店長';
$disp.='<td width=580>メッセージ';
$disp.='<td>削除';

$msgno=0;

foreach (@MESSAGE[$pagestart..$pageend])
{
$msgno++;
	chop;
	my($tm,$mode,$to,$msg)=split(/,/);
	my($message,$sname,$name)=split(/\t/,$msg);
	$tm=GetTime2FormatTime($tm);
	if(!$to)
	{
		$sname="★管理者";
	}

$disp.=$TR;
$disp.='<td width=48>'.GetTagImgKao($name,$mode);
$disp.='<td width=580> <SPAN>'.$sname.'</SPAN> <small> -'.$tm.'</small>';
$disp.='<br>'.$message;
	if(($DT==$DTS)||($DT->{id}==$to))
		{
$disp.=<<"STR";
<TD>
<FORM ACTION="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=hidden NAME=code VALUE="$code">
<INPUT TYPE=hidden NAME=dts VALUE="$Q{dts}">
<INPUT TYPE=hidden NAME=del VALUE="$msgno">
<INPUT TYPE=SUBMIT VALUE="削除">
</FORM>
STR
		}
$disp.=$TRE;

}
$disp.=$TBE;

$disp.=$pagecontrol;
}
$Q{bk}="none",$NOMENU=1 if $MASTER_USER;
RenewLog();
DataWrite();
DataCommitOrAbort();
UnLock();
OutSkin();
1;


sub ReadBoard
{
	undef @MESSAGE;
	open(IN,GetPath($SUBDATA_DIR,$DTS->{id}."-bbs"));
	@MESSAGE=<IN>;
	close(IN);
}

sub WriteGBBS
{
	my($msg,$maxlength)=@_;
	return ('','') if !$msg;
	return ($msg,'発言は半角'.$maxlength.'文字(全角'.int($maxlength/2).'文字)までです。現在半角'.length($msg).'文字です。<br>')
		if length($msg)>$maxlength;
	
	require $JCODE_FILE;
	my $msg=CutStr(jcode::sjis($msg,$CHAR_SHIFT_JIS&&'sjis'),$maxlength);
	$msg=~s/&/&amp;/g;
	$msg=~s/>/&gt;/g;
	$msg=~s/</&lt;/g;
	
	my $count=0;
	my $wait=0;
	my $lasttm=0;
	ReadBoard();
	foreach(@MESSAGE)
	{
		my($tm,$mode,$dummy,$id,$msgline)=split(/,/);
		($msgline)=split(/\t/,$msgline);
		next if $DT->{id}!=$id;
		return ('','重複投稿は出来ません。<br>') if $tm>$NOW_TIME-60*15 && $msgline eq $msg;
		$count++,$wait+=3**$count/($NOW_TIME-$tm+1) if $SECURE_MODE_BBS && $count<10;
		$lasttm||=$tm;
	}
	$wait=int($lasttm+$wait-$NOW_TIME);
	return ('','連続投稿は出来ません。あと'.$wait.'秒お待ち下さい。<br>') if $wait>0;
	
	Lock();

	WriteBoard(1,0,$msg."\t"."★管理者"."\t"."★管理者",1) if($MASTER_USER);
	WriteBoard($DT->{icon},$DT->{id},$msg."\t".$DT->{shopname}."\t".$DT->{name},1) unless($MASTER_USER);

	UnLock();

	return ('','');
}

sub WriteBoard
{
	my($mode,$to,$msg,$nolock)=@_;
	my @data=();

	Lock();

	open(IN,GetPath($SUBDATA_DIR,$DTS->{id}."-bbs"));
	@data=<IN>;
	close(IN);
	
	unshift(@data,"$NOW_TIME,$mode,$to,$msg\n");
	$MAX_BBS_MESSAGE=20 if !$MAX_BBS_MESSAGE;
	splice(@data,$MAX_BBS_MESSAGE);

	OpenAndCheck(GetPath($SUBDATA_DIR,$DTS->{id}."-bbs"));
	print OUT @data;
	close(OUT);

	UnLock();
}

sub DeleteBoard
{
	my @data=();
	my($msgno)=@_;
	$msgno--;

	Lock();

	open(IN,GetPath($SUBDATA_DIR,$DTS->{id}."-bbs"));
	@data=<IN>;
	close(IN);

	splice(@data,$msgno,1);

	OpenAndCheck(GetPath($SUBDATA_DIR,$DTS->{id}."-bbs"));
	print OUT @data;
	close(OUT);

	UnLock();
}