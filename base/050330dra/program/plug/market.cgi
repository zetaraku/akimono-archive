# market プラグイン 2003/07/19 由來

sub GetMarketStatus
{
	undef %marketitemlist;
	
	my($ITEM,$stock,$price,$mpl,$mph,$popular,$uppoint);
	
	foreach(@ITEM)
	{
		$ITEM=$_;
		$ITEM->{todaystock}=
		$ITEM->{todayprice}=
		$ITEM->{todaysale}=
		$ITEM->{yesterdaysale}=
		$ITEM->{marketprice}=
		$ITEM->{uppoint}=
		0;
	}
	
	foreach my $DT (@DT)
	{
		foreach my $caseno (0..$DT->{showcasecount}-1)
		{
			$_=$DT->{showcase}[$caseno];
			$stock=$DT->{item}[$_-1];
			next if !$_ || !$stock;
			$ITEM=$ITEM[$_];
			$ITEM->{todaystock}+=$stock;							# 陳列在庫トータル
			$price=$DT->{price}[$caseno];
			$ITEM->{todayprice}+=$price*$stock;						# 陳列金額トータル
			$mpl=\$ITEM->{marketpricelow};
			$mph=\$ITEM->{marketpricehigh};
			$$mpl=$price if $$mpl>$price || !$$mpl;	#最安値
			$$mph=$price if $$mph<$price;			#最高値
			$marketitemlist{$_}=$ITEM;
		}
		while(my($key,$value)=each %{$DT->{itemtoday}})
		{
			$ITEM=$ITEM[$key];
			$ITEM->{todaysale}+=$value;						# 今期売上数
			#$marketitemlist{$key}=$ITEM;				#カウントとりやめ
		}
		while(my($key,$value)=each %{$DT->{itemyesterday}})
		{
			$ITEM=$ITEM[$key];
			$ITEM->{yesterdaysale}+=$value;					# 前期売上数
			# $marketitemlist{$key}=$ITEM;  			#カウントとりやめ
		}
	}
	
	my $seed=$DTpeople*$SALE_SPEED/3/50;
	foreach my $ITEM (values %marketitemlist)
	{
		$stock=$ITEM->{todaystock};
		$popular=$ITEM->{popular};
		$uppoint=!$popular ? 100 : int($stock/$seed*$popular);
		$uppoint=10   if $uppoint<10;
		$uppoint=1000 if $uppoint>1000;
		
		$ITEM->{marketprice}=int($ITEM->{todayprice}/$stock) if $stock;
		
		$ITEM->{uppoint}=$uppoint;
	}
}

# 需要/供給バランスグラフ
sub GetMarketStatusGraph
{
	my($per,$noimage)=@_;
	my $ret="";
	my $width=100;
	my $type=0;
	
	$width=int($per>1000?$width:int($per*$width/1000)),$type=1 if $per>=110;
	$width=int((100-$per+10)*$width/100),$type=2 if $per<=90;
	
	my $imgwidth=int($width/2);
	my $imgwidthl=$type==1 ? 50 : 50-$imgwidth;
	my $imgwidthr=$type==2 ? 50 : 50-$imgwidth;
	
	if(!$MOBILE && !$noimage)
	{
		if($type)
		{
			$ret.=qq|<img src="$IMAGE_URL/t.gif" width="$imgwidthl" height="12">| if $imgwidthl;
			$ret.=" 飽和 " if $imgwidthl==50;
			$ret.=qq|<img src="$IMAGE_URL/|.('b','r')[$type-1].qq|.gif" width="$imgwidth" height="12">|;
			$ret.=" 不足 " if $imgwidthr==50;
			$ret.=qq|<img src="$IMAGE_URL/t.gif" width="$imgwidthr" height="12">| if $imgwidthr;
		}
		else
		{
			$ret.=qq|<img src="$IMAGE_URL/t.gif" width="50" height="12"> 均衡 |;
			$ret.=qq|<img src="$IMAGE_URL/t.gif" width="50" height="12">|;
		}
	}
	else
	{
		$width=!$type ? "" : " $width%";
		$ret.=('均衡 ','飽和 ','不足 ')[$type].$width;
	}
	return $ret;
}


1;
