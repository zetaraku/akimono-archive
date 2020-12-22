# 世界樹版アイテムデータ

# このファイルはアイテムデータの定義ファイルです。
# 好きなようにカスタマイズできます。詳細はマニュアルをご覧ください。

# アイテムのflag設定に icon を追加
# icon を記述することで、所持しているとランキング表示にそのアイテムの
# アイコンが表示されるようになります
# inc-html-ranking.cgi,inc-html-top.cgi,inc-makeitem.cgiを改変

@@DEFINE
	version	世界樹Ver1.80	#★商品データバージョン表記

	scale	個			#★デフォルトの数え単位
	type0	全			#全アイテムの集合
	type1	原料
	type2	薬品
	type3	香水
	type4	錬金
	type5	食材
	type6	細工
	type7	書物
	type8	道具
	
	job	writer		執筆師		#★職業コードは英小文字10文字以内
	job	pharmacist	薬剤師
	job	therapist	調合師
	job	alchemist	錬金術師
	job	cook		調理師
	job	designer	細工師

	MaxMoney		999999999	#★最大資金
	
	set NewShopMoney	200000		#初期資金 (@@FUNCNEWにて使用)
	set NewShopTime	24*60*60	#初期持時間(秒) (@@FUNCNEWにて使用)
	set NewShopItem	ギフト券:3	#初期所持商品 (@@FUNCNEWにて使用) 書式 商品名:個数:商品名:個数:...
	
	TimeEditShowcase	10m		#★陳列棚操作時間
	TimeShopping		20m		#★仕入時間(旧SOLD OUTとの互換性確保。今は使用せず)
	TimeSendItem		20m		#★アイテム仕入/移動時間(基本)
	TimeSendItemPlus	20s		#★アイテム仕入/移動時間(1個辺りの追加時間)
	TimeSendMoney		30m		#★資金移動時間(基本)
	TimeSendMoneyPlus	250000		#★ごみ処理時間計算用金額(この金額につきTimeSendMoney時間を消費)
	
	CostShowcase1		0		#★陳列棚1個時維持費
	CostShowcase2		4000		#陳列棚2個時維持費
	CostShowcase3		8000		#陳列棚3個時維持費
	CostShowcase4		16000		#陳列棚4個時維持費
	CostShowcase5		32000		#陳列棚5個時維持費
	CostShowcase6		64000		#陳列棚6個時維持費
	CostShowcase7		128000		#陳列棚7個時維持費
	CostShowcase8		256000		#陳列棚8個時維持費
	
	ItemUseTimeRate	0.5		#★アイテム使用時時間計算補正倍率(@USE内time,exptimeに有効)
	

#------ ここからアイテム定義 ---------------------------------

@@ITEM
	no	10
	type	道具
	code	book-make
	name	本執筆キット
	info	本を執筆する為の基本キット
	price	10000
	cost	100
	limit	10/4
	pop	0
	scale	セット
	plus	20m
	flag	noshowcase
	@@USE
		time	240m
		exp	2%
		exptime	120m
		job		執筆師	times/1.5
		scale	回
		action	書く
		name	『薬剤師入門』を執筆する
		info	『薬剤師入門』を執筆します
		okmsg	『薬剤師入門』を執筆しました
			use		1	本執筆キット
			use		5	世界樹の葉
			get		2	薬剤師入門
	@@USE
		time	400m
		exp	2%
		exptime	200m
		job		執筆師	times/2.5
		scale	回
		action	書く
		name	『薬剤師上級』を執筆する
		info	『薬剤師上級』を執筆します
		okmsg	『薬剤師上級』を執筆しました
			needexp	20%
			use		1	本執筆キット
			use		6	ハイポーション
			use		2	ハイエーテル
			get		1	薬剤師上級
	@@USE
		time	240m
		exp	2%
		exptime	120m
		job		執筆師	times/1.5
		scale	回
		action	書く
		name	『調合師入門』を執筆する
		info	『調合師入門』を執筆します
		okmsg	『調合師入門』を執筆しました
			use		1	本執筆キット
			use		1	世界樹の花
			use		2	ミネラル水
			use		2	アルコール
			get		2	調合師入門
	@@USE
		time	400m
		exp	2%
		exptime	200m
		job		執筆師	times/2.5
		scale	回
		action	書く
		name	『調合師上級』を執筆する
		info	『調合師上級』を執筆します
		okmsg	『調合師上級』を執筆しました
			needexp	20%
			use		1	本執筆キット
			use		5	コロン
			use		1	フラワーコロン
			use		1	リーフコロン
			get		1	調合師上級
	@@USE
		time	240m
		exp	2%
		exptime	120m
		job		執筆師	times/1.5
		scale	回
		action	書く
		name	『錬金術入門』を執筆する
		info	『錬金術入門』を執筆します
		okmsg	『錬金術入門』を執筆しました
			use		1	本執筆キット
			use		10	マナ鉱石
			get		2	錬金術入門
	@@USE
		time	400m
		exp	2%
		exptime	200m
		job		執筆師	times/2.5
		scale	回
		action	書く
		name	『錬金術上級』を執筆する
		info	『錬金術上級』を執筆します
		okmsg	『錬金術上級』を執筆しました
			needexp	20%
			use		1	本執筆キット
			use		1	マナ
			get		1	錬金術上級
	@@USE
		time	240m
		exp	2%
		exptime	120m
		job		執筆師	times/1.5
		scale	回
		action	書く
		name	『調理師入門』を執筆する
		info	『調理師入門』を執筆します
		okmsg	『調理師入門』を執筆しました
			use		1	本執筆キット
			use		1	世界樹の実
			use		5	木の実粉
			get		2	調理師入門
	@@USE
		time	400m
		exp	2%
		exptime	200m
		job		執筆師	times/2.5
		scale	回
		action	書く
		name	『調理師上級』を執筆する
		info	『調理師上級』を執筆します
		okmsg	『調理師上級』を執筆しました
			needexp	20%
			use		1	本執筆キット
			use		6	モーモー牛乳
			use		4	食パン
			use		2	木の実パン
			get		1	調理師上級
	@@USE
		time	240m
		exp	2%
		exptime	120m
		job		執筆師	times/1.5
		scale	回
		action	書く
		name	『細工師入門』を執筆する
		info	『細工師入門』を執筆します
		okmsg	『細工師入門』を執筆しました
			use		1	本執筆キット
			use		1	世界樹の枝
			get		2	細工師入門
	@@USE
		time	400m
		exp	2%
		exptime	200m
		job		執筆師	times/2.5
		scale	回
		action	書く
		name	『細工師上級』を執筆する
		info	『細工師上級』を執筆します
		okmsg	『細工師上級』を執筆しました
			needexp	20%
			use		1	本執筆キット
			use		4	マナ鉱石
			use		1	レアメタル
			get		1	細工師上級
	@@USE
		time	120m
		exp	2%
		exptime	120m
		job		執筆師	times*1
		scale	回
		action	書く
		name	『探索のススメ』を執筆する
		info	『探索のススメ』を執筆します
		okmsg	『探索のススメ』を執筆しました
			use		2	本執筆キット
			get		1	探索のススメ
@@ITEM
	no	79
	type	書物
	code	book-study
	name	教科書
	info	さまざまな知識を学べる本
	price	10000
	cost	500
	limit	1/1
	pop	0
	scale	冊
	plus	1d
	flag	noshowcase|norequest
	@@USE
		time	12h
		scale	勉強
		action	勉強する
		name	属性の勉強
		info	属性の影響力を勉強します
		okmsg	属性の知識を身につけました
		arg	nocount
			use		1	教科書
			use		10	マナ
			get		1	属性の知識
	@@USE
		time	18h
		scale	勉強
		action	勉強する
		name	魔法の勉強
		info	魔法の使い方を勉強します
		okmsg	魔法の知識を身につけました
		arg	nocount
			use		1	教科書
			use		10	マナエーテル
			use		10	マナ
			use		1	魔法の指輪
			get		1	魔法の知識
	@@USE
		time	24h
		scale	勉強
		action	勉強する
		name	禁断の勉強
		info	禁断の魔術を勉強します
		okmsg	禁断の知識を身につけました
		arg	nocount
			need		1	属性の知識
			need		1	魔法の知識
			use		1	教科書
			use		50	ダークマター
			get		1	禁断の知識
	@@USE
		time	12h
		scale	勉強
		action	勉強する
		name	商売の勉強
		info	商品の品質を勉強します
		okmsg	目利きの真髄を身につけました
		arg	nocount
			use		1	教科書
			use		5	世界樹の葉
			use		5	世界樹の実
			use		5	世界樹の花
			use		5	世界樹の枝
			use		5	マナ鉱石
			use		5	ミネラル水
			get		1	目利きの真髄
@@ITEM
	no	11
	type	書物
	code	book-search
	name	探索のススメ
	info	素材探しのスポットについて書かれている本
	price	25000
	limit	3/2
	pop	0
	plus	20h
	scale	冊
	cost	500
	flag	noshowcase
	@@use
		time	80m
		exp		2%
		exptime	40m
		job		執筆師		times*1.5
		job		薬剤師		times*1.5
		job		調合師		times*1.5
		job		錬金術師	times*1.5
		job		調理師		times*1.5
		job		細工師		times*1.5
		scale	往復
		action	探索に行く
		name	世界樹のふもとへ行く
		info	世界樹の枝が調達できるかもしれません
		okmsg	世界樹の枝を拾いました
		ngmsg	なにも見つかりませんでした…
			get		10	世界樹の枝	50%
		func	_local_
			my $fruit=@@ITEMNO"世界樹の実";
			my $town_fr=main::GetTownData("yggfr");
			if($town_fr)
			{
				my $get_fr=0;
				foreach(1..$count)
				{
					$get_fr+=int(rand(6)+7+$DT->{user}->{ygg});
				}
				$get_fr=$town_fr if($get_fr>$town_fr);
				$town_fr-=$get_fr;
				main::SetTownData("yggfr",$town_fr);
				WriteLog(2,0,"世界樹の実はすべて拾われてしまいました") if($town_fr==0);
				AddItem($fruit,$get_fr,'世界樹の実を拾いました');
			}
			my $flower=@@ITEMNO"世界樹の花";
			my $eventkey="ygg-flowering";
			if(grep($_ eq $eventkey,keys(%main::DTevent)))	#一斉に開花
			{
				my $get_fl=0;
				foreach(1..$count)
				{
					$get_fl+=int(rand(6)+7+$DT->{user}->{ygg});
				}
				AddItem($flower,$get_fl,'世界樹の花を拾いました');
			}
			return 0;
		_local_
	@@use
		time	2h
		exp		2%
		exptime	1h
		scale	往復
		action	探索に行く
		name	山の水源に行く
		info	ミネラル水が調達できるかもしれません
		okmsg	ミネラル水を汲みました
		ngmsg	なにも見つかりませんでした…
		func	lostbook
		param	10,costup-book
			get		250	ミネラル水	50%
		funcb	_local_	#雨が降っている間は収穫量2倍
			my($USE)=@_;
			my $eventkey=$USE->{param2};
			if(grep($_ eq $eventkey,keys(%main::DTevent)))
			{
			foreach(@{$USE->{result}->{create}})
			{
			$_->{count}*=2;
			}
			$USE->{result}->{message}->{resultok}="今回は収穫がいつもより多かったです";
			}
		_local_
	@@use
		time	2h
		exp		2%
		exptime	1h
		scale	往復
		action	探索に行く
		name	マナ鉱山に行く
		info	マナ鉱石が調達できるかもしれません
		okmsg	マナ鉱石を拾いました
		ngmsg	なにも見つかりませんでした…
		func	lostbook
		param	10,plusup-mana
			get		50	マナ鉱石	50%
		funcb	_local_	#マナ鉱脈が発見されている間は収穫量2倍
			my($USE)=@_;
			my $eventkey=$USE->{param2};
			if(grep($_ eq $eventkey,keys(%main::DTevent)))
			{
			foreach(@{$USE->{result}->{create}})
			{
			$_->{count}*=2;
			}
			$USE->{result}->{message}->{resultok}="今回は収穫がいつもより多かったです";
			}
		_local_
@@ITEM
	no	12
	type	書物
	code	book-medicine
	name	薬剤師入門
	info	薬を調合するための入門書です
	price	25000
	limit	20/1.5
	pop	lv3
	point	lv2
	plus	20h
	scale	冊
	cost	500
	@@use
		time	60m
		exp		2%
		exptime	20m
		job		薬剤師	times/1.5
		scale	セット
		action	作りまくる
		name	ポーションを作成する
		info	ポーションを作成しまくります
		okmsg	ポーションをたくさん作りました
		ngmsg	作成に失敗しました…
			use		1	世界樹の葉
			use		10	ミネラル水
			get		60	ポーション	90%
	@@use
		time	90m
		exp		2%
		exptime	30m
		scale	セット
		action	作りまくる
		name	ハイポーションを作成する
		info	ハイポーションを作成しまくります
		okmsg	ハイポーションをたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	25
			needexp	20%
			use		5	世界樹の葉
			use		5	ミネラル水
			use		5	ポーション
			get		60	ハイポーション	80%
	@@use
		time	60m
		exp		2%
		exptime	20m
		scale	セット
		action	作りまくる
		name	エーテルを作成する
		info	エーテルを作成しまくります
		okmsg	エーテルをたくさん作りました
		ngmsg	作成に失敗しました…
			needexp	20%
			use		1	世界樹の葉
			use		10	マナ水
			get		60	エーテル	70%
	@@use
		time	90m
		exp		2%
		exptime	30m
		scale	セット
		action	作りまくる
		name	ハイエーテルを作成する
		info	ハイエーテルを作成しまくります
		okmsg	ハイエーテルをたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	25
			needexp	40%
			use		5	世界樹の葉
			use		5	マナ水
			use		5	エーテル
			get		60	ハイエーテル	60%
@@ITEM
	no	13
	type	書物
	code	book-medicine-high
	name	薬剤師上級
	info	薬を調合するための技術書です
	price	50000
	limit	10/1
	pop	lv4
	point	lv2
	plus	-20m
	scale	冊
	cost	500
	@@use
		time	120m
		exp		2%
		exptime	40m
		job		薬剤師	times/2
		scale	セット
		action	作りまくる
		name	マナポーションを作成する
		info	マナポーションを作成しまくります
		okmsg	マナポーションをたくさん作りました
		ngmsg	作成に失敗しました…
		funcb	needexp
		param	12,500
			use		3	世界樹の葉
			use		10	マナ水
			use		5	ハイポーション
			use		1	マナ
			get		60	マナポーション	80%
	@@use
		time	120m
		exp		2%
		exptime	40m
		scale	セット
		action	作りまくる
		name	マナエーテルを作成する
		info	マナエーテルを作成しまくります
		okmsg	マナエーテルをたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	30
			needexp	10%
			use		3	世界樹の葉
			use		15	マナ水
			use		5	ハイエーテル
			use		1	マナ
			get		60	マナエーテル	60%
	@@use
		time	160m
		exp		2%
		exptime	50m
		scale	セット
		action	作りまくる
		name	エリクサーを作成する
		info	エリクサーを作成しまくります
		okmsg	エリクサーをたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	30
			needexp	30%
			need		1	薬剤師免許
			use		5	世界樹の葉
			use		3	世界樹の実
			use		1	世界樹の花
			use		20	マナ水
			use		5	マナポーション
			use		5	マナエーテル
			use		3	マナ
			get		60	エリクサー	50%
	@@use
		time	320m
		exp		2%
		exptime	120m
		scale	回
		action	作成する
		name	ラストエリクサーを作成する
		info	ラストエリクサーを作成します
		okmsg	ラストエリクサーを作成しました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	35
			needjob	薬剤師
			needexp	60%
			need		1	薬剤師免許
			use		10	世界樹の葉
			use		3	世界樹の実
			use		1	世界樹の花
			use		10	マナ水
			use		3	エリクサー
			use		1	火のマナ
			use		1	水のマナ
			use		1	風のマナ
			use		1	土のマナ
			use		1	ダークマター
			get		60	ラストエリクサー	40%
