# 郵便一覧 2004/01/20 由來

$NOMENU=1;
$Q{bk}="none";
$NOITEM=1;
DataRead();
CheckUserPass();
OutError("") if !$MASTER_USER;

ReadLetterName();
ReadLetter();

$disp.="<BIG>●郵便チェック</BIG><br><br>";

foreach my $i(0..$Lcount)
	{
	my $sname=SearchLetterName($LETTER[$i]->{fromid},$LETTER[$i]->{fromt});
	$sname="(不明)" if $sname eq "-1";
	my $tname=SearchLetterName($LETTER[$i]->{toid},$LETTER[$i]->{tot});
	$tname="(不明)" if $tname eq "-1";
	$disp.="□";
	$disp.=($LETTER[$i]->{mode}==1) ? "<SPAN>未読</SPAN>：" : "既読：";
	$disp.=GetTime2FormatTime($LETTER[$i]->{time})." … from：<span>".$sname."</span>";
	$disp.=" <small>（".$Tname{$LETTER[$i]->{fromt}}."）</small> ";
	$disp.=" … to：<span>".$tname."</span>";
	$disp.=" <small>（".$Tname{$LETTER[$i]->{tot}}."）</small>";
	$disp.="<table width=75%><tr><td>";
	$disp.="「".$LETTER[$i]->{title}."」<BR>";
	$disp.=$LETTER[$i]->{msg}."<BR>";
	$disp.="</td></tr></table><hr width=500 noshade size=1>";
	}

OutSkin();
1;
