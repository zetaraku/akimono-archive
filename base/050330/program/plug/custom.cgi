# custom プラグイン 2003/10/08 由來

sub DignityDefine
{
	my($count,$mode)=@_;
	return "" if !$count;
	my $num=0;
	foreach(1..$#DIG_POINT)
	{
		last if $count<$DIG_POINT[$_];
		$num++;
	}
	return $DIGNITY[$num] if !$mode;
	my $ret="";
	my $fn=$IMAGE_URL."/dig".$num.$IMAGE_EXT;
	$ret="<IMG class=\"i\" SRC=\"$fn\" ALT=\"$DIGNITY[$num]\">";
	return $ret if $mode==1;
	return $ret.$DIGNITY[$num];
}

sub GetCleanMessage
{
	my($rank,$mode)=@_;
	my $per=int($rank/50000);
	$per=100 if $per > 100;
	my $i="綺麗";
	$i="清潔" if $per>=20;$i="普通" if $per>=40;
	$i="不潔" if $per>=60;$i="汚屋敷" if $per>=80;
	return $i if $MOBILE || $mode;
	
	my $bar="";
	$bar ="<nobr>";
	$bar.=qq|<img src="$IMAGE_URL/r.gif" width="|.(    $per).qq|" height="12">| if $per;
	$bar.=qq|<img src="$IMAGE_URL/t.gif" width="|.(100-$per).qq|" height="12">| if $per!=100;
	$bar.=" ".$i;
	$bar.="</nobr><br>";
	
	return $bar;
}

sub GetTownData
{
	my($key)=@_;
	$key=~s/%([\dA-Fa-f]{2})/pack("H2",$1)/eg;
	my $val=$DTtown->{$key}||($DTtown->{$key} eq '0' ? 0 : '');
	$val=~s/%([\dA-Fa-f]{2})/pack("H2",$1)/eg;
	return $val;
}

sub SetTownData
{
	my($key,$val)=@_;
	$key=~s/([\x00-\x1f,%])/'%'.unpack("H2",$1)/ge;
	$val=~s/([\x00-\x1f,%])/'%'.unpack("H2",$1)/ge;
	delete($DTtown->{$key}),return '' if $val eq '';
	return $DTtown->{$key}=$val;
}
1;
