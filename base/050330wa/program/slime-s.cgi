# ドラゴンレース処理 2005/03/30 由來

$NOITEM=1;
$NOMENU=1;
CoLock();
DataRead();
CheckUserPass();
RequireFile('inc-dragon.cgi');

RequireFile("inc-dras-$Q{mode}.cgi");
CoUnLock();
OutSkin();
1;

