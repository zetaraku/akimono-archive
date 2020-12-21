# time プラグイン 2003/07/19 由來

sub GetTime2FormatTime
{
	return '--/--' if !$_[0];
	my($sec,$min,$hour,$mday,$mon,$year)=gmtime($_[0]+$TZ_JST);
	$mon++;
	return sprintf("%02d/%02d %02d:%02d",$mon,$mday,$hour,$min) if !$_[1];
	return sprintf("%02d:%02d",$hour,$min) if $_[0]>$NOW_TIME-12*3600 or int(($_[0]+$TZ_JST)/86400)==int(($NOW_TIME+$TZ_JST)/86400);
	return sprintf("%02d/%02d",$mon,$mday);
}

sub GetTime2found
{
	my($tm,$mode)=@_;
	
	my $h=int($tm/3600);
	return $h.'時間' if $h<24;
	return int($h/24).'日';
}
1;
