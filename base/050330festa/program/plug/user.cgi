# user プラグイン 2004/02/28 由來

sub GetID2UserName
{
	my($to)=@_;
	return ("貿易","") if $to==1;
	return ($DT[$id2idx{$to}]->{shopname},$DT[$id2idx{$to}]->{name}) if defined($id2idx{$to});
	return ('閉店済','');
}

sub CheckUserID
{
	my($id,$enable0)=@_;
	$id+=0;
	
	return 0 if $enable0 && !$id;
	OutError('その店舗は存在しません。') if !defined($id2idx{$id});

	return ($id,$id2idx{$id});
}

sub GetUserData
{
	#$_[0]->{user}={split(/[\t,]/,$_[0]->{user})} if !ref($_[0]->{user});
	return $_[0]->{user};
}

sub SetUserData
{
	#$_[0]->{user}=join(",",%{$_[0]->{user}}) if ref($_[0]->{user}) eq "HASH";
}

sub GetUserDataEx
{
	my($DT,$key)=@_;
	$key=~s/%([\dA-Fa-f]{2})/pack("H2",$1)/eg;
	my $val=$DT->{user}{$key}||($DT->{user}{$key} eq '0' ? 0 : '');
	$val=~s/%([\dA-Fa-f]{2})/pack("H2",$1)/eg;
	return $val;
}

sub SetUserDataEx
{
	my($DT,$key,$val)=@_;
	$key=~s/([\x00-\x1f,%:])/'%'.unpack("H2",$1)/ge;
	$val=~s/([\x00-\x1f,%:])/'%'.unpack("H2",$1)/ge;
	delete($DT->{user}{$key}),return '' if $val eq '';
	return $DT->{user}{$key}=$val;
}

sub ReadDTSub
{
	my($DT,$tag)=@_;
	
	return 0 if !$DT or !$DT->{id}; # error $DT
	return $DT->{"_$tag"}={} if !open(IN,GetPath($SUBDATA_DIR,$DT->{id}."-$tag")); # no file
	
	my @line=<IN>; # IN: key <LF> value <LF> key <LF> value <LF> ...
	close(IN);
	chop @line;
	
	foreach(@line){s/%([\dA-Fa-f]{2})/pack("H2",$1)/eg} # unescape
	
	return $DT->{"_$tag"}={@line};
}

sub WriteDTSub
{
	my($DT,$tag)=@_;
	
	CheckLockStatus();
	
	return 0 if !$DT or !$DT->{id}; # error $DT
	
	my $data=$DT->{"_$tag"}||{};
	while(my($key,$val)=each %$data){delete $data->{$key} if $data->{$key} eq ""} # delete empty data
	
	my @line=%$data;
	foreach(@line){s/([\x00-\x1f%])/'%'.unpack("H2",$1)/ge} # escape
	
	OpenAndCheck(GetPath($SUBDATA_DIR,$DT->{id}."-$tag"));
	print OUT join "\n",@line,"";
	close(OUT);
	
	return 1;
}

1;
