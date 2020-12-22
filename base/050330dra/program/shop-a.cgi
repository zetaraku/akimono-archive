# 商店一覧 2005/03/30 由來

DataRead();
CheckUserPass(1);

my $tp=int($Q{tp}+0);
my @itemlist=();
my $itn=int($Q{itn}+0);

my $rank=1;
my %itempro=();
my %itemlist=();
my %guild=();

foreach(@ITEM){$_->{no}}

foreach my $DT (@DT)
{
	my $shopname=$DT->{shopname};
	my $shopid=$DT->{id};
	$guild{$shopid}=$DT->{guild};
	my $itemtype=-1;
	foreach my $cnt (0..$DT->{showcasecount})
	{
		my $itemno=$DT->{showcase}[$cnt];
		next if !$itemno;
		my $ITEM=$ITEM[$itemno];
		my $itemtypew=$ITEM->{type};
		$itemtype=$itemtype!=-1 && $itemtypew!=$itemtype ? 0 : $itemtypew;
		next if $tp && $itemtypew!=$tp;;
		
		$itemlist{$itemno}=$ITEM;
		next if $itn && $itn!=$itemno;
		
		my $price=$DT->{price}[$cnt];
		my $stock=$DT->{item}[$itemno-1];
		my $sort=$price*$DTusercount+($DTusercount-$rank);
		push(@itemlist,[$shopid,$shopname,$cnt,$itemno,$price,$stock,$rank,$sort]);
	}
	$itempro{$shopid}=GetTagImgItemType(0,$itemtype,1)." " if $itemtype;
	
	$rank++;
}

my $itemlist="";
if($tp || !$MOBILE)
{
	$itemlist="<select name=itn>";
	foreach($ITEM[0],grep(!$tp || $_->{type}==$tp,sort{$a->{sort} <=> $b->{sort}}values(%itemlist)))
	{
		$itemlist.="<option value=\"$_->{no}\"".($_->{no}==$itn?' SELECTED':'').">".$_->{name};
	}
	$itemlist.="</select>";
}

#店別を追加
my $shoplist="";
$shoplist="<select name=ds><option value=\"\">すべて";
foreach (@DT)
{
	$shoplist.="<OPTION VALUE=\"$_->{id}\"".($Q{senditem}==$_->{id}?' SELECTED':'').">$_->{shopname}" if $DT->{id}!=$_->{id};
}
	$shoplist.="</select>";
#ここまで

my($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
	=GetPage($Q{pg},$LIST_PAGE_ROWS,$#itemlist+1);

$disp.="<BIG>●商店通り：商品別表\示</BIG><br><br>";

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

foreach my $cnt (0..$#ITEMTYPE)
{
	$disp.=$cnt==$tp ? "[" : "<A HREF=\"action.cgi?key=shop-a&$USERPASSURL&tp=$cnt\">";
	$disp.=GetTagImgItemType(0,$cnt) if $cnt && !$MOBILE;
	$disp.=$ITEMTYPE[$cnt];
	$disp.=$cnt==$tp ? "]" :"</A>";
	$disp.=" ";
}
	$disp.="<br>";

$pagectrl=GetPageControl($pageprev,$pagenext,"t=2&itn=$Q{itn}&tp=$tp","",$pagemax,$page);
$disp.=$pagectrl;

@itemlist=sort {$a->[7]<=>$b->[7]} @itemlist;

$disp.=$TB;
foreach my $item (@itemlist[$pagestart..$pageend])
{
	my($shopid,$shopname,$showcase,$itemno,$price,$stock,$rank)=@{$item};

	my $ITEM=$ITEM[$itemno];
	my $msg=$stock ? "残".$stock.$ITEM->{scale} : "売り切れ";
	
	$disp.=$TR.$TD;
	$disp.="<A HREF=\"action.cgi?key=buy&buy=$shopid!$showcase!$itemno&bk=p2!$page!$itn&$USERPASSURL\">" if $stock && !$GUEST_USER;
	$disp.=GetTagImgItemType($itemno).$ITEM->{name};
	$disp.="</A>" if $stock && !$GUEST_USER;
	
	$disp.=$TD.'@'.GetMoneyString($price);
	
	$disp.=$TD.$msg;
	
	$disp.=$TD."RANK ".$rank.$TD.GetTagImgGuild($guild{$shopid}).$itempro{$shopid}.$shopname;
	$disp.=$TRE;
	$disp.="<HR SIZE=\"1\">" if $MOBILE;
}
$disp.=$TBE;
$disp.=$pagectrl;

OutSkin();
1;
