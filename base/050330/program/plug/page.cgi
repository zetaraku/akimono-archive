# page プラグイン 2003/07/19 由來

sub GetPage
{
	my($page,$pageline,$count)=@_;
	my($pagestart,$pageend,$pagenext,$pageprev);
	
	$pageline=1 if $pageline<=0;
	
	$pagemax=int(($count-1)/$pageline);

	$page=0        if $page<0;
	$page=$pagemax if $page>$pagemax;
	
	$pagestart=$page*$pageline;
	$pageend=$pagestart+$pageline>$count ? $count-1 : $pagestart+$pageline-1;
	$pagenext=($page+1)*$pageline<$count ? $page+1 : 0;
	$pageprev=$page>0 ? $page-1 : -1;

	return ($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax);
}

sub GetPageControl
{
	my($pageprev,$pagenext,$addurl,$pgname,$pagemax,$pagenow)=@_;
	return if !$pagemax;
	
	my $ret="";
	
	$pgname="pg" if $pgname eq '';
	
	my $range=3;
	my $ps=$pagenow<$range ? 0 : $pagenow-$range;
	my $pe=$pagenow>$pagemax-$range ? $pagemax : $pagenow+$range;
	if($pe-$ps<$range*2)
	{
		$ps=$pe-$range*2 if $pe==$pagemax;
		$ps=0            if $ps<0;
		$pe=$ps+$range*2 if $ps==0;
		$pe=$pagemax     if $pe>$pagemax;
	}
	
	my $url="action.cgi?key=".$Q{key}."&".$USERPASSURL.($addurl?"&".$addurl:"")."&".$pgname."=";
	$ret.=GetTagA("≪",$url."0");
	$ret.=GetTagA("＜",$url.$pageprev,$pageprev<0);
	foreach($ps..$pe)
	{
		my $num=$_+1;
		$num="[$num]" if $_==$pagenow;
		$ret.=GetTagA($num,$url.$_,$_==$pagenow);
	}
	$ret.=GetTagA("＞",$url.$pagenext,$pagenext<=0);
	$ret.=GetTagA("≫",$url.$pagemax);
	
	return $ret."\n";
}
1;
