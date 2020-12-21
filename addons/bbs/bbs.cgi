# 一言掲示板 2004/01/20 由來

$NOITEM=1;
DataRead();
CheckUserPass();

$disp.="<BIG>●一言掲示板</BIG><br><br>";

$LOG_FILE='bbslog';
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

my $pagecontrol=GetPageControl($pageprev,$pagenext,"","lpg",$pagemax,$page);
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

