# lock プラグイン 2003/07/19 由來

sub Lock
{
	$LOCKED_LEVEL++,return if $LOCKED ne '';
	LockSub();
	DataCommitOrAbort(1); # abort
}

sub UnLock
{
	return if $LOCKED eq '' || --$LOCKED_LEVEL;
	$LOCKED='',return if rename($LOCKED,$DATA_DIR."/".$LOCK_FILE);
	WriteErrorLog("unlock error ".$LOCKED,$LOG_ERROR_FILE);
}

sub LockSub
{
	my $lockfile=$DATA_DIR."/".$LOCK_FILE;
	my $lockfiletime=$lockfile.$NOW_TIME."_".$$."_".$ENV{REMOTE_ADDR};
	$LOCKED=$lockfiletime;
	$LOCKED_LEVEL=1;
	foreach(1..5)
	{
		return if rename($lockfile,$lockfiletime);
		select(undef,undef,undef,0.2);
	}
	opendir(LOCKDIR,$DATA_DIR);
	@_=grep(/^$LOCK_FILE/o,readdir(LOCKDIR));
	closedir(LOCKDIR);
	foreach(@_)
	{
		next if !/^$LOCK_FILE(\d+)/ || $NOW_TIME-$1<$AUTO_UNLOCK_TIME || !rename($DATA_DIR."/".$_,$lockfiletime);
		select(undef,undef,undef,0.1);
		return if -e $lockfiletime;
		WriteErrorLog("lock check error",$LOG_ERROR_FILE);
	}
	WriteErrorLog("busy",$LOG_ERROR_FILE);
	$LOCKED='';
	OutError('busy');
}

sub RenameAndCheck
{
	foreach(1..5)
	{
		select(undef,undef,undef,0.2),next if !rename($_[0],$_[1]);
		return if !-e $_[0] && -e $_[1];
	}
	WriteErrorLog('rename error '.$_[0]."->".$_[1],$LOG_ERROR_FILE);
	OutError('異常処理です。中断しました。');
}

sub OpenAndCheck
{
	my $count=5;
	while(!open(OUT,">".$_[0]))
	{
		WriteErrorLog('write mode open error',$LOG_ERROR_FILE),OutError('異常処理です。中断しました。') if !$count--;
		select(undef,undef,undef,0.2);
	}
}

1;
