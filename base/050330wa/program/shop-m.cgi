# 市場 2005/01/06 由來

DataRead();
$DT={};
CheckUserPass(1);

RequireFile('inc-html-ownerinfo.cgi');

my $DTS=GetWholeStore();
my($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
	=GetPage($Q{pg},$LIST_PAGE_ROWS,$DTS->{showcasecount});

$disp.="<BIG>●市場</BIG><br><br>";

my $pagecontrol=GetPageControl($pageprev,$pagenext,"","",$pagemax,$page);
$disp.=$pagecontrol;

my $itemno;
my $ITEM;
$disp.=$TB;
foreach my $i ($pagestart..$pageend)
{
	$itemno=$DTS->{showcase}[$i];
	$ITEM=$ITEM[$itemno];
	next if !$itemno || !$ITEM->{code};
	
	$disp.=$TR.$TD;
	$disp.="<A HREF=\"action.cgi?key=buy&buy=0!$i!$itemno&bk=m!$page&$USERPASSURL\">" if !$GUEST_USER;
	$disp.=GetTagImgItemType($itemno).$ITEM->{name};
	$disp.="</A>" if !$GUEST_USER;
	$disp.=$TD.'@'.GetMoneyString($DTS->{price}[$i]).$TD."残".$DTS->{item}[$itemno-1].$ITEM->{scale};
	$disp.=$TD.$DT->{item}[$itemno-1].$ITEM->{scale}."所持" if $DT->{item}[$itemno-1];
	$disp.=$TRE;
}
$disp.=$TBE;
$disp.=$pagecontrol;

OutSkin();
1;
