# ギルド入団処理 2003/11/03 由來

my $functionname=$Q{edit};
OutError("bad request") if !defined(&$functionname);
&$functionname;
WriteEntry();
CoDataCA();
CoUnLock();
1;


sub new
{
	OutError("bad request") if (!$DT->{guild});
	my $checkok;
	$ckeckok=1 if ($GUILD_DETAIL{$DT->{guild}}->{leadt} eq $MYDIR && $GUILD_DETAIL{$DT->{guild}}->{leader} == $DT->{id});
	$ckeckok=1 if ($GUILD_DETAIL{$DT->{guild}}->{$MYDIR} == $DT->{id});
	OutError("bad request") if (!$ckeckok);
	my $town="";
	my $id="";
	foreach my $pg(@OtherDir)
		{
		$id=$Q{$pg}, $town=$pg if ($Q{$pg})
		}
	OutError('許可する相手を指定してください。') if !$id;
	foreach my $i(@MYENTRY)
		{
		OutError('すでに許可しています。') if ($ENTRY[$i]->{town} eq $town && $ENTRY[$i]->{id}==$id);
		}

	@ENTRY=reverse(@ENTRY);
	$Ecount++;
	my $i=$Ecount;
	$ENTRY[$i]->{no}=($i > 0) ? ($ENTRY[$i-1]->{no} + 1) : 1;
	$ENTRY[$i]->{tm}=$NOW_TIME + 2 * 86400;
	$ENTRY[$i]->{town}=$town;
	$ENTRY[$i]->{id}=$id;
	$ENTRY[$i]->{guild}=$DT->{guild};
	@ENTRY=reverse(@ENTRY);
	$Q{mode}="submit";
}

sub join
{
OutError("bad request") if ($DT->{guild});
OutError("ギルド戦中は入団できません") if ($DTevent{guildbattle});
my $checkok;
	foreach my $cnt(0..$Ecount)
		{
		next if ($ENTRY[$cnt]->{town} ne $MYDIR || $ENTRY[$cnt]->{id} != $DT->{id});
		my $guild=$ENTRY[$cnt]->{guild};
		undef $ENTRY[$cnt];
		next if ($Q{guild} ne $guild);
		$checkok=1;
		}
OutError("許可が出ていません") if (!$checkok);
	my $name=$GUILD{$Q{guild}}->[$GUILDIDX_name];
	my $member=$GUILD_DETAIL{$Q{guild}}->{member};
	PushLog(1,0,$DT->{shopname}."がギルド「".$name."」の".$member."となりました。");
	$DT->{guild}=$Q{guild};
RenewLog();
DataWrite();
DataCommitOrAbort();
UnLock();
$Q{mode}="joind";
}

sub WriteEntry
{
	undef @MYENTRY;		# 保存と再定義を同時に
	my @buf;
	foreach my $i(0..$Ecount)
		{
		next unless defined($ENTRY[$i]->{no});
		$buf[$i]=join(",",map{$ENTRY[$i]->{$_}}@ENTRYnamelist)."\n";
		push(@MYENTRY, $i) if ($ENTRY[$i]->{guild} eq $DT->{guild});
		}
	OpenAndCheck(GetPath($COTEMP_DIR,"entry"));
	print OUT @buf;
	close(OUT);
}


