# detail プラグイン 2005/01/06 由來

sub SortDT
{
	my($mode)=@_;
	
	@DT=grep($_->{status},@DT);
	foreach(@DT){$_->{point}=GetDTPoint($_);}
	@DT=sort{(!$a->{rankingyesterday})<=>(!$b->{rankingyesterday}) or $b->{point}<=>$a->{point}}@DT;
	
	%id2idx  =map{($DT[$_]->{id},$_)}(0..$#DT);
	%name2idx=map{($DT[$_]->{name},$_)}(0..$#DT);
}

sub GetRankMessage
{
	my($rank,$mode)=@_;
	my $per=int($rank/100);
	
	return $per.(!$mode?"%":"") if $MOBILE;
	
	my $bar="";
	$bar ="<nobr>";
	$bar.=qq|<img src="$IMAGE_URL/b.gif" width="|.(    $per).qq|" height="12">| if $per;
	$bar.=qq|<img src="$IMAGE_URL/t.gif" width="|.(100-$per).qq|" height="12">| if $per!=100 && !$mode;
	$bar.=" ".$per;
	$bar.="%" if !$mode;
	$bar.="</nobr><br>";
	
	return $bar;
}

#店舗売却税率計算
sub GetUserTaxRate
{
	my($DT,$usertax)=@_;
	
	return 0 if ($DTevent{rebel});
	return 0 if ($DT->{taxmode}==1);
	return $usertax*2 if ($DT->{taxmode}==2);
	return $usertax;
}

sub CheckShowCaseNumber
{
	my($DT,$sc)=@_;
	
	$sc+=0;
	OutError('そんな陳列棚はありません') if $sc<0 || $DT->{showcasecount}<=$sc;

	return $sc;
}

sub GetTopCountImage
{
	my($count)=@_;
	return "" if !$count;
	return $count."回優勝" if $MOBILE;

	my $ret="";
	my $num=1;
	foreach my $cnt(3,5,7,9,11)
	{
		last if $count<$cnt;
		$num++;
	}
	my $fn=$IMAGE_URL."/rank".$num.$IMAGE_EXT;
	$ret="<IMG class=\"i\" SRC=\"$fn\" ALT=\"$count回優勝\">";
	return $ret;
}

sub GetMoneyMessage
{
	my($money)=@_;

	return "<font color=\"#cc2266\"><b>$term[3]</b></FONT>" if $money < 0;
	$money=int(($money+9999)/10000);

	foreach my $rank (10,20,50,100,500,1000,5000)
	{
		return $rank."<font size=\"-3\">万$term[2]以下</font>" if $money<=$rank;
	}

	foreach my $rank (10000,50000,100000)
	{
		return int($rank/10000)."<font size=\"-3\">億$term[2]以下</font>" if $money<=$rank;
	}
}

sub GetTagImgShopIcon
{
	my($icon)=@_;
	
	return "" if $MOBILE || $icon eq '';
	
	return qq|<img src="$IMAGE_URL/shop-$icon$IMAGE_EXT" class="shopicon">|;
}
1;
