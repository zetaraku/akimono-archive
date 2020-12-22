# オリジナルメニュ 2003/08/20 由來

DataRead();
CheckUserPass();

$MENUSAY=GetMenuTag('move','[読み終える]');
Dragon();

OutSkin();
1;

sub Dragon
{
	my $rank=1;
	my @draDT=grep $_->{user}->{ori},map{$_->{_now_rank}=$rank++,$_}@DT;

	my($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
		=GetPage($Q{pg},$RANKING_PAGE_ROWS,scalar @draDT);
	
	my $pagecontrol=GetPageControl($pageprev,$pagenext,"","",$pagemax,$page);
	
	$disp.="<BIG>●オリジナルドラゴン一覧</BIG><br><br>";
	$disp.=$pagecontrol;
	$disp.=$TB;
	foreach my $DT (@draDT[$pagestart..$pageend])
	{
		my $itemtype=-1;
		my $itempro="";
		my $itemno=0;
		foreach(55..60)
		{
			next if !$DT->{item}[$_-1];
			$itemno=$_;
			last;
		}
		foreach my $no (@{$DT->{showcase}})
		{
			$itemtype=0,next if $itemtype!=-1 && $ITEM[$no]->{type}!=$itemtype;
			$itemtype=$ITEM[$no]->{type};
		}
		$itempro=GetTagImgItemType(0,$itemtype,1)." " if $itemtype;
		$disp.=$TR.$TDNW.$tdh_pt.GetTagImgKao($DT->{name},$DT->{icon});
		$disp.=$TD."<b>".$itempro.$DT->{shopname}."</b><br>".$DT->{comment};
		$disp.=$TD.GetTagImgItemType($itemno)." <SPAN>".$DT->{user}->{ori}."</SPAN><br>".$ITEM[$itemno]->{name}.$TRE;
	}
	$disp.=$TBE;
	$disp.=$pagecontrol;
}

