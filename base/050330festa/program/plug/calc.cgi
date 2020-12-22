# calc プラグイン 2005/01/06 由來

sub CheckCount
{
	my($cnt1,$cnt2,$min,$max)=@_;
	my $cnt;
	
	$cnt1+=0; $cnt2+=0;
	
	$cnt=$cnt2 ? $cnt2 : $cnt1;
	$cnt=$min if $cnt<$min;
	$cnt=$max if $cnt>$max;
	OutError('不正な値です。') if  $cnt =~/(nan|inf)/i;
	return int($cnt);
}

sub GetStockTime
{
	my($tm)=@_;
	my $tmp=$NOW_TIME-$tm;
	$tmp=$MAX_STOCK_TIME if $tmp>$MAX_STOCK_TIME;
	
	return $tmp;
}

sub UseTime
{
	my($tm)=@_;
	
	if($DT->{status})
	{
		OutError('bad request') if $tm<0;
		my $tmp=$NOW_TIME-$DT->{time};
		$DT->{time}=$NOW_TIME-$MAX_STOCK_TIME if $tmp>$MAX_STOCK_TIME;
		
		OutError('時間が足りません。') if $tmp<0 && $USER ne '';
		
		$DT->{time}+=$tm;
	}
}

sub EditMoney
{
	my($DT,$money)=@_;
	
	$DT->{money}+=int $money;
	$DT->{money}=$MAX_MONEY if $DT->{money}>$MAX_MONEY;
	$DT->{money}=0          if $DT->{money}<0;
}

sub EditTime
{
	my($DT,$time)=@_;
	
	my $stock=$DT->{time};
	$stock=$NOW_TIME-$MAX_STOCK_TIME if $stock<$NOW_TIME-$MAX_STOCK_TIME;
	$stock-=int $time;
	$stock=$NOW_TIME-$MAX_STOCK_TIME if $stock<$NOW_TIME-$MAX_STOCK_TIME;
	$DT->{time}=$stock;
}

sub GetItemUseTime
{
	my($USE)=@_;
	my $exp=$USE->{result}->{expold}ne'' ? $USE->{result}->{expold} : $DT->{exp}->{$USE->{itemno}};
	return $USE->{time}-int(($USE->{time}-$USE->{exptime})*$exp/1000);
}
1;