@@ITEM
	no	14
	type	書物
	code	book-aroma
	name	調合師入門
	info	香水を調合するための入門書です
	price	25000
	limit	20/1.5
	pop	lv3
	point	lv2
	plus	20h
	scale	冊
	cost	500
	@@use
		time	60m
		exp		2%
		exptime	20m
		job		調合師	times/1.5
		scale	セット
		action	作りまくる
		name	コロンを作成する
		info	コロンを作成しまくります
		okmsg	コロンをたくさん作りました
		ngmsg	作成に失敗しました…
			use		10	ミネラル水
			use		1	アルコール
			get		60	コロン		50%
	@@use
		time	90m
		exp		2%
		exptime	30m
		scale	セット
		action	作りまくる
		name	フラワーコロンを作成する
		info	フラワーコロンを作成しまくります
		okmsg	フラワーコロンをたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	25
			needexp	30%
			use		2	世界樹の花
			use		10	ミネラル水
			use		10	コロン
			use		1	アルコール
			get		60	フラワーコロン	40%
	@@use
		time	120m
		exp		2%
		exptime	40m
		scale	セット
		action	作りまくる
		name	リーフコロンを作成する
		info	リーフコロンを作成しまくります
		okmsg	リーフコロンをたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	25
			needexp	30%
			use		5	世界樹の葉
			use		10	ミネラル水
			use		5	枯れた世界樹の葉
			use		20	コロン
			use		1	アルコール
			get		60	リーフコロン	30%
	@@use
		time	120m
		exp		2%
		exptime	40m
		scale	セット
		action	作りまくる
		name	アロマオイルを作成する
		info	アロマオイルを作成しまくります
		okmsg	アロマオイルをたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	25
			needexp	50%
			use		3	世界樹の花
			use		3	フラワーコロン
			use		3	リーフコロン
			use		3	アルコール
			get		60	アロマオイル	20%
@@ITEM
	no	15
	type	書物
	code	book-aroma-high
	name	調合師上級
	info	香水を調合するための技術書です
	price	50000
	limit	10/1
	pop	lv4
	point	lv2
	plus	-20m
	scale	冊
	cost	500
	@@use
		time	200m
		exp		2%
		exptime	70m
		job		調合師	times/2
		scale	セット
		action	作りまくる
		name	アロマエキスを作成する
		info	アロマエキスを作成しまくります
		okmsg	アロマエキスをたくさん作りました
		ngmsg	作成に失敗しました…
		funcb	needexp
		param	14,500
			use		5	世界樹の花
			use		1	マナ水
			use		2	アロマオイル
			use		10	アルコール
			get		60	アロマエキス	20%
	@@use
		time	240m
		exp		2%
		exptime	80m
		scale	セット
		action	作りまくる
		name	コロン・サラマンダーを作成する
		info	コロン・サラマンダーを作成しまくります
		okmsg	コロン・サラマンダーをたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	30
			needexp	30%
			need		1	属性の知識
			use		2	世界樹の花
			use		5	ミネラル水
			use		3	アロマオイル
			use		3	アロマエキス
			use		1	火のマナ
			use		1	アルコール
			get		60	コロン・サラマンダー	20%
	@@use
		time	240m
		exp		2%
		exptime	80m
		scale	セット
		action	作りまくる
		name	コロン・ウンディーネを作成する
		info	コロン・ウンディーネを作成しまくります
		okmsg	コロン・ウンディーネをたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	30
			needexp	30%
			need		1	属性の知識
			use		2	世界樹の花
			use		5	ミネラル水
			use		3	アロマオイル
			use		3	アロマエキス
			use		1	水のマナ
			use		1	アルコール
			get		60	コロン・ウンディーネ	20%
	@@use
		time	240m
		exp		2%
		exptime	80m
		scale	セット
		action	作りまくる
		name	コロン・シルフを作成する
		info	コロン・シルフを作成しまくります
		okmsg	コロン・シルフをたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	30
			needexp	30%
			need		1	属性の知識
			use		2	世界樹の花
			use		5	ミネラル水
			use		3	アロマオイル
			use		3	アロマエキス
			use		1	風のマナ
			use		1	アルコール
			get		60	コロン・シルフ	20%
	@@use
		time	240m
		exp		2%
		exptime	80m
		scale	セット
		action	作りまくる
		name	コロン・ノームを作成する
		info	コロン・ノームを作成しまくります
		okmsg	コロン・ノームをたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	30
			needexp	30%
			need		1	属性の知識
			use		2	世界樹の花
			use		5	ミネラル水
			use		3	アロマオイル
			use		3	アロマエキス
			use		1	土のマナ
			use		1	アルコール
			get		60	コロン・ノーム	20%
	@@use
		time	320m
		exp		2%
		exptime	120m
		scale	回
		action	作成する
		name	禁断の香水を作成する
		info	禁断の香水を作成します
		okmsg	禁断の香水を作成しました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	35
			needjob	調合師
			needexp	60%
			need		1	禁断の知識
			use		10	コロン
			use		2	フラワーコロン
			use		2	リーフコロン
			use		1	コロン・サラマンダー
			use		1	コロン・ウンディーネ
			use		1	コロン・シルフ
			use		1	コロン・ノーム
			use		1	ダークマター
			use		10	アルコール
			use		1	ドライフラワー
			get		60	禁断の香水	20%
@@ITEM
	no	16
	type	書物
	code	book-alchemy
	name	錬金術入門
	info	魔力とマナについて書かれた入門書です
	price	25000
	limit	20/1.5
	pop	lv3
	point	lv2
	plus	20h
	scale	冊
	cost	500
	@@use
		time	120m
		exp		2%
		exptime	60m
		job		錬金術師	times/1.5
		scale	セット
		action	作りまくる
		name	マナを作成する
		info	魔力を用いてマナを作成します
		okmsg	マナをたくさん作りました
		ngmsg	作成に失敗しました…
			use		50	マナ鉱石
			use		5	エーテル
			get		60	マナ		25%
	@@use
		time	150m
		exp		2%
		exptime	75m
		scale	セット
		action	作りまくる
		name	火のマナを作成する
		info	魔力を用いてマナに火の属性を与えます
		okmsg	火のマナをたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	25
			needexp	40%
			need		1	属性の知識
			use		10	マナ
			use		5	ハイエーテル
			get		60	火のマナ	20%
	@@use
		time	150m
		exp		2%
		exptime	75m
		scale	セット
		action	作りまくる
		name	水のマナを作成する
		info	魔力を用いてマナに水の属性を与えます
		okmsg	水のマナをたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	25
			needexp	40%
			need		1	属性の知識
			use		10	マナ
			use		5	ハイエーテル
			get		60	水のマナ	20%
	@@use
		time	150m
		exp		2%
		exptime	75m
		scale	セット
		action	作りまくる
		name	風のマナを作成する
		info	魔力を用いてマナに風の属性を与えます
		okmsg	風のマナをたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	25
			needexp	40%
			need		1	属性の知識
			use		10	マナ
			use		5	ハイエーテル
			get		60	風のマナ	20%
	@@use
		time	150m
		exp		2%
		exptime	75m
		scale	セット
		action	作りまくる
		name	土のマナを作成する
		info	魔力を用いてマナに土の属性を与えます
		okmsg	土のマナをたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	25
			needexp	40%
			need		1	属性の知識
			use		10	マナ
			use		5	ハイエーテル
			get		60	土のマナ	20%
@@ITEM
	no	17
	type	書物
	code	book-alchemy-high
	name	錬金術上級
	info	マナと精霊について書かれた技術書です
	price	50000
	limit	10/1
	pop	lv4
	point	lv2
	plus	-20m
	scale	冊
	cost	500
	@@use
		time	240m
		exp		2%
		exptime	120m
		job		錬金術師	times/2
		scale	セット
		action	作りまくる
		name	レアメタルを作成する
		info	レアメタルを作成しまくります
		okmsg	レアメタルをたくさん作りました
		ngmsg	作成に失敗しました…
		funcb	needexp
		param	16,500
			use		1	世界樹の実
			use		50	マナ鉱石
			use		5	マナエーテル
			use		3	マナ
			get		60	レアメタル	70%
	@@use
		time	240m
		exp		2%
		exptime	120m
		scale	セット
		action	作りまくる
		name	ダークマターを作成する
		info	ダークマターを作成しまくります
		okmsg	ダークマターをたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	30
			needexp	10%
			need		1	属性の知識
			use		50	枯れた世界樹の葉
			use		5	マナエーテル
			use		1	火のマナ
			use		1	水のマナ
			use		1	風のマナ
			use		1	土のマナ
			get		60	ダークマター	35%
	@@use
		time	320m
		exp		2%
		exptime	160m
		scale	回
		action	作成する
		name	賢者の石を作成する
		info	賢者の石を作成します
		okmsg	賢者の石を作成しました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	35
			needjob	錬金術師
			needexp	60%
			need		1	属性の知識
			need		1	魔法の知識
			need		1	魔法の指輪
			use		5	エーテル
			use		5	ハイエーテル
			use		5	マナエーテル
			use		1	火のマナ
			use		1	水のマナ
			use		1	風のマナ
			use		1	土のマナ
			use		10	レアメタル
			use		10	ダークマター
			get		10	賢者の石	60%
	@@use
		time	400m
		exp		2%
		exptime	200m
		scale	回
		action	作成する
		name	サラマンダーを作成する
		info	サラマンダーを作成します
		okmsg	サラマンダーを作成しました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	40
			needjob	錬金術師
			needexp	90%
			need		1	属性の知識
			need		1	魔法の知識
			use		1	世界樹の花
			use		10	火のマナ
			use		5	ダークマター
			use		1	賢者の石
			use		1	火の指輪
			get		10	サラマンダー	45%
	@@use
		time	400m
		exp		2%
		exptime	200m
		scale	回
		action	作成する
		name	ウンディーネを作成する
		info	ウンディーネを作成します
		okmsg	ウンディーネを作成しました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	40
			needjob	錬金術師
			needexp	90%
			need		1	属性の知識
			need		1	魔法の知識
			use		1	世界樹の花
			use		10	水のマナ
			use		5	ダークマター
			use		1	賢者の石
			use		1	水の指輪
			get		10	ウンディーネ	45%
	@@use
		time	400m
		exp		2%
		exptime	200m
		scale	回
		action	作成する
		name	シルフを作成する
		info	シルフを作成します
		okmsg	シルフを作成しました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	40
			needjob	錬金術師
			needexp	90%
			need		1	属性の知識
			need		1	魔法の知識
			use		1	世界樹の花
			use		10	風のマナ
			use		5	ダークマター
			use		1	賢者の石
			use		1	風の指輪
			get		10	シルフ		45%
	@@use
		time	400m
		exp		2%
		exptime	200m
		scale	回
		action	作成する
		name	ノームを作成する
		info	ノームを作成します
		okmsg	ノームを作成しました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	40
			needjob	錬金術師
			needexp	90%
			need		1	属性の知識
			need		1	魔法の知識
			use		1	世界樹の花
			use		10	土のマナ
			use		5	ダークマター
			use		1	賢者の石
			use		1	土の指輪
			get		10	ノーム		45%
@@ITEM
	no	18
	type	書物
	code	book-cook
	name	調理師入門
	info	料理人になるための入門書です
	price	25000
	limit	20/1.5
	pop	lv3
	point	lv2
	plus	20h
	scale	冊
	cost	500
	@@use
		time	60m
		exp		2%
		exptime	20m
		job		調理師	times/1.5
		scale	セット
		action	作りまくる
		name	木の実粉を作成する
		info	木の実粉を作成しまくります
		okmsg	木の実粉をたくさん作りました
		ngmsg	作成に失敗しました…
			use		2	世界樹の実
			get		60	木の実粉	40%
	@@use
		time	60m
		exp		2%
		exptime	20m
		scale	セット
		action	作りまくる
		name	アルコールを作成する
		info	アルコールを作成しまくります
		okmsg	アルコールをたくさん作りました
		ngmsg	作成に失敗しました…
			use		20	ミネラル水
			use		5	木の実粉
			get		60	アルコール	30%
	@@use
		time	60m
		exp		2%
		exptime	20m
		scale	セット
		action	作りまくる
		name	食パンを作成する
		info	食パンを作成しまくります
		okmsg	食パンをたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	25
			use		5	ミネラル水
			use		5	モーモー牛乳
			use		5	木の実粉
			get		60	食パン		60%
	@@use
		time	90m
		exp		2%
		exptime	30m
		scale	セット
		action	作りまくる
		name	木の実パンを作成する
		info	木の実パンを作成しまくります
		okmsg	木の実パンをたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	25
			needexp	10%
			use		1	世界樹の実
			use		5	ミネラル水
			use		5	モーモー牛乳
			use		5	木の実粉
			get		60	木の実パン	50%
	@@use
		time	90m
		exp		2%
		exptime	30m
		scale	セット
		action	作りまくる
		name	チーズパンを作成する
		info	チーズパンを作成しまくります
		okmsg	チーズパンをたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	25
			needexp	30%
			use		5	ミネラル水
			use		5	モーモー牛乳
			use		5	木の実粉
			use		1	チーズ
			get		60	チーズパン	40%
@@ITEM
	no	19
	type	書物
	code	book-cook-high
	name	調理師上級
	info	料理人になるための技術書です
	price	50000
	limit	10/1
	pop	lv4
	point	lv2
	plus	-20m
	scale	冊
	cost	500
	@@use
		time	120m
		exp		2%
		exptime	40m
		job		調理師	times/2
		scale	セット
		action	作りまくる
		name	ヨーグルトを作成する
		info	ヨーグルトを作成しまくります
		okmsg	ヨーグルトをたくさん作りました
		ngmsg	作成に失敗しました…
		funcb	needexp
		param	18,500
			need		1	モーモー
			use		25	モーモー牛乳
			get		60	ヨーグルト	30%
	@@use
		time	160m
		exp		2%
		exptime	50m
		scale	セット
		action	作りまくる
		name	チーズを作成する
		info	チーズを作成しまくります
		okmsg	チーズをたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	30
			needexp	10%
			need		1	モーモー
			use		50	モーモー牛乳
			get		60	チーズ		30%
	@@use
		time	200m
		exp		2%
		exptime	70m
		scale	セット
		action	作りまくる
		name	美酒「世界樹」を作成する
		info	美酒「世界樹」を作成しまくります
		okmsg	美酒「世界樹」をたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	30
			needexp	20%
			need		1	酒醸造免許
			use		1	世界樹の葉
			use		1	世界樹の実
			use		20	ミネラル水
			use		5	木の実粉
			use		20	アルコール
			get		60	美酒「世界樹」	25%
	@@use
		time	240m
		exp		2%
		exptime	80m
		scale	セット
		action	作りまくる
		name	マジカルパウダーを作成する
		info	マジカルパウダーを作成しまくります
		okmsg	マジカルパウダーをたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	30
			needexp	40%
			need		1	魔法の知識
			need		1	魔法の指輪
			use		1	世界樹の花
			use		1	エリクサー
			use		1	マナ
			use		20	木の実粉
			use		10	マナ水
			get		60	マジカルパウダー	25%
	@@use
		time	320m
		exp		2%
		exptime	120m
		scale	回
		action	作成する
		name	闇鍋を作成する
		info	闇鍋を作成します
		okmsg	闇鍋を作成しました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	35
			needjob	調理師
			needexp	60%
			need		1	禁断の知識
			use		1	エリクサー
			use		1	火のマナ
			use		1	水のマナ
			use		1	風のマナ
			use		1	土のマナ
			use		5	ダークマター
			use		3	木の実パン
			use		10	ヨーグルト
			use		1	モーモー
			get		60	闇鍋		40%
@@ITEM
	no	20
	type	書物
	code	book-acce
	name	細工師入門
	info	木工細工について書かれた入門書です
	price	25000
	limit	20/1.5
	pop	lv3
	point	lv2
	plus	20h
	scale	冊
	cost	500
	@@use
		time	30m
		exp		2%
		exptime	10m
		job		細工師	times/1.5
		job		調合師	times/1.5
		scale	セット
		action	作りまくる
		name	ドライフラワーを作成する
		info	ドライフラワーを作成しまくります
		okmsg	ドライフラワーをたくさん作りました
		ngmsg	作成に失敗しました…
			use		10	世界樹の花
			use		1	コロン
			get		10	ドライフラワー
	@@use
		time	60m
		exp		2%
		exptime	20m
		job		調合師	times*1
		scale	セット
		action	作りまくる
		name	木の棒を作成する
		info	木の棒を作成しまくります
		okmsg	木の棒をたくさん作りました
		ngmsg	作成に失敗しました…
			use		4	世界樹の枝
			get		60	木の棒		10%
	@@use
		time	90m
		exp		2%
		exptime	30m
		scale	セット
		action	作りまくる
		name	木刀を作成する
		info	木刀を作成しまくります
		okmsg	木刀をたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	25
			use		3	木の棒
			get		60	木刀		55%
	@@use
		time	120m
		exp		2%
		exptime	40m
		scale	セット
		action	作りまくる
		name	木彫りの熊を作成する
		info	木彫りの熊を作成しまくります
		okmsg	木彫りの熊をたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	25
			needexp	20%
			use		3	世界樹の実
			use		3	木の棒
			get		60	木彫りの熊	40%
	@@use
		time	150m
		exp		2%
		exptime	50m
		scale	セット
		action	作りまくる
		name	木の椅子を作成する
		info	木の椅子を作成しまくります
		okmsg	木の椅子をたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	25
			needexp	40%
			use		1	世界樹の葉
			use		2	世界樹の枝
			use		3	レアメタル
			use		5	木の棒
			get		60	木の椅子	45%
	@@use
		time	180m
		exp		2%
		exptime	60m
		scale	セット
		action	作りまくる
		name	木の机を作成する
		info	木の机を作成しまくります
		okmsg	木の机をたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	25
			needexp	60%
			use		4	世界樹の枝
			use		4	レアメタル
			use		5	木の棒
			get		60	木の机		40%
