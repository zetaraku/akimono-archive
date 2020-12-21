# 相場調査 2005/01/06 由來

DataRead();
CheckUserPass(1);

$disp.="<BIG>●商店通り：相場表\示</BIG><br><br>";

# 需要/供給バランス計算
GetMarketStatus();

#店別追加バージョン
my $itemlist="";
$itemlist="<select name=itn>";
foreach($ITEM[0],grep(!$tp || $_->{type}==$tp,sort{$a->{sort} <=> $b->{sort}}values(%marketitemlist)))
{
	$itemlist.="<option value=\"$_->{no}\"".($_->{no}==$itn?' SELECTED':'').">".$_->{name};
}
$itemlist.="</select>";

my $shoplist="";
$shoplist="<select name=ds><option value=\"\">すべて";
foreach (@DT)
{
	$shoplist.="<OPTION VALUE=\"$_->{id}\"".($Q{senditem}==$_->{id}?' SELECTED':'').">$_->{shopname}" if $DT->{id}!=$_->{id};
}
	$shoplist.="</select>";

$disp.=<<"HTML";
$TBT$TRT
<td valign="bottom">
<form action="action.cgi" $METHOD>
<input type=hidden name=key value="shop-a">
$USERPASSFORM
<input type=hidden name=tp value=\"$tp\">
$itemlist
<input type=submit value="商品で検索"> 
</form>
<td valign="bottom">
<form action="action.cgi" $METHOD>
<input type=hidden name=key value="shop-b">
$USERPASSFORM
$shoplist
<input type=submit value="店名で検索"> 
</form>
<td valign="bottom">
<form action="action.cgi" $METHOD>
<input type=hidden name=key value="shop-c">
$USERPASSFORM
<input type=submit value="相場を調査">
</form>
$TRE$TBE
<br>
HTML

my($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
	=GetPage($Q{pg},$LIST_PAGE_ROWS,scalar(keys(%marketitemlist)));

$disp.=GetPageControl($pageprev,$pagenext,"t=3","",$pagemax,$page);

$disp.=$TB;
$disp.=$TR;
$disp.=$TDB.'商品名';
$disp.=$TDB.'今期<small>/前期</small><br>総売上数';
$disp.=$TDB.'最安値';
$disp.=$TDB.'最高値';
$disp.=$TDB.'販売相場';
$disp.=$TDB.'標準価格';
$disp.=$TDB.'需要供給バランス';
$disp.=$TRE;
foreach my $ITEM ((sort{$a->{sort} <=> $b->{sort}} values(%marketitemlist))[$pagestart..$pageend])
{
	my $itemno=$ITEM->{no};
	$disp.=$TR;
	$disp.=$TDNW."<A HREF='action.cgi?key=shop-a&$USERPASSURL&itn=".$itemno."'>";
	$disp.=GetTagImgItemType($itemno).$ITEM->{name}."</A>";
	$disp.=$TDNW.$ITEM->{todaysale}."<small>/".$ITEM->{yesterdaysale}."</small>";
	$disp.=$TDNW.($ITEM->{marketprice} ? GetMoneyString($ITEM->{marketpricelow}) : ($MOBILE?'0':' '));
	$disp.=$TDNW.($ITEM->{marketprice} ? GetMoneyString($ITEM->{marketpricehigh}) : ($MOBILE?'0':' '));
	$disp.=$TDNW.($ITEM->{marketprice} ? GetMoneyString($ITEM->{marketprice}) : ($MOBILE?'0':' '));
	$disp.=$TDNW.GetMoneyString($ITEM->{price});
	$disp.=$TDNW.GetMarketStatusGraph($ITEM->{uppoint});
	#$disp.=$TDNW.$todaystock{$itemno};
	$disp.=$TRE;
}
$disp.=$TBE;
$disp.=GetPageControl($pageprev,$pagenext,"t=3","",$pagemax,$page);

OutSkin();
1;
