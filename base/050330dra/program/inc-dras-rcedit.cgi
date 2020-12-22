# ドラゴンレース 牧場編集表示 2005/03/30 由來

ReadRanch();
$disp.="<BIG>●ドラゴンレース：牧場</BIG><br><br>";

my $functionname=$Q{code};
OutError("bad request") if !defined(&$functionname);
&$functionname;

WriteRanch();
RenewDraLog();
CoDataCA();
1;


sub new
{
OutError("bad request") if ($MYRC!=-1);
OutError('資金の余裕がありません。') if ($DT->{money} < $RCest);

	# 名前の正当性をチェック
	require $JCODE_FILE;
	$Q{name}=jcode::sjis($Q{name},$CHAR_SHIFT_JIS&&'sjis');

	if(!$Q{name})
	{
		OutError('名前を入力してください。');
	}
	if($Q{name} =~ /([,:;\t\r\n<>&])/ || CheckNGName($Q{name}) )
	{
		OutError('名前に使用できない文字が含まれています。');
	}
	OutError('名前が長すぎます。') if length($Q{name})>20;
	OutError('名前が短すぎます。') if length($Q{name})<6;

	@RC=reverse(@RC);
	$RCcount++;
	my $i=$RCcount;
	$RC[$i]->{no}=($i > 0) ? ($RC[$i-1]->{no} + 1) : 1 ;
	$RC[$i]->{birth}=$NOW_TIME;
	$RC[$i]->{name}=$Q{name};
	$RC[$i]->{town}=$MYDIR;
	$RC[$i]->{owner}=$DT->{id};
	@RC=reverse(@RC);

WritePayLog($MYDIR,$DT->{id},-$RCest);
PushDraLog(0,"新しい牧場「".$Q{name}."」が設立されました。");
$disp.="新しい牧場「<b>".$Q{name}."</b>」を設立しました。";
}

