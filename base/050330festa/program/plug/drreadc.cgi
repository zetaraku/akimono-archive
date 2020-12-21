# drread cプラグイン 2005/03/30 由來

sub ReadRace
{
my($fn)=@_;
$fn||="0";
$RDcount=0;
undef @RD;
@RDS=(0,0,0);
open(IN,GetPath($COMMON_DIR,"dra-rd$fn")) or return;
my @req=<IN>;
close(IN);
$RDcount=$#req;
chop $req[0];
@RDS=split(/,/,$req[0]);
return if $RDcount < 1;
foreach my $cnt(1..$RDcount)
	{
	chop $req[$cnt];
	my @buf=split(/,/,$req[$cnt]); my $i=0;
	foreach (@RDnamelist) { $RD[$cnt-1]->{$_}=$buf[$i];$i++;}
	}
}

sub GetRaceTime
{
	my($tm)=@_;
	my($hour,$min)=(int($tm/60) , ($tm % 60));
	return sprintf("%02d.%02d",$hour,$min);
}

1;
