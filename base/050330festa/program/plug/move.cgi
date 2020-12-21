# move プラグイン 2003/07/19 由來

sub GetHash
{
	my($time,$str)=@_;
	my $len=length($str);
	my $hash=$time;
	my $seed=0;
	for(my $i=0; $i<$len; $i++)
	{
		my $val=unpack('C',substr($str,$i,1));
		$seed= $i&1 ? $seed*($val+1) : $seed/($val+1);
		$seed+=$val;
	}
	$seed=int($seed);
	for(my $i=0; $i<$len; $i++)
	{
		my $val=unpack('C',substr($str,$i,1));
		$val*=($seed+1);
		$seed=($val+substr($hash,-3,3)) & 255;
		$hash.=$val*($seed & 15);
		my $len1=int(length($hash)/2);
		my $len2=length($hash)-$len1;
		$hash=substr($hash,$len1,$len2).substr($hash,0,$len1);
	}
	$hash=substr($hash,int(length($hash)/4),32);
	return $hash.$time.sprintf("%02d",length($time));
}

sub CheckHash
{
	my($hash,$plain)=@_;
	return 0 if $hash eq '';
	my $len=substr($hash,-2,2);
	my $time=substr($hash,-($len+2),$len);
	return 0 if $time<time()-$PASSWORD_HASH_EXPIRE_TIME; #$PASSWORD_HASH_EXPIRE_TIME秒以上前のHashは無効
	return GetHash($time,$plain) eq $hash;
}
1;
