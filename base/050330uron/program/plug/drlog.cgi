# drlog プラグイン 2005/03/30 由來

sub PushDraLog
{
	my($mode,$msg)=@_;
	unshift(@DLOG,"$NOW_TIME\t$mode\t$msg\n");
}

sub RenewDraLog
{
	return if !scalar(@DLOG);
	my $s0=GetPath($COMMON_DIR,"dra-log0");
	my $s1=GetPath($COMMON_DIR,"dra-log1");
	my $s2=GetPath($COMMON_DIR,"dra-log2");
	my $tempfile=GetPath($COTEMP_DIR,"dra-log0");
	
	if((stat($s1))[9]<$NOW_TIME-$LOG_EXPIRE_TIME)
	{
		RenameAndCheck($s1,$s2) if -e $s1;
		RenameAndCheck($s0,$s1) if -e $s0;
	}
	else
	{
		open(IN,(-e $tempfile ? $tempfile : $s0));
		push(@DLOG,<IN>);
		close(IN);
	}
	OpenAndCheck($tempfile);
	print OUT @DLOG;
	close(OUT);
}

sub WritePayLog
{
	my($file,$id,$money)=@_;
	my $fn=GetPath($COMMON_DIR,"drapay-".$file);
	open(OUT,">>$fn") or return;
	print OUT "$id\t$money\n";
	close(OUT);
}

1;
