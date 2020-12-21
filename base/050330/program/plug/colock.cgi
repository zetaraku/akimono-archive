# colock プラグイン 2003/07/19 由來

sub CoLock
{
	$COLOCKED_LEVEL++,return if $COLOCKED ne '';
	CoLockSub();
	CoDataCA(1); # abort
}

sub CoUnLock
{
	return if $COLOCKED eq '' || --$COLOCKED_LEVEL;
	$COLOCKED='',return if rename($COLOCKED,$COMMON_DIR."/".$LOCK_FILE);
	WriteErrorLog("unlock error ".$COLOCKED,$LOG_ERROR_FILE);
}

sub CoLockSub
{
	my $lockfile=$COMMON_DIR."/".$LOCK_FILE;
	my $lockfiletime=$lockfile.$NOW_TIME."_".$$."_".$ENV{REMOTE_ADDR};
	$COLOCKED=$lockfiletime;
	$COLOCKED_LEVEL=1;
	foreach(1..5)
	{
		return if rename($lockfile,$lockfiletime);
		select(undef,undef,undef,0.2);
	}
	opendir(LOCKDIR,$COMMON_DIR);
	@_=grep(/^$LOCK_FILE/o,readdir(LOCKDIR));
	closedir(LOCKDIR);
	foreach(@_)
	{
		next if !/^$LOCK_FILE(\d+)/ || $NOW_TIME-$1<$AUTO_UNLOCK_TIME || !rename($COMMON_DIR."/".$_,$lockfiletime);
		select(undef,undef,undef,0.1);
		return if -e $lockfiletime;
		WriteErrorLog("lock check error",$LOG_ERROR_FILE);
	}
	WriteErrorLog("busy",$LOG_ERROR_FILE);
	$COLOCKED='';
	OutError('busy');
}

sub CoDataCA
{
	my($abort)=@_;
	
	opendir(DIR,$COTEMP_DIR);
	my @tempfile=grep(/.$FILE_EXT$/,readdir(DIR));
	closedir(DIR);
	
	my $markfile=GetPath($COMMON_DIR,$COMMIT_FILE);
	
	if(scalar(@tempfile))
	{
		OpenAndCheck($markfile),close(OUT) if !$abort;
		if(!$abort || -e $markfile)
		{
			# commit
			foreach(@tempfile)
			{
				RenameAndCheck($COTEMP_DIR."/".$_,$COMMON_DIR."/".$_);
			}
		}
		else
		{
			# abort
			foreach(@tempfile)
			{
				unlink($COTEMP_DIR."/".$_);
			}
		}
	}
	unlink($markfile) if -e $markfile;
}
1;
