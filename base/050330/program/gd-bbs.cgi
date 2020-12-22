# ギルド掲示板 2004/02/28 由來

$NOITEM=1;
DataRead();
CheckUserPass();
RequireFile('inc-gd.cgi');

my $code = $DT->{guild};
$code=$Q{code} if $MASTER_USER;
OutError('使用不可です') if !$code;

$disp.=$TB.$TR.$TD.$image[0].$TD."<SPAN>ギルド受付</SPAN>：こちらは".GetTagImgGuild($DT->{guild});
$disp.="<BIG>".$GUILD{$DT->{guild}}->[$GUILDIDX_name]."</BIG> 作戦室です。<br>";
$disp.="メンバーからの伝言は，こちらです。".$TRE.$TBE;

$LOG_FILE='bbslog-'.$code;
if ($Q{msg})
	{
	RequireFile('inc-gd-bbs.cgi');
	($Q{msg},$errormsg)=WriteGBBS($Q{msg},180);
	}
ReadBoard();

my %printed=();

my($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
	=GetPage($Q{lpg},$RANKING_PAGE_ROWS,scalar(@MESSAGE));

$disp.=<<"STR";
<FORM ACTION="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=hidden NAME=code VALUE="$code">
$errormsg
<INPUT TYPE=TEXT NAME=msg SIZE=50 VALUE="$Q{msg}">
<INPUT TYPE=SUBMIT VALUE="書込">
</FORM>
STR

my $pagecontrol=GetPageControl($pageprev,$pagenext,($MASTER_USER ? "code=$code" : ""),"lpg",$pagemax,$page);
$disp.=$pagecontrol;

$disp.="<BR>";
$disp.=$TB;
foreach(@MESSAGE[$pagestart..$pageend])
{
	chop;
	my($tm,$mode,$town,$to,$msg,$no)=split(/,/);
	my($message,$sname,$name)=split(/\t/,$msg);
	$tm=GetTime2FormatTime($tm);
	if(!$to)
	{
		$sname="★管理者";
	}

$disp.=$TR;
$disp.='<td width=48>'.GetTagImgKao($name,$mode);
$disp.='<td width=580><b>No.'.$no.'</b> <SPAN>'.$sname.'</SPAN> <small>('.$town.') -'.$tm.'</small>';
$disp.='<br>'.$message;
$disp.=$TRE;

}
$disp.=$TBE;

$disp.=$pagecontrol;
$Q{bk}="none",$NOMENU=1 if $MASTER_USER;
OutSkin();
1;


sub ReadBoard
{
	undef @MESSAGE;
	open(IN,GetPath($COMMON_DIR,$LOG_FILE));
	@MESSAGE=<IN>;
	close(IN);
}

