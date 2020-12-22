# error プラグイン 2004/01/20 由來

sub OverLoad
{
	print <<"HTML";
Cache-Control: no-cache, must-revalidate
Pragma: no-cache
Content-type: text/html

<html>
<head>
<title>過負荷</title>
</head>
<body>
現在サーバが高負荷状態です。
申\し訳ありませんがしばらくアクセスを見合わせてください。<br>
負荷度 $_[0] CPUs
</body></html>
HTML
	exit;
}

sub OutError
{
	UnLock() if $LOCKED;
	CoUnLock() if $COLOCKED;
	my %msg=
	(
		"not defined function"=>
			'定義されていない関数を呼び出しました。管理者に以下の情報を連絡してください。<hr>'.
			"not defined function '$_[1]'",
		"busy"=>
			'アクセスが<SPAN>混雑</SPAN>しております。<br>'.
			'お手数ですが<SPAN>必ず５秒以上待ってから</SPAN>戻ってもう一度アクセスしてください。<br>'.
			($AUTO_UNLOCK_TIME*2).'秒以上経っても接続できない場合は'.
			'<a href="mailto:'.$ADMIN_EMAIL.'">管理人までご連絡</a>ください。',
		"no data"=>
			'<SPAN>データが見つかりませんでした</SPAN>。お手数ですが戻ってやり直してください。'.
			'このメッセージが続く場合は<a href="mailto:'.$ADMIN_EMAIL.'">管理人までご連絡</a>ください。',
		"stop"=>
			'この店舗は<SPAN>お休み中</SPAN>です。'.
			'プレイを再開するときは<a href="mailto:'.$ADMIN_EMAIL.'">管理人までご連絡</a>ください。',
		"no user"=>
			'存在しないIDです。IDをご確認ください。→'.$_[1],
		"incorrect"=>
			'パスワードが間違っています。ご確認ください→'.$_[1],
		"error rename"=>
			'データ更新に失敗しました',
		"timeout"=>
			'ログインから長時間が経過したため<SPAN>タイムアウト</SPAN>しました。<br>お手数ですがもう一度トップからログインし直してください。',
		"bad request"=>
			'<SPAN>不正な呼び出し</SPAN>です。ブラウザの「戻る/進む」を使っている場合は使わないようにしてください。',
	);
	my $msg=defined $msg{$_[0]} ? $msg{$_[0]} : $_[0];
	$NOMENU=0;$Q{bk}="";
	$disp=<<"HTML";
	<BIG>●エラーレポート</BIG><br><br>
	$msg
HTML
	OutSkin();
	exit;
}

sub WriteErrorLog
{
	eval(<<'__function__');
	my($msg,$file)=@_;
	
	return if !$LOG_SIZE_MAX || $file eq '';
	
	my $fn=GetPath($LOG_DIR,$file);
	rename($fn,GetPath($LOG_DIR,$file."-old")) if (stat($fn))[7]>$LOG_SIZE_MAX;
	open(ERR,">>$fn") or return;
	print ERR
		join("\t",
			(
				$NOW_TIME,
				$ENV{SCRIPT_NAME},
				$ENV{REMOTE_ADDR},
				$ENV{REMOTE_HOST},
				GetTrueIP(),
				$USER,
				$msg,
			)
		)."\n";
	close(ERR);
__function__
}

sub OutErrorBlockLogin
{
	OutError('
		ご指定のIDは<SPAN>'.$_[0].'</SPAN>のためアクセス制限されています。<br>
		プレイ中の「街名」「ユーザ名」「店舗名」を添えて<a href="mailto:'.$ADMIN_EMAIL.'">管理人までご連絡</a>ください。
	');
}
1;
