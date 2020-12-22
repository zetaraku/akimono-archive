★りどみ
ダウンロードありがとうございます。
本プログラムはCGIゲーム「商人物語」の追加スクリプトになります。
BASARA様(http://www.aitaii.com/~basara/merchant/ 閉鎖)にて配布されている
職業一覧スクリプトに多少の改良を加えました。
使用の際は規約に従い、以下の著作表示をstaff.cgiに記述してください。

<SPAN>職業一覧スクリプト</SPAN> ： BASARA 様 ... 商人物語 ver.BSR
<br><br>

●設置方法
inc-html-ranking.4.cgi,log.cgiをcustomディレクトリにアップロードします。
元からlog.cgiに改造を施している場合は、ファイルを見て適宜追加してください。

●変更点
action.cgiからの呼び出しを防ぐ為ファイル名を変更
書き換えの作業を不要に
ジョブアイコン表示

●以下原文

職業一覧スクリプト　BASARA　20050107

新聞の情報に現在の職業一覧リストを追加します。
自分で欲しいなと思って作っただけなので、有効性があるかわかりませんがご了承ください。
や、もっといい記述があると思いますが、面倒だったので（ォィ

設置方法
１、joblist.cgiの9行目と14行目のforeach文の職業をご自分のものに変更してください。

	例	通常版
		foreach("","drug","tool","weapon","armor","material","book","cow","peddle"){
		ドラゴノーマ版
		foreach("","warlock","dtamer","dmaster","btamer","shaman","thunter","peddle"){
		ワールドアトラス版
		foreach("","shipb","pirate","pros","explore","trader"){

	ま、てきとーなサジ加減で。

２、log.cgiにご自分で改造を加えている場合は

	.GetMenuTag('log',	'[職業]','&t=6');

	if ($Q{t}==6) {
	RequireFile('joblist.cgi');

	このへんをてきとーに追加して下さい。

３、customディレクトリにjoblist.cgiとlog.cgiをアップロードします。
終了