@@ITEM
	no	21
	type	書物
	code	book-acce-high
	name	細工師上級
	info	マナ細工について書かれた技術書です
	price	50000
	limit	10/1
	pop	lv4
	point	lv2
	plus	-20m
	scale	冊
	cost	500
	@@use
		time	160m
		exp		2%
		exptime	50m
		job		細工師	times/2
		scale	セット
		action	作りまくる
		name	魔法の指輪を作成する
		info	魔法の指輪を作成しまくります
		okmsg	魔法の指輪をたくさん作りました
		ngmsg	作成に失敗しました…
		funcb	needexp
		param	20,500
			use		1	世界樹の花
			use		3	マナ水
			use		5	マナ
			use		10	レアメタル
			get		60	魔法の指輪	25%
	@@use
		time	240m
		exp		2%
		exptime	80m
		scale	セット
		action	作りまくる
		name	火の指輪を作成する
		info	火の指輪を作成しまくります
		okmsg	火の指輪をたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	30
			needexp	20%
			need		1	属性の知識
			use		5	火のマナ
			use		10	レアメタル
			use		1	ダークマター
			get		60	火の指輪	20%
	@@use
		time	240m
		exp		2%
		exptime	80m
		scale	セット
		action	作りまくる
		name	水の指輪を作成する
		info	水の指輪を作成しまくります
		okmsg	水の指輪をたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	30
			needexp	20%
			need		1	属性の知識
			use		5	水のマナ
			use		10	レアメタル
			use		1	ダークマター
			get		60	水の指輪	20%
	@@use
		time	240m
		exp		2%
		exptime	80m
		scale	セット
		action	作りまくる
		name	風の指輪を作成する
		info	風の指輪を作成しまくります
		okmsg	風の指輪をたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	30
			needexp	20%
			need		1	属性の知識
			use		5	風のマナ
			use		10	レアメタル
			use		1	ダークマター
			get		60	風の指輪	20%
	@@use
		time	240m
		exp		2%
		exptime	80m
		scale	セット
		action	作りまくる
		name	土の指輪を作成する
		info	土の指輪を作成しまくります
		okmsg	土の指輪をたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	30
			needexp	20%
			need		1	属性の知識
			use		5	土のマナ
			use		10	レアメタル
			use		1	ダークマター	
			get		60	土の指輪	20%
	@@use
		time	320m
		exp		2%
		exptime	120m
		scale	回
		action	作成する
		name	世界樹のお守りを作成する
		info	世界樹のお守りを作成します
		okmsg	世界樹のお守りを作成しました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	35
			needjob	細工師
			needexp	60%
			use		5	世界樹の葉
			use		5	世界樹の実
			use		5	世界樹の花
			use		1	アロマエキス
			use		10	レアメタル
			use		1	火のマナ
			use		1	水のマナ
			use		1	風のマナ
			use		1	土のマナ
			get		60	世界樹のお守り	15%
@@EVENT
	start		15%
	basetime	2h
	plustime	12h
	code		costup-book
	startmsg	雨が降り始めました
	endmsg		雨が止みました
	info		湿気で書物が痛みやすくなっています
		param	薬剤師入門		cost*5
		param	薬剤師上級		cost*5
		param	調合師入門		cost*5
		param	調合師上級		cost*5
		param	錬金術入門		cost*5
		param	錬金術上級		cost*5
		param	調理師入門		cost*5
		param	調理師上級		cost*5
		param	細工師入門		cost*5
		param	細工師上級		cost*5
@@ITEM
	no	22
	type	薬品
	code	potion
	name	ポーション
	info	体力を回復させる薬
	price	100
	limit	5000/400
	base	10/3000
	pop	lv1
	point	lv7
	plus	2h
	scale	本
	cost	5
@@ITEM
	no	23
	type	薬品
	code	potion-high
	name	ハイポーション
	info	濃縮されたポーション
	price	500
	limit	1000/100
	base	400/1000
	pop	lv2
	point	lv6
	plus	-1h
	scale	本
	cost	20
@@ITEM
	no	24
	type	薬品
	code	potion-mana
	name	マナポーション
	info	マナの力を持ったポーション
	price	1000
	limit	600/60
	base	200/500
	pop	lv3
	point	lv6
	plus	-1h
	scale	本
	cost	50
@@ITEM
	no	25
	type	薬品
	code	ether
	name	エーテル
	info	魔力を回復させる薬
	price	500
	limit	1000/80
	base	10/2000
	pop	lv2
	point	lv6
	plus	5h
	scale	本
	cost	20
@@ITEM
	no	26
	type	薬品
	code	ether-high
	name	ハイエーテル
	info	濃縮されたエーテル
	price	1000
	limit	500/50
	base	200/500
	pop	lv3
	point	lv5
	plus	-1h
	scale	本
	cost	50
@@ITEM
	no	27
	type	薬品
	code	ether-mana
	name	マナエーテル
	info	マナの力を持ったエーテル
	price	2000
	limit	300/30
	base	100/500
	pop	lv4
	point	lv5
	plus	-1h
	scale	本
	cost	100
@@ITEM
	no	28
	type	薬品
	code	elixir
	name	エリクサー
	info	体力と魔力を回復させる薬
	price	5000
	limit	150/15
	base	100/200
	pop	lv5
	point	lv4
	plus	-1h
	scale	本
	cost	250
	funcs	_local_	#陳列していたエリクサーが売れた際にランダムで爵位が上昇するイベント発生
		my($ITEM,$DT,$count,$price)=@_;
		my $hitproba=$count*2;
		if(rand(1000)<$hitproba)
		{
		$DT->{dignity}+=1;
		WriteLog(2,0,$DT->{shopname}.'の販売したエリクサーが冒険者の命を救いました');
		WriteLog(2,0,$DT->{shopname}.'の功績を讃えて爵位が贈られました');
		WriteLog(0,$DT->{id},"爵位を1ポイント獲得しました");
		}
		return 0;
	_local_
@@ITEM
	no	29
	type	薬品
	code	elixir-last
	name	ラストエリクサー
	info	あまりの希少さにラスボス戦まで使われない薬
	price	10000
	limit	100/10
	base	100/200
	pop	lv6
	point	lv4
	plus	-1h
	scale	本
	cost	500
	funcs	_local_	#陳列していたラスエリが売れた際にランダムで爵位が上昇するイベント発生
		my($ITEM,$DT,$count,$price)=@_;
		my $hitproba=$count*5;
		if(rand(1000)<$hitproba)
		{
		$DT->{dignity}+=1;
		WriteLog(2,0,$DT->{shopname}.'の販売したラストエリクサーが勇者の命を救いました');
		WriteLog(2,0,$DT->{shopname}.'の功績を讃えて爵位が贈られました');
		WriteLog(0,$DT->{id},"爵位を1ポイント獲得しました");
		}
		return 0;
	_local_
@@EVENT
	start		10%
	basetime	18h
	plustime	12h
	code		plusdown-medicine
	startmsg	流行り病で薬品が高騰しています
	endmsg		流行り病は過ぎ去りました
	info		薬品が高騰しています
		param	ポーション		plus=-180
		param	ポーション		price*1.5
		param	ポーション		pop*2
		param	ハイポーション	price*1.5
		param	ハイポーション	pop*2
		param	マナポーション	price*1.5
		param	マナポーション	pop*2
		param	エーテル		plus=-180
		param	エーテル		price*1.5
		param	エーテル		pop*2
		param	ハイエーテル		price*1.5
		param	ハイエーテル		pop*2
		param	マナエーテル		price*1.5
		param	マナエーテル		pop*2
		param	エリクサー		price*1.5
		param	エリクサー		pop*2
		param	ラストエリクサー	price*1.5
		param	ラストエリクサー	pop*2
@@ITEM
	no	30
	type	香水
	code	cologne
	name	コロン
	info	ありふれた香水
	price	200
	limit	2500/250
	base	1000/2000
	pop	lv1
	point	lv8
	plus	-1h
	scale	本
	cost	10
@@ITEM
	no	31
	type	香水
	code	cologne-flower
	name	フラワーコロン
	info	花の香りの香水
	price	1500
	limit	400/40
	base	1000/2000
	pop	lv2
	point	lv7
	plus	-1h
	scale	本
	cost	75
@@ITEM
	no	32
	type	香水
	code	cologne-leaf
	name	リーフコロン
	info	森の香りの香水
	price	2500
	limit	300/30
	base	1000/2000
	pop	lv3
	point	lv6
	plus	-1h
	scale	本
	cost	125
@@EVENT
	start		10%
	basetime	12h
	plustime	12h
	code		pointup-cologne
	group		aroma
	startmsg	庶民の間でコロンがブームになっています
	endmsg		コロンブームは過ぎ去りました
	info		低価格のコロンが人気になっています
		param	コロン			point*2
		param	フラワーコロン	point*2
		param	リーフコロン		point*2
@@ITEM
	no	33
	type	香水
	code	aroma-oil
	name	アロマオイル
	info	花の香りを濃縮したオイル
	price	7500
	limit	100/10
	base	1000/2000
	pop	lv4
	point	lv5
	plus	-1h
	scale	本
	cost	275
@@ITEM
	no	34
	type	香水
	code	aroma-ex
	name	アロマエキス
	info	花の香りを凝縮したエキス
	price	12500
	limit	70/7
	base	1000/2000
	pop	lv5
	point	lv5
	plus	-1h
	scale	本
	cost	625
@@EVENT
	start		10%
	basetime	12h
	plustime	12h
	code		pointup-aroma
	group		aroma
	startmsg	巷ではアロマブームが巻き起こっています
	endmsg		アロマブームは過ぎ去りました
	info		アロマグッズが人気になっています
		param	アロマオイル		point*2
		param	アロマエキス		point*2
@@ITEM
	no	35
	type	香水
	code	cologne-salamander
	name	コロン・サラマンダー
	info	火の精霊を宿したコロン
	price	15000
	limit	60/6
	base	1000/2000
	pop	lv5
	point	lv5
	plus	-1h
	scale	本
	cost	750
@@ITEM
	no	36
	type	香水
	code	cologne-undine
	name	コロン・ウンディーネ
	info	水の精霊を宿したコロン
	price	15000
	limit	60/6
	base	1000/2000
	pop	lv5
	point	lv5
	plus	-1h
	scale	本
	cost	750
@@ITEM
	no	37
	type	香水
	code	cologne-sylph
	name	コロン・シルフ
	info	風の精霊を宿したコロン
	price	15000
	limit	60/6
	base	1000/2000
	pop	lv5
	point	lv5
	plus	-1h
	scale	本
	cost	750
@@ITEM
	no	38
	type	香水
	code	cologne-gnome
	name	コロン・ノーム
	info	土の精霊を宿したコロン
	price	15000
	limit	60/6
	base	1000/2000
	pop	lv5
	point	lv5
	plus	-1h
	scale	本
	cost	750
@@ITEM
	no	39
	type	香水
	code	aroma-forbidden
	name	禁断の香水
	info	色々混ぜた結果危ない香りになった香水
	price	20000
	limit	50/5
	base	1000/2000
	pop	lv6
	point	lv5
	plus	-1h
	scale	本
	cost	1000
	funcs	_local_	#陳列していた禁断の香水が売れた際にランダムで人気が上昇するイベント発生
		my($ITEM,$DT,$count,$price)=@_;
		my $hitproba=$count*10;
		if(rand(1000)<$hitproba)
		{
		$DT->{rank}+=int(($price/$count/20)*(2-$DT->{rank}/5000)) if($count);
		$DT->{rank}=10000 if($DT->{rank}>10000);
		WriteLog(2,0,$DT->{shopname}.'の販売した禁断の香水が雑誌に掲載されました');
		WriteLog(0,$DT->{id},"人気が上昇しました");
		}
		return 0;
	_local_
@@ITEM
	no	40
	type	錬金
	code	mana
	name	マナ
	info	魔力の結晶
	price	5000
	limit	150/15
	base	100/200
	pop	lv2
	point	lv2
	plus	-1h
	scale	個
	cost	100
@@ITEM
	no	41
	type	錬金
	code	mana-fire
	name	火のマナ
	info	火の魔力の結晶
	price	10000
	limit	100/10
	base	100/200
	pop	lv3
	point	lv2
	plus	-1h
	scale	個
	cost	100
@@ITEM
	no	42
	type	錬金
	code	mana-aqua
	name	水のマナ
	info	水の魔力の結晶
	price	10000
	limit	100/10
	base	100/200
	pop	lv3
	point	lv2
	plus	-1h
	scale	個
	cost	100
@@ITEM
	no	43
	type	錬金
	code	mana-wind
	name	風のマナ
	info	風の魔力の結晶
	price	10000
	limit	100/10
	base	100/200
	pop	lv3
	point	lv2
	plus	-1h
	scale	個
	cost	100
@@ITEM
	no	44
	type	錬金
	code	mana-earth
	name	土のマナ
	info	土の魔力の結晶
	price	10000
	limit	100/10
	base	100/200
	pop	lv3
	point	lv2
	plus	-1h
	scale	個
	cost	100
@@ITEM
	no	45
	type	錬金
	code	rare-metal
	name	レアメタル
	info	錬金術によって作られた貴金属
	price	3000
	limit	300/30
	base	100/200
	pop	lv3
	point	lv2
	plus	-1h
	scale	個
	cost	300
@@ITEM
	no	46
	type	錬金
	code	dark-matter
	name	ダークマター
	info	錬金術によって作られた暗黒物質
	price	6000
	limit	150/15
	base	100/200
	pop	lv4
	point	lv1
	plus	-1h
	scale	個
	cost	600
@@ITEM
	no	47
	type	錬金
	code	sophia-stone
	name	賢者の石
	info	高度錬金術の触媒とされる不思議な石
	price	40000
	limit	30/0
	pop	lv4
	point	lv2
	scale	個
	cost	1000
	funcs	_local_
		my($ITEM,$DT,$count,$price)=@_;
		my $hitproba=$count*5;
		if(rand(1000)<$hitproba)
		{
		$DT->{item}[@@ITEMNO"星屑"-1]++;
		$DT->{item}[@@ITEMNO"星屑"-1]=$ITEM[@@ITEMNO"星屑"]->{limit} if($DT->{item}[@@ITEMNO"星屑"-1]>$ITEM[@@ITEMNO"星屑"]->{limit});
		WriteLog(2,0,$DT->{shopname}.'の販売した賢者の石が不思議な光を発しました');
		WriteLog(0,$DT->{id},"なんと星屑を手に入れました");
		}
		return 0;
	_local_
@@ITEM
	no	48
	type	錬金
	code	salamander
	name	サラマンダー
	info	火の精霊
	price	80000
	limit	20/0
	pop	lv5
	point	lv2
	scale	体
	cost	1000
	flag	human
	@@use
		time	16h
		job		錬金術師	time/2
		scale	祭
		arg	nocount
		action	ギルドで祭開始
		name	ギルドで精霊祭
		info	火の精霊の祭りを開催します
			needevent	"priceup-fire"
			need		1	属性の知識
			need		1	火の指輪
			use		10	コロン・サラマンダー
			use		50	火のマナ
			use		5	サラマンダー	100%	不思議な力で活力が沸いてきました
		func	_local_
		main::OutError("ギルドに入っていません") if !$DT->{guild};
		WriteLog(3,0,"ギルド「".$main::GUILD{$DT->{guild}}->[$GUILDIDX_name]."」が精霊祭を開きました");
		foreach my $DTS (@DT)
			{
			next if ($DTS->{guild} ne $DT->{guild});
			my $up=int(500*(2-$DTS->{rank}/5000));
			$DTS->{rank}+=$up;
			$DTS->{rank}=10000 if $DTS->{rank}>10000;
			WriteLog(0,$DTS->{id},"精霊祭で人気が上昇しました");
			}
		return "";
		_local_
@@ITEM
	no	49
	type	錬金
	code	undine
	name	ウンディーネ
	info	水の精霊
	price	80000
	limit	20/0
	pop	lv5
	point	lv2
	scale	体
	cost	1000
	flag	human
	@@use
		time	16h
		job		錬金術師	time/2
		scale	祭
		arg	nocount
		action	ギルドで祭開始
		name	ギルドで精霊祭
		info	水の精霊の祭りを開催します
			needevent	"priceup-aqua"
			need		1	属性の知識
			need		1	水の指輪
			use		10	コロン・ウンディーネ
			use		50	水のマナ
			use		5	ウンディーネ	100%	不思議な力で活力が沸いてきました
		func	_local_
		main::OutError("ギルドに入っていません") if !$DT->{guild};
		WriteLog(3,0,"ギルド「".$main::GUILD{$DT->{guild}}->[$GUILDIDX_name]."」が精霊祭を開きました");
		foreach my $DTS (@DT)
			{
			next if ($DTS->{guild} ne $DT->{guild});
			my $up=int(500*(2-$DTS->{rank}/5000));
			$DTS->{rank}+=$up;
			$DTS->{rank}=10000 if $DTS->{rank}>10000;
			WriteLog(0,$DTS->{id},"精霊祭で人気が上昇しました");
			}
		return "";
		_local_
