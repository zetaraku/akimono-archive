# img プラグイン 2003/09/25 由來

sub GetTagImgGuild
{
	my($guildcode,$noimage,$movetown)=@_;
	
	return "" if $guildcode eq '';
	my $name=$GUILD{$guildcode}->[$GUILDIDX_name];
	$name="不明" if $name eq '';
	return $name if $MOBILE || $noimage;
	return qq|<IMG class="s" ALT="$name" SRC="$COMMON_URL/$guildcode.gif"> |;
}

sub GetTagImgItemType
{
	my($itemno,$type,$mode)=@_;
	
	my $ITEM;
	if(!$type)
	{
		return "" if !$itemno;
		$ITEM=$ITEM[$itemno];
		$type=$ITEM->{type};
	}
	
	if(!$MOBILE)
	{
		return qq|<IMG class="s" SRC="$IMAGE_URL/item-typesign$type$IMAGE_EXT">| if $mode==1;
		if($ITEM->{existimage})
		{
			my $filename=$ITEM->{existimage}==1 ? "item-code-$ITEM->{code}" : "item-no-$itemno";
			return qq|<IMG |.($mode==2?'width="32" height="32"':'class="i"').qq| SRC="$IMAGE_URL/$filename$IMAGE_EXT">|;
		}
		return qq|<IMG class="i" SRC="$IMAGE_URL/item-type$type$IMAGE_EXT">| if $mode!=2;
		return "";
	}
	
	return "" if $mode==2;
	return $ITEMTYPE[$type].($mode==1?'専門店':'').":";
}
1;
