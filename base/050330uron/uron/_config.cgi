# 設定ファイル 2005/01/06 由來
# このファイルのパーミッションを設定する必要は特にありません。設定するなら644などでＯＫ。

#-----------------------
# ◆はじめにする設定
#-----------------------
$MASTER_PASSWORD	='';			# 管理パスワード
$ADMIN_EMAIL		='';			# 管理者メールアドレス

$HTML_TITLE	='街の正式名称';		# 街の正式名称

$TOWN_TITLE	='略称';			# 街の名称（全角２文字くらいで短く）
						# 後になって街の名称を変えたときは，管理室で
						# 「初期化／破損修復」ボタンを押す必要があります。


#-----------------------
# ◆街の設定
#-----------------------
$TOWN_CODE	='uron';			# 街のコード（識別記号）
						# 半角英数小文字10文字以内で適当に設定しましょう。
						# 他の街と同じコードにならないように。

$TITLE_COMMENT	='';				# ログイン画面に載せるコメント。タグ使えます。

$HOME_PAGE	='../index.html';		# 「ホーム」のリンク先

$MOVETOWN_ENABLE	=0;			# 移転機能の有効化 1:有効 0:無効
						# サーバーがsocketに対応してないと移転機能は使えません。


#------------------------
# 基本的なゲーム設定
#------------------------
$MAX_USER	=50;				# 新装開店最大数：あまり大きくしてはいけません。
$MAX_MOVE_USER	=55;				# 移転最大数（他から移転してきた場合の受け入れ可能数）

$EXPIRE_TIME	=3600*24*7;			# 経営者不在期限(秒)
						# この期間ずっとアクセスがないとデータが抹消されます。

$ONE_DAY_TIME		=3600*36;		# 決算サイクル(秒)
$DATE_REVISE_TIME	=3600*6;		# 決算時刻をずらす秒数(-3600で1時間前倒し)

$MAX_STOCK_TIME		=72*60*60;		# 最大持ち時間(秒)

$LIMIT_EXP	=3600;				# 熟練度の合計値リミット（10倍の数値を指定）
						# 3600だと360%が上限。0にすると上限なし。

$REQUEST_LIMIT		=48*60*60;		# 「依頼所」の依頼が有効な時間(秒)
$REQUEST_CAPACITY	=1;			# 同時に依頼できる数

$HouseMax	=5;				# 「住宅」に保管できる個数：
						# 5 とすると，それぞれのアイテムが倉庫最大数の5倍まで保管できる。

$MAX_BOX	=5;				# 手紙の送信最大数
$BOX_STOCK_TIME	=48*60*60;			# 手紙が有効な時間(秒)

@DIGNITY=(					# 爵位の名前。右に行くほど地位が高くなります。
	"平民","士爵","子爵","伯爵","侯爵","公爵","大公"
	);
@DIG_POINT=(					# 必要な爵位ポイント。上と対応させてください。
	0,1,2,4,8,16,32
	);
$DIG_FORGUILD=16;				# ギルド結成に必要な爵位ポイント

$BAL_NAME	='バルバロス';			# 反乱ＮＰＣの名前
$BAL_JOB	='山賊';			# 反乱ＮＰＣの職業


#-------------------------------
# 用語に関する設定 : ゲーム内に出てくる用語を一気に変更できます。
#-------------------------------

@term=(
	'\\',			#前につける通貨単位
	'',			#後につける通貨単位
	'円',			#日本語表記される場合の通貨単位（順位などで使う）
	'サラ金生活',		#資金マイナス時（順位で使う）

);


#-------------------------------
# アクセスの制限に関する設定
#-------------------------------
$NEW_SHOP_ADMIN		=0;			# 新規オープン権限 0:一般 1:管理者のみ
						# 1 にすると管理画面からしか店を開けなくなります。

$NEW_SHOP_KEYWORD	='';			# 新規店舗オープンに必要なキーワード
						# キーワードを設定すると，その言葉を知らないと開店できなくなります。

$NEW_SHOP_BLOCKIP	=1;			# 1で同一IPによる連続登録(閉店後の再登録も含む)を阻止
$CHECK_IP		=1;			# 同一IP＆USER_AGENTのアクセスを自動的に制限する 1:制限する 0:制限しない
@NG_SHOP_NAME		=qw(管理 支 11 12 aa http ?);	# 店舗名として使用できない文字(スペースで区切る)

$NEW_OTHERTOWN_BLOCK	=0;			# 1 で街グループ全体で重複登録を検出。
						# 街グループ全体で1つしか店を持てなくなります。



#********************** 一般的な設定項目はここまでです **********************



#--------------------------------------------------------------------
# 画像に関する設定 ： 画像を差し替えたり，特殊な場所に置く人向け。
#--------------------------------------------------------------------
$IMAGE_URL		='./image';		# 画像ディレクトリのある場所（アドレス）
						# CGIが別サーバーとなるところでは変更の必要あり。
$IMAGE_DIR		='./image';		# 画像ディレクトリ（サーバーのフルパス）
						# nifty などの特殊なサーバーでは変更の必要あり。