@@ITEM
	no	50
	type	錬金
	code	sylph
	name	シルフ
	info	風の精霊
	price	80000
	limit	20/0
	pop	lv5
	point	lv2
	scale	体
	cost	1000
	flag	human
	@@use
		time	16h
		job		錬金術師	time/2
		scale	祭
		arg	nocount
		action	ギルドで祭開始
		name	ギルドで精霊祭
		info	風の精霊の祭りを開催します
			needevent	"priceup-wind"
			need		1	属性の知識
			need		1	風の指輪
			use		10	コロン・シルフ
			use		50	風のマナ
			use		5	シルフ		100%	不思議な力で活力が沸いてきました
		func	_local_
		main::OutError("ギルドに入っていません") if !$DT->{guild};
		WriteLog(3,0,"ギルド「".$main::GUILD{$DT->{guild}}->[$GUILDIDX_name]."」が精霊祭を開きました");
		foreach my $DTS (@DT)
			{
			next if ($DTS->{guild} ne $DT->{guild});
			my $up=int(500*(2-$DTS->{rank}/5000));
			$DTS->{rank}+=$up;
			$DTS->{rank}=10000 if $DTS->{rank}>10000;
			WriteLog(0,$DTS->{id},"精霊祭で人気が上昇しました");
			}
		return "";
		_local_
@@ITEM
	no	51
	type	錬金
	code	gnome
	name	ノーム
	info	土の精霊
	price	80000
	limit	20/0
	pop	lv5
	point	lv2
	scale	体
	cost	1000
	flag	human
	@@use
		time	16h
		job		錬金術師	time/2
		scale	祭
		arg	nocount
		action	ギルドで祭開始
		name	ギルドで精霊祭
		info	土の精霊の祭りを開催します
			needevent	"priceup-earth"
			need		1	属性の知識
			need		1	土の指輪
			use		10	コロン・ノーム
			use		50	土のマナ
			use		5	ノーム		100%	不思議な力で活力が沸いてきました
		func	_local_
		main::OutError("ギルドに入っていません") if !$DT->{guild};
		WriteLog(3,0,"ギルド「".$main::GUILD{$DT->{guild}}->[$GUILDIDX_name]."」が精霊祭を開きました");
		foreach my $DTS (@DT)
			{
			next if ($DTS->{guild} ne $DT->{guild});
			my $up=int(500*(2-$DTS->{rank}/5000));
			$DTS->{rank}+=$up;
			$DTS->{rank}=10000 if $DTS->{rank}>10000;
			WriteLog(0,$DTS->{id},"精霊祭で人気が上昇しました");
			}
		return "";
		_local_
@@ITEM
	no	53
	type	食材
	code	mowmow-milk
	name	モーモー牛乳
	info	飲めば健康、経営すこやか
	price	300
	limit	2000/0
	pop	lv7
	point	lv7
	scale	本
	cost	50
	@@use
		time	2m
		scale	本
		action	飲む
		price	0
		name	飲む
		info	モーモー牛乳を飲んでみます
			use		1	モーモー牛乳
		func	_local_
			my $val=$count;
			my $ret="";
			
			if($count>=30)
			{
				$DT->{rank}-=$count*2;
				$DT->{rank}=0 if $DT->{rank}<0;
				WriteLog(2,0,$DT->{shopname}.'の店主が救急車で運ばれました');
				WriteLog(2,0,'いっぺんにモーモー牛乳'.$count.'本を飲むなんて正気の沙汰じゃありません');
				$ret="…気が付いたら病院のベッドの上でした";
			}
			elsif($count>=10)
			{
				$ret='オナカを壊してしまいました　いっぺんにモーモー牛乳'.$count.'本は飲み過ぎです';
				WriteLog(0,$DT->{id},$ret);
			}
			else
			{
				$DT->{rank}+=int(rand($count+1))+$count;
				$DT->{rank}=10000 if $DT->{rank}>10000;
				$ret='モーモー牛乳を飲んで健康になった気がします';
				WriteLog(0,$DT->{id},$ret);
			}
			return $ret;
		_local_
@@ITEM
	no	54
	type	食材
	code	fruit-powder
	name	木の実粉
	info	広く料理に使われる粉
	price	600
	limit	1000/100
	base	5000/10000
	pop	lv5
	point	lv4
	plus	1h
	scale	袋
	cost	50
@@ITEM
	no	55
	type	食材
	code	alcohol
	name	アルコール
	info	お酒や香水に使われる液体
	price	900
	limit	800/80
	base	5000/10000
	pop	lv5
	point	lv4
	plus	1h
	scale	本
	cost	100
@@ITEM
	no	56
	type	食材
	code	bread
	name	食パン
	info	市民の主食
	price	400
	limit	1600/160
	base	2000/10000
	pop	lv5
	point	lv5
	plus	1h
	scale	斤
	cost	30
@@ITEM
	no	57
	type	食材
	code	bread-fruit
	name	木の実パン
	info	木の実を混ぜた人気のパン
	price	800
	limit	1200/120
	base	1000/2000
	pop	lv5
	point	lv5
	plus	-1h
	scale	個
	cost	60
@@ITEM
	no	58
	type	食材
	code	bread-cheese
	name	チーズパン
	info	チーズを混ぜた通のパン
	price	1200
	limit	800/80
	base	1000/2000
	pop	lv5
	point	lv5
	plus	-1h
	scale	個
	cost	90
@@EVENT
	start		5%
	basetime	24h
	plustime	24h
	code		plusdown-powder
	group		bread
	startmsg	エネルギー革命で木の実粉が高騰しています
	endmsg		木の実粉の相場は落ち着きを取り戻したようです
	info		木の実粉製品が高騰しています
		param	木の実粉	plus=-180
		param	木の実粉	price*1.5
		param	木の実粉	pop*2
		param	食パン		plus=-180
		param	食パン		price*1.5
		param	食パン		pop*2
		param	木の実パン	price*1.5
		param	木の実パン	pop*2
		param	チーズパン	price*1.5
		param	チーズパン	pop*2
@@EVENT
	start		5%
	basetime	24h
	plustime	24h
	code		pricedown-bread
	group		bread
	startmsg	パンへの異物混入が発見されました
	endmsg		パンの相場は落ち着きを取り戻したようです
	info		パンの相場が下落しています
		param	食パン		price/1.5
		param	食パン		pop*1.5
		param	食パン		point/2
		param	木の実パン	price/1.5
		param	木の実パン	pop*1.5
		param	木の実パン	point/2
		param	チーズパン	price/1.5
		param	チーズパン	pop*1.5
		param	チーズパン	point/2
@@ITEM
	no	59
	type	食材
	code	yogurt
	name	ヨーグルト
	info	牛乳を発酵させて作る乳製品
	price	2000
	limit	300/30
	base	1000/2000
	pop	lv6
	point	lv5
	plus	-1h
	scale	個
	cost	200
@@ITEM
	no	60
	type	食材
	code	cheese
	name	チーズ
	info	ワインに合う栄養価の高い乳製品
	price	4000
	limit	150/15
	base	1000/2000
	pop	lv7
	point	lv4
	plus	-1h
	scale	個
	cost	400
@@EVENT
	start		10%
	basetime	24h
	plustime	24h
	code		priceup-milk
	group		bread
	startmsg	健康志向で乳製品が人気になっています
	endmsg		乳製品の相場は落ち着きを取り戻したようです
	info		乳製品が高騰しています
		param	モーモー牛乳	price*1.5
		param	モーモー牛乳	pop*2
		param	チーズパン	price*1.5
		param	チーズパン	pop*2
		param	ヨーグルト	price*1.5
		param	ヨーグルト	pop*2
		param	チーズ		price*1.5
		param	チーズ		pop*2
@@ITEM
	no	61
	type	食材
	code	sake-ygg
	name	美酒「世界樹」
	info	丁寧に醸造された名産の酒
	price	8000
	limit	100/10
	base	1000/2000
	pop	lv7
	point	lv5
	plus	-1h
	scale	本
	cost	500
	@@use
		time	20m
		scale	本
		action	飲む
		name	一人で月見酒
		info	一人寂しくお酒を飲みます
			use		1	美酒「世界樹」
		funcb	nightonly
		func	_local_
			my $val=$count;
			my $ret="";
			
			if($count>=10)
			{
				$DT->{rank}-=$count*10;
				$DT->{rank}=0 if $DT->{rank}<0;
				WriteLog(2,0,$DT->{shopname}.'の店主が救急車で運ばれました');
				WriteLog(2,0,'いっぺんに美酒「世界樹」'.$count.'本を飲むなんて正気の沙汰じゃありません');
				$ret="…気が付いたら病院のベッドの上でした";
			}
			elsif($count>=4)
			{
				$ret='酔っ払ってしまいました　いっぺんに美酒「世界樹」'.$count.'本は飲み過ぎです';
				WriteLog(0,$DT->{id},$ret);
			}
			else
			{
				$DT->{rank}+=$count*50;
				$DT->{rank}=10000 if $DT->{rank}>10000;
				$ret='美酒「世界樹」を飲んでほろ酔い気分です';
				WriteLog(0,$DT->{id},$ret);
			}
			return $ret;
		_local_
	@@use
		time	8h
		scale	宴会
		arg	nocount
		action	ギルドで宴会開始
		name	ギルドで花見酒
		info	昼間から大盤振る舞いです
			use		100	世界樹の花
			use		20	美酒「世界樹」	100%	明日への活力が沸いてきました
			use		10	マジカルパウダー
		funcb	dayonly
		func	_local_
		main::OutError("ギルドに入っていません") if !$DT->{guild};
		WriteLog(3,0,"ギルド「".$main::GUILD{$DT->{guild}}->[$GUILDIDX_name]."」が宴会を開きました");
		foreach my $DTS (@DT)
			{
			next if ($DTS->{guild} ne $DT->{guild});
			my $up=int(250*(2-$DTS->{rank}/5000));
			$DTS->{rank}+=$up;
			$DTS->{rank}=10000 if $DTS->{rank}>10000;
			WriteLog(0,$DTS->{id},"宴会で人気が上昇しました");
			}
		return "";
		_local_
@@ITEM
	no	62
	type	食材
	code	magical-powder
	name	マジカルパウダー
	info	舐めると不思議な気分になれる魔法の粉
	price	5000
	limit	200/20
	base	1000/2000
	pop	lv8
	point	lv4
	plus	-1h
	scale	ｇ
	cost	100
	@@use
		time	2m
		scale	ｇ
		action	食べる
		price	0
		name	食べる
		info	マジカルパウダーを食べてみます
			use		1	マジカルパウダー
		func	_local_
			my $val=$count;
			my $ret="";
			
			if($count>=30)
			{
				$DT->{rank}-=$count*2;
				$DT->{rank}=0 if $DT->{rank}<0;
				WriteLog(2,0,$DT->{shopname}.'の店主が救急車で運ばれました');
				WriteLog(2,0,'いっぺんにマジカルパウダー'.$count.'ｇを食べるなんて正気の沙汰じゃありません');
				$ret="…気が付いたら病院のベッドの上でした";
			}
			elsif($count>=10)
			{
				$DT->{time}+=$count*180;
				$ret='めまいがしてきました　いっぺんにマジカルパウダー'.$count.'ｇは食べすぎです';
				WriteLog(0,$DT->{id},$ret);
			}
			else
			{
				$DT->{time}-=$count*180;
				$ret='マジカルパウダーを食べていい気分になりました';
				WriteLog(0,$DT->{id},$ret);
			}
			return $ret;
		_local_
@@EVENT
	start		10%
	basetime	24h
	plustime	24h
	code		priceup-magical-powder
	startmsg	巷ではマジカルパウダーが流行しているようです
	endmsg		マジカルパウダーの流行は過ぎ去りました
	info		マジカルパウダーが流行しています
		param	マジカルパウダー	price*2
		param	マジカルパウダー	pop*1.5
		param	マジカルパウダー	point*3
@@ITEM
	no	63
	type	食材
	code	yaminabe
	name	闇鍋
	info	何が入っているのかは誰にもわからない禁断の料理
	price	13000
	limit	100/10
	base	1000/2000
	pop	lv9
	point	lv3
	plus	-1h
	scale	杯
	cost	1300
	funcs	_local_	#陳列していた闇鍋が売れた際にランダムで人気が上下するイベント発生
		my($ITEM,$DT,$count,$price)=@_;
		my $hitproba=$count*10;
		if(rand(1000)<$hitproba)
		{
			$DT->{rank}+=int($price/$count/10) if($count);
			$DT->{rank}=10000 if($DT->{rank}>10000);
			WriteLog(2,0,$DT->{shopname}.'の販売した闇鍋が雑誌に掲載されました');
			WriteLog(0,$DT->{id},"人気が上昇しました");
		}
		elsif(rand(1000)<$hitproba)
		{
			$DT->{rank}-=int($price/$count/10) if($count);
			$DT->{rank}=0 if($DT->{rank}<0);
			WriteLog(2,0,$DT->{shopname}.'の販売した闇鍋が食中毒を引き起こしました');
			WriteLog(0,$DT->{id},"人気が低下しました");
		}
		return 0;
	_local_
	@@use
		time	8h
		job		調理師	time/2
		scale	パーティ
		arg	target|nocount
		action	招待してパーティ開始
		name	闇鍋パーティ
		info	今夜は無礼講です
			use		8	チーズパン
			use		6	チーズ
			use		4	美酒「世界樹」
			use		2	闇鍋	100%	明日への活力が沸いてきました
		funcb	nightonly
		func	_local_
		main::OutError("自店を指定することはできません") if($DT==$DTS);
		$DT->{rank}+=400;
		$DT->{rank}=10000 if($DT->{rank}>10000);
		$DTS->{rank}+=400;
		$DTS->{rank}=10000 if($DTS->{rank}>10000);
		WriteLog(3,0,"$DT->{shopname}が$DTS->{shopname}を誘って闇鍋パーティを開きました");
		WriteLog(0,$DT->{id},"闇鍋パーティで人気が上昇しました");
		WriteLog(0,$DTS->{id},"闇鍋パーティに誘われて人気が上昇しました");
		return "";
		_local_
@@ITEM
	no	64
	type	細工
	code	dry-flower
	name	ドライフラワー
	info	世界樹の花を乾燥させたもの
	price	3500
	limit	200/20
	base	1000/2000
	pop	lv3
	point	lv3
	plus	-1h
	scale	個
	cost	50
	@@use
		time	2m
		scale	回
		action	浸けてみる
		name	水に浸けてみる
		info	ドライフラワーが世界樹の花に戻るかもしれません
		okmsg	ドライフラワーは世界樹の花に戻りました
			use		10	ドライフラワー
			use		1	ミネラル水
			get		10	世界樹の花
@@ITEM
	no	65
	type	細工
	code	wood-rod
	name	木の棒
	info	このままでも武器になる棒
	price	7000
	limit	100/10
	base	500/5000
	pop	lv4
	point	lv2
	plus	4h
	scale	本
	cost	100
@@ITEM
	no	66
	type	細工
	code	wood-sword
	name	木刀
	info	観光地のお土産として有名
	price	1500
	limit	400/40
	base	1000/2000
	pop	lv3
	point	lv3
	plus	-1h
	scale	本
	cost	100
@@ITEM
	no	67
	type	細工
	code	wood-bear
	name	木彫りの熊
	info	観光地のお土産として有名
	price	3000
	limit	200/20
	base	1000/2000
	pop	lv3
	point	lv3
	plus	-1h
	scale	個
	cost	200
	funcs	_local_
		my($ITEM,$DT,$count,$price)=@_;
		my $hitproba=$count*2;
		if(rand(1000)<$hitproba)
		{
		$DT->{rank}+=int(($price/$count/20)*(2-$DT->{rank}/5000)) if($count);
		$DT->{rank}=10000 if($DT->{rank}>10000);
		WriteLog(2,0,$DT->{shopname}.'の販売した木彫りの熊が話題になっています');
		WriteLog(0,$DT->{id},"人気が上昇しました");
		}
		return 0;
	_local_
@@EVENT
	start		5%
	basetime	24h
	plustime	24h
	code		priceup-wood
	group		wood
	startmsg	街は観光ブームで賑わっています
	endmsg		観光ブームは過ぎ去りました
	info		お土産グッズが高騰しています
		param	木刀		price*1.5
		param	木刀		pop*2
		param	木彫りの熊	price*1.5
		param	木彫りの熊	pop*2
@@ITEM
	no	68
	type	細工
	code	wood-chair
	name	木の椅子
	info	手作り感あふれる木の椅子
	price	4500
	limit	150/15
	base	1000/2000
	pop	lv4
	point	lv3
	plus	-1h
	scale	個
	cost	300
