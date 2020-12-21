# ギルド入団 2004/01/20 由來

CoLock() if ($Q{edit});
Lock() if ($Q{edit} eq "join");
DataRead();
CheckUserPass();
RequireFile('inc-gd.cgi');

@ENTRYnamelist=qw(
		no tm town id guild
		);
ReadEntry();

$Q{er}='gd';
RequireFile('inc-gd-entry.cgi') if ($Q{edit});
my $functionname=$Q{mode};
$functionname||="join";
OutError("bad request") if !defined(&$functionname);
&$functionname;

OutSkin();
1;


sub join
{
OutError("bad request") if ($DT->{guild});
$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>ギルド受付</SPAN>：入団するには，団長または軍師の許可が必要です。<br>
入りたいギルドの入団条件を参照し，問い合わせてみるとよいでしょう。
$TRE$TBE<br>
HTML
$disp.="ギルド戦中は入団できません",return if ($DTevent{guildbattle});
my $join="";
	foreach my $cnt(0..$Ecount)
		{
		next if ($ENTRY[$cnt]->{town} ne $MYDIR || $ENTRY[$cnt]->{id} != $DT->{id});
		my $guild=$ENTRY[$cnt]->{guild};
$join.=<<"HTML";
<form action="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<BIG>●$GUILD_DETAIL{$guild}->{shortname}</BIG>：入団許可が出ています。 
<INPUT TYPE=HIDDEN NAME=edit VALUE="join">
<INPUT TYPE=HIDDEN NAME=guild VALUE="$guild">
<INPUT TYPE=SUBMIT VALUE="入団する">
</form><br>
HTML
	}
$disp.=($join) ? $join : "入団許可が出ていません";
}

sub submit
{
OutError("bad request") if (!$DT->{guild});
my $checkok;
$ckeckok=1 if ($GUILD_DETAIL{$DT->{guild}}->{leadt} eq $MYDIR && $GUILD_DETAIL{$DT->{guild}}->{leader} == $DT->{id});
$ckeckok=1 if ($GUILD_DETAIL{$DT->{guild}}->{$MYDIR} == $DT->{id});
OutError("bad request") if (!$ckeckok);

ReadLetterName();
$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>ギルド受付</SPAN>：誰の入団を許可しますか？<br>
一度許可すると，撤回はできないのでご注意ください。
$TRE$TBE<br>
HTML
$disp.="ギルド戦中は許可できません",return if ($DTevent{guildbattle});
EntryList() if scalar(@MYENTRY);
EntryForm();
}

sub EntryList
{
	$disp.=<<"HTML";
$TB$TR
$TDB店名
$TDB所属街
$TDB有効期限
$TRE
HTML

foreach my $i(@MYENTRY)
	{
	my($no,$town,$id)=($ENTRY[$i]->{no},$ENTRY[$i]->{town},$ENTRY[$i]->{id});
	my $sname=SearchLetterName($id,$town);
	$disp.=$TR.$TD.$sname;
	$disp.=$TD.$Tname{$town};
	$disp.="$TDあと".GetTime2HMS($ENTRY[$i]->{tm}-$NOW_TIME);
	}
$disp.=$TRE.$TBE."<br>";
}

sub EntryForm
{
$disp.=<<"HTML";
<FORM ACTION="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
$TB
$TR$TDB<b>入団許可</b>（いずれか１つ）
HTML

my $r=int(scalar(@OtherDir) / 2 + 0.5);$r||=1;
foreach(0..$#OtherDir)
	{
	my $pg=$OtherDir[$_];
	$disp.=( ($_ % $r) ? "<br>" : $TD);
	$disp.="$Tname{$pg} <SELECT NAME=$pg><OPTION VALUE=\"\">選択";
	foreach my $i(0..$Ncount{$pg})
		{
		$disp.="<OPTION VALUE=\"$LID{$pg}[$i]\"".($Q{$pg}==$LID{$pg}[$i] ? ' SELECTED' : '').">$LNAME{$pg}[$i]";
		}
	$disp.="</SELECT>\n";
	}
$disp.=<<"HTML";
$TRE$TBE
<br><INPUT TYPE=HIDDEN NAME=edit VALUE="new">
<INPUT TYPE=SUBMIT VALUE="入団を許可する">
</FORM>
HTML
}

sub joind
{
$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>ギルド受付</SPAN>：入団手続を完了しました。<br>
ギルドの作戦室などであいさつしておくとよいでしょう。
$TRE$TBE<br>
HTML
}

sub ReadEntry
{
	undef @ENTRY;
	undef @MYENTRY;
	open(IN,GetPath($COMMON_DIR,"entry")) or return;
	my @ent=<IN>;
	close(IN);
	$Ecount=$#ent;
	return if $Ecount < 0;
	foreach my $cnt(0..$Ecount)
		{
		chop $ent[$cnt];
		my @buf=split(/,/,$ent[$cnt]); my $i=0;
		foreach (@ENTRYnamelist) { $ENTRY[$cnt]->{$_}=$buf[$i];$i++;}
		undef $ENTRY[$cnt],next if ($ENTRY[$cnt]->{tm} < $NOW_TIME);	# 期限切れを削除。
		push(@MYENTRY, $cnt) if ($ENTRY[$cnt]->{guild} eq $DT->{guild});
	}
}

