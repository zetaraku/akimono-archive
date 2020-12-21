# オリジナルメニュ 2004/01/20 由來

DataRead();
CheckUserPass();

$disp.=GetMenuTag('orilist',	'[うどん]')
	.GetMenuTag('orilist',	'[そば]','&mode=soba');
$disp.="<hr width=500 noshade size=1>";

my $functionname=$Q{mode};
$functionname="udon" if !defined(&$functionname);
&$functionname if defined(&$functionname);
OutSkin();
1;

sub udon
{
	my $rank=1;
	my @udonDT=grep $_->{user}->{udon},map{$_->{_now_rank}=$rank++,$_}@DT;

	my($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
		=GetPage($Q{pg},$RANKING_PAGE_ROWS,scalar @udonDT);
	
	my $pagecontrol=GetPageControl($pageprev,$pagenext,"mode=udon","",$pagemax,$page);
	
	$disp.="<BIG>●オリジナルうどん開発店</BIG><br><br>";
	$disp.=$pagecontrol;
	$disp.=$TB;
	foreach my $DT (@udonDT[$pagestart..$pageend])
	{
		my $itemtype=-1;
		my $itempro="";
		my $salelist="";
		foreach my $no (@{$DT->{showcase}})
		{
			$itemtype=0,next if $itemtype!=-1 && $ITEM[$no]->{type}!=$itemtype;
			$itemtype=$ITEM[$no]->{type};
		}
		$itempro=GetTagImgItemType(0,$itemtype,1)." " if $itemtype;
		$disp.=$TR.$TDNW.$tdh_pt.GetTagImgKao($DT->{name},$DT->{icon});
		$disp.=$TD.GetTagImgItemType(44)." <SPAN>".$DT->{user}->{udon}."</SPAN><br><b>".$itempro.$DT->{shopname}."</b>";
		$disp.=$TD.$DT->{comment}.$TRE;
	}
	$disp.=$TBE;
	$disp.=$pagecontrol;
}

sub soba
{
	my $rank=1;
	my @sobaDT=grep $_->{user}->{soba},map{$_->{_now_rank}=$rank++,$_}@DT;

	my($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
		=GetPage($Q{pg},$RANKING_PAGE_ROWS,scalar @sobaDT);
	
	my $pagecontrol=GetPageControl($pageprev,$pagenext,"mode=soba","",$pagemax,$page);
	
	$disp.="<BIG>●オリジナルそば開発店</BIG><br><br>";
	$disp.=$pagecontrol;
	$disp.=$TB;
	foreach my $DT (@sobaDT[$pagestart..$pageend])
	{
		my $itemtype=-1;
		my $itempro="";
		my $salelist="";
		foreach my $no (@{$DT->{showcase}})
		{
			$itemtype=0,next if $itemtype!=-1 && $ITEM[$no]->{type}!=$itemtype;
			$itemtype=$ITEM[$no]->{type};
		}
		$itempro=GetTagImgItemType(0,$itemtype,1)." " if $itemtype;
		$disp.=$TR.$TDNW.$tdh_pt.GetTagImgKao($DT->{name},$DT->{icon});
		$disp.=$TD.GetTagImgItemType(56)." <SPAN>".$DT->{user}->{soba}."</SPAN><br><b>".$itempro.$DT->{shopname}."</b>";
		$disp.=$TD.$DT->{comment}.$TRE;
	}
	$disp.=$TBE;
	$disp.=$pagecontrol;
}
