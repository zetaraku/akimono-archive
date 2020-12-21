# item プラグイン 2003/07/19 由來

sub CheckShowCaseItem
{
	my($DT,$sc)=@_;
	
	$sc+=0;
	my $itemno=$DT->{showcase}[$showcase];
	$itemno=0 if $itemno && !$DT->{item}[$itemno-1];

	return ($itemno,$DT->{price}[$sc],$DT->{item}[$itemno-1]) if $itemno;

	return (0,0,0);
}

sub CheckItemNo
{
	my($itemno,$DT)=@_;
	$itemno+=0;
	$DT=$main::DT if !$DT;
	
	OutError('そんなアイテムはないです。') if $itemno<1 || $itemno>$MAX_ITEM;
	OutError('アイテムの在庫がありません。') if !$DT->{item}[$itemno-1];

	return $itemno;
}

sub GetSaleTax
{
	my($itemno,$itemcnt,$price,$plustaxrate)=@_;
	
	my $taxrate=$ITEM[$itemno]->{price} && $itemcnt ? ($price/$itemcnt/$ITEM[$itemno]->{price}-1) : 0;
	$taxrate=$taxrate*5 if $taxrate>0;
	my $taxratedown=1;
	$taxratedown=$taxrate+1,$taxrate=0 if $taxrate<0;
	$taxrate=int(($taxrate+$plustaxrate)*$taxratedown + 0.5);
	$taxrate=99 if $taxrate>99;
	my $tax=int($price*$taxrate/100);
	
	return ($taxrate,$tax);
}

# 資金/商品移動時の時間消費計算
sub GetTimeDeal
{
	my($price,$itemno,$itemcount)=@_;
	
	if(!$itemno)
	{
		#資金移動
		return 0 if !$price;
		return $TIME_SEND_MONEY if !$TIME_SEND_MONEY_PLUS;
		return int($TIME_SEND_MONEY*$price/$TIME_SEND_MONEY_PLUS)+$TIME_SEND_MONEY;
	}
	
	return 0 if !$itemcount;
	
	my $mul=1;
	
	#$mul=$ITEM[$itemno]->{price}/($price/$itemcount) if $price && $ITEM[$itemno]->{price};
	$mul=2 - ($price / $itemcount / $ITEM[$itemno]->{price}) if $price && $ITEM[$itemno]->{price};
	$mul=2 if (!$price && $ITEM[$itemno]->{price}) || $mul>2;	#20を2に変更
	$mul=0.5 if $mul<0.5;	#追加
	
	return int($TIME_SEND_ITEM*$mul);
}

# 資金/商品移動時の時間消費
sub UseTimeDeal
{
	my($price,$itemno,$itemcount)=@_;
	
	UseTime(GetTimeDeal($price,$itemno,$itemcount));
}
1;
