# ギルド編集フォーム 2004/01/20 由來

$NOITEM=1;
DataRead();
CheckUserPass(1);
RequireFile('inc-gd.cgi');

if ($DT->{guild})
{
GuildEditMenu();
}
elsif ($DT->{dignity} < $DIG_FORGUILD)
{
$disp.=$TB.$TR.$TD.$image[0].$TD."<SPAN>ギルド受付</SPAN>：こちらはギルド結成届出所です。<br>";
$disp.="ギルドを結成するには，$DIG_FORGUILDポイント以上の爵位が必要となります。".$TRE.$TBE."<br>";
$disp.="条件を満たしていません";
}
else
{
GuildBuildMenu();
}
OutSkin();
1;


sub GuildEditMenu
{
my $leaderid=$GUILD_DETAIL{$DT->{guild}}->{leader};
OutError('ギルドを変更できるのは団長だけです') if (defined($id2idx{$leaderid}) && $leaderid != $DT->{id});
ReadLetterName();
$code=$DT->{guild};
$GUILD_DETAIL{$code}->{url}="http://" if !$GUILD_DETAIL{$code}->{url};
$disp.=$TB.$TR.$TD.$image[0].$TD."<SPAN>ギルド受付</SPAN>：こちらは".GetTagImgGuild($code);
$disp.="<BIG>".$GUILD{$code}->[$GUILDIDX_name]."</BIG> 執務室です。<br>";
$disp.="団長様，今後のギルドをどのようになさるおつもりですか？".$TRE.$TBE."<br>";
my $i=GuildCommonForm();

$disp.=<<"HTML";
<FORM ACTION="action.cgi" enctype="multipart/form-data" $METHOD>
<INPUT TYPE=hidden NAME=key VALUE="gd-b">
$USERPASSFORM
<INPUT TYPE=hidden NAME=mode VALUE="edit">
$TB$TR$TDB<b>ギルドコード</b>
<td colspan=2><b>$code</b><INPUT TYPE=HIDDEN NAME=code VALUE="$code">$TRE
$TR$TDB<b>ギルド画像</b><br>(32*16pt)
<td colspan=2>gif形式画像のみ（指定しないと現状のまま）<br><input type=file name=upfile size=36>$TRE
$TR$TDB<b>ギルドホームページ</b><br>(60文字以内)
<td colspan=2>一般向けホームページ<br><INPUT TYPE=TEXT NAME=url SIZE=56 VALUE="$GUILD_DETAIL{$code}->{url}">$TRE
$i
$TR$TDB<b>軍師任命</b><br>(各街 1名まで)
HTML

my $r=int(scalar(@OtherDir) / 2 + 0.5);$r||=1;
foreach(0..$#OtherDir)
	{
	my $pg=$OtherDir[$_];
	$disp.=( ($_ % $r) ? "<br>" : $TD);
	$disp.="$Tname{$pg} <SELECT NAME=$pg><OPTION VALUE=\"\">－－－－";
	foreach my $i(0..$Ncount{$pg})
		{
		$disp.="<OPTION VALUE=\"$LID{$pg}[$i]\"".($GUILD_DETAIL{$code}->{$pg}==$LID{$pg}[$i] ? ' SELECTED' : '').">$LNAME{$pg}[$i]";
		}
	$disp.="</SELECT>\n";
	}

$disp.=<<"HTML";
$TRE$TBE
<br><INPUT TYPE=SUBMIT VALUE="以上の内容で決定">
<br>(反映されるには数分かかります)
</FORM>
HTML
}


sub GuildBuildMenu
{
$code="";
$disp.=$TB.$TR.$TD.$image[0].$TD."<SPAN>ギルド受付</SPAN>：こちらはギルド結成届出所です。<br>";
$disp.="新しい団長様，どのようなギルドを結成なさるおつもりですか？".$TRE.$TBE."<br>";
my $i=GuildCommonForm();

$disp.=<<"HTML";
<FORM ACTION="action.cgi" enctype="multipart/form-data" $METHOD>
<INPUT TYPE=hidden NAME=key VALUE="gd-b">
$USERPASSFORM
<INPUT TYPE=hidden NAME=mode VALUE="make">
$TB$TR$TDB<b>ギルドコード</b><br>(10文字以内)
<td colspan=2>半角英数<b>小文字のみ</b><br><INPUT TYPE=TEXT NAME=code SIZE=10 VALUE="">$TRE
$TR$TDB<b>ギルド画像</b><br>(32*16pt)
<td colspan=2>gif形式画像のみ<br><input type=file name=upfile size=36>$TRE
$i
$TBE
<br><INPUT TYPE=SUBMIT VALUE="以上の内容で決定">
<br>(反映されるには数分かかります)
</FORM>
HTML
}

sub GuildCommonForm
{
my $i.=<<"HTML";
$TR$TDB<b>ギルド正式名称</b><br>(30文字以内)
<td colspan=2>詳細表\示の際に使われる名前<br><INPUT TYPE=TEXT NAME=name SIZE=24 VALUE="$GUILD_DETAIL{$code}->{name}">$TRE
$TR$TDB<b>ギルド通称</b><br>(12文字以内)
<td colspan=2>通常使われる名前<br><INPUT TYPE=TEXT NAME=shortname SIZE=12 VALUE="$GUILD_DETAIL{$code}->{shortname}">$TRE
$TR$TDB<b>ギルド間割引増率</b><br>(半角数字のみ)
<td colspan=2>10倍の値を指定（30%にするには300と記入。10～500）<br><INPUT TYPE=TEXT NAME=dealrate SIZE=6 VALUE="$GUILD_DETAIL{$code}->{dealrate}">$TRE
$TR$TDB<b>ギルド間会費率</b><br>(半角数字のみ)
<td colspan=2>10倍の値を指定（3%にするには30と記入。10～500）<br><INPUT TYPE=TEXT NAME=feerate SIZE=6 VALUE="$GUILD_DETAIL{$code}->{feerate}">$TRE
$TR$TDB<b>メンバー呼称</b><br>(6文字以内)
<td colspan=2>「会員」「同志」など<br><INPUT TYPE=TEXT NAME=member SIZE=6 VALUE="$GUILD_DETAIL{$code}->{member}">$TRE
$TR$TDB<b>決め台詞</b><br>(30文字以内)
<td colspan=2>一覧に表\示される看板文句<br><INPUT TYPE=TEXT NAME=comment SIZE=24 VALUE="$GUILD_DETAIL{$code}->{comment}">$TRE
$TR$TDB<b>活動紹介</b><br>(120文字以内)
<td colspan=2>ギルドの活動目的や内容<br><INPUT TYPE=TEXT NAME=appeal SIZE=60 VALUE="$GUILD_DETAIL{$code}->{appeal}">$TRE
$TR$TDB<b>入団条件</b><br>(120文字以内)
<td colspan=2>「入りたい方は団長宛てに手紙を」など<br><INPUT TYPE=TEXT NAME=needed SIZE=60 VALUE="$GUILD_DETAIL{$code}->{needed}">$TRE
HTML
return $i;
}

