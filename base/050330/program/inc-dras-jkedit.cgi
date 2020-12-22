# ドラゴンレース 騎手編集 2005/03/30 由來

ReadJock();
$disp.="<BIG>●ドラゴンレース：騎手</BIG><br><br>";

my $functionname=$Q{code};
OutError("bad request") if !defined(&$functionname);
&$functionname;

WriteJock();
RenewDraLog();
CoDataCA();
1;


sub new
{
OutError("bad request") if ($MYJK!=-1);
OutError("bad request") if (scalar @JK >= $JKmax);
OutError('資金の余裕がありません。') if ($DT->{money} < $JKest);

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

	@JK=reverse(@JK);
	$JKcount++;
	my $i=$JKcount;
	$JK[$i]->{no}=($i > 0) ? ($JK[$i-1]->{no} + 1) : 1 ;
	$JK[$i]->{birth}=$NOW_TIME;
	$JK[$i]->{name}=$Q{name};
	$JK[$i]->{town}=$MYDIR;
	$JK[$i]->{owner}=$DT->{id};
	$JK[$i]->{ahead}=int(rand(15));
	$JK[$i]->{back}=int(rand(15));

	# 特徴付与
	if ($JK[$i]->{ahead} > $JK[$i]->{back})
		{
		$JK[$i]->{ahead}+=15;
		}
		else
		{
		$JK[$i]->{back}+=15;
		}
	@JK=reverse(@JK);

WritePayLog($MYDIR,$DT->{id},-$JKest);
PushDraLog(0,"新しい騎手「".$Q{name}."」がデビューしました。");
$disp.="新しい騎手「<b>".$Q{name}."</b>」を雇いました。";
}

