# guildsub プラグイン 2003/11/03 由來

sub ReadGuild
{
	my($code)=@_;
	
	undef %GUILD_DETAIL;
	
	my @guildlist=GetGuildDirFiles();
	
	return "" if !scalar(@guildlist);
	
	foreach my $code (@guildlist)
	{
		my @data=ReadConfig($COMMON_DIR."/".$code.".pl");	#ギルドファイルのみ拡張子変更
		$GUILD_DETAIL{$code}={'code',$code,@data} if scalar(@data);
	}
	
	return ($code ne '' ? $GUILD_DETAIL{$code} : "");
}

sub GetGuildDirFiles
{
	opendir(DIR,$COMMON_DIR);
	my $FILE_PL='.pl';	#ギルドファイルのみ拡張子変更
	my @guildlist=sort map{/^(\w+)$FILE_PL$/} grep(/^\w+$FILE_PL$/,readdir(DIR));
	closedir(DIR);
	return @guildlist;
}

sub MakeGuildFile
{
	my @guildlist=GetGuildDirFiles();
	
	OpenAndCheck(GetPath($TEMP_DIR,$GUILD_FILE));
	print OUT '$GUILDIDX_name=0;$GUILDIDX_dealrate=1;$GUILDIDX_feerate=2;';
	print OUT '%GUILD=(';
	foreach my $code (keys(%GUILD_DETAIL))
	{
		my $detail=$GUILD_DETAIL{$code};
		print OUT "'$code'=>[";
		print OUT (GetString($detail->{shortname})),",";
		print OUT $detail->{dealrate}.",";
		print OUT $detail->{feerate}.",";
		print OUT "],";
	}
	print OUT ');1;';
	close(OUT);
	
	my %okguild=map{($_,1)}keys(%GUILD_DETAIL);
	foreach my $code (grep(!$okguild{$_},keys(%GUILD)))
	{
		next if $code eq '';
		PushLog(1,0,"ギルド「".$GUILD{$code}->[$GUILDIDX_name]."」は滅びました。",1);
		foreach my $DT (@DT)
		{
			$DT->{guild}="",delete $DT->{user}{_so_e} if ($DT->{guild} eq $code);
		}
	}
	foreach my $code (grep(!$GUILD{$_},keys(%okguild)))
	{
		next if $code eq '';
		PushLog(1,0,"ギルド「".$GUILD_DETAIL{$code}->{shortname}."」が結成されました。",1);
	}
}
1;
