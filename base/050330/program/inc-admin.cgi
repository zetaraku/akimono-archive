# 管理室画面下請け 2003/09/25 由來

if(-e "$DATA_DIR/$LASTTIME_FILE$FILE_EXT")
	{
		push(@log,'現在メンテモードにつき，ゲームの進行が止まっています。') if -e "./lock" or -e "$DATA_DIR/lock";
		push(@log,'ゲームデータがなくなっています。'," バックアップを復元するか初期化が必要です。") if !-e "$DATA_DIR/$DATA_FILE$FILE_EXT";
		my $init=' 初期化ボタン（メニュー下部）を押して修復してください。';
		push(@log,'ギルド定義ファイルがなくなっています。',$init) if !-e "$DATA_DIR/$GUILD_FILE$FILE_EXT";
		push(@log,'ロックファイルがなくなっています。',$init) if !GetFileList($DATA_DIR,"^$LOCK_FILE");
		push(@log,'共有ロックファイルがなくなっています。',$init) if !GetFileList($COMMON_DIR,"^$LOCK_FILE");
		foreach my $dir ($SESSION_DIR,$TEMP_DIR,$COTEMP_DIR,$LOG_DIR,$SUBDATA_DIR,$BACKUP_DIR)
		{
			push(@log,$dir.' がなくなっています。',$init) if !-e $dir;
		}
		push(@log,' 商品データを作成してください。') if !-e $ITEM_DIR;
	}
	else
	{
		push(@log,' 初期化を行ってください（メニュー下部）');
	}
	
if(-e "$DATA_DIR/$ERROR_COUNT_FILE$FILE_EXT")
	{
	my $errorcount=(-s "$DATA_DIR/$ERROR_COUNT_FILE$FILE_EXT")+0;
	unlink("$DATA_DIR/$ERROR_COUNT_FILE$FILE_EXT");
	push(@log,'前回の管理から現在まで '.$errorcount.'回のエラーを検知しました。');
	}
	push(@log,"<A HREF=\"$DATA_DIR/error.log\">[エラー情報]</A> が報告されています。") if(-e "$DATA_DIR/error.log");
	
	my $backupselect=qq|<option value="" selected>バックアップを選択|;
	my $backupbasedir=$BACKUP_DIR;
	$backupbasedir=~s/\/([^\/]*)$//;
	foreach(GetFileList($backupbasedir,"^$1"))
	{
		my $file=$_;
		my $time=(stat("$file/$DATA_FILE$FILE_EXT"))[9];
		next if !$time;
		my($s,$min,$h,$d,$m,$y)=gmtime($time+$TZ_JST);
		my $timestr=sprintf("%04d-%02d-%02d %02d:%02d",$y+1900,$m+1,$d,$h,$min);
		$backupselect.=qq|<option value="$_">$timestr|;
	}
	
	my $userselect=qq|<option value="" selected>ユーザーを選択|;
