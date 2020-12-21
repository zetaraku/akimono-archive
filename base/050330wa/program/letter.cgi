# 郵便 2004/01/20 由來

$Q{mode}='new',  if ($Q{form} eq "make")&&($Q{ok}); 	# 送信モード切替
CoLock() if $Q{mode};

$NOITEM=1;
DataRead();
CheckUserPass();

$image[0]=GetTagImgKao("お手伝い","help");
$WriteFlag=0;						# 更新フラグ。

ReadLetterName();
ReadLetter();

RequireFile('inc-letter-edit.cgi') if ($Q{mode});	# 各種処理

if ($Q{form})
{
RequireFile('inc-letter-form.cgi');
}
else
{
RequireFile('inc-letter.cgi');
}

	if ($WriteFlag)
	{
	CoLock() if !$COLOCKED;
	WriteLetter();
	CoDataCA();
	CoUnLock();
	}
OutSkin();
1;
