# 上位表示 2005/01/06 由來

my ($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
	=GetPage($Q{pg},$TOP_RANKING_PAGE_ROWS,$DTusercount);

$disp.="<BIG>●トップ $TOP_RANKING_PAGE_ROWSの店舗</BIG>：".GetMenuTag('log','[詳細]','&t=4')."<br><br>";
$disp.=$TB;

	$disp.=$TR;
	$disp.=$TDB."点数";
	$disp.=$TDB."店長";
	$disp.=$TDB."ジョブ";
	$disp.=$TDB."店名　人気";
	$disp.=$TDB."今期売上";
	$disp.=$TDB."資金";
	$disp.=$TDB."熟練";
	$disp.=$TDB."商品 【創業】 コメント";
	$disp.=$TRE;

foreach my $idx ($pagestart..$pageend)
{
	my $DT=$DT[$idx];
	
	my $rankupdown="(新)";
	if($DT->{rankingyesterday})
	{
		$rankupdown=$DT->{rankingyesterday}-$idx-1;
		$rankupdown=$rankupdown==0 ? " → ": $rankupdown<0 ? "↓".(-$rankupdown) : "↑".$rankupdown;
		$rankupdown="<small>($rankupdown)</small>";
	}
	my $itemtype=-1;
	my $itempro="";
	my $salelist="";
	foreach(0..$DT->{showcasecount}-1)
	{
		my $no=$DT->{showcase}[$_];
		$salelist.=GetTagImgItemType($no);
		$itemtype=0,next if $itemtype!=-1 && $ITEM[$no]->{type}!=$itemtype;
		$itemtype=$ITEM[$no]->{type};
	}
	$itempro=GetTagImgItemType(0,$itemtype,1)." " if $itemtype;
	my $itemno=$DT->{showcase}[0];
	if ($itemno==44)
	{
	$salelist.=($DT->{user}->{udon}) ? " $DT->{user}->{udon}" : " （他店のオリジナルうどん）";
	$salelist.=" ".GetMoneyString($DT->{price}[0]);
	}
	elsif ($itemno==56)
	{
	$salelist.=($DT->{user}->{soba}) ? " $DT->{user}->{soba}" : " （他店のオリジナルそば）";
	$salelist.=" ".GetMoneyString($DT->{price}[0]);
	}
	elsif ($itemno)
	{
	$salelist.=" ".$ITEM[$itemno]->{name}." ".GetMoneyString($DT->{price}[0]);
	}
	
	my $expsum=0;
	foreach(values(%{$DT->{exp}})){$expsum+=$_;}
	$expsum=int($expsum/10)."%";
	
	$disp.=$TR;
	$disp.="<td align=right><b>No.".($idx+1)."</b>".$rankupdown;
	$disp.="<br>".$DT->{point};
	$disp.=$TDNW.$tdh_pt.GetTagImgKao($DT->{name},$DT->{icon});
	$disp.="<td align=center>".GetTagImgJob($DT->{job},$DT->{icon});
	$disp.=$TD.$tdh_nm;
	$disp.=    "<a href=\"shop.cgi?ds=$DT->{id}&$USERPASSURL\">" if !$GUEST_USER;
	$disp.=    GetTagImgGuild($DT->{guild}).$job.$DT->{shopname};
	$disp.=    "</a>" if !$GUEST_USER;
	$disp.=GetTopCountImage($DT->{rankingcount}+0) if $DT->{rankingcount};
	$disp.="<BR>";
	$disp.=GetRankMessage($DT->{rank});
	$disp.=$TDNW.$tdh_ts.GetMoneyString($DT->{saletoday});
	$disp.=$TDNW.$tdh_mo.GetMoneyMessage($DT->{money});
	$disp.=$TDNW.$tdh_ex.$expsum;
	
	$disp.=$TD;
	
	$disp.=$tdh_sc.$itempro.$salelist;
	
	$disp.="<BR>";
	
	$disp.=$tdh_fd."【".GetTime2found($NOW_TIME-$DT->{foundation})."】";
	$disp.=$tdh_cm.$DT->{comment} if $DT->{comment};
	$disp.=$TRE;
}
$disp.=$TBE;
1;