if(open(IN,"$DATA_DIR/$DATA_FILE$FILE_EXT"))
	{
		while(<IN>){s/[\r\n]//g; last if $_ eq '//';}
		my @data=<IN>;
		close(IN);
		if(scalar(@data))
		{
			for(my $idx=0; $idx<$#data; $idx+=2)
			{
				@_=split(/,/,$data[$idx],5);
				
				$userselect.=qq|<option value="$_[2]">$_[2] : $_[3]|;
			}
		}
	}
	eval {
	require "$ITEM_DIR/item.cgi" if -e "$ITEM_DIR/item.cgi";
	};
	if ($@)
	{
	push(@log,' inc-item-data.cgiにエラーがあり，データを取得できません。');
	push(@log,'一部の管理機能が正常に動作しない可能性があります。');
	}
	else
	{
	foreach(1..$MAX_ITEM){$sort[$_]=$ITEM[$_]->{sort}};
	my @itemlist=sort { $sort[$a] <=> $sort[$b] } (1..$MAX_ITEM);
	$formitem="<OPTION VALUE=\"\">アイテムを選択";
	foreach my $idx (@itemlist)
		{
		$formitem.="<OPTION VALUE=\"$idx\">$ITEM[$idx]->{name}";
		}
	}
	eval {
	require "$INCLUDE_DIR/inc-version.cgi";
	};

	my($s,$min,$h,$d,$m,$y)=gmtime(time()+$TZ_JST);
	$y+=1900;$m++;

	$disp.="<hr width=700 noshade size=1><SPAN>基本管理機能\</SPAN>";
	$disp.="<table><tr><td bgcolor=\"#CBC5FF\"><table width=200>";
	$disp.="<tr><td>perl version</td><td>$]</td></tr>";
	foreach('.',$DATA_DIR,$INCLUDE_DIR,$AUTOLOAD_DIR,$TOWN_DIR,$COMMON_DIR,"_config.cgi","action.cgi",$MYNAME)
	{
		$disp.="<tr><td>".$_."<td>".substr(sprintf("%o",(stat($_))[2]),-3,3)."</tr>";
	}
	$disp.="</table><td bgcolor=\"#DBD5FF\">";
	
	$disp.=<<"HTML";
	<table width=500><tr><td colspan=2>
	<FORM ACTION="$MYNAME" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=admin VALUE="$Q{admin}">
	<INPUT TYPE="HIDDEN" NAME=mode VALUE="menteon">
	<INPUT TYPE="SUBMIT" VALUE="◆ メンテモードに移行 ◆"></FORM>
	<td colspan=2><FORM ACTION="$MYNAME" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=admin VALUE="$Q{admin}">
	<INPUT TYPE="HIDDEN" NAME=mode VALUE="menteoff">
	<INPUT TYPE="SUBMIT" VALUE="◆ メンテモードを解除 ◆">
	</FORM></tr><tr><td colspan=2>
	<FORM ACTION="admin.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=key VALUE="makeitem">
	<INPUT TYPE="HIDDEN" NAME=admin VALUE="$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="■ 商品データを作成 ■">
	</FORM>
	<td colspan=2><FORM TARGET="_blank" ACTION="action.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=key VALUE="item-list">
	<INPUT TYPE="HIDDEN" NAME=u VALUE="soldoutadmin!$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="□ 商品データを確認 □">
	</FORM></tr><tr><td>
	<FORM TARGET="_blank" ACTION="http://www.geocities.co.jp/Playtown-Bingo/8587/diff/$BASE_VERSION.htm" METHOD="GET">
	<INPUT TYPE="SUBMIT" VALUE="■ 更新を確認 ■">
	</FORM>
	<td>
	<FORM TARGET="_blank" ACTION="action.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=key VALUE="treebbs">
	<INPUT TYPE="HIDDEN" NAME=nm VALUE="soldoutadmin">
	<INPUT TYPE="HIDDEN" NAME=pw VALUE="$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="掲示板">
	</FORM>
	<td>
	<FORM ACTION="$MYNAME" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=admin VALUE="$Q{admin}">
	<INPUT TYPE="HIDDEN" NAME=mode VALUE="errdel">
	<INPUT TYPE="SUBMIT" VALUE="エラー情報削除">
	</FORM>
	<td>
	<FORM TARGET="_blank" ACTION="action.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=key VALUE="admin-sub2">
	<INPUT TYPE="HIDDEN" NAME=log VALUE=".">
	<INPUT TYPE="HIDDEN" NAME=nm VALUE="soldoutadmin">
	<INPUT TYPE="HIDDEN" NAME=pw VALUE="$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="各種ログ閲覧">
	</FORM></tr><tr><td colspan=3>
	<FORM TARGET="_blank" ACTION="action.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=key VALUE="admin-sub2">
	<INPUT TYPE="HIDDEN" NAME=nm VALUE="soldoutadmin">
	<INPUT TYPE="HIDDEN" NAME=pw VALUE="$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="メンバーリスト">
	<INPUT TYPE="CHECKBOX" NAME=host>ホスト表\示
	<INPUT TYPE="CHECKBOX" NAME=only>一覧のみ
	</FORM>
	<td>
	<FORM TARGET="_blank" ACTION="index.cgi" METHOD="POST">
	<INPUT TYPE="SUBMIT" VALUE="トップ画面へ">
	</FORM></tr><tr><td colspan=4>
	<FORM TARGET="_blank" ACTION="action.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=key VALUE="admin-sub2">
	<INPUT TYPE="HIDDEN" NAME=mode VALUE="delitem">
	<INPUT TYPE="HIDDEN" NAME=u VALUE="soldoutadmin!$Q{admin}">
	・プレイデータから <SELECT NAME=num1>$formitem</SELECT> または No.<INPUT TYPE=TEXT NAME=num2 SIZE=5> を
	<INPUT TYPE="SUBMIT" VALUE="消去する">
	</FORM></tr><tr><td colspan=4>
	<FORM TARGET="_blank" ACTION="action.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=key VALUE="admin-sub2">
	<INPUT TYPE="HIDDEN" NAME=u VALUE="soldoutadmin!$Q{admin}">
	・イベントコード <INPUT TYPE="TEXT" size=12 NAME=ecode> を<br>
	終了時刻 <INPUT TYPE="TEXT" NAME=tlyear SIZE=5 VALUE="$y">年<INPUT TYPE="TEXT" NAME=tlmon SIZE=3 VALUE="$m">月
	<INPUT TYPE="TEXT" NAME=tlday SIZE=3 VALUE="$d">日 <INPUT TYPE="TEXT" NAME=tlhour SIZE=3 VALUE="$h">時
	<INPUT TYPE="TEXT" NAME=tlmin SIZE=3 VALUE="$min">分<INPUT TYPE="TEXT" NAME=tlsec SIZE=3 VALUE="$s">秒
	まで <INPUT TYPE="SUBMIT" VALUE="発生させる">
	</FORM></tr></table>
	</tr></table><hr width=700 noshade size=1>
	<SPAN>メンバー賞品授与機能\</SPAN>
	<table width=700 bgcolor="#DBD5FF"><tr><td>
	<FORM TARGET="_blank" ACTION="action.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=key VALUE="admin-sub">
	<INPUT TYPE="HIDDEN" NAME=u VALUE="soldoutadmin!$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="賞品授与"> <SELECT NAME=user>$userselect</SELECT> 
	<INPUT TYPE="TEXT" size=46 NAME=comment VALUE="">←コメント(任意)<br>
	・アイテム <SELECT NAME=senditem>$formitem</SELECT>：<INPUT TYPE="TEXT" size=3 NAME=count VALUE="1">個
	／・資金：<INPUT TYPE="TEXT" size=5 NAME=sendmoney VALUE="0">円
	／・時間：<INPUT TYPE="TEXT" size=3 NAME=sendtime VALUE="0">時間
	／・爵位：<INPUT TYPE="TEXT" size=3 NAME=senddig VALUE="0">ポイント<br>
	※それぞれを一度に指定することもできます。コメントを空欄にすると公表\しません。
	</FORM></tr></table><hr width=700 noshade size=1>
	<SPAN>メンバー管理機能\</SPAN>
	<table width=700 bgcolor="#DBD5FF"><tr><td width=280>
	<FORM TARGET="_blank" ACTION="action.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=key VALUE="new">
	<INPUT TYPE="HIDDEN" NAME=admin VALUE="$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="新規店舗オープン"><br>
	※定員にかかわらずオープン可能\。</FORM>
	<td><FORM TARGET="_blank" ACTION="action.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=pw VALUE="$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="ユーザー店舗入店"> <SELECT NAME=nm>$userselect</SELECT><br>
	※本人が入店していても同時に操作できます。
	</FORM></tr>
	<tr><td colspan=2>
	<FORM TARGET="_blank" ACTION="action.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=key VALUE="user">
	<INPUT TYPE="HIDDEN" NAME=pw VALUE="$Q{admin}">
	<INPUT TYPE=HIDDEN NAME=mode VALUE=repass>
	<INPUT TYPE="SUBMIT" VALUE="パスワード変更"> <SELECT NAME=nm>$userselect</SELECT>
	<INPUT TYPE="TEXT" size=5 NAME=pw1 VALUE="">←新パス
	<INPUT TYPE="TEXT" size=5 NAME=pw2 VALUE="">←新パスもう一度
	</FORM></tr>
	<tr><td colspan=2>
	<FORM TARGET="_blank" ACTION="action.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=key VALUE="admin-sub">
	<INPUT TYPE="HIDDEN" NAME=u VALUE="soldoutadmin!$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="ユーザー店舗凍結"> <SELECT NAME=user>$userselect</SELECT>
	<INPUT TYPE="TEXT"   NAME=blocklogin VALUE="">←凍結理由<br>
	※「off」と入力で凍結解除：「mark」と入力でログイン履歴ログ：「stop」と入力で休止扱い
	</FORM></tr>
	<tr><td colspan=2>
	<FORM TARGET="_blank" ACTION="action.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=key VALUE="admin-sub">
	<INPUT TYPE="HIDDEN" NAME=u VALUE="soldoutadmin!$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="重複登録許可／禁止"> <SELECT NAME=user>$userselect</SELECT>
	<SELECT NAME=nocheckip><option value="nocheck">重複許可<option value="check">重複禁止</SELECT>
	</FORM></tr>
	<tr><td colspan=2>
	<FORM TARGET="_blank" ACTION="action.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=key VALUE="admin-sub">
	<INPUT TYPE="HIDDEN" NAME=u VALUE="soldoutadmin!$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="ユーザー店舗追放"> <SELECT NAME=user>$userselect</SELECT> 
	<INPUT TYPE="TEXT" NAME=comment VALUE="">←コメント（任意）<br>
	<INPUT TYPE="CHECKBOX" NAME=log>←通知しない 
	<INPUT TYPE="TEXT" NAME=closeshop VALUE="">← 確認のため closeshop と入力
	</FORM></tr></table><hr width=700 noshade size=1>
	<SPAN>データ初期化・削除機能\</SPAN>
	<table width=700 bgcolor="#DBD5FF"><tr><td>
	<FORM ACTION="$MYNAME" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=admin VALUE="$Q{admin}">
	<INPUT TYPE="HIDDEN" NAME=mode VALUE="init">
	<INPUT TYPE="SUBMIT" VALUE="初期化/破損修復">（復旧機能\です。すでにあるデータは削除されません）
	</FORM></tr><tr><td>
	<FORM ACTION="$MYNAME" METHOD="POST">
	ゲームデータのうち，商品データ・関連ディレクトリだけを<INPUT TYPE="HIDDEN" NAME=mode VALUE="mini">
	<INPUT TYPE="SUBMIT" VALUE="最小アンインストールする"> <INPUT TYPE="PASSWORD" size=5 NAME=admin VALUE="">管理パス
	</FORM></tr>
	<tr><td>
	<FORM ACTION="$MYNAME" METHOD="POST">
	ユーザーデータを残しつつ，ゲームデータ・関連ディレクトリを<INPUT TYPE="HIDDEN" NAME=mode VALUE="piece">
	<INPUT TYPE="SUBMIT" VALUE="部分アンインストールする"> <INPUT TYPE="PASSWORD" size=5 NAME=admin VALUE="">管理パス
	</FORM></tr>
	<tr><td>
	<FORM ACTION="$MYNAME" METHOD="POST">
	ユーザーデータを含めて，全ゲームデータ・関連ディレクトリを<INPUT TYPE="HIDDEN" NAME=mode VALUE="delunit">
	<INPUT TYPE="SUBMIT" VALUE="完全アンインストールする"> <INPUT TYPE="PASSWORD" size=5 NAME=admin VALUE="">管理パス
	</FORM></tr>
	<tr><td>
	<FORM ACTION="$MYNAME" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=mode VALUE="timeedit">
	最終更新時刻を<INPUT TYPE="TEXT" NAME=tlyear SIZE=5 VALUE="$y">年<INPUT TYPE="TEXT" NAME=tlmon SIZE=3 VALUE="$m">月
	<INPUT TYPE="TEXT" NAME=tlday SIZE=3 VALUE="$d">日 <INPUT TYPE="TEXT" NAME=tlhour SIZE=3 VALUE="$h">時
	<INPUT TYPE="TEXT" NAME=tlmin SIZE=3 VALUE="$min">分<INPUT TYPE="TEXT" NAME=tlsec SIZE=3 VALUE="$s">秒
	に<INPUT TYPE="SUBMIT" VALUE="変更する">
	<INPUT TYPE="PASSWORD" size=5 NAME=admin VALUE="">管理パス
	</FORM></tr>
	<tr><td>
	<FORM ACTION="$MYNAME" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=mode VALUE="backup">
	ゲームデータを<SELECT NAME=backup>$backupselect</SELECT>
	の時点に<INPUT TYPE="SUBMIT" VALUE="復元する">
	<INPUT TYPE="PASSWORD" size=5 NAME=admin VALUE="">管理パス
	</FORM></tr></table><br><br>
HTML
1;
