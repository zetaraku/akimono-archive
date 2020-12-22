# name プラグイン 2003/10/08 由來

sub CheckNGName
{
	my($sname)=@_;
	return scalar(grep(index($sname,$_)!=-1,@NG_SHOP_NAME));
}

sub GetDoubleName
{
	my @OtherDir=($MYDIR) if !$NEW_OTHERTOWN_BLOCK;
	foreach my $pg(@OtherDir)
	{
	my $datafile='../'.$pg.'/data/user.cgi';
	my($name)=@_;
	open(IN,$datafile) or return();
	my @data=<IN>;
	close(IN);
	my @list=map{(split(/\t/,$_))[1]}@data;
	@list=grep($_ eq $name,@list) if $name ne '';
	return @list if (@list);
	}
}
1;