@@ITEM
	no	69
	type	細工
	code	wood-desk
	name	木の机
	info	手作り感あふれる木の机
	price	6000
	limit	100/10
	base	1000/2000
	pop	lv5
	point	lv2
	plus	-1h
	scale	個
	cost	400
@@EVENT
	start		5%
	basetime	24h
	plustime	24h
	code		priceup-school
	group		wood
	startmsg	街に学校建設計画が持ち上がりました
	endmsg		学校建設計画は白紙に戻りました
	info		机と椅子が高騰しています
		param	木の椅子	price*1.5
		param	木の椅子	pop*2
		param	木の机		price*1.5
		param	木の机		pop*2
@@EVENT
	start		5%
	basetime	24h
	plustime	12h
	code		popdown-wood
	group		wood
	startmsg	素朴な木工細工が人気になっています
	endmsg		木工細工ブームは過ぎ去りました
	info		木工細工がよく売れています
		param	木の棒		pop/1.5
		param	木刀		pop/1.5
		param	木彫りの熊	pop/1.5
		param	木の椅子	pop/1.5
		param	木の机		pop/1.5
@@ITEM
	no	70
	type	細工
	code	ring-magic
	name	魔法の指輪
	info	身に着けると魔法が使えるようになる指輪
	price	9000
	limit	100/10
	base	1000/2000
	pop	lv4
	point	lv3
	plus	-1h
	scale	個
	cost	100
@@ITEM
	no	71
	type	細工
	code	ring-fire
	name	火の指輪
	info	火の魔力を秘めた指輪
	price	18000
	limit	50/5
	base	1000/2000
	pop	lv5
	point	lv3
	plus	-1h
	scale	個
	cost	100
@@ITEM
	no	72
	type	細工
	code	ring-aqua
	name	水の指輪
	info	水の魔力を秘めた指輪
	price	18000
	limit	50/5
	base	1000/2000
	pop	lv5
	point	lv3
	plus	-1h
	scale	個
	cost	100
@@ITEM
	no	73
	type	細工
	code	ring-wind
	name	風の指輪
	info	風の魔力を秘めた指輪
	price	18000
	limit	50/5
	base	1000/2000
	pop	lv5
	point	lv3
	plus	-1h
	scale	個
	cost	100
@@ITEM
	no	74
	type	細工
	code	ring-earth
	name	土の指輪
	info	土の魔力を秘めた指輪
	price	18000
	limit	50/5
	base	1000/2000
	pop	lv5
	point	lv3
	plus	-1h
	scale	個
	cost	100
@@EVENT
	start		5%
	basetime	24h
	plustime	12h
	code		popdown-ring
	startmsg	街では結婚ラッシュです
	endmsg		結婚ラッシュは過ぎ去りました
	info		恋人に贈る指輪がよく売れています
		param	魔法の指輪		pop/1.5
		param	火の指輪		pop/1.5
		param	水の指輪		pop/1.5
		param	風の指輪		pop/1.5
		param	土の指輪		pop/1.5
@@ITEM
	no	75
	type	細工
	code	talisman-ygg
	name	世界樹のお守り
	info	運気が上昇する世界樹のお守り
	price	36000
	limit	30/3
	base	1000/2000
	pop	lv6
	point	lv6
	plus	-1h
	scale	個
	cost	500
	funcs	_local_
		my($ITEM,$DT,$count,$price)=@_;
		my $hitproba=$count*10;
		if(rand(1000)<$hitproba)
		{
			if(rand(1000)<750)
			{
				$DT->{rank}+=int(($price/$count/20)*(2-$DT->{rank}/5000)) if($count);
				$DT->{rank}=10000 if($DT->{rank}>10000);
				WriteLog(2,0,$DT->{shopname}.'の販売した世界樹のお守りが雑誌に掲載されました');
				WriteLog(0,$DT->{id},"人気が上昇しました");
			}
			else
			{
				$DT->{item}[@@ITEMNO"星屑"-1]++;
				$DT->{item}[@@ITEMNO"星屑"-1]=$ITEM[@@ITEMNO"星屑"]->{limit} if($DT->{item}[@@ITEMNO"星屑"-1]>$ITEM[@@ITEMNO"星屑"]->{limit});
				WriteLog(2,0,$DT->{shopname}.'の販売した世界樹のお守りが不思議な光を発しました');
				WriteLog(0,$DT->{id},"なんと星屑を手に入れました");
			}
		}
		return 0;
	_local_
	funct	_local_
		#標準価格未満で陳列中の場合1日10%の無条件人気アップ
		my($ITEM,@DT)=@_;
		my $rankup=$TIMESPAN/86.4;
		$rankup=$rankup<1 && rand(1)<$rankup ? 1 : int($rankup);
		return if !$rankup;
		foreach my $DT (@DT)
		{
			next if $DT->{showcase}[0]!=$ITEM->{no} || $DT->{price}[0]>$ITEM->{price};
			
			$DT->{rank}+=$rankup;
			$DT->{rank}=10000 if $DT->{rank}>10000;
		}
	_local_
@@ITEM
	no	1
	type	原料
	code	ygg-leaf
	name	世界樹の葉
	info	万病に効くとされる世界樹の葉
	price	1000
	limit	500/0
	pop	10d
	point	25%
	scale	枚
	cost	100
@@ITEM
	no	2
	type	原料
	code	ygg-fruit
	name	世界樹の実
	info	万病に効くとされる世界樹の実
	price	2000
	limit	300/0
	pop	10d
	point	25%
	scale	個
	cost	200
@@ITEM
	no	3
	type	原料
	code	ygg-flower
	name	世界樹の花
	info	万病に効くとされる世界樹の花
	price	3000
	limit	200/0
	pop	10d
	point	25%
	scale	個
	cost	300
@@ITEM
	no	4
	type	原料
	code	ygg-branch
	name	世界樹の枝
	info	世界樹の根元で拾った枝の一折
	price	5000
	limit	100/10
	base	10/100
	pop	10d
	point	25%
	plus	-20m
	scale	本
	cost	50
	@@use
		time	1h
		scale	本
		action	むしり取る
		name	世界樹の葉を取る
		info	枝から世界樹の葉を取ります
		okmsg	世界樹の葉をたくさん取りました
		ngmsg	葉は1枚も取れませんでした…
			use		1	世界樹の枝
			get		10	世界樹の葉	50%
			get		2	世界樹の実	50%	世界樹の実を見つけました
@@ITEM
	no	5
	type	原料
	code	ygg-leaf-bright
	name	輝く世界樹の葉
	info	不思議な輝く世界樹の葉
	price	100000
	limit	3/0
	pop	0
	scale	枚
	cost	100
	flag	noshowcase|onlysend
	@@use
		time	0
		scale	回
		action	使ってみる
		name	不思議な力を使う
		info	輝く葉に秘められた不思議な力を使います
		param	24
		arg	nocount
			use		3	輝く世界樹の葉
		func	_local_
		$cnt=$USE->{param1}*$count;
		$DT->{time}-=$cnt*3600;
		$ret="不思議な力で活動時間が$cnt時間増加しました";
		WriteLog(0,$DT->{id},$ret);
		WriteLog(3,0,"$DT->{shopname}が輝く世界樹の葉を使いました");	
		return $ret;
		_local_
@@ITEM
	no	6
	type	原料
	code	ygg-leaf-withered
	name	枯れた世界樹の葉
	info	枯れてしまった世界樹の葉
	price	10
	limit	1000/10
	base	1000/1500
	pop	10d
	point	25%
	plus	-20m
	scale	枚
	cost	10
	@@use
		time	8h
		job		調理師	time/2
		scale	パーティ
		arg	target|nocount
		action	招待してパーティ開始
		name	焼き芋パーティ
		info	枯れ葉で盛大に焼き芋します
			need		1	火の指輪
			use		10	世界樹の枝
			use		1000	枯れた世界樹の葉	100%	明日への活力が沸いてきました
			use		10	火のマナ
		funcb	dayonly
		func	_local_
		main::OutError("自店を指定することはできません") if($DT==$DTS);
		$DT->{rank}+=400;
		$DT->{rank}=10000 if($DT->{rank}>10000);
		$DTS->{rank}+=400;
		$DTS->{rank}=10000 if($DTS->{rank}>10000);
		WriteLog(3,0,"$DT->{shopname}が$DTS->{shopname}を誘って焼き芋パーティを開きました");
		WriteLog(0,$DT->{id},"焼き芋パーティで人気が上昇しました");
		WriteLog(0,$DTS->{id},"焼き芋パーティに誘われて人気が上昇しました");
		return "";
		_local_
@@ITEM
	no	7
	type	原料
	code	mana-ore
	name	マナ鉱石
	info	魔力の源であるマナの鉱石
	price	500
	limit	1000/500
	base	300/3000
	pop	10d
	point	25%
	plus	-20m
	scale	個
	cost	10
	@@use
		time	20m
		scale	回
		action	溶かし込む
		name	マナを水に溶かし込む
		info	マナを水に溶かして加工しやすくします
		okmsg	マナ水をたくさん作りました
			use		10	マナ鉱石	80%
			use		10	ミネラル水
			get		10	マナ水
@@EVENT
	start		33%
	basetime	18h
	plustime	12h
	code		plusup-mana
	startmsg	新たにマナ鉱脈が見つかりました
	endmsg		新しいマナ鉱脈が閉山しました
	info		マナ鉱石の流通量が急激に増えています
		param	マナ鉱石	plus=600
@@ITEM
	no	8
	type	原料
	code	water-mineral
	name	ミネラル水
	info	ちょっとおいしい気がする水
	price	100
	limit	1000/400
	base	100/2000
	pop	lv1
	point	lv2
	plus	1h
	scale	本
	cost	10
@@EVENT
	start		10%
	basetime	24h
	plustime	24h
	code		plusdown-water
	startmsg	ミネラル水業者の水源が枯れてしまったようです
	endmsg		ミネラル水業者がミネラル水の卸を再開しました
	info		市場へのミネラル水供給が止まっています
		param	ミネラル水	plus=-180
@@ITEM
	no	9
	type	原料
	code	water-mana
	name	マナ水
	info	魔力の源であるマナを溶かした水
	price	1000
	limit	500/200
	base	1000/10000
	pop	lv2
	point	lv2
	plus	-20m
	scale	本
	cost	10
@@EVENT
	start		5%
	basetime	3h
	plustime	6h
	code		plusup-mana-water
	startmsg	ミネラル水業者がマナ水の卸を始めました
	endmsg		ミネラル水業者がマナ水の卸を打ち切りました
	info		マナ水の流通量が急激に増えています
		param	マナ水		plus=1000
@@ITEM
	no	52
	type	道具
	code	mowmow
	name	モーモー
	info	家畜の一種
	price	20000
	cost	3000
	limit	10/2
	pop	0
	plus	1d
	scale	頭
	flag	noshowcase
	@@use
		time	80m
		exp		1%
		exptime	40m
		scale	搾乳
		action	搾る
		name	乳を搾る
		info	モーモーから乳を搾ります
		param	1.5
			need		1	モーモー
			use		1	枯れた世界樹の葉
		func	_local_	#搾乳バランス改変
			my $val=$USE->{param1}*$count;
			my $milk=@@ITEMNO"モーモー牛乳";
			my $cow=$USE->{itemno};
			my $expert=int($DT->{exp}{$cow}/50)+1;
			$val=$val*$DT->{item}[$cow-1]+$expert;
			$val=int(rand($val))+$DT->{item}[$cow-1];
			AddItem($milk,$val,'モーモー牛乳を精製しました');
			
			my $useproba=$USE->{param1}*$USE->{param1};
			my $usecount=0;
			foreach(1..$count)
			{
				$usecount++ if rand(1000)<$useproba;
			}
			UseItem($cow,$usecount,$ITEM[$cow]->{name}.'が'.($USE->{param1}==1.5?'寿命':'過労').'で天に召されました') if $usecount;
			
			my $ret='モーモー牛乳を'.$val.'本精製しました';
			return $ret;
		_local_
	@@use
		time	80m
		exp		1%
		exptime	40m
		scale	搾乳
		action	搾る
		name	ハードに乳を搾る
		info	モーモーからハードに乳を搾ります
		param	3
		func	_local_1
			needexp	20%
			need		1	モーモー
			use		3	枯れた世界樹の葉
@@ITEM
	no	76
	type	道具
	code	qualification
	name	資格申請書
	info	一部アイテムの作成に必要な資格を取得します
	price	1000
	cost	0
	limit	3/2
	pop	0
	plus	10h
	scale	枚
	flag	noshowcase|norequest
	@@use
		time	1h
		scale	回
		action	受験する
		name	薬剤師の資格を取る
		info	薬剤師の資格試験を受験します
		arg	nocount
		param	77,12:13,200,850	#手に入るアイテム,熟練度が必要なアイテム,合格率下限,合格率上限
			needpoint	15000
			use		1	資格申請書
		func	_local_
			my $getitem=$USE->{param1};
			my $val=$USE->{param3};

			foreach my $exps (split(/:/,$USE->{param2}))
			{
			my $valplus=int($DT->{exp}{$exps});
			$val+=$valplus;
			}
			$val=$USE->{param4} if($val>$USE->{param4});
			my $ret="";
			if(rand(1000)<$val)
			{
			AddItem($getitem,1,$ITEM[$getitem]->{name}.'を取得しました');
			WriteLog(3,0,"$DT->{shopname}が$ITEM[$getitem]->{name}を取得しました");
			$ret.="試験に合格しました！";
			}
			else
			{
			$ret.="試験に落第しました…";
			}
			return $ret;
		_local_
	@@use
		time	1h
		scale	回
		action	受験する
		name	酒醸造の資格を取る
		info	酒醸造の資格試験を受験します
		arg	nocount
		param	78,18:19,250,900
			needpoint	15000
			use		1	資格申請書
		funcb	_local_	#爵位が必要
			my($USE)=@_;
			my $val=$DT->{dignity};
			my $needdignity=1;
			if($val< $needdignity)
			{
			$USE->{name}='爵位が足りません';
			return 2;
			}
			return 0;
		_local_
		func	_local_1
@@ITEM
	no	77
	type	道具
	code	license-pharmacist
	name	薬剤師免許
	info	一部薬品の作成に必要な免許
	price	0
	limit	1/0
	pop	0
	scale	資格
	flag	noshowcase|norequest
@@ITEM
	no	78
	type	道具
	code	license-sake
	name	酒醸造免許
	info	お酒の醸造に必要な免許
	price	0
	limit	1/0
	pop	0
	scale	資格
	flag	noshowcase|norequest
@@ITEM
	no	80
	type	道具
	code	skill-element
	name	属性の知識
	info	属性の影響力に関する知識
	price	0
	cost	0
	limit	1/0
	pop	0
	scale	知識
	flag	noshowcase|norequest
@@ITEM
	no	81
	type	道具
	code	skill-magic
	name	魔法の知識
	info	魔法の使い方に関する知識
	price	0
	cost	0
	limit	1/0
	pop	0
	scale	知識
	flag	noshowcase|norequest
@@ITEM
	no	82
	type	道具
	code	skill-forbidden
	name	禁断の知識
	info	禁断の魔術に関する知識
	price	0
	cost	0
	limit	1/0
	pop	0
	scale	知識
	flag	noshowcase|norequest
@@ITEM
	no	83
	type	道具
	code	skill-shopping
	name	目利きの真髄
	info	良い商品をすばやく選別する真髄
	price	0
	cost	0
	limit	1/0
	pop	0
	scale	真髄
	flag	noshowcase|norequest
@@ITEM
	no	84
	type	道具
	code	edit-showcase
	name	陳列棚増築取壊キット
	info	陳列棚の増築や取り壊し等に必要な道具一式
	price	50000
	limit	1/1
	pop	0
	plus	1d
	scale	キット
	cost	500
	flag	noshowcase|norequest
	@@use
		time	1h
		scale	回
		action	作業する
		name	陳列棚を2つ減らす
		info	陳列棚を2つ減らします
		arg	nocount
		param	-2
			use		1	陳列棚増築取壊キット
		funcb	_local_
		my $oldcnt=$DT->{showcasecount};
		return 1 if($oldcnt < 3);
		_local_
		func	_local_
		$oldcnt=$DT->{showcasecount};
		$cntplus=$USE->{param1};
		$newcnt=$oldcnt+$cntplus;
		$DT->{showcasecount}=$newcnt;

		if($oldcnt < $newcnt)
		{
		foreach ($oldcnt..$newcnt-1)
		{
			$DT->{showcase}[$_]=0;
			$DT->{price}[$_]=0;
		}
		}
		if($oldcnt > $newcnt)
		{
			splice(@{$DT->{showcase}},$newcnt);
			splice(@{$DT->{price}},$newcnt);
		}

		$ret="陳列棚を$DT->{showcasecount}個にしました";
		WriteLog(2,0,"$DT->{shopname}の陳列棚が$DT->{showcasecount}個になりました");
		WriteLog(0,$DT->{id},$ret);
		return $ret;
		_local_
	@@use
		time	10m
		name	陳列棚を1つ減らす
		info	陳列棚を1つ減らします
		arg	nocount
		param	-1
			use		1	陳列棚増築取壊キット
		funcb	_local_
		my $oldcnt=$DT->{showcasecount};
		return 1 if($oldcnt < 2);
		_local_
		func	_local_1
	@@use
		time	2h
		name	陳列棚を1つ増やす
		info	陳列棚を1つ増やします
		arg	nocount
		param	1
			use		1	陳列棚増築取壊キット
		funcb	_local_
		my $oldcnt=$DT->{showcasecount};
		return 1 if($oldcnt > 7);
		_local_
		func	_local_1
	@@use
		time	5h
		name	陳列棚を2つ増やす
		info	陳列棚を2つ増やします
		arg	nocount
		param	2
			use		1	陳列棚増築取壊キット
		funcb	_local_
		my $oldcnt=$DT->{showcasecount};
		return 1 if($oldcnt > 6);
		_local_
		func	_local_1
