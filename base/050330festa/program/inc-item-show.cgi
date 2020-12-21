# アイテム陳列下請け 2004/01/20 由來

$disp.=<<STR;
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="sc-s">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=bk VALUE="$Q{bk}">
<INPUT TYPE=HIDDEN NAME=item VALUE="$itemno">
<BIG>●陳列：</BIG>
<SELECT NAME=no>
STR
foreach my $cnt (1..$DT->{showcasecount})
{
	$disp.="<OPTION VALUE='".($cnt-1)."'".($showcase==$cnt?' SELECTED':'').">";
	$disp.="棚$cnt($ITEM[$DT->{showcase}[$cnt-1]]->{name})";
}
	$disp.="</SELECT>";
	$disp.="へ標準価格の";
	$disp.=<<STR;
<SELECT NAME=per>
<OPTION VALUE='50'>5割引
<OPTION VALUE='60'>4割引
<OPTION VALUE='70'>3割引
<OPTION VALUE='80'>2割引
<OPTION VALUE='90'>1割引
<OPTION VALUE='100' SELECTED>まま
<OPTION VALUE='110'>1割増
<OPTION VALUE='120'>2割増
</SELECT>
または
<INPUT TYPE=TEXT NAME=prc SIZE=6 VALUE="$Q{pr}">円
で
<INPUT TYPE=SUBMIT VALUE='陳列する'>
(時間${\GetTime2HMS($TIME_EDIT_SHOWCASE)}消費)
</FORM>
STR
1;
