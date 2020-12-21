# ドラゴンレース 厩舎編集 2005/03/30 由來

ReadStable();
$disp.="<BIG>●ドラゴンレース：厩舎</BIG><br><br>";

my $functionname=$Q{code};
OutError("bad request") if !defined(&$functionname);
&$functionname;

WriteStable();
RenewDraLog();
CoDataCA();
1;


sub new
{
OutError("bad request") if ($MYST!=-1);
OutError("bad request") if (scalar @ST >= $STmax);
OutError('資金の余裕がありません。') if ($DT->{money} < $STest);

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

	@ST=reverse(@ST);
	$STcount++;
	my $i=$STcount;
	$ST[$i]->{no}=($i > 0) ? ($ST[$i-1]->{no} + 1) : 1 ;
	$ST[$i]->{birth}=$NOW_TIME;
	$ST[$i]->{name}=$Q{name};
	$ST[$i]->{town}=$MYDIR;
	$ST[$i]->{owner}=$DT->{id};
	$ST[$i]->{emp}=$Q{emp};
	$ST[$i]->{sp}=1;
	$ST[$i]->{tr}=int(rand(15));
	$ST[$i]->{con}=int(rand(15));
	$ST[$i]->{wt}=int(rand(15));
	@ST=reverse(@ST);

WritePayLog($MYDIR,$DT->{id},-$STest);
PushDraLog(0,"新しい厩舎「".$Q{name}."」が設立されました。");
$disp.="新しい厩舎「<b>".$Q{name}."</b>」を設立しました。";
}

sub large
{
OutError("bad request") if ($MYST==-1);
OutError('資金の余裕がありません。') if ($DT->{money} < $STest);
my $n=int(($NOW_TIME - $ST[$MYST]->{birth})/86400/2) + 1;
my $cost=($ST[$MYST]->{sp} + $ST[$MYST]->{sr} + $ST[$MYST]->{ag} + $ST[$MYST]->{pw} + $ST[$MYST]->{hl} + $ST[$MYST]->{fl});
OutError("bad request") if ($n < $cost);

	my @large=qw(
		sp sr ag pw hl fl
		);

	my $lar=$large[$Q{lar}];

	$ST[$MYST]->{$lar}++;
	OutError('これ以上，この施設は増築できません') if ($ST[$MYST]->{$lar} > 3);

WritePayLog($MYDIR,$DT->{id},-$STest);
$disp.="厩舎を増築しました。";
}

