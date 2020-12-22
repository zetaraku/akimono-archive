# 新聞 2004/01/20 由來

$NOITEM=1 if ($Q{t}==1);
DataRead();
CheckUserPass(1);

$disp.=GetMenuTag('log',	'[速報]')
	.GetMenuTag('log',	'[入賞]','&t=3')
	.GetMenuTag('log',	'[順位]','&t=4')
	.GetMenuTag('log',	'[爵位]','&t=5');
$disp.="<hr width=500 noshade size=1>";

if ($Q{t}==5) {
RequireFile('inc-html-ranking-2.cgi');
} elsif ($Q{t}==4) {
RequireFile('inc-html-ranking.cgi');
} elsif ($Q{t}==3) {
RequireFile('inc-html-ranking-3.cgi');
} else {
ReadLog($DT->{id},$Q{lmd}+0,$Q{kw},$Q{tgt});
RequireFile('inc-html-log.cgi');
}

OutSkin();
1;
