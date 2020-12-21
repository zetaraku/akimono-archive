# log プラグイン 2003/07/19 由來

sub ReadLog
{
	my($id,$mode,$keyword,$target)=@_;
	$id=$DT->{id} if $id eq '';
	undef @MESSAGE;
	
	open(IN,GetPath("log0"));
	push(@MESSAGE,<IN>);
	close(IN);
	open(IN,GetPath("log1"));
	push(@MESSAGE,<IN>);
	close(IN);
	
	@MESSAGE=grep(/^\d+\t\d+\t($id|0)\t/o,@MESSAGE);
	if($mode)
	{
		$mode+=0;
		@MESSAGE=grep(/^\d+\t$mode\t/o,@MESSAGE);
	}
	if($keyword)
	{
		require $JCODE_FILE;
		$keyword=jcode::sjis($keyword,$CHAR_SHIFT_JIS&&'sjis');
		@MESSAGE=grep(/\Q$keyword\E/oi,@MESSAGE);
	}
	if($target)
	{
		require $JCODE_FILE;
		$target=jcode::sjis($target,$CHAR_SHIFT_JIS&&'sjis');
		@MESSAGE=grep(/\Q$target\E/o,@MESSAGE);
	}
	@MESSAGE=("0\t0\t0\t情報はありません\n") if !scalar(@MESSAGE);
}

sub PushLog
{
	my($mode,$id,$msg)=@_;
	unshift(@LOG,"$NOW_TIME\t$mode\t$id\t$msg\n");
}

# 互換性確保
sub WriteLog
{
	PushLog($_[0],$_[1],$_[3]);
}

sub RenewLog
{
	return if !scalar(@LOG);
	my $s0=GetPath("log0");
	my $s1=GetPath("log1");
	my $s2=GetPath("log2");
	my $tempfile=GetPath($TEMP_DIR,"log0");
	
	if((stat($s1))[9]<$NOW_TIME-$LOG_EXPIRE_TIME)
	{
		RenameAndCheck($s1,$s2) if -e $s1;
		RenameAndCheck($s0,$s1) if -e $s0;
	}
	else
	{
		open(IN,(-e $tempfile ? $tempfile : $s0));
		push(@LOG,<IN>);
		close(IN);
	}
	OpenAndCheck($tempfile);
	print OUT @LOG;
	close(OUT);
}
1;