$ICON_NUMBER		=25;			# 店長顔アイコンの数
$ICON_SIZE		='WIDTH=48 HEIGHT=48';	# 顔アイコンのサイズ

$IMAGE_EXT		='.png';		# 画像拡張子

$COMMON_URL		='../common';		# グローバルデータディレクトリ（ギルド等）
						# CGIが別サーバーとなるところでは変更の必要あり。
$COMMON_DIR		='../common';		# グローバルデータディレクトリ（サーバーのフルパス）
						# nifty などの特殊なサーバーでは変更の必要あり。

#---------------------------------------------------------
# 高度なゲームバランス設定 ： バランスを熟知した人向け。
#---------------------------------------------------------
$UPDATE_TIME		=60*5;			# 最短更新サイクル(秒)

$PROFIT_DAY_COUNT	=3;			# 点数計算の際考慮する過去の純利益（期）
$SALE_SPEED		=12;			# 売れ行き倍率(inc-item-data.cgiでの設定を1として)
$POP_DOWN_RATE	=5;				# 現在の人気に応じての上下幅

$EXP_DOWN_POINT		=5;			# 決算時に減少する熟練度ポイント(1%==10)
$EXP_DOWN_RATE		=60;			# 決算時に減少する熟練度割合(6%==60)
						# 例:現在の熟練度50%の場合、固定の0.5%と50%の6%で3%、合わせて3.5%減少


#---------------------------------------------------------
# 細かい表示設定 ： むやみに変更すると見栄えが崩れます。
#---------------------------------------------------------
$TOP_RANKING_PAGE_ROWS	=5;			# 「トップ」ランキング表示件数
$MAIN_LOG_PAGE_ROWS	=10;			# 「店長室」最近の出来事表示件数
$SHOP_PAGE_ROWS		=5;			# 「他店」店舗表示件数
$RANKING_PAGE_ROWS	=10;			# ランキング表示件数
$LIST_PAGE_ROWS_PC	=25;			# 各種リスト表示件数（通常）
$LIST_PAGE_ROWS_MOBILE	=5;			# 各種リスト表示件数（携帯）



#********************** これより下の設定はなるべくそのままで **********************

$DATA_DIR		='./data';
$LOG_DIR		=$DATA_DIR.'/log';
$ITEM_DIR		=$DATA_DIR.'/item';
$SESSION_DIR		=$DATA_DIR.'/session';
$BACKUP_DIR		=$DATA_DIR.'/backup';
$TEMP_DIR		=$DATA_DIR.'/temp';
$SUBDATA_DIR		=$DATA_DIR.'/subdata';

$COTEMP_DIR		=$COMMON_DIR.'/temp';

$INCLUDE_DIR		='../program';
$AUTOLOAD_DIR		=$INCLUDE_DIR.'/plug';
$TOWN_DIR		=$INCLUDE_DIR.'/town';
$JCODE_FILE		=$INCLUDE_DIR.'/jcode.pl';
$CUSTOM_DIR		='./custom';

$DIR_PERMISSION		=0777;
$TZ_JST			=60*60*9;

$FILE_EXT		='.cgi';

$COMMIT_FILE		='commit';
$LASTTIME_FILE		='lasttime';
$LOCK_FILE		='lockfile';
$DATA_FILE		='play';
$LOG_FILE		='log';
$BBS_FILE		='treelog';
$BOX_FILE		='box';
$GUILDBAL_FILE		='guildbal';
$GUILD_FILE		='guild';
$ERROR_COUNT_FILE	='errorcnt';

$LOG_ERROR_FILE		='error';
$LOG_DELETESHOP_FILE	='delete';
$LOG_MOVESHOP_FILE	='moveshop';
$LOG_LOGIN_FILE		='login';
$LOG_DEBUG_FILE		='debug';
$LOG_MARK_FILE		='mark';
$LOG_SIZE_MAX		=30000;

$PASSWORD_CRYPT	=1;
$CHAR_SHIFT_JIS		=0;

$AUTO_UNLOCK_TIME		=60;
$SESSION_TIMEOUT_TIME		=3600;
$LOG_EXPIRE_TIME		=3600*36;
$PASSWORD_HASH_EXPIRE_TIME	=60*15;

$BACKUP_TIME		=3600;
$BACKUP		=3;
@BACKUP_FILES		=(
		$LOG_FILE.'0',
		$LOG_FILE.'1',
		$LOG_FILE.'2',
		$GUILDBAL_FILE,
		$DATA_FILE,
			);

# 技術者向けデバッグ用 
$DEBUG_MOBILE		=0;			# 1で携帯端末処理固定
$DEBUG_LOG_ENABLE	=0;			# 1でitem::DebugLog()とevent::DebugLog()を有効化

# set umask
umask(~$DIR_PERMISSION & 0777);
require './_config-local.cgi' if -e './_config-local.cgi';

sub RequireFile
{
	my $customfile="$CUSTOM_DIR/$_[0]";
	require $customfile,return if -e $customfile;
	my $fname="$INCLUDE_DIR/$_[0]";
	OutError('ファイルが見つかりません - '.$fname) unless -e $fname;
	require $fname;
}
1;
