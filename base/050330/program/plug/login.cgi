# login プラグイン 2003/10/08 由來

sub CheckLogin
{
	my($username,$password,$fn)=@_;
	my $trueip=GetTrueIP();
	my $ua=$ENV{HTTP_USER_AGENT};
	my $hr=$ENV{HTTP_REFERER};
	my $ha=$ENV{HTTP_ACCEPT};
	
	if (!CheckPassword($password,$name2pass{$username}))
	{
	OutError('incorrect',$password) if $password ne $MASTER_PASSWORD;
	$MASTER_USER=1;
	}
	
	$session=crypt(rand(),GetSalt());
	$session=~s/[^0-9A-Za-z]//g;
	$session=substr($session,-5,5);
	
	open(SESS,$fn); my @client=<SESS>; close(SESS);
	if($MASTER_USER)
	{
		$session=$client[0],chop($session) if ($client[0]);
		shift(@client);
	}
	else
	{
		$client[0]=join("\t",GetTime2FormatTime($NOW_TIME),$trueip,$ua,$ha)."\n";
		my %same=();
		@client=grep(!$same{(split(/\t/,$_,2))[1]}++,@client);
	}
	open(SESS,">$fn");
	print SESS $session."\n";
	print SESS @client[0..9];
	close(SESS);
	
	my $DT=$DT[$name2idx{$username}];

	if(!$MASTER_USER)
	{
		my $ipfile=GetPath("user");
		my $overlap=0;
		my @buf=();
		Lock();
		if(open(DATA,$ipfile))
		{
			my @data=<DATA>;
			close(DATA);
			foreach my $line (@data)
			{
				@_=split(/\t/,$line,2);
				next if !defined($name2idx{$_[0]}) || $_[0] eq $username;
				@_=split(/\t/,$_[1]);
				$overlap=1 if $_[3] eq $trueip && $_[4] eq $ua;
				push(@buf,$line);
			}
			push(@buf,join("\t",$username,$DT->{shopname},$DT->{id},GetTime2FormatTime($NOW_TIME),$trueip,$ua,$password)."\n");
		}
		else
			{WriteErrorLog("ip file read error ",$LOG_ERROR_FILE);}
		
		if(open(DATA,">$ipfile"))
		{
			print DATA @buf;
			close(DATA);
		}
		else
			{WriteErrorLog("ip file write error ",$LOG_ERROR_FILE);}
		
		UnLock();
		
		OutError('stop') if $DT->{blocklogin} eq 'stop';
		OutErrorBlockLogin($DT->{blocklogin}) if $DT->{blocklogin} ne '' && $DT->{blocklogin} ne 'mark';
		OutErrorBlockLogin('重複登録検出') if !$MOBILE && $CHECK_IP && !$DT->{nocheckip} && $overlap;
		
		if($DT->{blocklogin} eq 'mark')
		{
			local $USER=$username;
			WriteErrorLog("$ENV{HTTP_USER_AGENT} $ENV{HTTP_ACCEPT}",$LOG_MARK_FILE);
		}
	}
	return $session;
}

sub CheckPassword
{
	return 0 if $_[0] eq '' || $_[1] eq '' || $_[1] ne ($PASSWORD_CRYPT ? crypt($_[0],$_[1]) : $_[0]);
	return 1;
}

sub GetSalt
{
	my $saltlist='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
	my $len=length($saltlist);
	my $salt=substr($saltlist,int(rand($len)),1).substr($saltlist,int(rand($len)),1);
	return $salt;
}
1;