@@ITEM
	no	85
	type	書物
	code	book-jobchange
	name	転職のススメ
	info	他業種への転職について書かれた本
	price	50000
	limit	1/1
	pop	0
	plus	1d
	scale	冊
	cost	500
	flag	noshowcase|norequest
	@@USE
		time	6h
		action	転職する
		scale	回
		arg	nocount
		name	すっぴん
		info	すっぴんに転職します
			use		1	転職のススメ
		funcb _local_
			return 1 if !$DT->{job};
		_local_
		func	jobport
	@@USE
		time	6h
		action	転職する
		scale	回
		arg	nocount
		name	執筆師
		info	執筆師に転職します
		param	10,250,writer
			use		1	転職のススメ
		funcb	needexp
		func	jobport
	@@USE
		time	6h
		action	転職する
		scale	回
		arg	nocount
		name	薬剤師
		info	薬剤師に転職します
		param	12,250,pharmacist
			use		1	転職のススメ
		funcb	needexp
		func	jobport
	@@USE
		time	6h
		action	転職する
		scale	回
		arg	nocount
		name	調合師
		info	調合師に転職します
		param	14,250,therapist
			use		1	転職のススメ
		funcb	needexp
		func	jobport
	@@USE
		time	6h
		action	転職する
		scale	回
		arg	nocount
		name	錬金術師
		info	錬金術師に転職します
		param	16,250,alchemist
			use		1	転職のススメ
		funcb	needexp
		func	jobport
	@@USE
		time	6h
		action	転職する
		scale	回
		arg	nocount
		name	調理師
		info	調理師に転職します
		param	18,250,cook
			use		1	転職のススメ
		funcb	needexp
		func	jobport
	@@USE
		time	6h
		action	転職する
		scale	回
		arg	nocount
		name	細工師
		info	細工師に転職します
		param	20,250,designer
			use		1	転職のススメ
		funcb	needexp
		func	jobport
@@ITEM
	no	86
	type	道具
	code	cm
	name	広告パック
	info	人気を上げられますが失敗することも…
	price	100000
	limit	1/0.1
	base	10/50
	pop	0
	plus	5d
	scale	パック
	cost	10000
	flag	noshowcase
	@@USE
		time	10h
		scale	回
		action	広告する
		name	自店の広告を出す
		info	自分の店の人気を上げられます
		arg		nocount
			use		1	広告パック
		func	_local_
				my $up=int(500*(2-$DT->{rank}/5000));
				if ( rand(1000)<250 ) {
					$DT->{rank}-=$up;
					$DT->{rank}=1000 if $DT->{rank}<1000;
					my $ret="広告は裏目に出てしまいました：人気".int($up/100)."%ダウン";
					WriteLog(0,$DT->{id},$ret);
					WriteLog(3,0,$DT->{shopname}."が広告を出しましたがかえって逆効果でした。");
					return $ret;
				}
				$DT->{rank}+=$up;
				$DT->{rank}=10000 if $DT->{rank}>10000;
				my $ret="広告を出しました：人気".int($up/100)."%アップ";
				WriteLog(0,$DT->{id},$ret);
				WriteLog(3,0,$DT->{shopname}."が広告を出しました。");
				return $ret;
			_local_
	@@USE
		time	10h
		name	他店の広告を出す
		info	他店の人気を上げられます
		arg		target|nocount
			use		1	広告パック
		func	_local_
				return '自店を指定することはできません' if ($DT==$DTS);
				my $up=int(500*(2-$DTS->{rank}/5000));
				$DTS->{rank}+=$up;
				$DTS->{rank}=10000 if $DTS->{rank}>10000;
				my $ret="広告を出しました：".$DTS->{shopname}."の人気".int($up/100)."%アップ";
				WriteLog(0,$DT->{id},$ret);
				WriteLog(3,0,$DT->{shopname}."が".$DTS->{shopname}."の広告を出しました。");
				return $ret;
			_local_
	@@USE
		time	16h
		name	ギルドの広告を出す
		info	同ギルド所属店全ての人気を上げられます
		arg		nocount
			use		1	広告パック
			use		20	世界樹の花
		func	_local_
				return 'ギルドに入っていないため広告を出せませんでした' if !$DT->{guild};

				WriteLog(3,0,$DT->{shopname}."がギルド「".$main::GUILD{$DT->{guild}}->[$GUILDIDX_name]."」の広告を出しました。");
				foreach my $DTS (@DT)
				{
				next if ($DTS->{guild} ne $DT->{guild});
				my $up=int(500*(2-$DTS->{rank}/5000));
				$DTS->{rank}+=$up;
				$DTS->{rank}=10000 if $DTS->{rank}>10000;
				my $ret="ギルド広告を出しました：".$DTS->{shopname}."の人気".int($up/100)."%アップ";
				WriteLog(0,$DT->{id},$ret);
				}
				return 'ギルド広告を出しました';
			_local_
@@ITEM
	no	87
	type	書物
	code	book-work
	name	困った時に読む本
	info	経営に行き詰った時に
	price	0
	limit	1/1
	pop	0
	plus	10h
	scale	冊
	flag	noshowcase|norequest
	@@USE
		time	4h
		scale	回
		action	働く
		name	ティッシュ配りで資金稼ぎ
		info	お手軽に稼ぎましょう
		param	3000
		func	_local_
			$DT->{money}+=$USE->{param1}*$count;
			my $ret=GetMoneyString($USE->{param1}*$count).'稼ぎました';
			WriteLog(0,$DT->{id},"バイトし、$ret");
			WriteLog(3,0,$DT->{shopname}."がバイトしたようです");
			return $ret;
		_local_
	@@USE
		time	8h
		scale	回
		action	働く
		name	日雇い土木作業で資金稼ぎ
		info	ちょっときついけどそこそこの稼ぎです
		param	10000
		func	_local_1
	@@USE
		time	6h
		price	1000000
		arg	select|nocount
		action	忘却する
		name	熟練度を忘却する
		info	専門職の熟練度を忘れてしまいます
		argselect	職業選択;10;執筆師;12:13;薬剤師;14:15;調合師;16:17;錬金術師;18:19;調理師;20:21;細工師
		func	_local_
			$select=$USE->{arg}{select};
			$job="$USE->{arg}{select_hash}{$select}";
			foreach my $exps (split(/:/,$select))
			{
			$DT->{exp}{$exps}=0;
			}
 			$ret=$job.'の熟練度を忘却しました';
			WriteLog(3,0,$DT->{shopname}."が$ret");
			return $ret;
		_local_
@@ITEM
	no	88
	type	道具
	code	robot
	name	店番ロボット
	info	商品の陳列を手伝ってくれる優しいロボット
	price	250000
	cost	10000
	limit	5/0
	pop	0
	scale	台
	flag	noshowcase|human
@@ITEM
	no	89
	type	道具
	code	cat-white
	name	白猫さん
	info	お店のマスコット猫になってくれます
	price	500000
	cost	30000
	limit	1/0.1
	pop	0
	plus	5d
	scale	匹
	flag	noshowcase|human|icon
	funct	_local_
		my($ITEM,@DT)=@_;
		my $rankup=($TIMESPAN/86.4)*((10000-$DT->{rank})/10000);
		$rankup*=0.9;
		$rankup=$rankup<1 && rand(1)<$rankup ? 1 : int($rankup);
		return if !$rankup;
		my $itemno=$ITEM->{no};
		foreach my $DT (@DT)
		{
			next if !$DT->{item}[$itemno-1];
			$DT->{rank}+=$rankup;
			$DT->{rank}=10000 if $DT->{rank}>10000;
		}
	_local_
@@EVENT
	start		30%
	basetime	0h
	plustime	0h
	code		cat-bye-white
	info		白猫さん家出
	startfunc	_local_
		foreach my $DT (@DT)
		{
			next if !$DT->{item}[@@ITEMNO"白猫さん"-1];
			next if (rand(1000)>100);

			$DT->{item}[@@ITEMNO"白猫さん"-1]--;
			WriteLog(0,$DT->{id},"お店にいたはずの白猫さんがいなくなっています");
			return (0,$DT->{shopname}.'の白猫さんはどこかへ行ってしまいました');
		}
		return 0;
	_local_
@@ITEM
	no	90
	type	道具
	code	cat-black
	name	黒猫さん
	info	お店のマスコット猫になってくれます
	price	500000
	cost	30000
	limit	1/0.1
	pop	0
	plus	5d
	scale	匹
	flag	noshowcase|human|icon
	funct	_local_
		my($ITEM,@DT)=@_;
		my $rankup=($TIMESPAN/86.4)*((10000-$DT->{rank})/10000);
		$rankup=$rankup<1 && rand(1)<$rankup ? 1 : int($rankup);
		return if !$rankup;
		my $itemno=$ITEM->{no};
		foreach my $DT (@DT)
		{
			next if !$DT->{item}[$itemno-1];
			$DT->{rank}+=$rankup;
			$DT->{rank}=10000 if $DT->{rank}>10000;
		}
	_local_
@@EVENT
	start		40%
	basetime	0h
	plustime	0h
	code		cat-bye-black
	info		黒猫さん家出
	startfunc	_local_
		foreach my $DT (@DT)
		{
			next if !$DT->{item}[@@ITEMNO"黒猫さん"-1];
			next if (rand(1000)>100);

			$DT->{item}[@@ITEMNO"黒猫さん"-1]--;
			WriteLog(0,$DT->{id},"お店にいたはずの黒猫さんがいなくなっています");
			return (0,$DT->{shopname}.'の黒猫さんはどこかへ行ってしまいました');
		}
		return 0;
	_local_
@@ITEM
	no	91
	type	道具
	code	gift
	name	ギフト券
	info	欲しいものを手に入れよう！
	price	50000
	cost	10
	limit	10/0
	pop	0
	scale	枚
	flag	noshowcase
	@@USE
		time	20m
		scale	回
		action	引き換え
		name	本執筆キットと引き換え
		info	本執筆キットと引き換えます
		okmsg	ご利用ありがとうございました
		arg	nocount
			use		1	ギフト券
			get		5	本執筆キット
	@@USE
		time	20m
		scale	回
		action	引き換え
		name	陳列棚増築取壊キットと引き換え
		info	陳列棚増築取壊キットと引き換えます
		okmsg	ご利用ありがとうございました
		arg	nocount
			use		1	ギフト券
			get		1	陳列棚増築取壊キット
	@@USE
		time	20m
		scale	回
		action	引き換え
		name	転職のススメと引き換え
		info	転職のススメと引き換えます
		okmsg	ご利用ありがとうございました
		arg	nocount
			use		1	ギフト券
			get		1	転職のススメ
	@@USE
		time	20m
		scale	回
		action	引き換え
		name	モーモーと引き換え
		info	モーモーと引き換えます
		okmsg	ご利用ありがとうございました
		arg	nocount
			use		2	ギフト券
			get		5	モーモー
	@@USE
		time	20m
		scale	回
		action	引き換え
		name	広告パックと引き換え
		info	広告パックと引き換えます
		okmsg	ご利用ありがとうございました
		arg	nocount
			use		2	ギフト券
			get		1	広告パック
	@@USE
		time	20m
		scale	回
		action	引き換え
		name	お掃除券と引き換え
		info	お掃除券と引き換えます
		okmsg	ご利用ありがとうございました
		arg	nocount
			use		2	ギフト券
			get		1	お掃除券
	@@USE
		time	20m
		scale	回
		action	引き換え
		name	初心者セットと引き換え
		info	初心者セットと引き換えます
		okmsg	ご利用ありがとうございました
		arg	nocount
			use		3	ギフト券
			get		1	本執筆キット
			get		1	探索のススメ
			get		8	世界樹の葉
			get		30	ミネラル水
			get		1	陳列棚増築取壊キット
			get		1	転職のススメ
	@@USE
		time	20m
		scale	回
		action	引き換え
		name	店番ロボットと引き換え
		info	店番ロボットと引き換えます
		okmsg	ご利用ありがとうございました
		arg	nocount
			use		5	ギフト券
			get		1	店番ロボット
	@@USE
		time	20m
		scale	回
		action	引き換え
		name	魔法の箒と引き換え
		info	魔法の箒と引き換えます
		okmsg	ご利用ありがとうございました
		arg	nocount
			use		10	ギフト券
			get		1	魔法の箒
@@ITEM
	no	92
	type	道具
	code	sweep
	name	お掃除券
	info	店内のお掃除を依頼できます
	price	100000
	cost	10
	limit	5/0
	pop	0
	scale	枚
	flag	noshowcase
	@@USE
		time	0
		scale	回
		action	依頼する
		name	お掃除依頼
		info	ごみをすべて片付けてもらえます
		arg	nocount
			use		1	お掃除券
		func	_local_
			$DT->{trush}=0;
			my $ret="店内が綺麗になりました";
			WriteLog(3,0,$DT->{shopname}."がお掃除券を使いました");
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_
@@ITEM
	no	93
	type	道具
	code	magical-broom
	name	魔法の箒
	info	持っているだけで掃除をするのが速くなります
	price	500000
	cost	1000
	limit	1/0
	pop	0
	scale	本
	flag	noshowcase|icon
@@ITEM
	no	94
	type	道具
	code	star1
	name	一等星
	info	入賞の景品
	price	50000
	limit	1/0
	pop	lv7
	point	lv7
	scale	星
	cost	0
	flag	onlysend
@@ITEM
	no	95
	type	道具
	code	star2
	name	二等星
	info	入賞の景品
	price	40000
	limit	1/0
	pop	lv7
	point	lv7
	scale	星
	cost	0
	flag	onlysend
@@ITEM
	no	96
	type	道具
	code	star3
	name	三等星
	info	入賞の景品
	price	30000
	limit	1/0
	pop	lv7
	point	lv7
	scale	星
	cost	0
	flag	onlysend
@@ITEM
	no	97
	type	道具
	code	wrapping-tape
	name	ラッピングテープ
	info	あるものを包装するのに使います
	price	10000
	limit	1/0
	pop	lv3
	point	lv3
	scale	個
	cost	0
	flag	onlysend
	@@use
		time	2h
		scale	回
		action	ラッピング
		name	星をラッピングする
		info	星をラッピングします
		okmsg	流星群ができあがりました
		arg	nocount
			use		1	ラッピングテープ
			use		1	一等星
			use		1	二等星
			use		1	三等星
			get		1	流星群
@@ITEM
	no	98
	type	道具
	code	meteo-swarm
	name	流星群
	info	使うと不思議なことが起こります
	price	200000
	limit	1/0
	pop	0
	scale	群
	cost	0
	flag	noshowcase|onlysend
	@@USE
		time	0
		scale	回
		action	使ってみる
		name	使ってみる
		info	流星群を使ってみます
		arg	nocount
			use		1	流星群
		funcb	nightonly
		func	_local_
			WriteLog(3,0,$DT->{shopname}."が流星群を使いました");
			WriteLog(1,0,"流星群が観測されました");

			foreach my $DTS (@DT)
			{
				next if((rand(1000)>200) && ($DTS->{name} ne $DT->{name}));

				WriteLog(2,0,$DTS->{shopname}."に流星群が降り注ぎました");
				WriteLog(0,$DTS->{id},"星屑を手に入れました");
				$DTS->{item}[@@ITEMNO"星屑"-1]++;
				$DTS->{item}[@@ITEMNO"星屑"-1]=$ITEM[@@ITEMNO"星屑"]->{limit} if($DTS->{item}[@@ITEMNO"星屑"-1]>$ITEM[@@ITEMNO"星屑"]->{limit});
			}
			return '街に流星群が降り注ぎました<br>星屑が散乱したようです';
		_local_
@@ITEM
	no	99
	type	道具
	code	star-dust
	name	星屑
	info	流星群の星屑です
	price	100000
	limit	3/0
	pop	0
	scale	ｇ
	cost	0
	flag	noshowcase|onlysend
	@@use
		time	0
		scale	回
		action	使ってみる
		name	使ってみる
		info	星屑に秘められた不思議な力を使います
		param	6
		arg	nocount
			use		1	星屑
		funcb	nightonly
		func	_local_
		$cnt=$USE->{param1}*$count;
		$DT->{time}-=$cnt*3600;
		$ret="不思議な力で活動時間が$cnt時間増加しました";
		WriteLog(0,$DT->{id},$ret);
		WriteLog(3,0,"$DT->{shopname}が星屑を使いました");	
		return $ret;
		_local_
