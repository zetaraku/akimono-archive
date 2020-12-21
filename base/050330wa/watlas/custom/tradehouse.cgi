# 商館 2005/01/06 由來
# ワールドアトラス版

DataRead();
CheckUserPass(1);
RequireFile('inc-sea.cgi');

$disp.=GetMenuTag('tradehouse',		'[欧州]')
	.GetMenuTag('tradehouse',	'[アフリカ]','&sea=2')
	.GetMenuTag('tradehouse',	'[中近東]','&sea=3')
	.GetMenuTag('tradehouse',	'[インド]','&sea=4')
	.GetMenuTag('tradehouse',	'[アジア]','&sea=5')
	.GetMenuTag('tradehouse',	'[新大陸]','&sea=6');
$disp.="<hr width=500 noshade size=1>";
$Q{sea}||=1;
ReadSea($Q{sea});
my @AREA=("","欧州","アフリカ","中近東","インド","アジア","新大陸");

$disp.="<BIG>●商館</BIG><br><br>";

$disp.="$TB$TR$TDB".$AREA[$Q{sea}];
$disp.="$TD<SPAN>未踏破領域</SPAN>：".(100 - $Civ)." %";
$disp.="$TD<SPAN>海賊出現率</SPAN>：".($Pir + 0)." %";
$disp.="$TD<SPAN>海軍偵察率</SPAN>：".($Pro + 0)." %";
$disp.=$TRE.$TBE;

$disp.=<<STR;
<br>
$TB$TR
$TDB都市名
$TDB発見者
$TDB産物
$TDB仕入値
$TDB産出量
$TDB航路
$TRE
STR

foreach(1..$#SEA)
	{
	my @buf=split(',',$main::SEA[$_]);
	next if !$buf[0];
	$disp.=$TR;
	$disp.=$TD.$buf[1];
	$disp.=defined($id2idx{$buf[2]}) ?'<td>'.$DT[$id2idx{$buf[2]}]->{shopname} : '<td>なし';
	$disp.=$TD.GetTagImgItemType($buf[3]).$ITEM[$buf[3]]->{name}."<br>";
	$disp.="<small>(定価 ".GetMoneyString($ITEM[$buf[3]]->{price}).")</small>";
	$disp.=$TD.GetMoneyString($buf[4])."<br>";
	$disp.="<small>(定価の".int($buf[4] / $ITEM[$buf[3]]->{price} * 100)."%)</small>";
	$disp.=$TD.GetAmountMessage($buf[0]);
	$disp.=$TD."(".($buf[5] + 0)."本)";
	$disp.=$TRE;
	}
	$disp.=$TBE;

OutSkin();
1;


sub GetAmountMessage
{
	my($rank)=@_;
	my $per=int(($rank - $NOW_TIME)/8640);
	$per=100 if $per > 100;
	$per=0 if $per < 0;
	my $i="品薄";
	$i="普通" if $per>=30;
	$i="豊富" if $per>=60;
	$i="底無" if $per>=80;
	my $bar="";
	$bar ="<nobr>";
	$bar.=qq|<img src="$IMAGE_URL/b.gif" width="|.(    $per).qq|" height="12">| if $per;
	$bar.=qq|<img src="$IMAGE_URL/t.gif" width="|.(100-$per).qq|" height="12">| if $per!=100;
	$bar.=" ".$i;
	$bar.="</nobr><br>";
	
	return $bar;
}

