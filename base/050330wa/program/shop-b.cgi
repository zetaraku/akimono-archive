# 店別一覧 2005/03/30 由來

DataRead();
CheckUserPass(1);

#検索フォームを追加
my @itemlist=();
my $rank=1;
my %itempro=();
my %itemlist=();
my %guild=();

foreach my $DT (@DT)
{
	my $shopname=$DT->{shopname};
	my $shopid=$DT->{id};
	$guild{$shopid}=$DT->{guild};
	foreach my $cnt (0..$DT->{showcasecount})
	{
		my $itemno=$DT->{showcase}[$cnt];
		next if !$itemno;
		my $ITEM=$ITEM[$itemno];
		$itemlist{$itemno}=$ITEM;
		
		my $price=$DT->{price}[$cnt];
		my $stock=$DT->{item}[$itemno-1];
		my $sort=$price*$DTusercount+($DTusercount-$rank);
		push(@itemlist,[$shopid,$shopname,$cnt,$itemno,$price,$stock,$rank,$sort]);
	}
	$rank++;
}

my $itemlist="";
$itemlist="<select name=itn>";
foreach($ITEM[0],sort{$a->{sort} <=> $b->{sort}}values(%itemlist))
{
	$itemlist.="<option value=\"$_->{no}\">".$_->{name};
}
$itemlist.="</select>";

my $shoplist="";
$shoplist="<select name=ds><option value=\"\">すべて";
foreach (@DT)
{
	$shoplist.="<OPTION VALUE=\"$_->{id}\"".($Q{senditem}==$_->{id}?' SELECTED':'').">$_->{shopname}" if $DT->{id}!=$_->{id};
}
	$shoplist.="</select>";

my($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax);

if($Q{ds}!=0)
{
	my($id,$idx)=CheckUserID($Q{ds});
	($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)=
		(0,$idx,$idx,0,0,0)
}
else
{
	($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)=
		GetPage($Q{pg},$SHOP_PAGE_ROWS,$DTusercount);
}

$disp.="<BIG>●商店通り：店名別表\示</BIG>";
$disp.="<br><br>";

#店別追加バージョン
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

my $pagecontrol=GetPageControl($pageprev,$pagenext,"","",$pagemax,$page);
$disp.=$pagecontrol."<hr width=500 noshade size=1>" if $pagecontrol ne '';

foreach my $cnt ($pagestart .. $pageend)
{
	my $DT=$DT[$cnt];
	next if !$DT->{status};
	
	$disp.="<SPAN>RANK ".($cnt+1)."</SPAN> ";
	$disp.="<BR>" if $MOBILE;
	$disp.=GetTagImgGuild($DT->{guild})." ".$DT->{shopname}."<br>";
	
	$disp.=$TB;
	foreach my $idx (0..$DT->{showcasecount}-1)
	{
		my $itemno=$DT->{showcase}[$idx];
		if($itemno)
		{
			my $ITEM=$ITEM[$itemno];
			$stock=$DT->{item}[$itemno-1];
			my $msg=$stock ? "残".$stock.$ITEM->{scale} : "売り切れ";
			$disp.=$TR.$TD;
			$disp.="<A HREF=\"action.cgi?key=buy&buy=$DT->{id}!$idx!$itemno&bk=p!$page&$USERPASSURL\">" if $stock && !$GUEST_USER;
			$disp.=GetTagImgItemType($itemno).$ITEM->{name};
			$disp.="</A>" if $stock && !$GUEST_USER;
			$disp.=$TD.'@'.GetMoneyString($DT->{price}[$idx]);
			$disp.=$TD.$msg;
			$disp.=$TD.($DT->{itemtoday}{$itemno}+0).$ITEM->{scale}."売上";
			$disp.=$TRE;
		}
	}
	$disp.=$TBE;
	$disp.="<hr width=500 noshade size=1>";
}
$disp.=$pagecontrol;
OutSkin();
1;
