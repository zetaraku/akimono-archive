# アイテムリスト 2005/03/30 由來

# -------- 設定部分 ---------
# 閲覧設定
$listcheck=2;		# アイテム紹介は0:店舗所有者しか見れない， 1:誰でも見れる， 2:管理者しか見れない（推奨）。

# プレイヤーには見せないアイテム（番号で指定）
# 指定例… $DENYITEM='25,86';  ←No.25と86を表示しない。

$DENYITEM='';

# プレイヤーが見るときの表示設定
$design_no=0;		#アイテムＮｏを0:表示しない（推奨）， 1:表示する。
$design_sale=0;		#売れ行きを0:表示しない（推奨）， 1:表示する。
$design_prof=1;		#利益率を0:数値で表示， 1:５段階表示（推奨）。
$design_rank=1;		#人気率を0:数値で表示， 1:５段階表示（推奨）。
$design_plus=1;		#市場入荷を0:数値で表示， 1:○×で表示（推奨）。

# -------- 設定完了 ---------

DataRead();
CheckUserPass($listcheck);
$DENYITEM=','.$DENYITEM.',';

if ($MASTER_USER) {
$NOMENU=1;
$Q{bk}="none";
@NGItem=(0);
$design_no=1;
$design_sale=1;
$design_prof=0;
$design_rank=0;
$design_plus=0;
$disp.="<BIG>●アイテムデータ</BIG><br><br>";
} else {
OutError("bad request") if ($listcheck == 2);
$disp.="<BIG>●アイテム紹介</BIG><br><br>";
}

my $tp=int($Q{tp}+0);
undef %adminitemlist;
my($ITEM,$stock,$price,$mpl,$mph,$popular,$uppoint);

foreach my $no(1..$MAX_ITEM)
{
	next if ($DENYITEM =~ /,$no,/);
	$ITEM=$ITEM[$no];
	next if ($ITEM->{type} != $tp)&&($tp != 0);;
	$adminitemlist{$no}=$ITEM;
}

foreach my $cnt (0..$#ITEMTYPE)
{
	$disp.=$cnt==$tp ? "[" : "<A HREF=\"action.cgi?key=item-list&$USERPASSURL&tp=$cnt\">";
	$disp.=GetTagImgItemType(0,$cnt) if $cnt && !$MOBILE;
	$disp.=$ITEMTYPE[$cnt];
	$disp.=$cnt==$tp ? "]" :"</A>";
	$disp.=" ";
}
	$disp.="<br>";

my($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
	=GetPage($Q{pg},$LIST_PAGE_ROWS,scalar(keys(%adminitemlist)));

$disp.=GetPageControl($pageprev,$pagenext,"tp=$tp","",$pagemax,$page);

$disp.=$TB;
$disp.=$TR;
$disp.=$TDB.'No.' if $design_no;
$disp.=$TDB.'商品名';
$disp.=$TDB.'標準価格';
$disp.=$TDB.'維持費';
$disp.=$TDB.'売行' if $design_sale;
$disp.=$TDB.'利益率';
$disp.=$TDB.'人気率';
$disp.=$TDB.'入荷';
$disp.=$TDB.'説明';
$disp.=$TRE;
foreach my $ITEM ((sort{$a->{sort} <=> $b->{sort}} values(%adminitemlist))[$pagestart..$pageend])
{
	my $itemno=$ITEM->{no};
	$disp.=$TR;
	$disp.=$TDNW.$itemno if $design_no;
	$disp.=$TDNW;
	$disp.=GetTagImgItemType($itemno).$ITEM->{name}."</A>";
	$disp.=$TDNW.GetMoneyString($ITEM->{price});
	$disp.=$TDNW.GetMoneyString($ITEM->{cost});

	my $admin_item=int($ITEM->{popular}/$SALE_SPEED);

	$disp.=$TDNW.($admin_item ? GetTime2HMS($admin_item) : "×")  if $design_sale;

	if ($design_prof) {
	$disp.=$TDNW.($admin_item ? GetStarRank(int($ITEM->{price} *24*6*6/10 / $admin_item)) : "");
	} else {
	$disp.=$TDNW.($admin_item ? int($ITEM->{price} *24*6*6/10 / $admin_item) : "---");
	}

	if ($design_rank) {
	$disp.=$TDNW.($admin_item ? GetStarRank(int($ITEM->{point} *24*6*6/10 / $admin_item)) : "");
	} else {
	$disp.=$TDNW.($admin_item ? int($ITEM->{point} *24*6*6/10 / $admin_item) : "---");
	}

	if ($ITEM->{plus} > 0) { 
	$disp.=($design_plus ? $TDNW."○" : $TDNW.GetTime2HMS($ITEM->{plus}));
	} else { $disp.=$TDNW."×" }

	$disp.=$TDNW."<small>".$ITEM->{info}."</small>";
	$disp.=$TRE;
}
$disp.=$TBE;
$disp.=GetPageControl($pageprev,$pagenext,"tp=$tp","",$pagemax,$page);
OutSkin();
1;

sub GetStarRank		#表示のカスタマイズ可能。
{
	my($no)=@_;
	my $flag='<font color="#cccc99">||</font>';
	$flag.='<font color="#ddcc44">||</font>' if $no > 50;
	$flag.='<font color="#ffcc00">||</font>' if $no > 90;
	$flag.='<font color="#ff9900">||</font>' if $no > 120;
	$flag.='<font color="#ff6600">||</font>' if $no > 180;
	return $flag;
}