@@ITEM
	no	100
	type	道具
	code	loto7
	name	ロト７
	info	7つの数字を選ぶだけ
	price	10000
	limit	1/1
	pop	0
	plus	1h
	scale	枚
	cost	0
	flag	noshowcase|norequest
	@@USE
		time	0
		name	登録状況
		info	登録状況
		funcb	_local_
		my($USE)=@_;
		$loto=$DT->{user}->{loto};
		if(length($loto) eq 7)
		{
		$USE->{name}='[「'.substr($loto,0,1).substr($loto,1,1).substr($loto,2,1).substr($loto,3,1).substr($loto,4,1).substr($loto,5,1).substr($loto,6,1).'」で登録中]';
		return 2;
		}
		else
		{
		$USE->{name}='[未登録]';
		return 2;
		}
		_local_
	@@USE
		time	10m
		arg	nocount|message7
		argmessage	数字を半角で入力
		scale	回
		action	登録する
		name	登録する
		info	7桁の数字（0000000～9999999）を半角英数で入力してください<br>同じ数字を複数回選んでも構いません<br>順番は当選に影響します
		func _local_
		my $loto=$USE->{arg}->{message};
		main::OutError('数値指定が不正です') if ($loto=~ /[^0123456789]+/);
		main::OutError('数値指定が不正です') if (length($loto) ne 7);
		main::OutError('数値指定が不正です') if ($loto < 0);
		main::OutError('数値指定が不正です') if ($loto > 9999999);
		$DT->{user}->{loto}=$loto;
		return '「'.substr($loto,0,1).substr($loto,1,1).substr($loto,2,1).substr($loto,3,1).substr($loto,4,1).substr($loto,5,1).substr($loto,6,1).'」で登録しました';
		_local_
@@EVENT
	start		50%
	basetime	0h
	plustime	0h
	code		loto7
	info		ロト７抽選会
	startfunc	_local_
		$hitno[0]=int(rand(10));
		$hitno[1]=int(rand(10));
		$hitno[2]=int(rand(10));
		$hitno[3]=int(rand(10));
		$hitno[4]=int(rand(10));
		$hitno[5]=int(rand(10));
		$hitno[6]=int(rand(10));
		WriteLog(2,0,"ロト７の抽選会が開かれ、当選数字として「".$hitno[0].$hitno[1].$hitno[2].$hitno[3].$hitno[4].$hitno[5].$hitno[6]."」が選ばれました");
		foreach $DT(@DT)
		{
			if (($DT->{item}[@@ITEMNO"ロト７"-1]) && (length($DT->{user}->{loto}) eq 7))
			{
				$hit=0;
				$loto=$DT->{user}->{loto};
				foreach(0..6)
				{
					$cnt=substr($loto,$_,1);
					$hit+=1 if($cnt eq $hitno[$_]);
				}
				if($hit)
				{
					$gettime=$hit*$hit;
					WriteLog(2,0,"$DT->{shopname}が$hitつ当てて$gettime時間手に入れました");
					WriteLog(0,$DT->{id},"活動時間が$gettime時間増加しました");
					$DT->{time}-=$gettime*3600;
				}
				$DT->{item}[@@ITEMNO"ロト７"-1]=0;
			}
		}
		return 0;
	_local_
@@event
	start		10%
	basetime	5h
	plustime	5h
	code		happy
	startmsg	感謝祭がこの街で始まりました
	endmsg		感謝祭は幕を閉じました
	info		感謝祭で街はにぎわっています
	func		_local_
		my $time=$main::TIMESPAN;
		$time=10*3600 if $time>10*3600; # 最大10%制限
		$time=int($time/36);
		
		foreach(@DT)
		{
			$_->{rank}+=int(rand($time));
			$_->{rank}=10000 if $_->{rank}>10000;
		}
		return 0;
	_local_
@@EVENT
	start		10%
	basetime	24h
	plustime	24h
	code		priceup-fire
	group		element
	startmsg	火の属性の影響力が強まっています
	endmsg		火の属性の影響力は正常に戻りました
	info		火の属性の影響力が強まっています
		param	コロン・サラマンダー	price/3*4
		param	火のマナ		price/2*3
		param	サラマンダー		price/4*5
		param	火の指輪		price/3*4
		param	コロン・ウンディーネ	price/3*2
		param	水のマナ		price/2
		param	ウンディーネ		price/4*3
		param	水の指輪		price/3*2
@@EVENT
	start		10%
	basetime	24h
	plustime	24h
	code		priceup-aqua
	group		element
	startmsg	水の属性の影響力が強まっています
	endmsg		水の属性の影響力は正常に戻りました
	info		水の属性の影響力が強まっています
		param	コロン・ウンディーネ	price/3*4
		param	水のマナ		price/2*3
		param	ウンディーネ		price/4*5
		param	水の指輪		price/3*4
		param	コロン・サラマンダー	price/3*2
		param	火のマナ		price/2
		param	サラマンダー		price/4*3
		param	火の指輪		price/3*2
@@EVENT
	start		10%
	basetime	24h
	plustime	24h
	code		priceup-wind
	group		element
	startmsg	風の属性の影響力が強まっています
	endmsg		風の属性の影響力は正常に戻りました
	info		風の属性の影響力が強まっています
		param	コロン・シルフ	price/3*4
		param	風のマナ		price/2*3
		param	シルフ			price/4*5
		param	風の指輪		price/3*4
		param	コロン・ノーム	price/3*2
		param	土のマナ		price/2
		param	ノーム			price/4*3
		param	土の指輪		price/3*2
@@EVENT
	start		10%
	basetime	24h
	plustime	24h
	code		priceup-earth
	group		element
	startmsg	土の属性の影響力が強まっています
	endmsg		土の属性の影響力は正常に戻りました
	info		土の属性の影響力が強まっています
		param	コロン・ノーム	price/3*4
		param	土のマナ		price/2*3
		param	ノーム			price/4*5
		param	土の指輪		price/3*4
		param	コロン・シルフ	price/3*2
		param	風のマナ		price/2
		param	シルフ			price/4*3
		param	風の指輪		price/3*2
@@EVENT
	start		30%
	code		getmoney
	info		資金援助
	startfunc	_local_(100000)
		my($money)=@_;
		
		foreach(reverse(@DT))
		{
			next if rand(1000)>300;
			
			$_->{money}+=$money;
			$_->{money}=$main::MAX_MONEY if $_->{money}>$main::MAX_MONEY;
			return (0,$_->{shopname}.'へ'.GetMoneyString($money).'の補助金が支給されました');
		}
		return 0;
	_local_
@@EVENT
	start		30%
	basetime	0h
	plustime	0h
	code		getpop
	info		人気アップ
	startfunc	_local_(1000)
		my($pop)=@_;
		
		foreach(reverse(@DT))
		{
			next if rand(1000)>300;
			
			$_->{rank}+=$pop;
			$_->{rank}=10000 if $_->{rank}>10000;
			return (0,$_->{shopname}.'が雑誌で紹介され人気が上がったようです');
		}
		return 0;
	_local_
@@EVENT
	start		50%
	basetime	0h
	plustime	0h
	code		longfoot
	info		足長おじさん
	startfunc	_local_
		foreach(reverse(@DT))
		{
			if (rand(1000)<50)
			{
				return 0 if((!$_->{item}[@@ITEMNO"白猫さん"-1])&&(rand(1000)<150));
				return 0 if((!$_->{item}[@@ITEMNO"黒猫さん"-1])&&(rand(1000)<150));
				my $count=0;
				foreach my $idx (0..$_->{showcasecount}-1)
				{
					my $itemno=$_->{showcase}[$idx];
					next if !$itemno;	
					if($_->{price}[$idx] < ($ITEM[$itemno]->{price}*2))
					{
						my $cnt=int($_->{item}[$itemno-1]/2);
						$_->{item}[$itemno-1]-=$cnt;
						$count+=$cnt*$_->{price}[$idx];
					}
				}
				$_->{money}+=$count*3;
				$_->{saletoday}+=$count*3;
				return (0,"足長おじさんが$_->{shopname}の商品総額".GetMoneyString($count)."を高値で買い取っていきました") if $count;
				return (0,"$_->{shopname}に立ち寄った足長おじさんは何も買わずに去っていきました");
			}
		}
		return 0;
	_local_
@@EVENT
	start		25%
	basetime	0h
	plustime	0h
	code		peddle
	info		行商人
	startfunc	_local_
		foreach my $DT (@DT)
		{
			if (rand(1000)<100)
			{
				return (0,"$DT->{shopname}へ立ち寄った行商人は店番ロボットに追い返されました") if($DT->{item}[@@ITEMNO"店番ロボット"-1]);
				my $count=0;
				foreach my $idx (0..$DT->{showcasecount}-1)
				{
					my $itemno=$DT->{showcase}[$idx];
					next if !$itemno;	
					if($DT->{price}[$idx] < ($ITEM[$itemno]->{price}*2))
					{
						my $cnt=int($DT->{item}[$itemno-1]/2);
						$DT->{item}[$itemno-1]-=$cnt;
						$count+=$cnt*$DT->{price}[$idx];
					}
				}
				$DT->{money}+=int($count/2);
				$DT->{saletoday}+=int($count/2);
				return (0,"行商人が$DT->{shopname}の商品総額".GetMoneyString($count)."を安値で買い叩いていきました") if $count;
				return (0,"$DT->{shopname}に立ち寄った行商人は何も買わずに去っていきました");
			}
		}
		return 0;
	_local_
@@EVENT
	start		150%
	basetime	0h
	plustime	0h
	code		burn-out
	info		火災
	startfunc	_local_
		foreach my $DT (@DT)
		{
			if((rand(1000)<500)&&($DT->{trush}>4500000))				#汚屋敷店舗に高確率で発動
			{
				WriteLog(2,0,'汚屋敷と化した'.$DT->{shopname}.'で火災が発生しました');
				my $count=0;
				foreach my $idx (0..$DT->{showcasecount}-1)			#陳列中の商品をランダムに燃やす
				{
					my $itemno=$DT->{showcase}[$idx];
					next if !$itemno;
					my $cnt=int(rand($DT->{item}[$itemno-1]));
					$DT->{item}[$itemno-1]-=$cnt;
					$count+=$cnt*$DT->{price}[$idx];
				}
				$DT->{trush}=500000;							#ごみを500000に
				$DT->{rank}=int($DT->{rank}/2);					#人気を半減する
				WriteLog(0,$DT->{id},'陳列中の商品総額'.GetMoneyString($count).'が燃えてしまいました') if($count);
				$main::STATE->{develop}=int($main::STATE->{develop}*18/19);	#開拓度数を下げる
				return 0;
			}
		}
		return 0;
	_local_
@@EVENT
	start		10%
	basetime	0h
	plustime	0h
	code		god-eye
	info		目利きの真髄
	startfunc	_local_
		foreach(reverse(@DT))
		{
			next if(rand(1000)>($_->{user}->{ygg}*50+50));
			next if(!$_->{item}[@@ITEMNO"目利きの真髄"-1]);
			next if(!$_->{item}[@@ITEMNO"枯れた世界樹の葉"-1]);
			$_->{item}[@@ITEMNO"枯れた世界樹の葉"-1]--;
			$_->{item}[@@ITEMNO"輝く世界樹の葉"-1]++;
			$_->{item}[@@ITEMNO"輝く世界樹の葉"-1]=$ITEM[@@ITEMNO"輝く世界樹の葉"]->{limit} if($_->{item}[@@ITEMNO"輝く世界樹の葉"-1]>$ITEM[@@ITEMNO"輝く世界樹の葉"]->{limit});
			WriteLog(3,0,"$_->{shopname}が目利きの真髄を発揮しました");
			WriteLog(0,$_->{id},"枯れ葉の中に輝く世界樹の葉を見つけました");
			return 0;
		}
		return 0;
	_local_
@@EVENT
	start		25%
	basetime	0h
	plustime	0h
	code		ygg-shine
	info		不思議な光
	startfunc	_local_
		$ygg_pt=main::GetTownData("yggpt");
		return 0 if(rand($ygg_pt)<800);
		WriteLog(2,0,"世界樹が不思議な光を発しました");
		foreach my $DT (@DT)
		{
			my $cnt=int($DT->{user}->{ygg}*2);
			if($cnt)
			{
				$DT->{time}-=$cnt*3600;
				WriteLog(0,$DT->{id},"不思議な力で活動時間が$cnt時間増加しました");
			}
		}
		return 0;
	_local_
@@EVENT
	start		100%
	basetime	0h
	plustime	0h
	code		get-ygg-leaf
	info		世界樹の葉
	startfunc	_local_
		$ygg_pt=main::GetTownData("yggpt");
		return 0 if(rand($ygg_pt)<500);
		WriteLog(2,0,"世界樹の葉が落ちてきました");
		my $leaf=@@ITEMNO"世界樹の葉";
		my $leaf_sp=@@ITEMNO"輝く世界樹の葉";
		foreach my $DT (@DT)
		{
			my $get_le=int(rand($DT->{user}->{ygg}*2+2)+$DT->{user}->{ygg}+($ygg_pt/100));
			$get_le=($ITEM[$leaf]->{limit}-$DT->{item}[$leaf-1]) if($get_le>($ITEM[$leaf]->{limit}-$DT->{item}[$leaf-1]));
			if($get_le>=1)
			{
				$DT->{item}[$leaf-1]+=$get_le;
				WriteLog(0,$DT->{id},$ITEM[$leaf]->{name}."を$get_le枚手に入れました");
			}
			if(rand(1000)<$DT->{user}->{ygg})
			{
				WriteLog(0,$DT->{id},"なんと".$ITEM[$leaf_sp]->{name}."を1枚手に入れました") if($DT->{item}[$leaf_sp-1]<$ITEM[$leaf_sp]->{limit});
				$DT->{item}[$leaf_sp-1]++;
				$DT->{item}[$leaf_sp-1]=$ITEM[$leaf_sp]->{limit} if($DT->{item}[$leaf_sp-1]>$ITEM[$leaf_sp]->{limit});
			}
		}
		return 0;
	_local_
@@EVENT
	start		50%
	basetime	0h
	plustime	0h
	code		get-ygg-fruit
	info		世界樹の実
	startfunc	_local_
		$ygg_pt=main::GetTownData("yggpt");
		return 0 if(rand($ygg_pt)<700);
		WriteLog(2,0,"世界樹の実が落ちてきました");
		my $leaf=@@ITEMNO"世界樹の実";
		foreach my $DT (@DT)
		{
			my $get_le=int(rand($DT->{user}->{ygg}*2+2)+$DT->{user}->{ygg}+($ygg_pt/100));
			$get_le=($ITEM[$leaf]->{limit}-$DT->{item}[$leaf-1]) if($get_le>($ITEM[$leaf]->{limit}-$DT->{item}[$leaf-1]));
			if($get_le>=1)
			{
				$DT->{item}[$leaf-1]+=$get_le;
				WriteLog(0,$DT->{id},$ITEM[$leaf]->{name}."を$get_le個手に入れました");
			}
		}
		return 0;
	_local_
@@EVENT
	start		50%
	basetime	0h
	plustime	0h
	code		get-ygg-flower
	info		世界樹の花
	startfunc	_local_
		$ygg_pt=main::GetTownData("yggpt");
		return 0 if(rand($ygg_pt)<600);
		WriteLog(2,0,"世界樹の花が落ちてきました");
		my $leaf=@@ITEMNO"世界樹の花";
		foreach my $DT (@DT)
		{
			my $get_le=int(rand($DT->{user}->{ygg}*2+2)+$DT->{user}->{ygg}+($ygg_pt/100));
			$get_le=($ITEM[$leaf]->{limit}-$DT->{item}[$leaf-1]) if($get_le>($ITEM[$leaf]->{limit}-$DT->{item}[$leaf-1]));
			if($get_le>=1)
			{
				$DT->{item}[$leaf-1]+=$get_le;
				WriteLog(0,$DT->{id},$ITEM[$leaf]->{name}."を$get_le個手に入れました");
			}
		}
		return 0;
	_local_
@@EVENT
	start		100%
	basetime	0h
	plustime	0h
	code		get-ygg-withered
	info		枯れた世界樹の葉
	startfunc	_local_
		$ygg_pt=main::GetTownData("yggpt");
		return 0 if($ygg_pt>=300);
		WriteLog(2,0,"枯れた世界樹の葉が落ちてきました");
		my $leaf=@@ITEMNO"枯れた世界樹の葉";
		foreach my $DT (@DT)
		{
			my $get_le=int(rand($DT->{user}->{ygg}*2+2)+$DT->{user}->{ygg}+($ygg_pt/100));
			$get_le=($ITEM[$leaf]->{limit}-$DT->{item}[$leaf-1]) if($get_le>($ITEM[$leaf]->{limit}-$DT->{item}[$leaf-1]));
			if($get_le>=1)
			{
				$DT->{item}[$leaf-1]+=$get_le;
				WriteLog(0,$DT->{id},$ITEM[$leaf]->{name}."を$get_le枚手に入れました");
			}
		}
		return 0;
	_local_
