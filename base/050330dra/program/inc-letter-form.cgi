# フォーム表示 2004/01/20 由來

$disp.=GetMenuTag('letter','[受信箱]')
	.GetMenuTag('letter','[送信箱]','&old=list')
	."<b>[手紙を書く]</b>";
$disp.="<hr width=500 noshade size=1>";
my $cnt=$MAX_BOX - scalar(@SENLETTER);
if ($cnt > 0)
{
$preerror="";
LFormCheck() if ($Q{form} eq 'check');
NewLform() if ($preerror || $Q{form} eq 'make');
}
else
{
$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>お手伝い</SPAN>：これ以上の手紙を送ることはできません。<br>
送信済みの手紙を削除してください。
$TRE$TBE
HTML

}


1;

sub NewLform
{
$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>お手伝い</SPAN>：あと $cnt通まで手紙を送ることができます。<br>
マナーを守り，もらう立場の人のことを考えて書きましょう。
$TRE$TBE<br>$preerror
<FORM ACTION="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
$TB
$TR$TDB<b>宛先</b>（いずれか１つ）
HTML

my $r=int(scalar(@OtherDir) / 2 + 0.5);$r||=1;
foreach(0..$#OtherDir)
	{
	my $pg=$OtherDir[$_];
	$disp.=( ($_ % $r) ? "<br>" : $TD);
	$disp.="$Tname{$pg} <SELECT NAME=$pg><OPTION VALUE=\"-1\">宛先選択";
	foreach my $i(0..$Ncount{$pg})
		{
		$disp.="<OPTION VALUE=\"$LID{$pg}[$i]\"".($Q{$pg}==$LID{$pg}[$i] ? ' SELECTED' : '').">$LNAME{$pg}[$i]";
		}
	$disp.="</SELECT>\n";
	}

$disp.=<<"HTML";
$TRE
$TR$TDB<b>タイトル</b>（40字以内）
<td colspan=2><INPUT TYPE=TEXT NAME=title SIZE=40 VALUE="$Q{title}">$TRE
$TR$TDB<b>内容</b>（400字以内）
<td colspan=2><INPUT TYPE=TEXT NAME=msg SIZE=60 VALUE="$Q{msg}">$TRE
$TBE
<br><INPUT TYPE=HIDDEN NAME=form VALUE="check">
<INPUT TYPE=SUBMIT VALUE="送信確認">
</FORM>
HTML
}

sub LFormCheck
{
my $sendmail="";
my $sendto="";
foreach my $pg(@OtherDir)
	{
	$sendmail=$Q{$pg}, $sendto=$pg if ($Q{$pg} != -1)
	}
$preerror="宛先を指定してください。", return if !$sendto;
my $Ln=SearchLetterName($sendmail,$sendto);
$preerror="存在しない店舗です。", return if ($Ln == -1);
$preerror="メッセージを記入してください。", return if (!$Q{msg});
$Q{title}="（無題）" if !$Q{title};
$preerror='タイトルは半角40字(全角20字)までです。現在半角'.length($Q{title}).'字です。', return if length($Q{title})>40;
$preerror='内容文は半角400文字(全角200文字)までです。現在半角'.length($Q{msg}).'文字です。', return if length($Q{msg})>400;

$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
お手伝い：以下の内容で手紙を送ります。<br>
これでよろしいかご確認ください。
$TRE$TBE<br>
<table width=60%>$TR$TD
<SPAN>宛先</SPAN>：$Ln <small>（$Tname{$sendto}）</small><br>
<SPAN>タイトル</SPAN>：「$Q{title}」<br>
<SPAN>内容</SPAN>：$Q{msg}<br>
$TRE$TBE
<FORM ACTION="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=$sendto VALUE="$sendmail">
<INPUT TYPE=HIDDEN NAME=title VALUE="$Q{title}">
<INPUT TYPE=HIDDEN NAME=msg VALUE="$Q{msg}">
<INPUT TYPE=HIDDEN NAME=form VALUE="make">
<INPUT TYPE=SUBMIT NAME=ok VALUE="送信">
<INPUT TYPE=SUBMIT NAME=ng VALUE="再編集">
</FORM>
HTML
}
