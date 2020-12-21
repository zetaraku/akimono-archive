# BGM 2003/09/25 由來

$NOMENU=1;
$Q{bk}="none";
$USERPASSURL="u=$Q{u}" if $Q{u};

print "Content-type: text/html\n\n";
print <<"EOM";
<html lang="ja">
<head><title>$HTML_TITLE</title>
</head>
<frameset rows="0,*" border="0" frameborder="NO">
<frame name="bgm" src="action.cgi?key=midi&$USERPASSURL" noresize>
<frame name="game" src="action.cgi?key=$Q{mode}&$USERPASSURL">
<noframes>
<body>フレーム非対応のブラウザの方はご利用できません</body>
</noframes>
</frameset>
</html>
EOM
exit;
1;
