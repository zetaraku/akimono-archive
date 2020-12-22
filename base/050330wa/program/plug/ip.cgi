# ip プラグイン 2003/07/19 由來

sub GetTrueIP
{
	my $addr=	$ENV{REMOTE_ADDR};
	my $via=	$ENV{HTTP_VIA};
	my $hua=	$ENV{HTTP_USER_AGENT};
	my $sphost=	$ENV{HTTP_SP_HOST};
	my $clip=	$ENV{HTTP_CLIENT_IP};
	my $hfrom=	$ENV{HTTP_FROM};
	my $foward=	$ENV{HTTP_FORWARDED};
	my $xfoward=$ENV{HTTP_X_FORWARDED_FOR};
	
	my $trueip=$addr;
	$trueip=$sphost if $sphost ne"";
	$trueip=$via if $via=~s/.*\s(\d+)\.(\d+)\.(\d+)\.(\d+)/$1.$2.$3.$4/;
	if($clip=~s/^(\d+)\.(\d+)\.(\d+)\.(\d+)(\D*).*/$1.$2.$3.$4/ )
	{
		$trueip=$clip;
	}
	elsif($clip=~s/^([\dA-F]{2})([\dA-F]{2})([\dA-F]{2})([\dA-F]{2})/$1$2$3$4/i)
	{
		$clip=join('.', hex($1),hex($2),hex($3),hex($4));
		$trueip=$clip;
	}
	$trueip=$foward if $foward=~s/.*\s(\d+)\.(\d+)\.(\d+)\.(\d+)/$1.$2.$3.$4/;
	$trueip=$xfoward if $xfoward=~s/^(\d+)\.(\d+)\.(\d+)\.(\d+)(\D*).*/$1.$2.$3.$4/;
	$trueip=$hfrom if $hfrom ne"";
	
	$trueip.="!".$addr if $addr ne $trueip;
	
	return $trueip;
}

sub GetIPList
{
	my($ip)=@_;
	open(IN,GetPath("user")) or return();
	my @data=<IN>;
	close(IN);
	my @list=map{(split(/\t/,$_))[4]}@data;
	@list=grep($_ eq $ip,@list) if $ip ne '';
	return @list;
}
1;
