# config プラグイン 2003/07/19 由來

sub ReadConfig
{
	open(IN,$_[0]) or return ();;
	my @data=();
	while(<IN>)
	{
		chop;
		s/#.*$//;
		#各種設定ファイルでは危険回避のため「< > "」は使用不可「&」は使用可
		#s/&/&amp;/g;
		s/</&lt;/g;
		s/>/&gt;/g;
		s/"/&quot;/g;
		push(@data,$1,$2) if /^\s*(.+?)\s*=\s*(.+?)\s*$/;
	}
	close(IN);
	return @data;
}

1;
