# 結婚 2004/01/20 由來

@BRIDEnamelist=qw(
	no tm mode ida idb stbase ctbase money place reform
	);
$image[0]='<IMG ALT="住宅" WIDTH="19" HEIGHT="22" BORDER="0" SRC="'.$IMAGE_URL.'/house1.gif">共用倉庫';
$image[1]='<IMG ALT="住宅" WIDTH="19" HEIGHT="22" BORDER="0" SRC="'.$IMAGE_URL.'/house1.gif">一戸建て';
$image[2]='<IMG ALT="プロポーズ" WIDTH="16" HEIGHT="16" BORDER="0" SRC="'.$IMAGE_URL.'/house2.png">プロポーズ';
$image[3]=GetTagImgKao("神父","father");

Lock() if ($Q{mode});	# できるだけ早くロック。
DataRead();
CheckUserPass(1);
ReadBride();
RequireFile('inc-html-bride-edit.cgi') if ($Q{mode});	# 各種データ処理

if ($Q{no})
{
RequireFile('inc-html-bride-list.cgi');
}
else
{
$disp.="<BIG>●教会</BIG><br><br>";
RequireFile('inc-html-bride.cgi');
}

OutSkin();
1;


sub ReadBride
{
	open(IN,GetPath('bride')) or return;
	my @bride=<IN>;
	close(IN);
	$married=0;
	$Scount=$#bride;
	foreach my $cnt(0..$Scount)
		{
		chop $bride[$cnt];
		my @buf=split(/,/,$bride[$cnt]); my $i=0;
		foreach (@BRIDEnamelist) { $BRIDE[$cnt]->{$_}=$buf[$i];$i++;}
		undef $BRIDE[$cnt],next if !defined($id2idx{$BRIDE[$cnt]->{ida}}) || !defined($id2idx{$BRIDE[$cnt]->{idb}});	# 閉店，移転による消滅。
		@BRIDE[$cnt]->{stock}=[split(/:/,$BRIDE[$cnt]->{stbase})];
		@BRIDE[$cnt]->{cnt}=[split(/:/,$BRIDE[$cnt]->{ctbase})];
		$BRIDE[$cnt]->{point}=0;
		$BRIDE[$cnt]->{point}=$DT[$id2idx{$BRIDE[$cnt]->{ida}}]->{point}+$DT[$id2idx{$BRIDE[$cnt]->{idb}}]->{point} if ($BRIDE[$cnt]->{mode});
		$married=1 if ($DT->{id} == $BRIDE[$cnt]->{ida}) || ($DT->{id} == $BRIDE[$cnt]->{idb});
		}
}

sub SearchBride
{
	my($no)=@_;
	my $idx=-1;
	foreach(0..$Scount)
	{
		if($BRIDE[$_]->{no}==$no)
		{
			$idx=$_;
			last;
		}
	}
	return $idx;
}
