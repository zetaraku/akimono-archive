# 仕入れ詳細 2005/01/06 由來

$NOMENU=1;
DataRead();
CheckUserPass();

($id,$showcase,$mstno)=split('!',$Q{buy},3);
$id=int($id+0);
$showcase=int($showcase+0);

if($id==0)
{
	# 市場
	$DTS=GetWholeStore();
}
else
{
	# 一般店
	$DTS=$DT[(CheckUserID($id))[1]];
}

$showcase=CheckShowCaseNumber($DTS,$showcase);
($itemno,$price,$stock)=CheckShowCaseItem($DTS,$showcase);

OutError("陳列棚には何もありません") if !$itemno || !$stock;
OutError("陳列が変化したようです") if $itemno!=$mstno;

RequireFile('inc-html-ownerinfo.cgi');

$TIME_SEND_ITEM=int($TIME_SEND_ITEM/2) if !$id;
my $usetime=GetTimeDeal($price,$itemno,1);

my $baseprice=$price;
my($guild,$guildrate,$guildmargin)=CheckGuild($DT,$DTS,$baseprice);
my $saleprice=$baseprice+($guild==1 ? -$guildmargin : $guildmargin);
$price=$saleprice;

$disp.="<BIG>●購入</BIG><br><br>";

my $ITEM=$ITEM[$itemno];

$disp.=$TB.$TR.$TDB."店名".$TD.GetTagImgGuild($DTS->{guild}).$DTS->{shopname}.$TRE;
$disp.=$TR.$TDB;
$disp.=(($ITEM->{flag}=~/h/)? "名前" : "商品");
$disp.=$TD.GetTagImgItemType($itemno).$ITEM->{name}.$TRE;
$disp.=$TR.$TDB.$TD.$ITEM->{info}.$TRE;
$disp.=$TR.$TDB."価格".$TD.'@'.GetMoneyString($baseprice).$TRE;
$disp.=$TR.$TDB.("ギルド内割引価格","ギルド間割増価格")[$guild-1].$TD.'@'.GetMoneyString($saleprice).$TRE if $guild>0;
$disp.=$TR.$TDB."ギルド資金不足".$TD."ギルド内割引補助はありません".$TRE if $guild==-1;
$disp.=$TR.$TDB."販売在庫数".$TD.$stock.$ITEM->{scale}.$TRE;
$disp.=$TR.$TDB.'自店保有数'.$TD.($DT->{item}[$itemno-1]+0).$ITEM->{scale}.$TRE;
$disp.=$TBE;

if ($ITEM->{flag}!~/s/) {		# s 陳列不可
	$disp.="<SPAN>※この商品は陳列しても売れません</SPAN><br>" if ($ITEM->{popular}==0);
	$disp.="<SPAN>※この商品は陳列してもほとんど売れません</SPAN><br>" if ($ITEM->{popular} > 800000);
	}
$disp.="<hr width=500 noshade size=1>";

if($DT->{item}[$itemno-1]>=$ITEM->{limit})
	{$disp.='<BR>もう倉庫は'.$ITEM->{name}.'が一杯です<BR>';}
elsif($DT->{money}<$price && $price > 0)
	{$disp.='<BR>資金が足りません<BR>';}
elsif(GetStockTime($DT->{time})<$usetime)
	{$disp.='<BR>時間が足りません<BR>';}
else
{
	$disp.="<FORM ACTION=\"action.cgi\" $METHOD>";
	$disp.="<INPUT TYPE=HIDDEN NAME=key VALUE=\"buy-s\">";
	$disp.="$USERPASSFORM";
	$disp.="<INPUT TYPE=HIDDEN NAME=bk VALUE=\"$Q{bk}\">";
	$disp.="<INPUT TYPE=HIDDEN NAME=id VALUE=\"$id\">";
	$disp.="<INPUT TYPE=HIDDEN NAME=pr VALUE=\"$price\">";
	$disp.="<INPUT TYPE=HIDDEN NAME=sc VALUE=\"$showcase\">";
	$disp.="<INPUT TYPE=HIDDEN NAME=it VALUE=\"$itemno\">";
	$disp.="上記を ";
	$limit=$ITEM[$itemno]->{limit}-$DT->{item}[$itemno-1];
	my $money=$MAX_MONEY;
	$money=int($DT->{money}/$price) if $price;
	$msg{1}=1;
	$msg{10}=10;
	$msg{100}=100;
	$msg{1000}=1000;
	$msg{10000}=10000;
	$msg{$stock}="$stock(全部)";
	$msg{$limit}="$limit(倉庫最大)";
	$msg{$money}="$money(資金最大)";
	$disp.="<SELECT NAME=num1 SIZE=1>";
	my $oldcnt=0;
	foreach my $cnt (sort { $a <=> $b } (1,10,100,1000,10000,$stock,$limit,$money))
	{
		last if $stock<$cnt || $cnt>$money || $cnt>$limit || $cnt==$oldcnt;
	
		$disp.="<OPTION VALUE=\"$cnt\">$msg{$cnt}";
		$oldcnt=$cnt;
	}
	$disp.="</SELECT> $ITEM[$itemno]->{scale}、もしくは ";
	$disp.="<INPUT TYPE=TEXT NAME=num2 SIZE=5> $ITEM[$itemno]->{scale} ";

  if ($ITEM->{flag}=~/h/) {  $disp.="<INPUT TYPE=SUBMIT VALUE='雇う'>";  }
         else 	{ $disp.="<INPUT TYPE=SUBMIT VALUE='買う'>"; }

	$disp.="<br>(消費時間:".GetTime2HMS($usetime).")";
	$disp.="</FORM>";
}

OutSkin();
1;
