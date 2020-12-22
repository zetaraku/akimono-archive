# whole プラグイン 2003/07/19 由來

sub GetWholeStore
{
	my $DT={};
	$DT->{name}="マスター";
	$DT->{shopname}="市場";
	
	my $cnt=0;
	
	my @wholelist=grep($DTwholestore[$_],0..$MAX_ITEM-1);
	my @sortkey;
	foreach(@wholelist)
		{$sortkey[$_]=$ITEM[$_+1]->{sort}};
	
	foreach my $i (sort {$sortkey[$a]<=>$sortkey[$b]} @wholelist)
	{
		my $stock=$DTwholestore[$i];
		next if !$stock;
		
		my $itemno=$i+1;
		my $ITEM=$ITEM[$itemno];
		
		my $price=$ITEM->{price};
		if($ITEM->{pricehalf})
		{
			$price=int($price/ ((($stock-$ITEM->{pricebase})/$ITEM->{pricehalf})+1) );
			$price=1 if $price<=0 && $ITEM->{price};
		}
		$DT->{showcase}[$cnt]=$itemno;
		$DT->{price}[$cnt++]=$price;
		$DT->{item}[$i]=$stock;
	}
	$DT->{showcasecount}=$cnt;

	return $DT;
}

sub SetWholeStore
{
	my($DT)=@_;
	
	foreach my $i (0..$MAX_ITEM-1)
	{
		$DTwholestore[$i]=$DT->{item}[$i];
	}
}

sub CheckWholeStore
{
# 郵便関係処理を削除。

	foreach my $cnt (1..$MAX_ITEM)
	{
		next if !$ITEM[$cnt]->{code};
		my $ITEM=$ITEM[$cnt];
		
		#上限数チェック
		my $limit=0;
		foreach my $DT (@DT)
			{$limit+=$DT->{item}[$cnt-1];}
# $limit+=$boxitem[$cnt];
		my $shopcount=@DT; $shopcount||=1;
		my $limitcount=$ITEM->{wslimit}<0 ? -$ITEM->{wslimit} : int($ITEM->{wslimit}*$shopcount+0.99);
		
		if($limit+$DTwholestore[$cnt-1]>$limitcount)
		{
			$limit=$limitcount if $limitcount<$limit;
			$DTwholestore[$cnt-1]=$limitcount-$limit;
		}
		#下限数チェック
		$DTwholestore[$cnt-1]=0 if $DTwholestore[$cnt-1]<0;
	}
}


1;
