# ギルド人事 2004/01/20 由來

Lock(), $Q{mode}=$Q{edit} if $Q{edit};
DataRead();
CheckUserPass();
RequireFile('inc-gd.cgi');

$Q{er}='gd';
my $functionname=$Q{mode};
$functionname||="leave";
OutError("bad request") if !defined(&$functionname);
&$functionname;

OutSkin();
1;


sub leave
{
OutError("bad request") if (!$DT->{guild});
$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>ギルド受付</SPAN>：ギルドを退団しますか？<br>
メンバーに連絡してから退団することをおすすめします。
$TRE$TBE<br>
HTML
$disp.="ギルド戦中は退団できません",return if ($DTevent{guildbattle});
$disp.=<<STR;
	<form action="action.cgi" $METHOD>
	<INPUT TYPE=HIDDEN NAME=key VALUE="user">
	<INPUT TYPE=HIDDEN NAME=mode SIZE=10 VALUE="guild">
	$USERPASSFORM
	<SPAN>ギルド退団</SPAN>
	<INPUT TYPE=TEXT NAME=guild SIZE=10 VALUE="">
	(leaveと入力)
	<INPUT TYPE=SUBMIT VALUE="退団する"></FORM>
STR
}

sub submit
{
OutError("bad request") if (!$DT->{guild});
my $checkok;
$ckeckok=1 if ($GUILD_DETAIL{$DT->{guild}}->{leadt} eq $MYDIR && $GUILD_DETAIL{$DT->{guild}}->{leader} == $DT->{id});
$ckeckok=1 if ($GUILD_DETAIL{$DT->{guild}}->{$MYDIR} == $DT->{id});
OutError("bad request") if (!$ckeckok);
$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>ギルド受付</SPAN>：人事室では，メンバーに肩書きをつけたり，退団させたりできます。<br>
ただし，この街のメンバーに限りますのでご注意ください。
$TRE$TBE<br>
HTML

my $formmember;
foreach(@DT)
{
	next if ($_->{guild} ne $DT->{guild});
	$formmember.="<OPTION VALUE=\"$_->{id}\">$_->{shopname}";
}

$disp.=<<STR;
<form action="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<BIG>●肩書き命名</BIG>：
<INPUT TYPE=HIDDEN NAME=edit VALUE="name">
<SELECT NAME=id SIZE=1>
<OPTION VALUE="">選択
$formmember
</SELECT> の肩書きを
<INPUT TYPE=TEXT NAME=name SIZE=16 VALUE="">
と <INPUT TYPE=SUBMIT VALUE="命名する"> (20文字以内)
</FORM>
<hr width=500 noshade size=1>
<form action="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<SPAN>退団処分</SPAN>：
<INPUT TYPE=HIDDEN NAME=edit VALUE="fire">
<SELECT NAME=id SIZE=1>
<OPTION VALUE="">選択
$formmember
</SELECT> を <INPUT TYPE=SUBMIT VALUE="退団させる">
<INPUT TYPE=TEXT NAME=guild SIZE=10 VALUE="">
(leaveと入力)
</FORM>
STR
}

sub name
{
OutError("bad request") if (!$DT->{guild});
my $checkok;
$ckeckok=1 if ($GUILD_DETAIL{$DT->{guild}}->{leadt} eq $MYDIR && $GUILD_DETAIL{$DT->{guild}}->{leader} == $DT->{id});
$ckeckok=1 if ($GUILD_DETAIL{$DT->{guild}}->{$MYDIR} == $DT->{id});
OutError("bad request") if (!$ckeckok);

OutError('命名する相手を選んでください。') if !$Q{id};
OutError('存在しない店舗です。') if !defined($id2idx{$Q{id}});
my $tg=$id2idx{$Q{id}};
OutError('命名権限がありません。') if ($DT[$tg]->{guild} ne $DT->{guild});
OutError('肩書きが長すぎです。') if length($Q{name})>20;

$DT[$tg]->{user}{_so_e}=$Q{name};
my $ret=$DT[$tg]->{shopname}."を「".$Q{name}."」に叙しました。";
PushLog(2,0,"ギルド「".$GUILD{$DT->{guild}}->[$GUILDIDX_name]."」は".$ret);
$disp.=$ret;

RenewLog();
DataWrite();
DataCommitOrAbort();
UnLock();
}

sub fire
{
OutError("bad request") if (!$DT->{guild});
my $checkok;
$ckeckok=1 if ($GUILD_DETAIL{$DT->{guild}}->{leadt} eq $MYDIR && $GUILD_DETAIL{$DT->{guild}}->{leader} == $DT->{id});
$ckeckok=1 if ($GUILD_DETAIL{$DT->{guild}}->{$MYDIR} == $DT->{id});
OutError("bad request") if (!$ckeckok);

OutError('退団させるメンバーを選んでください。') if !$Q{id};
OutError('存在しない店舗です。') if !defined($id2idx{$Q{id}});
my $tg=$id2idx{$Q{id}};
OutError('権限がありません。') if ($DT[$tg]->{guild} ne $DT->{guild});
OutError('団長を退団させることはできません。') if ($GUILD_DETAIL{$DT->{guild}}->{leadt} eq $MYDIR && $GUILD_DETAIL{$DT->{guild}}->{leader} == $Q{id});
OutError('退団させるにはleaveと入力してください') if $Q{guild} ne 'leave';

delete $DT[$tg]->{user}{_so_e};
$DT[$tg]->{guild}="";
my $name=$GUILD{$DT->{guild}}->[$GUILDIDX_name];
PushLog(1,0,$DT[$tg]->{shopname}."がギルド「".$name."」から除名されました。");
$disp.=$DT[$tg]->{shopname}."を退団させました。";

RenewLog();
DataWrite();
DataCommitOrAbort();
UnLock();
}

