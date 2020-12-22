# 試験成績 2004/01/20 由來
# キャンパスフェスタ独自

DataRead();
CheckUserPass(1);

$disp.=GetMenuTag('mark',	'[総合]')
	.GetMenuTag('mark',	'[英語]','&t=1')
	.GetMenuTag('mark',	'[数学]','&t=2')
	.GetMenuTag('mark',	'[国語]','&t=3');
$disp.="<hr width=500 noshade size=1>";

$disp.='<BIG>●定期試験成績表</BIG>';
my $i;

if ($Q{t}==1) {
$disp.="：英語<br><br>";
$i=20;
} elsif ($Q{t}==2) {
$disp.="：数学<br><br>";
$i=21;
} elsif ($Q{t}==3) {
$disp.="：国語<br><br>";
$i=22;
} else {
$disp.="：総合<br><br>";
foreach(@DT) { $_->{item}[1-1]=$_->{item}[20-1] + $_->{item}[21-1] + $_->{item}[22-1]; }
$i=1;
}
	@DT=sort{$b->{item}[$i-1]<=>$a->{item}[$i-1]}@DT;
$disp.=$TB;
foreach my $n(0,1,2)
	{
next if !$DT[$n]->{id};
$disp.=$TR.$TDNW.$tdh_pt.GetTagImgKao($DT[$n]->{name},$DT[$n]->{icon});
$disp.=$TD."<SPAN>第 ".($n+1)."位</SPAN> ： <b>".$DT[$n]->{shopname}."</b>";
$disp.="<br>".$DT[$n]->{comment};
$disp.=$TD.($DT[$n]->{item}[$i-1])."点";
$disp.=$TRE;
	}
if ($DTusercount>6)
	{
	$disp.=$TR.'<td colspan="3" align="center">・・・';
	$disp.=$TRE;

	foreach my $n(($DTusercount-3),($DTusercount-2),($DTusercount-1))
		{
	$disp.=$TR.$TDNW.$tdh_pt.GetTagImgKao($DT[$n]->{name},$DT[$n]->{icon});
	$disp.=$TD."<SPAN>第 ".($n+1)."位</SPAN> ： <b>".$DT[$n]->{shopname}."</b>";
	$disp.="<br>".$DT[$n]->{comment};
	$disp.=$TD.($DT[$n]->{item}[$i-1])."点";
	$disp.=$TRE;
		}
	}
$disp.=$TBE;
OutSkin();
1;
