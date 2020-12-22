# 手紙編集 2003/07/19 由來

if ($Q{mode} eq 'new')
{
	$Q{old} = "list";	#送信済みトレイを表示。
	$Q{form} = "";
	NewLetter();
}
else
{
	undef @RECLETTER;
	$NeverR=0;
	undef @SENLETTER;
	$NeverS=0;
	foreach my $i(0..$Lcount)
	{
	my $delete="del_".$LETTER[$i]->{no};
	$LETTER[$i]->{mode}=2 , next if ($Q{$delete});
	if ($MYDIR eq $LETTER[$i]->{tot} && $LETTER[$i]->{toid}==$DT->{id})
		{
		push(@RECLETTER, $i);
		$NeverR++ if ($LETTER[$i]->{mode}==1);
		}
	if ($MYDIR eq $LETTER[$i]->{fromt} && $LETTER[$i]->{fromid}==$DT->{id})
		{
		push(@SENLETTER, $i);
		$NeverS++ if ($LETTER[$i]->{mode}==1);
		}
	}
}

$WriteFlag=1;		# データ更新を指示。
1;


sub NewLetter
{
my $sendmail="";
my $sendto="";
foreach my $pg(@OtherDir)
	{
	$sendmail=$Q{$pg}, $sendto=$pg if ($Q{$pg})
	}
OutError('宛先を指定してください。') if !$sendto;

	CheckNewBoxArg();

	@LETTER=reverse(@LETTER);
	$Lcount++;
	my $i=$Lcount;
	$LETTER[$i]->{no}=($i) ? ($LETTER[$i-1]->{no} + 1) : 1 ;
	$LETTER[$i]->{time}=$NOW_TIME;
	$LETTER[$i]->{fromt}=$MYDIR;
	$LETTER[$i]->{fromid}=$DT->{id};
	$LETTER[$i]->{tot}=$sendto;
	$LETTER[$i]->{toid}=$sendmail;
	$LETTER[$i]->{title}=$Q{title};
	$LETTER[$i]->{msg}=$Q{msg};
	$LETTER[$i]->{mode}=1;	#未読設定
	$LETTER[$i]->{other}=$DT->{shopname};
	@LETTER=reverse(@LETTER);

	undef @SENLETTER;	# 読み直し
	$NeverS=0;
	foreach my $i(0..$Lcount)
	{
	if ($MYDIR eq $LETTER[$i]->{fromt} && $LETTER[$i]->{fromid}==$DT->{id})
		{
		push(@SENLETTER, $i);
		$NeverS++ if ($LETTER[$i]->{mode}==1);
		}
	}
}

sub CheckNewBoxArg
{
	require $JCODE_FILE;
	
	$Q{msg}=CutStr(jcode::sjis($Q{msg},$CHAR_SHIFT_JIS&&'sjis'),400);
	$Q{title}=CutStr(jcode::sjis($Q{title},$CHAR_SHIFT_JIS&&'sjis'),40);
	OutError('内容がありません') if $Q{msg}eq'';
	$Q{title}="（無題）" if $Q{title}eq'';
}