@@EVENT
	start		50%
	basetime	4h
	plustime	4h
	code		ygg-flowering
	startmsg	世界樹が一斉に開花を始めました
	endmsg		世界樹の開花現象は終息しました
	info		世界樹が一斉に開花しています
	startfunc	_local_
		$ygg_pt=main::GetTownData("yggpt");
		return 0 if(rand($ygg_pt)<700);
		return 1;
	_local_

@@FUNCINIT
#目利きの真髄を持っている場合、買い物に必要な時間を3/4にする。
$TIME_SEND_ITEM=int($TIME_SEND_ITEM/4*3) if $DT->{item}[@@ITEMNO"目利きの真髄"-1];

#職業が「行商人」の場合、買い物に必要な時間を1/2にする。
#$TIME_SEND_ITEM=int($TIME_SEND_ITEM/2) if $DT->{job} eq 'peddle';

#店番ロボットを持っている場合、陳列に必要な時間を1台につき1分短縮する。
$TIME_EDIT_SHOWCASE-=$DT->{item}[@@ITEMNO"店番ロボット"-1]*60 if $DT->{item}[@@ITEMNO"店番ロボット"-1];

#魔法の箒を持っている場合、掃除に必要な時間を3/4にする。
$TIME_SEND_MONEY=int($TIME_SEND_MONEY/4*3) if $DT->{item}[@@ITEMNO"魔法の箒"-1];

@@FUNCITEM
sub lostbook
{
	my $itemno=$USE->{itemno};
	if(rand(1000)<$USE->{param1})
	{
		UseItem($itemno,1,$ITEM[$itemno]->{name}.'が読めない程ボロボロになりましたので破棄しました');
	}
	return "";
}

sub needexp	#使用するのに他のアイテムの熟練度が必要
{		#funcb needexp
my($USE)=@_;	#param	itemno,needexp（100%=1000として）
my $needitem=$USE->{param1};
my $needexp=$USE->{param2};
return 1 if($DT->{exp}{$needitem} < $needexp);
return 1 if(($DT->{job} eq $USE->{param3}) && $USE->{param3});	#転職のススメ用　職業がparam3のとき使用不可
}

sub jobport
{
$DT->{job}=$USE->{param3};
$jobname=$main::JOBTYPE{$USE->{param3}};
$jobname="すっぴん" if(!$USE->{param3});
WriteLog(2,0,"$DT->{shopname}の職業が「$jobname」になりました");
my $ret;
$ret.="本を片手に転職の神殿へと向かった。<br><br>";
$ret.="<TABLE><tr><td>";
$ret.="神官アムザ：<br>";
$ret.="…ふむ。$jobnameになりたいというのですね。<br>";
$ret.="さすれば，全知\全\能\の神よ！<br>いまここに<b>$DT->{shopname}</b>が<br>";
$ret.="$jobnameの道を歩むことを許したまえ！";
$ret.="</td></tr></table><br>";
$ret.="ジョブが$jobnameになりました。";
return $ret;
}

sub nightonly#夜限定
{
my($USE)=@_;
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst)=localtime(time());
if(($hour >= 6) && ($hour < 18))
{
$USE->{name}='日中は使用できません';
return 2;
}
}

sub dayonly#昼限定
{
my($USE)=@_;
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst)=localtime(time());
return 0 if(($hour >= 6) && ($hour < 18));
$USE->{name}='夜間は使用できません';
return 2;
}

@@FUNCUPDATE
sub UpdateResetBefore #決算直前の処理(関数名固定)
{
	UpdateTodayPrize();
	
	sub UpdateTodayPrize
	{
		#賞品授与
		my @TOP123=(
			[
				['ギフト券',		[[@@ITEMNO "ギフト券", 3],			],],
				['ギフト券',		[[@@ITEMNO "ギフト券", 2],			],],
				['ギフト券',		[[@@ITEMNO "ギフト券", 2],			],],
				['ギフト券',		[[@@ITEMNO "ギフト券", 2],			],],
				['ギフト券',		[[@@ITEMNO "ギフト券", 1],			],],
				['店番ロボット',	[[@@ITEMNO "店番ロボット", 1],		],],
				['一等星',		[[@@ITEMNO "一等星", 1],			],],
			],
			[
				['ギフト券',		[[@@ITEMNO "ギフト券", 2],			],],
				['ギフト券',		[[@@ITEMNO "ギフト券", 2],			],],
				['ギフト券',		[[@@ITEMNO "ギフト券", 2],			],],
				['ギフト券',		[[@@ITEMNO "ギフト券", 1],			],],
				['ギフト券',		[[@@ITEMNO "ギフト券", 1],			],],
				['輝く世界樹の葉',	[[@@ITEMNO "輝く世界樹の葉", 1],		],],
				['二等星',		[[@@ITEMNO "二等星", 1],			],],
			],
			[
				['ギフト券',		[[@@ITEMNO "ギフト券", 2],			],],
				['ギフト券',		[[@@ITEMNO "ギフト券", 2],			],],
				['ギフト券',		[[@@ITEMNO "ギフト券", 1],			],],
				['ギフト券',		[[@@ITEMNO "ギフト券", 1],			],],
				['ギフト券',		[[@@ITEMNO "ギフト券", 1],			],],
				['広告パック',	[[@@ITEMNO "広告パック", 1],		],],
				['三等星',		[[@@ITEMNO "三等星", 1],			],],
			],
			[
				['ギフト券',		[[@@ITEMNO "ギフト券", 1],			],],
				['ギフト券',		[[@@ITEMNO "ギフト券", 1],			],],
				['ギフト券',		[[@@ITEMNO "ギフト券", 1],			],],
				['お掃除券',		[[@@ITEMNO "お掃除券", 1],			],],
				['広告パック',	[[@@ITEMNO "広告パック", 1],		],],
				['広告パック',	[[@@ITEMNO "広告パック", 1],		],],
				['ラッピングテープ',	[[@@ITEMNO "ラッピングテープ", 1],		],],
			],
		);
		
		TopGetItem($DT[0],$TOP123[0],"今回優勝の") if defined($DT[0]);
		TopGetItem($DT[1],$TOP123[1],"惜しくも2位の") if defined($DT[1]);
		TopGetItem($DT[2],$TOP123[2],"ぎりぎり入賞の") if defined($DT[2]);
	
		for(my $i=9; $i<$#DT; $i+=10)
		{
			TopGetItem($DT[$i],$TOP123[3],"特別賞として".($i+1)."位の") if defined($DT[$i]);
		}

		sub TopGetItem
		{
			my($DT,$itemlist,$head)=@_;
			
			my @list=@{$itemlist};
			my @getitem=@{$list[int(rand($#list+1))]};
			
			my $msg=$head.$DT->{shopname}."さんには".$getitem[0]."が贈られました";
			WriteLog(2,0,0,$msg,1);
			foreach (@{$getitem[1]})
			{
				my @itemnocount=@{$_};
				
				my $cnt=AddItem($DT,$itemnocount[0],$itemnocount[1]);
				my $ITEM=$ITEM[$itemnocount[0]];
				WriteLog(0,$DT->{id},0,$head."賞品として".$ITEM->{name}."を".$itemnocount[1].$ITEM->{scale}."獲得しました",1);
				$cnt=$itemnocount[1]-$cnt;
				WriteLog(0,$DT->{id},0,"しかし最大所持数以上だったので".$cnt.$ITEM->{scale}."破棄しました",1) if $cnt;
			}
		}
	}
}

sub UpdateResetAfter #決算直後の処理(関数名固定)
{

	UpdateTodayEraseTech();
	
	sub UpdateTodayEraseTech
	{
		#3期に1度高額納税者を表彰
		#他のバージョンに組み込む際はタウンデータのturncntが存在しない点に注意
		$turncnt=main::GetTownData("turncnt");
		if($turncnt%3==0)
		{
			@DTsale=(sort{$b->{taxyesterday}<=>$a->{taxyesterday}}@DT)[0..1];
			if($DTsale[0])
			{
				WriteLog(1,0,0,"「今期の高額納税店は$DTsale[0]->{shopname}さんでした」",1);
				$msg="「納税額は".GetMoneyString($DTsale[0]->{taxyesterday});
				$msg.="で、2位との差は".GetMoneyString($DTsale[0]->{taxyesterday}-$DTsale[1]->{taxyesterday}) if($DTsale[1]);
				$msg.="でした」";
				WriteLog(1,0,0,$msg,1);
				WriteLog(2,0,0,"今期功労者の$DTsale[0]->{shopname}さんには爵位が贈られました",1);
				$DTsale[0]->{dignity}+=2;
				WriteLog(0,$DTsale[0]->{id},0,"爵位を2ポイント獲得しました",1);
			}
			if($DTsale[1])
			{
				WriteLog(2,0,0,"準功労者の$DTsale[1]->{shopname}さんには爵位が贈られました",1);
				$DTsale[1]->{dignity}+=1;
				WriteLog(0,$DTsale[1]->{id},0,"爵位を1ポイント獲得しました",1);
			}
		}

		#葉＆花が枯れる処理
		my $wither=@@ITEMNO"世界樹の葉";
		my $withered=@@ITEMNO"枯れた世界樹の葉";
		my $flower=@@ITEMNO"世界樹の花";

		foreach my $DT (@DT)
		{
			if($DT->{item}[$wither-1])
			{
				$DT->{item}[$withered-1]+=$DT->{item}[$wither-1];
				$DT->{item}[$withered-1]=$ITEM[$withered]->{limit} if($DT->{item}[$withered-1]>$ITEM[$withered]->{limit});
				$DT->{item}[$wither-1]=0;
				WriteLog(0,$DT->{id},0,$ITEM[$wither]->{name}."はすべて枯れてしまいました",1);
			}
			if(($DT->{item}[$flower-1]) && ($turncnt%2==1))	#2期に1度
			{
				$DT->{item}[$flower-1]=0;
				WriteLog(0,$DT->{id},0,$ITEM[$flower]->{name}."はすべて枯れてしまいました",1);
			}
		}

		#世界樹処理
		RequireFile('inc-ygg.cgi');
		$ygg_pt=main::GetTownData("yggpt");
		$ygg_fr=main::GetTownData("yggfr");

		WriteLog(2,0,0,$YGG_NAME."の葉が落ちてきました",1);
		my $leaf=@@ITEMNO"世界樹の葉";
		my $leaf_sp=@@ITEMNO"輝く世界樹の葉";
		foreach my $DT (@DT)
		{
			my $get_le=int($ygg_pt*$GET_LE_RATE);
			$get_le=($ITEM[$leaf]->{limit}-$DT->{item}[$leaf-1]) if($get_le>($ITEM[$leaf]->{limit}-$DT->{item}[$leaf-1]));
			if($get_le>=1)
			{
				$DT->{item}[$leaf-1]+=$get_le;
				WriteLog(0,$DT->{id},0,$ITEM[$leaf]->{name}."を$get_le枚手に入れました",1);
			}
			if(rand(100)<$DT->{user}->{ygg})
			{
				WriteLog(0,$DT->{id},0,"なんと".$ITEM[$leaf_sp]->{name}."を1枚手に入れました",1) if($DT->{item}[$leaf_sp-1]<$ITEM[$leaf_sp]->{limit});
				$DT->{item}[$leaf_sp-1]++;
				$DT->{item}[$leaf_sp-1]=$ITEM[$leaf_sp]->{limit} if($DT->{item}[$leaf_sp-1]>$ITEM[$leaf_sp]->{limit});
			}
			$DT->{user}->{ygg}=0;
		}

		if($ygg_pt>=$YGG_PT_NEED)	#開花条件を満たした場合
		{
			WriteLog(2,0,0,$YGG_NAME."が開花しました",1);
			my $flower=@@ITEMNO"世界樹の花";
			foreach my $DT (@DT)
			{
				my $get_fl=int($ygg_pt*$GET_FL_RATE);
				$get_fl=($ITEM[$flower]->{limit}-$DT->{item}[$flower-1]) if($get_fl>($ITEM[$flower]->{limit}-$DT->{item}[$flower-1]));
				if($get_fl>=1)
				{
					$DT->{item}[$flower-1]+=$get_fl;
					WriteLog(0,$DT->{id},0,$ITEM[$flower]->{name}."を$get_fl個手に入れました",1);
				}
			}
			$ygg_fr=int($DTusercount*$ygg_pt*$GET_FR_RATE);
			$ygg_pt-=int($YGG_PT_USE);
			$ygg_pt=int($YGG_PT_MIN) if($ygg_pt<$YGG_PT_MIN);
		}
		else
		{
			$ygg_fr=0;
		}
		$ygg_pt-=int($DTusercount*$YGG_DT_RATE);
		$ygg_pt=int($YGG_PT_MIN) if($ygg_pt<$YGG_PT_MIN);

		main::SetTownData("yggpt",$ygg_pt);
		main::SetTownData("yggfr",$ygg_fr);

		foreach my $DT (@DT)
		{
			$DT->{profitstock}=5000000 if ($DT->{profitstock} > 5000000);
			$DT->{profitstock}=-1000000 if ($DT->{profitstock} < -1000000);
			#1億円以上で祝賀会
			if ($DT->{money} > 100000000)
			{
				$DT->{money} -= int( ($DT->{money} - 60000000)/2 );
				$DT->{rank} += int( (10000 - $DT->{rank})/2 );
				$DT->{rank}=10000 if $DT->{rank}>10000;
				PushLog(2,0,$DT->{shopname}.'にて祝賀会が行われました');
			}

			#2期に1度資格期限切れ
			if($turncnt%2==0)
			{
				foreach my $itemno (@@ITEMNO"薬剤師免許",@@ITEMNO"酒醸造免許")
				{
					if($DT->{item}[$itemno-1])
					{
						my $msg=$DT->{shopname}."の".$ITEM[$itemno]->{name}."が期限切れになりました";
						WriteLog(2,0,0,$msg,1);
						WriteLog(0,$DT->{id},0,$ITEM[$itemno]->{name}."を失いました",1);
						$DT->{item}[$itemno-1]--;
					}
				}
			}

			#新規開店店舗の免税の解除
			if((($NOW_TIME-$DT->{foundation})>86400*3)&&($DT->{taxmode}==1)&&($DT->{user}->{new}))
			{
				$DT->{taxmode}="";
				$DT->{user}->{new}="";
				WriteLog(2,0,0,"開店から3日以上経過したため、$DT->{shopname}の免税が解除されました",1);
				WriteLog(0,$DT->{id},0,"税率が通常に戻りました",1);
			}
		}
	}
}

@@FUNCBUY

if($BUY->{whole})
{
	if (rand(1000) > 990 && $BUY->{num} > 10)
	{
	$count=AddItemSub(@@ITEMNO"ギフト券",1,$BUY->{dt});
	WriteLog(0,$BUY->{dt}{id},'市場の抽選でギフト券が'.$count.'枚あたりました');
	$main::ret.='<br>抽選でギフト券が'.$count.'枚あたりました！';
	}
}

@@FUNCNEW

{
# @@DEFINE Set NewShopMoney NewShopTime NewShopItem の処理
$DT->{money}=@@VALUE"NewShopMoney" if @@VALUE"NewShopMoney";
$DT->{time}=$NOW_TIME-eval(@@VALUE"NewShopTime") if @@VALUE"NewShopTime";
if(@@VALUE"NewShopItem")
{
	my %item=split /:/,@@VALUE"NewShopItem";
	while(my($key,$val)=each %item)
	{
		foreach my $item (@ITEM)
		{
			 $DT->{item}[$item->{no}-1]+=$val,last if $key eq $item->{code} or $key eq $item->{name};
		}
	}
}

#新規開店した店舗を免税にする
$DT->{taxmode}=1;
$DT->{user}->{new}=1;
$DEFINE_FUNCNEW_NOLOG=1;#開店時のログの順序を変えたいので
PushLog(1,0,"$DT->{shopname}が新装開店しました");
PushLog(2,0,"$DT->{shopname}の開店を祝して、商店会は$DT->{shopname}を免税にしました");
PushLog(0,$DT->{id},"免税になりました");

#世界樹関連　初期化
RequireFile('inc-ygg.cgi');

$ygg_pt=GetTownData("yggpt");
$ygg_fr=GetTownData("yggfr");
$ygg_pt=int($YGG_PT_BASE) if !$ygg_pt;
$ygg_fr=0 if !$ygg_fr;
SetTownData("yggpt",$ygg_pt);
SetTownData("yggfr",$ygg_fr);

$DT->{user}->{ygg}=0;
}

@@END #定義終了宣言(以降コメント扱い)