# スタンダード版アイテムデータ 2005/01/06 由來

# このファイルはアイテムデータの定義ファイルです。
# 好きなようにカスタマイズできます。詳細はマニュアルをご覧ください。

@@DEFINE
	version	05-01-06(SD)		#★商品データバージョン表記
					# 最後の「SD」はスタンダード版であることを示します。
					# もしあなたが独自アイテムを目玉にした商人物語を作るなら，
					# この記号を変えるのがよいでしょう。

	scale	個			#★デフォルトの数え単位
	type0	全			#全アイテムの集合
	type1	原料
	type2	本
	type3	薬
	type4	剣
	type5	鎧
	type6	盾
	type7	杖
	type8	アクセサリ
	type9	地図
	type10	道具
	
	job	drug		薬屋		#★職業コードは英小文字10文字以内
	job	tool		道具屋
	job	weapon		武器屋
	job	armor		防具屋
	job	material	山師
	job	book		本屋
	job	cow		酪農家
	job	peddle		行商人
	
	# 職業別時間短縮用変数設定
	set job_drug_time_rate		1.5	#★職業についていると1.5倍早くなる
	set job_tool_time_rate		1.5
	set job_weapon_time_rate	1.5
	set job_armor_time_rate		1.5
	set job_material_time_rate	1.5
	set job_book_time_rate		1.5
	set job_cow_time_rate		1.5
	set job_peddle_time_rate	1.5

	MaxMoney	999999999	#★最大資金
	
	set NewShopMoney	100000					#初期資金 (@@FUNCNEWにて使用)
	set NewShopTime		12*60*60				#初期持時間(秒) (@@FUNCNEWにて使用)
	set NewShopItem		陳列棚増築取壊キット:1:ギフト券:5	#初期所持商品 (@@FUNCNEWにて使用) 書式 商品名:個数:商品名:個数:...
	
	TimeEditShowcase	10m		#★陳列棚操作時間
	TimeShopping		20m		#★仕入時間(旧SOLD OUTとの互換性確保。今は使用せず)
	TimeSendItem		20m		#★アイテム仕入/移動時間(基本)
	TimeSendItemPlus	20s		#★アイテム仕入/移動時間(1個辺りの追加時間)
	TimeSendMoney		20m		#★資金移動時間(基本)
	TimeSendMoneyPlus	100000		#★ごみ処理時間計算用金額(この金額につきTimeSendMoney時間を消費)
	
	CostShowcase1		0		#★陳列棚1個時維持費
	CostShowcase2		2000	#陳列棚2個時維持費
	CostShowcase3		4000	#陳列棚3個時維持費
	CostShowcase4		8000	#陳列棚4個時維持費
	CostShowcase5		16000	#陳列棚5個時維持費
	CostShowcase6		32000	#陳列棚6個時維持費
	CostShowcase7		64000	#陳列棚7個時維持費
	CostShowcase8		128000	#陳列棚8個時維持費
	
	ItemUseTimeRate		0.5		#★アイテム使用時時間計算補正倍率(@USE内time,exptimeに有効)
	

#------ ここからアイテム定義 ---------------------------------


@@ITEM					#★アイテムデータ定義宣言
	no		10		#★アイテム番号(重複しないように)
	type	道具			#★アイテム分類(@@DEFINEのtype?の定義を使用)
	code	book-make		#★コード(重複しないように)
	name	本執筆キット			#★名称(重複しないように)
	info	本を執筆する為の基本キット	#★説明
	price	5000				#★標準価格
	cost	100
	limit	20/10
	pop	20d			#★売れ行き率基準(20日に1個売れる確率)
	scale	セット			#★数え単位
	plus	20m			#★市場入荷率(20分に1個入荷する確率)
	@@USE				#★アイテム使用データ定義宣言
		time	3h
		exp	2%
		exptime	1h
		job		本屋	times/job_book_time_rate
		scale	回
		action	書く
		name	『薬調合入門』を執筆する
		info	薬の作り方を勉強し、本にしようと思います
		okmsg	『薬調合入門』を執筆しました
		ngmsg	執筆に失敗しました…
			use		1	本執筆キット
			use		30	薬草
			use		10	ポーション
			use		10	エーテル
			get		5	薬調合入門	40%
	@@USE
		time	3h
		exp	2%
		exptime	1h
		name	『革細工入門』を執筆する
		info	革細工の作り方を勉強し、本にしようと思います
		okmsg	『革細工入門』を執筆しました
		ngmsg	執筆に失敗しました…
			use		1	本執筆キット
			use		50	獣の革
			get		5	革細工入門	40%
	@@USE
		time	3h
		exp	2%
		exptime	1h
		name	『木工入門』を執筆する
		info	木工の作り方を勉強し、本にしようと思います
		okmsg	『木工入門』を執筆しました
		ngmsg	執筆に失敗しました…
			use		1	本執筆キット
			use		50	木の枝
			use		10	丸太
			get		5	木工細工入門	40%
	@@USE
		time	6h
		exp	2%
		exptime	2h
		name	『装飾細工入門』を執筆する
		info	装飾細工の技術を勉強し、本にしようと思います
		okmsg	『装飾細工入門』を執筆しました
		ngmsg	執筆に失敗しました…
			use		1	本執筆キット
			need		1	革細工入門
			need		1	木工細工入門
			use		20	鉄塊
			use		5	ミスリル塊
			use		5	オリハルコン塊
			get		5	装飾細工入門	40%
	@@USE
		time	6h
		exp	2%
		exptime	2h
		name	『剣の鍛え方』を執筆する
		info	剣の鍛え方を勉強し、本にしようと思います
		okmsg	『剣の鍛え方』を執筆しました
		ngmsg	執筆に失敗しました…
			needexp	20%
			need		1	鍛冶屋の技術
			use		1	本執筆キット
			use		20	鉄塊
			use		1	木刀
			get		5	剣の鍛え方	40%
	@@USE
		time	6h
		exp	2%
		exptime	2h
		name	『盾の作り方』を執筆する
		info	盾の構造を勉強し、本にしようと思います
		okmsg	『盾の作り方』を執筆しました
		ngmsg	執筆に失敗しました…
			needexp	20%
			use		1	本執筆キット
			need		1	鍛冶屋の技術
			use		20	鉄塊
			use		1	革の盾
			get		5	盾の作り方	40%
	@@USE
		time	6h
		exp	2%
		exptime	2h
		name	『鎧の作り方』を執筆する
		info	鎧の構造を勉強し、本にしようと思います
		okmsg	『鎧の作り方』を執筆しました
		ngmsg	執筆に失敗しました…
			needexp	20%
			need		1	鍛冶屋の技術
			use		1	本執筆キット
			use		20	鉄塊
			use		1	革の胸当て
			get		5	鎧の作り方	40%
	@@USE
		time	6h
		exp	2%
		exptime	2h
		name	『杖の作り方』を執筆する
		info	杖の構造を勉強し、本にしようと思います
		okmsg	『杖の作り方』を執筆しました
		ngmsg	執筆に失敗しました…
			needexp	20%
			need		1	魔法の知識
			use		1	本執筆キット
			use		20	鉄塊
			use		1	木の杖
			get		5	杖の作り方	40%

@@ITEM
	no		37
	type	道具
	code	book-syugyou
	name	修行キット
	info	いろんな修行をするためのキット
	price	5000
	cost	500
	limit	1/1
	pop	0
	scale	セット
	plus	1d
	flag	noshowcase|norequest
	@@USE
		time	12h
		exp		5%
		scale	修行
		action	修行する
		name	鍛冶屋に弟子入り
		info	鍛冶屋の技術を勉強し、身につけようと思います
		okmsg	鍛冶屋の技術を身につけました
			use		1	修行キット
			use		20	鉄塊
			use		5	ミスリル塊
			use		3	オリハルコン塊
			get		1	鍛冶屋の技術
	@@USE
		time	12h
		exp		5%
		scale	勉強
		action	修行する
		name	魔法の基礎講座
		info	魔法の基礎について勉強し、身につけようと思います
		okmsg	魔法の基礎をたたきこまれました
			use		1	修行キット
			use		30	魔石
			get		1	魔法の知識
	@@USE
		time	12h
		exp		5%
		scale	開眼
		action	開眼する
		name	違いが分かる男(女)になる
		info	商品の違いを見極め、物を見る目を養おうと思います
		okmsg	違いが分かる男(女)になった気がする
			needexp	20%
			use		1	修行キット
			use		3	薬草
			use		3	獣の革
			use		3	木の枝
			use		3	丸太
			use		3	鉄塊
			use		3	ミスリル塊
			use		3	オリハルコン塊
			use		3	魔石
			get		1	目利きの真髄
	@@USE
		time	12h
		exp		5%
		scale	修行
		action	修行する
		name	バラシの極意を学んでみる
		info	分解することに命を懸けてみませんか？
		okmsg	なんでもバラせる気がするぞ
			use		1	修行キット
			use		20	革の胸当て
			use		20	革の盾
			use		20	木の杖
			use		20	木刀
			get		1	解体屋の魂

@@ITEM
	no		39
	type	道具
	code	book-kaitai
	name	解体/梱包キット
	info	解体や梱包作業に必要なキット
	price	500
	limit	10/3
	pop		2d
	scale	セット
	plus	5h
	@@USE
		name	木刀/木の杖を解体する
		time	4h
		exptime	2h
		exp		1%
		job		武器屋	times/job_weapon_time_rate
		use		1	解体/梱包キット
		need	1	解体屋の魂
		use		10	木刀
		use		10	木の杖
		get		50	木の枝	80%
	@@USE
		name	革の盾/胸当てを解体する
		time	4h
		exptime	2h
		exp		1%
		job		防具屋	times/job_armor_time_rate
		use		1	解体/梱包キット
		need	1	解体屋の魂
		use		10	革の盾
		use		10	革の胸当て
		get		50	獣の革	80%
	@@USE
		name	木の盾/胸当てを解体する
		time	4h
		exptime	2h
		exp		1%
		job		防具屋	times/job_armor_time_rate
		use		1	解体/梱包キット
		need	1	解体屋の魂
		use		10	木の盾
		use		10	木の胸当て
		get		50	木の枝	80%
	@@USE
		name	鉄の剣/杖を解体する
		time	4h
		exptime	3h
		exp		1%
		job		武器屋	times/job_weapon_time_rate
		use		1	解体/梱包キット
		need	1	解体屋の魂
		use		10	鉄の剣
		use		10	鉄の杖
		get		50	鉄塊	80%
		get		10	魔石	50%
	@@USE
		name	鉄の盾/鎧を解体する
		time	4h
		exptime	3h
		exp		1%
		job		防具屋	times/job_armor_time_rate
		use		1	解体/梱包キット
		need	1	解体屋の魂
		use		10	鉄の盾
		use		10	鉄の鎧
		get		50	鉄塊	80%
	@@USE
		name	鋼鉄の剣/杖を解体する
		time	5h
		exptime	3.5h
		exp		1%
		job		武器屋	times/job_weapon_time_rate
		use		1	解体/梱包キット
		need	1	解体屋の魂
		use		10	鋼鉄の剣
		use		10	鋼鉄の杖
		get		100	鉄塊	80%
		get		10	魔石	50%
	@@USE
		name	鋼鉄の盾/鎧を解体する
		time	5h
		exptime	3.5h
		exp		1%
		job		防具屋	times/job_armor_time_rate
		use		1	解体/梱包キット
		need	1	解体屋の魂
		use		10	鋼鉄の盾
		use		10	鋼鉄の鎧
		get		100	鉄塊	80%
	@@USE
		name	ミスリルの剣/杖を解体する
		time	6h
		exptime	4h
		exp		1%
		job		武器屋	times/job_weapon_time_rate
		use		1	解体/梱包キット
		need	1	解体屋の魂
		use		10	ミスリルの剣
		use		10	ミスリルの杖
		get		50	ミスリル塊	70%
		get		20	魔石	50%
	@@USE
		name	ミスリルの盾/鎧を解体する
		time	6h
		exptime	4h
		exp		1%
		job		防具屋	times/job_armor_time_rate
		use		1	解体/梱包キット
		need	1	解体屋の魂
		use		10	ミスリルの盾
		use		10	ミスリルの鎧
		get		50	ミスリル塊	70%
	@@USE
		name	オリハルコンの剣/杖を解体する
		time	7h
		exptime	5h
		exp		1%
		job		武器屋	times/job_weapon_time_rate
		use		1	解体/梱包キット
		need	1	解体屋の魂
		use		10	オリハルコンの剣
		use		10	オリハルコンの杖
		get		50	オリハルコン塊	60%
		get		30	魔石	50%
	@@USE
		name	オリハルコンの盾/鎧を解体する
		time	7h
		exptime	5h
		exp		1%
		job		防具屋	times/job_armor_time_rate
		use		1	解体/梱包キット
		need	1	解体屋の魂
		use		10	オリハルコンの盾
		use		10	オリハルコンの鎧
		get		50	オリハルコン塊	60%
	@@USE
		name	ロボットを解体する
		time	12h
		use		1	解体/梱包キット
		need	1	解体屋の魂
		use		1	店番ロボット
		get		300	鉄塊
		get		50	ミスリル塊
		get		10	オリハルコン塊
		get		30	魔石
		get		1	禁断の書
		get		1	丸太
	@@USE
		name	革製装備一式を梱包する
		time	4h
		exptime	2h
		exp		1%
		job		道具屋	times/job_tool_time_rate
		use		1	解体/梱包キット
		use		10	革の盾
		use		10	革の胸当て
		get		10	革製装備一式
	@@USE
		name	木製装備一式を梱包する
		time	5h
		exptime	3h
		exp		1%
		job		道具屋	times/job_tool_time_rate
		use		1	解体/梱包キット
		use		10	木刀
		use		10	木の盾
		use		10	木の胸当て
		use		10	木の杖
		get		10	木製装備一式
	@@USE
		name	鉄製装備一式を梱包する
		time	6h
		exptime	4h
		exp		1%
		job		道具屋	times/job_tool_time_rate
		use		1	解体/梱包キット
		use		10	鉄の剣
		use		10	鉄の盾
		use		10	鉄の鎧
		use		10	鉄の杖
		get		10	鉄製装備一式
	@@USE
		name	鋼鉄製装備一式を梱包する
		time	7h
		exptime	4.5h
		exp		1%
		job		道具屋	times/job_tool_time_rate
		use		1	解体/梱包キット
		use		10	鋼鉄の剣
		use		10	鋼鉄の盾
		use		10	鋼鉄の鎧
		use		10	鋼鉄の杖
		get		10	鋼鉄製装備一式
	@@USE
		name	ミスリル製装備一式を梱包する
		time	8h
		exptime	5h
		exp		1%
		job		道具屋	times/job_tool_time_rate
		use		1	解体/梱包キット
		use		10	ミスリルの剣
		use		10	ミスリルの盾
		use		10	ミスリルの鎧
		use		10	ミスリルの杖
		get		10	ミスリル製装備一式
	@@USE
		name	オリハルコン製装備一式を梱包する
		time	9h
		exptime	6h
		exp		1%
		job		道具屋	times/job_tool_time_rate
		use		1	解体/梱包キット
		use		10	オリハルコンの剣
		use		10	オリハルコンの盾
		use		10	オリハルコンの鎧
		use		10	オリハルコンの杖
		get		10	オリハルコン製装備一式
	@@USE
		name	お祝いグッズを梱包する
		time	8h
		job		道具屋	times/job_tool_time_rate
		use		1	解体/梱包キット
		use		1	七面鳥の丸焼き
		use		1	こだわりのラム酒
		use		1	おしゃれブーツ
		get		1	お祝いセット

@@ITEM
	no		15
	type	本
	code	book-tyougou
	name	薬調合入門
	info	薬を調合するための技術書です
	price	25000
	limit	40/1	#★所持最大数/市場入荷最大数(1店舗あたり)
			#  10店舗のゲームだと、この例では市場には最大10個入荷する。
			#  また、負数の場合は絶対数となる。(10/-2なら市場には最大2個)
			#  市場最大数を指定しない書式パターン1の場合は、所持最大数と同じ。
	pop	2d
	plus	20h
	scale	冊
	cost	200
	@@use
		time	30m
		exp		2%
		exptime	10m
		job		薬屋	times/job_drug_time_rate
		scale	セット
		action	作りまくる
		name	ポーションを作成する
		info	ポーションを作成しまくります
		okmsg	ポーションをたくさん作りました
		ngmsg	作成に失敗しました…
			use		10	薬草
			get		20	ポーション	80%
	@@use
		time	30m
		exp		2%
		exptime	10m
		name	ハイポーションを作成する
		info	ハイポーションを作成しまくります
		okmsg	ハイポーションを作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	25
			needexp	20%
			use		10	ポーション
			get		20	ハイポーション	80%
	@@use
		time	30m
		exp		2%
		exptime	10m
		name	エーテルを作成する
		info	エーテルを作成しまくります
		okmsg	エーテルを作りました
		ngmsg	作成に失敗しました…
			needexp	20%
			use		20	薬草
			get		20	エーテル	64%
	@@use
		time	30m
		exp		2%
		exptime	10m
		name	ハイエーテルを作成する
		info	ハイエーテルを作成しまくります
		okmsg	ハイエーテルを作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	25
			needexp	40%
			use		10	エーテル
			get		10	ハイエーテル	90%
	@@use
		time	30m
		exp		2%
		exptime	10m
		name	エリ草を作成する
		info	エリ草を作成しまくります
		okmsg	エリ草を作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	50
			needexp	60%
			use		10	ハイポーション
			use		10	ハイエーテル
			get		5	エリ草
@@ITEM
	no		16
	type	本
	code	book-kawazaiku
	name	革細工入門
	info	革細工師を目指す人へ
	price	25000
	limit	40/1
	pop	2d
	plus	20h
	scale	冊
	cost	500
	@@use
		time	1h
		exp		2%
		exptime	20m
		job		防具屋	times/job_armor_time_rate
		scale	セット
		action	作りまくる
		name	革の盾を作成する
		info	革の盾を作成します
		okmsg	革の盾を作りました
		ngmsg	作成に失敗しました…
			use		24	獣の革
			get		30	革の盾	80%
	@@use
		time	1h
		exp		2%
		exptime	20m
		scale	セット
		action	作りまくる
		name	革の胸当てを作成する
		info	革の胸当てを作成します
		okmsg	革の胸当てを作りました
		ngmsg	作成に失敗しました…
			use		24	獣の革
			get		32	革の胸当て	80%

@@ITEM
	no		17
	type	本
	code	book-mokkouzaiku
	name	木工細工入門
	info	木工細工師を目指す人へ
	price	25000
	limit	40/1
	pop	2d
	plus	20h
	scale	冊
	cost	500
	@@use
		time	1h
		exp		2%
		exptime	20m
		job		武器屋	times/job_weapon_time_rate
		scale	セット
		action	作りまくる
		name	木刀を作成する
		info	木刀を作成します
		okmsg	木刀を作りました
		ngmsg	作成に失敗しました…
			use		20	木の枝
			get		20	木刀	80%
	@@use
		time	1h
		exp		2%
		exptime	20m
		name	木の杖を作成する
		info	木の杖を作成します
		okmsg	木の杖を作りました
		ngmsg	作成に失敗しました…
			use		20	木の枝
			get		20	木の杖	80%
	@@use
		time	2h
		exp		2%
		exptime	40m
		job		防具屋	times/job_armor_time_rate
		name	木の盾を作成する
		info	木の盾を作成します
		okmsg	木の盾を作りました
		ngmsg	作成に失敗しました…
			use		10	丸太
			get		20	木の盾	80%
	@@use
		time	2h
		exp		2%
		exptime	40m
		job		防具屋	times/job_armor_time_rate
		name	木の胸当てを作成する
		info	木の胸当てを作成します
		okmsg	木の胸当てを作りました
		ngmsg	作成に失敗しました…
			use		10	丸太
			get		24	木の胸当て	80%

@@ITEM
	no		66
	type	本
	code	book-sousyoku
	name	装飾細工入門
	info	装飾細工師を目指す人へ
	price	50000
	limit	20/0.5
	pop	2d
	plus	20h
	scale	冊
	cost	1000
	@@use
		time	90m
		exp		2%
		exptime	30m
		job		道具屋	times/job_tool_time_rate
		scale	セット
		action	作りまくる
		name	鉄のピアスを作成する
		info	鉄のピアスを作成しまくります
		okmsg	鉄のピアスをたくさん作りました
		ngmsg	作成に失敗しました…
			need	1	鍛冶屋の技術
			need	1	魔法の知識
			use		20	鉄塊
			get		20	鉄のピアス	80%
	@@use
		time	3h
		exp		2%
		exptime	1h
		scale	セット
		action	作りまくる
		name	ミスリルの指輪を作成する
		info	ミスリルの指輪を作成しまくります
		okmsg	ミスリルの指輪をたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	50
			needexp	25%
			need	1	鍛冶屋の技術
			need	1	魔法の知識
			use		20	ミスリル塊
			use		2	魔石
			get		20	ミスリルの指輪	60%
	@@use
		time	4h
		exp		2%
		exptime	80m
		scale	セット
		action	作りまくる
		name	オリハルコンの腕輪を作成する
		info	オリハルコンの腕輪を作成しまくります
		okmsg	オリハルコンの腕輪をたくさん作りました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	50
			needexp	50%
			need	1	鍛冶屋の技術
			need	1	魔法の知識
			use		20	オリハルコン塊
			use		2	魔石
			get		20	オリハルコンの腕輪	40%
	@@use
		time	6h
		exp	2%
		exptime	5h
		scale	セット
		action	作り上げる
		name	なゆたの首飾りを作成する
		info	なゆたの首飾りを作り上げます
		okmsg	伝説が今、目の前に！
		ngmsg	作成に失敗しました…
		func	lostbook
		param	200
			needexp	50%
			need	1	鍛冶屋の技術
			need	1	魔法の知識
			need	1	目利きの真髄
			use		20	鉄塊
			use		20	ミスリル塊
			use		20	オリハルコン塊
			use		6	魔石
			get		1	なゆたの首飾り
	
@@ITEM
	no		20
	type	本
	code	book-ken
	name	剣の鍛え方
	info	武器の代表「剣」の鍛え方
	price	50000
	limit	20/0.5
	pop	2d
	plus	20h
	scale	冊
	cost	1000
	@@use
		time	90m
		exp		2%
		exptime	30m
		job		武器屋	times/job_weapon_time_rate
		scale	セット
		action	鍛える
		name	鉄の剣を鍛える
		info	オーソドックスな鉄の剣を鍛えてみましょう
		okmsg	鉄の剣を鍛えました
		ngmsg	鍛えるのに失敗しました…
			need	1	鍛冶屋の技術
			use		20	鉄塊
			get		20	鉄の剣	80%
	@@use
		time	3h
		exptime	1h
		name	鋼鉄の剣を鍛える
		info	鋼鉄の剣を鍛えてみましょう
		okmsg	鋼鉄の剣を鍛えました
		ngmsg	鍛えるのに失敗しました…
			needexp	20%
			need	1	鍛冶屋の技術
			use		40	鉄塊
			get		20	鋼鉄の剣	80%
	@@use
		time	3h
		exptime	1h
		name	ミスリルの剣を鍛える
		info	上級冒険者の御用達，ミスリルの剣を鍛えてみましょう
		okmsg	ミスリルの剣を鍛えました
		ngmsg	鍛えるのに失敗しました…
		func	lostbook
		param	50
			needexp	40%
			need	1	鍛冶屋の技術
			use		20	ミスリル塊
			get		20	ミスリルの剣	60%
	@@use
		time	4h
		exptime	80m
		name	オリハルコンの剣を鍛える
		info	めったに手に入らない、オリハルコンの剣を鍛えてみましょう
		okmsg	オリハルコンの剣を鍛えました
		ngmsg	鍛えるのに失敗しました…
		func	lostbook
		param	50
			needexp	60%
			need	1	鍛冶屋の技術
			use		20	オリハルコン塊
			get		20	オリハルコンの剣	40%
@@ITEM
	no		21
	type	本
	code	book-tate
	name	盾の作り方
	info	回避系防御装備「盾」の作り方
	price	50000
	limit	20/0.5
	pop	2d
	plus	20h
	scale	冊
	cost	1000
	@@use
		time	90m
		exp		2%
		exptime	30m
		job		防具屋	times/job_armor_time_rate
		scale	セット
		action	作成する
		name	鉄の盾を作成する
		info	オーソドックスな鉄の盾を作成してみましょう
		okmsg	鉄の盾を作成しました
		ngmsg	作成に失敗しました…
			need	1	鍛冶屋の技術
			use		20	鉄塊
			get		20	鉄の盾	80%
	@@use
		time	3h
		exptime	1h
		name	鋼鉄の盾を作成する
		info	鋼鉄の盾を作成してみましょう
		okmsg	鋼鉄の盾を作成しました
		ngmsg	作成に失敗しました…
			needexp	20%
			need	1	鍛冶屋の技術
			use		40	鉄塊
			get		20	鋼鉄の盾	80%
	@@use
		time	3h
		exptime	1h
		name	ミスリルの盾を作成する
		info	上級冒険者の御用達，ミスリルの盾を作成してみましょう
		okmsg	ミスリルの盾を作成しました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	50
			needexp	40%
			need	1	鍛冶屋の技術
			use		20	ミスリル塊
			get		20	ミスリルの盾	60%
	@@use
		time	4h
		exptime	80m
		name	オリハルコンの盾を作成する
		info	めったに手に入らない、オリハルコンの盾を作成してみましょう
		okmsg	オリハルコンの盾を作成しました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	50
			needexp	60%
			need	1	鍛冶屋の技術
			use		20	オリハルコン塊
			get		20	オリハルコンの盾	40%
@@ITEM
	no		22
	type	本
	code	book-yoroi
	name	鎧の作り方
	info	耐撃系防御装備「鎧」の作り方
	price	50000
	limit	20/0.5
	pop	2d
	plus	20h
	scale	冊
	cost	1000
	@@use
		time	120m
		exp		2%
		exptime	40m
		job		防具屋	times/job_armor_time_rate
		scale	セット
		action	作成する
		name	鉄の鎧を作成する
		info	オーソドックスな鉄の鎧を作成してみましょう
		okmsg	鉄の鎧を作成しました
		ngmsg	作成に失敗しました…
			need	1	鍛冶屋の技術
			use		20	鉄塊
			get		20	鉄の鎧	80%
	@@use
		time	210m
		exptime	70m
		name	鋼鉄の鎧を作成する
		info	鋼鉄の鎧を作成してみましょう
		okmsg	鋼鉄の鎧を作成しました
		ngmsg	作成に失敗しました…
			needexp	20%
			need	1	鍛冶屋の技術
			use		40	鉄塊
			get		20	鋼鉄の鎧	80%
	@@use
		time	210m
		exptime	70m
		name	ミスリルの鎧を作成する
		info	上級冒険者の御用達，ミスリルの鎧を作成してみましょう
		okmsg	ミスリルの鎧を作成しました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	50
			needexp	40%
			need	1	鍛冶屋の技術
			use		20	ミスリル塊
			get		20	ミスリルの鎧	60%
	@@use
		time	270m
		exptime	90m
		name	オリハルコンの鎧を作成する
		info	めったに手に入らない、オリハルコンの鎧を作成してみましょう
		okmsg	オリハルコンの鎧を作成しました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	50
			needexp	60%
			need	1	鍛冶屋の技術
			use		20	オリハルコン塊
			get		20	オリハルコンの鎧	40%

@@ITEM
	no		23
	type	本
	code	book-tue
	name	杖の作り方
	info	魔法系攻撃装備「杖」の作り方
	price	50000
	limit	20/0.5
	pop	2d
	plus	20h
	scale	冊
	cost	1000
	@@use
		time	90m
		exp		2%
		exptime	30m
		job		武器屋	times/job_weapon_time_rate
		scale	セット
		action	作成する
		name	鉄の杖を作成する
		info	オーソドックスな鉄の杖を作成してみましょう
		okmsg	鉄の杖を作成しました
		ngmsg	作成に失敗しました…
			need	1	魔法の知識
			use		20	鉄塊
			use		2	魔石
			get		20	鉄の杖	80%
	@@use
		time	3h
		exptime	1h
		name	鋼鉄の杖を作成する
		info	鋼鉄の杖を作成してみましょう
		okmsg	鋼鉄の杖を作成しました
		ngmsg	作成に失敗しました…
			needexp	25%
			need	1	魔法の知識
			use		40	鉄塊
			use		4	魔石
			get		20	鋼鉄の杖	80%
	@@use
		time	3h
		exptime	1h
		name	ミスリルの杖を作成する
		info	上級冒険者の御用達，ミスリルの杖を作成してみましょう
		okmsg	ミスリルの杖を作成しました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	50
			needexp	50%
			need	1	魔法の知識
			use		20	ミスリル塊
			use		6	魔石
			get		20	ミスリルの杖	60%
	@@use
		time	4h
		exptime	80m
		name	オリハルコンの杖を作成する
		info	めったに手に入らない、オリハルコンの杖を作成してみましょう
		okmsg	オリハルコンの杖を作成しました
		ngmsg	作成に失敗しました…
		func	lostbook
		param	50
			needexp	70%
			need	1	魔法の知識
			use		20	オリハルコン塊
			use		10	魔石
			get		20	オリハルコンの杖	40%

@@ITEM
	no		12
	type	地図
	code	book-mtsearch
	name	近くの山への地図
	info	材料調達にはもってこいの山です
	price	10000
	limit	3/3
	pop	0
	plus	1h
	base	50/150
	scale	冊
	cost	500
	flag	noshowcase
	@@use
		time	2h
		exp		2%
		exptime	30m
		job		山師	times/job_material_time_rate
		scale	往復
		action	探索しに行く
		name	山のふもとを探索
		info	いろんな材料が調達できるかもしれません
		func	lostbook
		param	10
		ngmsg	なにも見つかりませんでした…
			get		80	薬草	90%	薬草がたくさん生えていました
			get		2	獣の革	90%
			get		2	木の枝	90%
			get		2	丸太	45%
	@@use
		time	2h
		exp		2%
		exptime	30m
		scale	往復
		action	探索しに行く
		name	林道を探索
		info	いろんな材料が調達できるかもしれません
		ngmsg	なにも見つかりませんでした…
		func	lostbook
		param	10
			get		4	薬草	90%
			get		2	獣の革	90%
			get		40	木の枝	90%	木の枝がたくさん落ちていました
			get		2	丸太	45%
	@@use
		time	2h
		exp		2%
		exptime	30m
		scale	往復
		action	探索しに行く
		name	獣道を探索
		info	材料が調達できるかもしれません
		ngmsg	なにも見つかりませんでした…
		func	lostbook
		param	10
			get		4	薬草	90%
			get		40	獣の革	90%	獣をたくさん狩りました
			get		2	木の枝	90%
			get		2	丸太	45%
	@@use
		time	2h
		exp		2%
		exptime	30m
		scale	往復
		action	探索しに行く
		name	雑木林の奥を探索
		info	材料が調達できるかもしれません
		ngmsg	なにも見つかりませんでした…
		func	lostbook
		param	10
			get		4	薬草	90%
			get		2	獣の革	90%
			get		2	木の枝	90%
			get		40	丸太	45%		丸太がたくさん見つかりました
	
@@ITEM
	no		9
	type	地図
	code	book-metalsearch
	name	近くの鉱山への地図
	info	各種鉱物の採取ができそうです
	price	10000
	limit	3/3
	pop	0
	plus	1h
	base	50/150
	scale	冊
	cost	500
	flag	noshowcase
	@@use
		time	2h
		exp		2%
		exptime	30m
		job		山師	times/job_material_time_rate
		scale	往復
		action	採取しに行く
		name	鉄鉱山へ行く
		info	いろんな鉱物が調達できるかもしれません
		ngmsg	なにも見つかりませんでした…
		func	lostbook
		param	10
			get		30	鉄塊			80%
			get		2	ミスリル塊		60%
			get		1	オリハルコン塊	80%
	@@use
		time	2h
		exp		2%
		exptime	30m
		scale	往復
		action	採取しに行く
		name	ミスリル鉱山へ行く
		info	いろんな鉱物が調達できるかもしれません
		ngmsg	なにも見つかりませんでした…
		func	lostbook
		param	10
			get		3	鉄塊			80%
			get		20	ミスリル塊		60%
			get		1	オリハルコン塊	80%
	@@use
		time	2h
		exp		2%
		exptime	30m
		scale	往復
		action	採取しに行く
		name	オリハルコン鉱山へ行く
		info	いろんな鉱物が調達できるかもしれません
		ngmsg	なにも見つかりませんでした…
		func	lostbook
		param	10
			get		3	鉄塊			80%
			get		2	ミスリル塊		60%
			get		10	オリハルコン塊	80%

@@ITEM
	no		14
	type	地図
	code	shiire-ken
	name	剣市への地図
	info	剣の市場までの地図
	price	10000
	limit	3/3
	pop	0
	plus	1h
	base	50/150
	scale	冊
	cost	500
	flag	noshowcase
	@@use
		time	4h
		exp	2%
		exptime	2h
		job		行商人	times/job_peddle_time_rate
		scale	往復
		action	仕入に行く
		price	12000					#★使用時費用額
		name	剣の市場へ仕入に行く
		info	剣を仕入に行きます
		func	lostbook
		param	100
		ngmsg	なにも仕入れられませんでした…
			get		10	木刀			40%
			get		10	鉄の剣			35%
			get		10	鋼鉄の剣		15%
			get		10	ミスリルの剣		6%	ミスリルの剣が安かったです
			get		10	オリハルコンの剣	3%	オリハルコンの剣が掘り出し物として出てました!
		funcb	_local_
			# 1/10の確率で収穫量が2倍になる
			return 0 if rand(1000)>100;
			
			my $USE=$_[0];
			
			# $USE->{result}->{create}->[0..?]->{count} を2倍にする
			foreach(@{$USE->{result}->{create}})
			{
				$_->{count}*=2;
			}
			
			# okmsg を設定する
			$USE->{result}->{message}->{resultok}='今回は収穫がいつもより多かったです';
			return 0;
		_local_
	

@@ITEM
	no		30
	type	薬
	code	posyon
	name	ポーション
	info	体力を回復させる薬
	price	100
	limit	5000/500
	pop	20m
	plus	2h
	base	10/1000
	scale	個
	cost	5
	point	10%
@@ITEM
	no		31
	type	薬
	code	posyon-hi
	name	ハイポーション
	info	薬の一種
	price	200
	limit	2500/250
	base	400/1000
	plus	-1h
	pop	30m
	scale	個
	point	10%
@@ITEM
	no		32
	type	薬
	code	eteru
	name	エーテル
	info	魔力を回復させる薬
	price	250
	limit	2000/200
	pop	50m
	plus	5h
	base	10/500
	scale	個
	cost	10
	point	20%
@@ITEM
	no		33
	type	薬
	code	eteru-hi
	name	ハイエーテル
	info	薬の一種
	price	500
	limit	1000/100
	base	200/500
	plus	-1h
	pop	60m
	scale	個
	cost	50
	point	20%
@@ITEM
	no		34
	type	薬
	code	erikusa
	name	エリ草
	info	薬の一種
	price	2500
	plus	-1h
	limit	400/40
	base	40/100
	pop	4h
	scale	個
	cost	100
	point	40%
@@ITEM
	no		40
	type	剣
	code	ken-ki
	name	木刀
	info	お土産に最適
	price	1200
	limit	600
	base	100/200
	plus	-1h
	pop	3h
	scale	本
@@ITEM
	no		41
	type	剣
	code	ken-tetu
	name	鉄の剣
	info	鉄の剣
	price	1500
	limit	500
	base	50/100
	plus	-1h
	pop	3h
	scale	本
@@ITEM
	no		42
	type	剣
	code	ken-hagane
	name	鋼鉄の剣
	info	鋼鉄の剣
	price	3200
	limit	300
	base	30/60
	plus	-1h
	pop	5h
	scale	本
	point	80%
@@ITEM
	no		43
	type	剣
	code	ken-misuriru
	name	ミスリルの剣
	info	ミスリルの剣
	price	8000
	limit	100
	base	20/40
	plus	-1h
	pop	10h
	scale	本
	point	70%
@@ITEM
	no		44
	type	剣
	code	ken-oriharukon
	name	オリハルコンの剣
	info	オリハルコンの剣
	price	12000
	limit	75
	base	12/24
	plus	-1h
	pop	16h
	scale	本
	point	60%

@@ITEM
	no		51
	type	鎧
	code	yoroi-kawa
	name	革の胸当て
	info	防寒効果すら無し
	price	750
	limit	1000
	base	150/300
	plus	-1h
	pop	110m
	scale	個
	point	40%
@@ITEM
	no		52
	type	鎧
	code	yoroi-ki
	name	木の胸当て
	info	かろうじて胸当て
	price	1000
	limit	750
	base	100/200
	plus	-1h
	pop	150m
	scale	個
	point	50%
@@ITEM
	no		53
	type	鎧
	code	yoroi-tetu
	name	鉄の鎧
	info	鉄の鎧
	price	1600
	limit	500
	base	50/100
	plus	-1h
	pop	190m
	scale	個
	point	80%
@@ITEM
	no		54
	type	鎧
	code	yoroi-hagane
	name	鋼鉄の鎧
	info	鋼鉄の鎧
	price	3400
	limit	300
	base	30/60
	plus	-1h
	pop	320m
	scale	個
	point	80%
@@ITEM
	no		55
	type	鎧
	code	yoroi-misuriru
	name	ミスリルの鎧
	info	ミスリルの鎧
	price	9000
	limit	100
	base	20/40
	plus	-1h
	pop	680m
	scale	個
	point	75%
@@ITEM
	no		56
	type	鎧
	code	yoroi-oriharukon
	name	オリハルコンの鎧
	info	オリハルコンの鎧
	price	12500
	limit	75
	base	12/24
	plus	-1h
	pop	17h
	scale	個
	point	60%

@@ITEM
	no		45
	type	盾
	code	tate-kawa
	name	革の盾
	info	無いよりはマシ
	price	800
	limit	1000
	base	100/200
	plus	-1h
	pop	120m
	scale	個
	point	75%
@@ITEM
	no		46
	type	盾
	code	tate-ki
	name	木の盾
	info	子供の練習用
	price	1200
	limit	600
	base	100/200
	plus	-1h
	pop	3h
	scale	個
@@ITEM
	no		47
	type	盾
	code	tate-tetu
	name	鉄の盾
	info	鉄の盾
	price	1500
	limit	500
	base	50/100
	plus	-1h
	pop	3h
	scale	個
@@ITEM
	no		48
	type	盾
	code	tate-hagane
	name	鋼鉄の盾
	info	鋼鉄の盾
	price	3200
	limit	300
	base	30/60
	plus	-1h
	pop	5h
	scale	個
	point	80%
@@ITEM
	no		49
	type	盾
	code	tate-misuriru
	name	ミスリルの盾
	info	ミスリルの盾
	price	7500
	limit	100
	base	20/40
	plus	-1h
	pop	10h
	scale	個
	point	70%
@@ITEM
	no		50
	type	盾
	code	tate-oriharukon
	name	オリハルコンの盾
	info	オリハルコンの盾
	price	11000
	limit	75
	base	12/24
	plus	-1h
	pop	15h
	scale	個
	point	60%

@@ITEM
	no		57
	type	杖
	code	tue-ki
	name	木の杖
	info	おもちゃの杖
	price	1200
	limit	600
	base	100/200
	plus	-1h
	pop	3h
	scale	本
@@ITEM
	no		58
	type	杖
	code	tue-tetu
	name	鉄の杖
	info	鉄の杖
	price	2000
	limit	500
	base	50/100
	plus	-1h
	pop	5h
	scale	本
@@ITEM
	no		59
	type	杖
	code	tue-hagane
	name	鋼鉄の杖
	info	鋼鉄の杖
	price	4000
	limit	300
	base	30/60
	plus	-1h
	pop	8h
	scale	本
	point	80%
@@ITEM
	no		60
	type	杖
	code	tue-misuriru
	name	ミスリルの杖
	info	ミスリルの杖
	price	10000
	limit	100
	base	20/40
	plus	-1h
	pop	15h
	scale	本
	point	70%
@@ITEM
	no		61
	type	杖
	code	tue-oriharukon
	name	オリハルコンの杖
	info	オリハルコンの杖
	price	16000
	limit	75
	base	12/24
	plus	-1h
	pop	24h
	scale	本
	point	60%

@@ITEM
	no		67
	type	アクセサリ
	code	sousyoku-tetu
	name	鉄のピアス
	info	手作り感溢れるピアス
	price	1500
	limit	500/0
	pop	4h
	base	20/30
	scale	個
@@ITEM
	no		68
	type	アクセサリ
	code	sousyoku-misuriru
	name	ミスリルの指輪
	info	ミスリルの指輪
	price	8000
	limit	100/0
	pop	14h
	base	20/40
	plus	-1h
	scale	個
@@ITEM
	no		69
	type	アクセサリ
	code	sousyoku-oriharukon
	name	オリハルコンの腕輪
	info	オリハルコンの腕輪
	price	12000
	limit	75/0
	pop	20h
	base	12/24
	plus	-1h
	scale	個
@@ITEM
	no		70
	type	アクセサリ
	code	sousyoku-nayuta
	name	なゆたの首飾り
	info	伝説の英雄を称えた首飾り
	price	50000
	limit	1/0
	pop		2d
	scale	個
	cost	200
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
			DebugLog("item $ITEM->{name} $DT->{shopname} 人気 +".($rankup/100)."\%");
		}
	_local_

@@ITEM
	no		71
	type	道具
	code	soubiset-kawa
	name	革製装備一式
	info	革製の装備をまとめたセット商品
	price	3000
	limit	300/0
	pop	6h
	scale	セット
@@ITEM
	no		72
	type	道具
	code	soubiset-ki
	name	木製装備一式
	info	木製の装備をまとめたセット商品
	price	9000
	limit	100/0
	pop	18h
	scale	セット
@@ITEM
	no		73
	type	道具
	code	soubiset-tetu
	name	鉄製装備一式
	info	鉄製の装備をまとめたセット商品
	price	12000
	limit	80/0
	pop	24h
	scale	セット
@@ITEM
	no		74
	type	道具
	code	soubiset-hagane
	name	鋼鉄製装備一式
	info	鋼鉄製の装備をまとめたセット商品
	price	27000
	limit	40/0
	pop	54h
	scale	セット
@@ITEM
	no		75
	type	道具
	code	soubiset-misuriru
	name	ミスリル製装備一式
	info	ミスリル製の装備をまとめたセット商品
	price	60000
	limit	20/0
	pop	108h
	scale	セット
@@ITEM
	no		76
	type	道具
	code	soubiset-oriharukon
	name	オリハルコン製装備一式
	info	オリハルコン製の装備をまとめたセット商品
	price	81000
	limit	10/0
	pop	148h
	scale	セット

@@ITEM
	no		1
	type	原料
	code	yakusou
	name	薬草
	info	薬になる草
	price	50
	limit	4000/1000
	pop	10d
	plus	-20m
	base	200/1400
	scale	本
	cost	10
	point	25%
@@ITEM
	no		2
	type	原料
	code	kemononokawa
	name	獣の革
	info	なめした獣の毛皮
	price	100
	limit	2000/500
	pop	10d
	plus	-20m
	base	100/700
	scale	枚
	cost	30
	point	50%
@@ITEM
	no		3
	type	原料
	code	kinoeda
	name	木の枝
	info	腕の太さ程度の枝
	price	120
	limit	1500/500
	pop	10d
	plus	-20m
	base	200/600
	scale	本
	cost	40
	point	50%
@@ITEM
	no		4
	type	原料
	code	maruta
	name	丸太
	info	丸太
	price	240
	limit	500/100
	pop	10d
	plus	-20m
	base	100/500
	scale	本
	cost	100
@@ITEM
	no		8
	type	原料
	code	magicstone
	name	魔石
	info	魔力が封じ込められた鉱石
	price	250
	limit	200/50
	pop	10d
	plus	6h
	base	500/2500
	scale	個
	cost	100
@@ITEM
	no		5
	type	原料
	code	tetu
	name	鉄塊
	info	鉄のかたまり
	price	200
	limit	1000/250
	pop	10d
	plus	-20m
	base	300/800
	scale	kg
	cost	60
@@ITEM
	no		6
	type	原料
	code	misuriru
	name	ミスリル塊
	info	ミスリルのかたまり
	price	400
	limit	800/200
	pop	10d
	plus	-20m
	base	300/600
	scale	kg
	cost	80
@@ITEM
	no		7
	type	原料
	code	oriharukon
	name	オリハルコン塊
	info	オリハルコンのかたまり
	price	600
	limit	600/150
	pop	10d
	plus	-20m
	base	300/600
	scale	kg
	cost	90

@@ITEM
	no		62
	type	道具
	code	cm
	name	広告パック
	info	人気を上げられますが失敗することも…
	price	100000
	limit	1/1
	pop	10d
	plus	5d
	base	10/50
	scale	パック
	cost	10000
	@@use
		time	10h
		exp	10%
		job		行商人	times/job_peddle_time_rate
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
	@@use
		time	10h
		exp	0%
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
	@@use
		time	16h
		exp	0%
		name	ギルドの広告を出す
		info	同ギルド所属店全ての人気を上げられます
		arg		nocount
			use		1	広告パック
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
	no		13
	type	本
	code	book-work
	name	資金調達の方法
	info	今すぐお金が必要なときはコレ
	price	0
	limit	1/1
	pop	0
	plus	10h
	scale	冊
	flag	noshowcase
	@@use
		time	4h
		job		行商人	times/job_peddle_time_rate
		scale	回
		action	働く
		name	ティッシュ配りで資金稼ぎ
		info	お手軽に稼ぎましょう
		param	3000
		func	_local_
			# ★バイト
			#   param1 取得額
			$DT->{money}+=$USE->{param1}*$count;
			
			my $ret=GetMoneyString($USE->{param1}*$count).'稼ぎました';
			
			WriteLog(0,$DT->{id},"バイトし、$ret");
			WriteLog(3,0,$DT->{shopname}."がバイトしたようです");
			
			return $ret;
		_local_
	@@use
		time	8h
		job		行商人	times/job_peddle_time_rate
		scale	回
		action	働く
		name	日雇い土木作業で資金稼ぎ
		info	ちょっときついけどそこそこの稼ぎです
		param	10000
		func	_local_1

@@ITEM
	no		63
	type	道具
	code	edit-showcase
	name	陳列棚増築取壊キット
	info	陳列棚の増築や取り壊し等に必要な道具一式です
	price	0
	limit	1/1
	pop	0
	plus	1d
	scale	キット
	flag	noshowcase|norequest
	@@use
		time	1h
		scale	回
		action	作業する
		price	10000
		name	陳列棚を1つにする
		info	陳列棚を1つにする
		arg		nocount		#★使用時の選択肢指定。
							#  nocount -> 使用回数選択なし
		param	1			#★独自関数用パラメータ
			use	1	陳列棚増築取壊キット
		func	_local_
			# ★陳列棚数変更
			#   param1 変更後の棚数
			my $oldcnt=$DT->{showcasecount};
			my $newcnt=$USE->{param1};
			$DT->{showcasecount}=$newcnt;
			
			if($oldcnt<$newcnt)
			{
				foreach ($oldcnt..$newcnt-1)
				{
					$DT->{showcase}[$_]=0;
					$DT->{price}[$_]=0;
				}
			}
			if($oldcnt>$newcnt)
			{
				splice(@{$DT->{showcase}},$newcnt);
				splice(@{$DT->{price}},$newcnt);
			}
			my $ret="陳列棚を$DT->{showcasecount}個にしました";
			WriteLog(0,$DT->{id},$ret);
			WriteLog(0,0,$DT->{shopname}."の陳列棚が$DT->{showcasecount}個になりました。");
			
			return $ret;
		_local_
	@@use
		time	2h
		price	20000
		name	陳列棚を2つにする
		info	陳列棚を2つにする
		func	_local_1
		arg		nocount
		param	2
			use	1	陳列棚増築取壊キット
	@@use
		time	3h
		price	30000
		name	陳列棚を3つにする
		info	陳列棚を3つにする
		func	_local_1
		arg		nocount
		param	3
			use	1	陳列棚増築取壊キット
	@@use
		time	4h
		price	40000
		name	陳列棚を4つにする
		info	陳列棚を4つにする
		func	_local_1
		arg		nocount
		param	4
			use	1	陳列棚増築取壊キット
	@@use
		time	5h
		price	50000
		name	陳列棚を5つにする
		info	陳列棚を5つにする
		func	_local_1
		arg		nocount
		param	5
			use	1	陳列棚増築取壊キット
	@@use
		time	6h
		price	60000
		name	陳列棚を6つにする
		info	陳列棚を6つにする
		func	_local_1
		arg		nocount
		param	6
			use	1	陳列棚増築取壊キット
	@@use
		time	7h
		price	70000
		name	陳列棚を7つにする
		info	陳列棚を7つにする
		func	_local_1
		arg		nocount
		param	7
			use	1	陳列棚増築取壊キット
	@@use
		time	8h
		price	80000
		name	陳列棚を8つにする
		info	陳列棚を8つにする
		func	_local_1
		arg		nocount
		param	8
			use	1	陳列棚増築取壊キット
		
@@ITEM
	no		65
	type	本
	code	badgossip
	name	禁断の書
	info	やってはならないがやらなくてはならないときに…
	price	50000
	cost	5000
	limit	1/1
	pop		0
	plus	1d
	scale	冊
	@@use
		time	10h
		exp	20%
		exptime	8h
		scale	回
		price	50000
		scale	回
		action	悪い噂を流す
		price	0
		name	悪い噂を流す
		info	成功すれば相手のお店の人気を下げられますが，失敗することも…
		arg	target|nocount
			needpoint	20000
			use		1	禁断の書
		func	_local_
			my $ret;
			if(rand(1000)<800 && !$DTS->{exp}{@@ITEMNO"広告パック"})
			{
				$DTS->{rank}-=int($DTS->{rank}/3);
				$ret=$DTS->{shopname}.'の悪い噂を流す作戦が成功しました';
				WriteLog(0,$DT->{id},$ret);
				WriteLog(2,0,$DTS->{shopname}.'の悪い噂が広まり人気が下がりました。');
			}
			else
			{
				$DTS->{exp}{@@ITEMNO"広告パック"}-=100;
				$DTS->{exp}{@@ITEMNO"広告パック"}=0 if ($DTS->{exp}{@@ITEMNO"広告パック"} < 0);
				$DT->{rank}-=int($DT->{rank}/4);
				$ret=$DTS->{shopname}.'の悪い噂を流す作戦は失敗しました';
				WriteLog(0,$DT->{id},$ret);
				WriteLog(3,0,$DT->{shopname}."が".$DTS->{shopname}.'の悪い噂を仕掛けていたようです。');
			}
			return $ret;
			_local_
	@@use
		time	10h
		exp	25%
		exptime	8h
		scale	回
		action	万引きする
		price	50000
		name	万引きする
		info	そこまで追い込まれてるのなら，しょうがないね…
		arg	target|nocount
			needpoint	20000
			use		1	禁断の書
		func	_local_
			return '自分から万引きすることはできません。万引きは失敗です。' if  ($DT->{id} eq $DTS->{id});
			my $ret="万引きは失敗しました。賠償金".GetMoneyString(500000)."を取られてしまいました。";
			if($DTS->{item}[@@ITEMNO"店番ロボット"-1])
			{
			$DTS->{item}[@@ITEMNO"店番ロボット"-1]--;
			$DT->{rank}-=int($DT->{rank}/4);
			$DTS->{money}+=500000;
			$DTS->{saletoday}+=500000;
			$DT->{money}-=500000;
			$DT->{paytoday}+=500000;
			WriteLog(3,0,$DT->{shopname}."が".$DTS->{shopname}."へ万引きに入り店番ロボットを破壊しましたが捕まりました。");
			WriteLog(3,0,$DT->{shopname}."は".$DTS->{shopname}."に賠償金".GetMoneyString(500000)."を支払いました。");
			WriteLog(0,$DT->{id},$ret);
			return $ret;
			}
			if(rand(1000)>900)
			{
			$DTS->{money}+=500000;
			$DTS->{saletoday}+=500000;
			$DT->{money}-=500000;
			$DT->{paytoday}+=500000;
			$DT->{rank}-=int($DT->{rank}/4);
			WriteLog(3,0,$DT->{shopname}."が".$DTS->{shopname}."へ万引きに入りましたが失敗しました。");
			WriteLog(3,0,$DT->{shopname}."は".$DTS->{shopname}."に賠償金".GetMoneyString(500000)."を支払いました。");
			WriteLog(0,$DT->{id},$ret);
			return $ret;
			}
			$ret="万引きは成功しました";
			my $manbiki_count=0;
			foreach my $idx (0..$DTS->{showcasecount}-1)
			{
				my $itemno=$DTS->{showcase}[$idx];
				if($itemno)
				{
					my $cnt=int($DTS->{item}[$itemno-1]*3/4);
					$cnt=$ITEM[$itemno]->{limit}-$DT->{item}[$itemno-1] if $DT->{item}[$itemno-1]+$cnt>$ITEM[$itemno]->{limit};
					$DTS->{item}[$itemno-1]-=$cnt;
					$DT->{item}[$itemno-1]+=$cnt;
					$manbiki_count+=$cnt*$DTS->{price}[$idx];
				}
			}
		$main::STATE->{safety}=int($main::STATE->{safety} * 18 / 19);
		WriteLog(2,0,$DTS->{shopname}."が総額".GetMoneyString($manbiki_count)."相当の万引き被害に遭いました。") if $manbiki_count;
		WriteLog(2,0,$DTS->{shopname}."に入った万引き犯は何も取らずに逃げました。") if !$manbiki_count;
		WriteLog(0,$DT->{id},$ret);
		return $ret;
		_local_
	@@use
		time	16h
		exp	5%
		exptime	14h
		scale	回
		action	取扱商品の悪い噂を流す
		price	50000
		name	業種の悪い噂を流す
		info	専門店キラー
		arg		target|nocount
			needpoint	20000
			use		1	禁断の書
		func	_local_
			my %category=qw(4 ken 5 yoroi 6 tate 7 tue); #分類番号とイベントコードの対応
			my $ret;
			my $itemno=$DTS->{showcase}->[int rand($DTS->{showcasecount})];
			my $itemtype=$ITEM[$itemno]->{type};
			my $category=$category{$itemtype};
			my $eventkey="kill-$category";
			
			#陳列棚の商品が%category外だったり，既に発動中なら失敗。
			return '噂を流すのに失敗しました' if !$category || grep($_ eq $eventkey,keys(%main::DTevent));
			
			#8時間持続でイベント発動
			$main::DTevent{$eventkey}=$main::NOW_TIME+8*60*60;
			$ret=$main::ITEMTYPE[$itemtype].'市場の悪い噂を広めました';
			WriteLog(0,$DT->{id},$ret);
			WriteLog(2,0,$main::ITEMTYPE[$itemtype].'市場の悪い噂が広まっているようです。');
			return $ret;
		_local_
@@event
	start		-1 #イベント自然発動無し
	code		kill-ken
	endmsg		反剣運動が収まりました
	info		反剣運動が起こっています
		param	木刀				point=0    #+-0%
		param	鉄の剣				point=-100 #-10%
		param	鋼鉄の剣			point=-200 #-20%
		param	ミスリルの剣		point=-300 #-30%
		param	オリハルコンの剣	point=-400 #-40%
@@event
	start		-1
	code		kill-yoroi
	endmsg		反鎧運動が収まりました
	info		反鎧運動が起こっています
		param	革の胸当て			point=0
		param	木の胸当て			point=0
		param	鉄の鎧				point=-100
		param	鋼鉄の鎧			point=-200
		param	ミスリルの鎧		point=-300
		param	オリハルコンの鎧	point=-400
@@event
	start		-1
	code		kill-tate
	endmsg		反盾運動が収まりました
	info		反盾運動が起こっています
		param	革の盾				point=0
		param	木の盾				point=0
		param	鉄の盾				point=-100
		param	鋼鉄の盾			point=-200
		param	ミスリルの盾		point=-300
		param	オリハルコンの盾	point=-400
@@event
	start		-1
	code		kill-tue
	endmsg		反杖運動が収まりました
	info		反杖運動が起こっています
		param	木の杖				point=0
		param	鉄の杖				point=-100
		param	鋼鉄の杖			point=-200
		param	ミスリルの杖		point=-300
		param	オリハルコンの杖	point=-400

@@ITEM
	no		18
	type	アクセサリ
	code	skill-kajiya
	name	鍛冶屋の技術
	info	鍛冶屋のオヤジ直伝
	price	50000
	cost	1000
	limit	1/0
	pop	0
	scale	技
	flag	noshowcase|norequest
@@ITEM
	no		19
	type	アクセサリ
	code	skill-magic
	name	魔法の知識
	info	魔法の基礎知識です
	price	50000
	cost	1000
	limit	1/0
	pop	0
	scale	知識
	flag	noshowcase|norequest
@@ITEM
	no		24
	type	アクセサリ
	code	skill-mekiki
	name	目利きの真髄
	info	違いが分かると早くなる
	price	50000
	cost	1000
	limit	1/0
	pop	0
	scale	真髄
	flag	noshowcase|norequest
@@ITEM
	no		38
	type	アクセサリ
	code	skill-kaitai
	name	解体屋の魂
	info	分解に命を懸ける
	price	50000
	cost	1000
	limit	1/0
	pop	0
	scale	魂
	flag	noshowcase|norequest

@@ITEM
	no		64
	type	アクセサリ
	code	defence-manbiki
	name	店番ロボット
	info	店内の監視をしてくれます
	price	500000
	cost	5000
	limit	1/0.5
	pop	1d
	plus	30m
	scale	体
	flag	noshowcase|onlysend

@@ITEM
	no		11
	type	アクセサリ
	code	loto
	name	宝くじ
	info	一攫千金も夢じゃない（抽選日は2日に1回の<B>確率</B>）
	price	2000
	cost	10
	limit	50/20
	plus	10m
	scale	枚
	pop	0
	flag	noshowcase|norequest

@@ITEM
	no		25
	type	道具
	code	mino
	name	ミノタウロス♀
	info	ちょっとおっかない家畜
	price	10000
	cost	1000
	limit	20/1.5
	plus	1d
	scale	頭
	pop		1d
	@@use
		time	2h
		exp		1%
		job		酪農家	times/job_cow_time_rate
		scale	搾乳
		action	搾る
		price	0
		name	乳を搾る
		info	ミノさんから乳を搾ります
		param	1
			need		1	ミノタウロス♀
		func	_local_
			# ★ミノタウロス搾乳
			#   param1 搾乳レベル（１～）
			my $val=$USE->{param1}*$count;
			
			$val*=$DT->{item}[25-1];
			$val=int(rand($val))+1;
			AddItem(26,$val,'ミノ牛乳を精製しました');
			
			my $useproba=$USE->{param1}*$USE->{param1};
			my $usecount=0;
			foreach(1..$count)
			{
				$usecount++ if rand(1000)<$useproba;
			}
			UseItem(25,$usecount,$ITEM[25]->{name}.'が'.($USE->{param1}==1?'寿命':'過労').'で天に召されました') if $usecount;
			
			my $ret='ミノ牛乳を'.$val.'本精製しました';
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_
		
	@@use
		time	2h
		exp		1%
		job		酪農家	times/job_cow_time_rate
		scale	搾乳
		action	搾る
		price	0
		name	ハードに乳を搾る
		info	ミノさんからハードに乳を搾ります
		param	2
		func	_local_1
			need		1	ミノタウロス♀

@@ITEM
	no		26
	type	薬
	code	mino_milk
	name	ミノ牛乳
	info	飲めば健康、経営すこやか
	price	200
	cost	50
	pop		30m
	limit	2500/0
	scale	本
	point	15%
	@@use
		time	3m
		job		酪農家	times/job_cow_time_rate
		scale	本
		action	飲む
		price	0
		name	飲む
		info	ミノ牛乳を飲んでみます
			use		1	ミノ牛乳
		func	_local_
			# ★ミノ牛乳を飲む
			my $val=$count;
			my $ret="";
			
			if($count>=30)
			{
				$DT->{rank}-=$count*2;
				$DT->{rank}=0 if $DT->{rank}<0;
				WriteLog(2,0,$DT->{shopname}.'の店主が救急車で運ばれました');
				WriteLog(2,0,'いっぺんにミノ牛乳'.$count.'本を飲むなんて正気の沙汰じゃありません');
				$ret="…気が付いたら病院のベッドの上でした";
			}
			elsif($count>=10)
			{
				$ret='オナカを壊してしまいました　いっぺんにミノ牛乳'.$count.'本は飲み過ぎです';
				WriteLog(0,$DT->{id},$ret);
			}
			else
			{
				$DT->{rank}+=int(rand($count+1))+$count;
				$DT->{rank}=10000 if $DT->{rank}>10000;
				$ret='ミノ牛乳を飲んで健康になった気がします';
				WriteLog(0,$DT->{id},$ret);
			}
			return $ret;
		_local_
	@@use
		time	72m
		job		酪農家	times/job_cow_time_rate
		scale	セット
		action	ライト発酵させる
		price	0
		name	ライト発酵
		info	ミノ牛乳を軽く発酵させてみます
			need	5	ミノタウロス♀
			use		15	ミノ牛乳
			get		2	ミノヨーグルト
	@@use
		time	144m
		job		酪農家	times/job_cow_time_rate
		scale	セット
		action	ヘビー発酵させる
		price	0
		name	ヘビー発酵
		info	ミノ牛乳をかなり発酵させてみます
			need	10	ミノタウロス♀
			use		15	ミノ牛乳
			get		1	ミノチーズ

@@ITEM
	no		35
	type	薬
	code	mino_yogurt
	name	ミノヨーグルト
	info	ミノ牛乳から作った高級ヨーグルト　ちょっとミノくさい
	price	3000
	cost	100
	pop	6h
	limit	300/0
	scale	個
	@@use
		time	10m
		job		酪農家	times/job_cow_time_rate
		scale	個
		action	食べる
		price	0
		name	食べる
		info	ミノヨーグルトを食べてみます
		ngmsg	庶民のオクチには合わないようだ…
			use		1	ミノヨーグルト

@@ITEM
	no		36
	type	薬
	code	mino_cheese
	name	ミノチーズ
	info	ミノ牛乳から作った高級チーズ　おえーってくらいミノくさい
	price	6000
	cost	200
	pop	10h
	limit	150/0
	scale	個
	@@use
		time	20m
		job		酪農家	times/job_cow_time_rate
		scale	個
		action	食べる
		price	0
		name	食べる
		info	ミノチーズを食べてみます
		ngmsg	クサくて吐いた…
			use		1	ミノチーズ


@@ITEM
	no		27
	type	薬
	code	seven_face
	name	七面鳥の丸焼き
	info	お祝いごとにはかかせませんね
	price	10000
	cost	0
	limit	1/0
	scale	匹
	pop		1d
	@@use
		time	1h
		scale	匹
		action	食べる
		price	0
		name	食べる
		info	お祝いしましょうか
		arg		nocount
			use		1	七面鳥の丸焼き	100%	オナカ一杯になりました

@@ITEM
	no		28
	type	薬
	code	ramusyu
	name	こだわりのラム酒
	info	あの伝説の勇者が好きだったというラム酒です
	price	20000
	cost	0
	limit	1/0
	scale	本
	pop		1d
	@@use
		time	1h
		scale	本
		action	飲む
		price	0
		name	飲む
		info	お祝いしましょうか
		arg		nocount
			use		1	こだわりのラム酒	100%	いい気分になりました

@@ITEM
	no		29
	type	アクセサリ
	code	boots
	name	おしゃれブーツ
	info	すんごいおしゃれなブーツです
	price	20000
	cost	0
	limit	1/0
	scale	足
	pop		1d
	@@use
		time	1h
		scale	足
		action	履く
		price	0
		name	履いてお出かけする
		info	街にくり出してお祝いしましょうか
		arg		nocount
			use		1	おしゃれブーツ	100%	みんなの視線を一人占めにしました

@@ITEM
	no		77
	type	道具
	code	party
	name	お祝いセット
	info	パーッといきたいときにはコレ
	price	200000
	cost	0
	limit	1/0
	scale	セット
	@@use
		time	4h
		action	パーティ開始
		price	0
		name	お祝いパーティ
		info	今夜は無礼講です
		func	popup
		param	1000,パーティを開きました
		arg		nocount
			use		1	お祝いセット	100%	明日への活力が沸いてきました

@@ITEM
	no		78
	type	本
	code	port-exp
	name	転職のススメ
	info	転職したい人のために
	price	10000
	limit	1
	pop		1d
	scale	セット
	plus	1h
	@@USE
		time	6h
		action	転職修行開始
		arg		nocount
		name	薬屋へ転職したい
		info	他の職業の技術経験を全て捨て、薬を扱う技術を習得します
		okmsg	薬屋になれた気がします
		param	15,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,drug
			use		1	転職のススメ
		func	_local_
			######################################################################
			# ★熟練度交換（指定アイテムへ、他のアイテムの熟練度を移動させる）
			#   param1 熟練度をプラスしたいアイテムの番号(1~)
			#   param2 熟練度をマイナスするアイテムの番号(1~) (:区切りで複数指定化)
			#   param3 熟練度を移動する際の係数（0~) (0.5だと半分にして移動)
			#   注意：熟練度の合計チェックはしていないので、係数を1より大きくするのはやめた方がいいです。
			######################################################################
			my $ret="";
			
			if($USE->{param1})
			{
				my $exp1=$DT->{exp}{$USE->{param1}};
				my $exp2=0;
				
				foreach my $exps (split(/:/,$USE->{param2}))
				{
					my $exp=$DT->{exp}{$exps};
					next if !$exp || $exps==$exp1;
					$exp2+=$exp;
					delete($DT->{exp}{$exps});
					my $msg=$ITEM[$exps]->{name}."の熟練度 ".int($exp/10)."% が 0% になりました";
					$ret.=$msg."<br>";
					WriteLog(0,$DT->{id},$msg);
				}
				$exp2=int($exp2*$USE->{param3});
				$exp1+=$exp2;
				$exp1=1000 if $exp1>1000;
				my $msg=$ITEM[$USE->{param1}]->{name}."の熟練度 ".int($DT->{exp}{$USE->{param1}}/10)."% が ".int($exp1/10)."% になりました";
				$ret.=$msg."<br>";
				WriteLog(0,$DT->{id},$msg);
				$DT->{exp}{$USE->{param1}}=$exp1;
			}
			$DT->{job}=$USE->{param4},$ret.='職業が「'.$main::JOBTYPE{$USE->{param4}}.'」になりました' if $USE->{param4} && $USE->{param4} ne '_default_';
			$DT->{job}='',$ret.='職業が「不定」になりました' if $USE->{param4} eq '_default_';
			
			return $ret;
		_local_
	@@USE
		time	6h
		action	転職修行開始
		arg		nocount
		name	革細工屋へ転職したい
		info	他の職業の技術経験を全て捨て、革細工の技術を習得します
		okmsg	革細工屋になれた気がします
		func	_local_1
		param	16,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,tool
			use		1	転職のススメ
	@@USE
		time	6h
		action	転職修行開始
		arg		nocount
		name	木工細工屋へ転職したい
		info	他の職業の技術経験を全て捨て、木工細工の技術を習得します
		okmsg	木工細工屋になれた気がします
		func	_local_1
		param	17,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,tool
			use		1	転職のススメ
	@@USE
		time	6h
		action	転職修行開始
		arg		nocount
		name	装飾細工屋へ転職したい
		info	他の職業の技術経験を全て捨て、装飾細工の技術を習得します
		okmsg	装飾細工屋になれた気がします
		func	_local_1
		param	66,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,tool
			use		1	転職のススメ
	@@USE
		time	6h
		action	転職修行開始
		arg		nocount
		name	剣屋へ転職したい
		info	他の職業の技術経験を全て捨て、剣屋に必要な技術を習得します
		okmsg	剣屋になれた気がします
		func	_local_1
		param	20,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,weapon
			use		1	転職のススメ
	@@USE
		time	6h
		action	転職修行開始
		arg		nocount
		name	盾屋へ転職したい
		info	他の職業の技術経験を全て捨て、盾屋に必要な技術を習得します
		okmsg	盾屋になれた気がします
		func	_local_1
		param	21,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,armor
			use		1	転職のススメ
	@@USE
		time	6h
		action	転職修行開始
		arg		nocount
		name	鎧屋へ転職したい
		info	他の職業の技術経験を全て捨て、鎧屋に必要な技術を習得します
		okmsg	鎧屋になれた気がします
		func	_local_1
		param	22,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,armor
			use		1	転職のススメ
	@@USE
		time	6h
		action	転職修行開始
		arg		nocount
		name	杖屋へ転職したい
		info	他の職業の技術経験を全て捨て、杖屋に必要な技術を習得します
		okmsg	杖屋になれた気がします
		func	_local_1
		param	23,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,weapon
			use		1	転職のススメ
	@@USE
		time	6h
		action	転職修行開始
		arg		nocount
		name	探鉱夫へ転職したい
		info	他の職業の技術経験を全て捨て、探鉱夫に必要な技術を習得します
		okmsg	探鉱夫になれた気がします
		func	_local_1
		param	9,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,material
			use		1	転職のススメ
	@@USE
		time	6h
		action	転職修行開始
		arg		nocount
		name	木こりへ転職したい
		info	他の職業の技術経験を全て捨て、木こりに必要な技術を習得します
		okmsg	木こりになれた気がします
		func	_local_1
		param	12,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,material
			use		1	転職のススメ
	@@USE
		time	6h
		action	転職修行開始
		arg		nocount
		name	本屋へ転職したい
		info	他の職業の技術経験を全て捨て、本屋に必要な技術を習得します
		okmsg	本屋になれた気がします
		func	_local_1
		param	10,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,book
			use		1	転職のススメ
	@@USE
		time	6h
		action	転職修行開始
		arg		nocount
		name	酪農家へ転職したい
		info	他の職業の技術経験を全て捨て、酪農家に必要な技術を習得します
		okmsg	酪農家になれた気がします
		func	_local_1
		param	25,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,cow
			use		1	転職のススメ
	@@USE
		time	6h
		action	転職修行開始
		arg		nocount
		name	行商人へ転職したい
		info	他の職業の技術経験を全て捨て、行商人に必要な技術を習得します
		okmsg	行商人になれた気がします
		func	_local_1
		param	14,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,peddle
			use		1	転職のススメ
	@@USE
		time	6h
		action	転職修行開始
		arg		nocount
		name	看板を下ろしたい
		info	あなたの肩に重くのしかかっているその看板を下ろします
		func	_local_1
		param	0,,0,_default_
			use		1	転職のススメ

@@ITEM
	no		79
	type	道具
	code	gift
	name	ギフト券
	info	欲しいものを手に入れよう！
	price	10000
	cost	10
	limit	10/0
	scale	枚
	@@USE
		time	1h
		action	引き換え
		name	地図セットと引き換え
		info	いろんな地図の詰め合わせです
		okmsg	ご利用ありがとうございました
			use		2	ギフト券
			get		1	近くの山への地図
			get		1	近くの鉱山への地図
			get		1	剣市への地図
	@@USE
		time	1h
		action	引き換え
		name	入門本セットと引き換え
		info	いろんな本の詰め合わせです
		okmsg	ご利用ありがとうございました
			use		5	ギフト券
			get		1	15
			get		1	16
			get		1	17
	@@USE
		time	1h
		action	引き換え
		name	上級本セットと引き換え
		info	いろんな本の詰め合わせです
		okmsg	ご利用ありがとうございました
			use		10	ギフト券
			get		1	20
			get		1	21
			get		1	22
			get		1	23
	@@USE
		time	1h
		action	引き換え
		name	修行キットと引き換え
		info	己を磨きたい人へ
		okmsg	ご利用ありがとうございました
			use		2	ギフト券
			get		1	修行キット
	@@USE
		time	1h
		action	引き換え
		name	ミノタウロスと引き換え
		info	ミノタウロスを愛する方へ
		okmsg	ご利用ありがとうございました
			use		1	ギフト券
			get		1	25

@@event
	start		10%
	basetime	5h
	plustime	5h
	code		happy
	startmsg	感謝祭がこの街で始まりました。
	endmsg		感謝祭は幕を閉じました。
	info		感謝祭で街はにぎわっています。
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

@@EVENT				#★イベント定義宣言
	start		7%		#★イベント発動確率(1日)
	basetime	12h		#★イベント持続時間ベース
	plustime	24h		#★イベント持続時間ランダム増加。（ランダムで0～24hプラス)
	code		boom-posyon	#★コード（ユニーク）
	startmsg	巷ではちょっとしたポーションブームです	#★イベント発動時メッセージ
	endmsg		ポーションブームが終わったようです		#★イベント終了時メッセージ
	info		ポーション関連商品が人気です			#★イベント発動中メッセージ
		param	薬草			pop/1.5	#★イベント内容（アイテムパラメータ増減指示）
		param	ポーション		pop/1.5	#  書式:アイテム名称,パラメータ名[+-/*]数値
		param	ハイポーション	pop/1.5 #  それぞれのアイテムのパラメータを増減させます。
		param	エーテル		pop/1.5 #  パラメータ名は customize.txt と item.cgi で確認してください。
		param	ハイエーテル	pop/1.5 #  なお、pop==popular,money==price,base==pricebase,half==pricehalf
		param	エリ草			pop/1.5 #  で自動変換されます。
		param	薬草			point*2 #  注意点として、pop 等は値が時間(秒数)なので、
		param	ポーション		point*2 #  売れ行き率を上げたい場合は、値を減少させることになります。
		param	ハイポーション	point*3 #  ちなみにこの例では、薬草系のアイテムの売れ行き率を1.5倍。
		param	エーテル		point*2 #  売却時の人気上昇率を2～4倍に上げています。
		param	ハイエーテル	point*3
		param	エリ草			point*4

@@EVENT
	start		10%
	basetime	6h
	plustime	24h
	code		ken-sale
	startmsg	剣の需要が高まっているようです
	endmsg		剣の需要が通常レベルに戻りました
	info		剣の需要が高まっています
		param	木刀				pop/2
		param	鉄の剣				pop/2
		param	鋼鉄の剣			pop/2
		param	ミスリルの剣		pop/2
		param	オリハルコンの剣	pop/2
@@EVENT
	start		10%
	basetime	6h
	plustime	24h
	code		tate-sale
	startmsg	盾の需要が高まっているようです
	endmsg		盾の需要が通常レベルに戻りました
	info		盾の需要が高まっています
		param	革の盾				pop/2
		param	木の盾				pop/2
		param	鉄の盾				pop/2
		param	鋼鉄の盾			pop/2
		param	ミスリルの盾		pop/2
		param	オリハルコンの盾	pop/2
@@EVENT
	start		10%
	basetime	6h
	plustime	24h
	code		yoroi-sale
	startmsg	鎧の需要が高まっているようです
	endmsg		鎧の需要が通常レベルに戻りました
	info		鎧の需要が高まっています
		param	革の胸当て			pop/2
		param	木の胸当て			pop/2
		param	鉄の鎧				pop/2
		param	鋼鉄の鎧			pop/2
		param	ミスリルの鎧		pop/2
		param	オリハルコンの鎧	pop/2
@@EVENT
	start		10%
	basetime	6h
	plustime	24h
	code		tue-sale
	startmsg	杖の需要が高まっているようです
	endmsg		杖の需要が通常レベルに戻りました
	info		杖の需要が高まっています
		param	木の杖				pop/2
		param	鉄の杖				pop/2
		param	鋼鉄の杖			pop/2
		param	ミスリルの杖		pop/2
		param	オリハルコンの杖	pop/2
@@EVENT
	start		50%		#★発動確率は50%だが、発動は下の「startfunc」次第。
	start		-1		#発動しない
	basetime	12h		#★12hでイベント終了だが、実際終了するかどうかは下の「endfunc」次第。
	plustime	0		#
	code		priceup-yakusou
	startmsg	薬草が不足しています
	endmsg		薬草不足が解消されました
	info		薬草不足で関連商品の価格が高騰しています
	startfunc	stock_le(1,70)		#★イベント発動条件判断の関数呼び出し。（inc-event-function.cgi）
	#endfunc		stock_ge(1,71)		#★イベント終了条件判断の関数呼び出し。（inc-event-function.cgi）
		param	薬草			price*2		#★標準価格が2倍になります。
		param	ポーション		price*1.5
		param	ハイポーション	price*1.5
		param	エーテル		price*1.5
		param	ハイエーテル	price*1.5
		param	エリ草			price*1.5
		param	薬草			pop*2		#★この場合は売れ行き率が1/2に下がります。
		param	ポーション		pop*1.5
		param	ハイポーション	pop*1.5
		param	エーテル		pop*1.5
		param	ハイエーテル	pop*1.5
		param	エリ草			pop*1.5
@@EVENT
	start		50%
	start		-1
	basetime	12h
	plustime	0
	code		priceup-tetu
	startmsg	鉄が不足しています
	endmsg		鉄不足が解消されました
	info		鉄不足で関連商品の価格が高騰しています
	startfunc	stock_le(5,70)
	#endfunc		stock_ge(5,71)
		param	鉄塊			price*2
		param	鉄の剣			price*1.5
		param	鋼鉄の剣		price*1.5
		param	鉄の盾			price*1.5
		param	鋼鉄の盾		price*1.5
		param	鉄の鎧			price*1.5
		param	鋼鉄の鎧		price*1.5
		param	鉄の杖			price*1.5
		param	鋼鉄の杖		price*1.5
		param	鉄塊			pop*2
		param	鉄の剣			pop*1.5
		param	鋼鉄の剣		pop*1.5
		param	鉄の盾			pop*1.5
		param	鋼鉄の盾		pop*1.5
		param	鉄の鎧			pop*1.5
		param	鋼鉄の鎧		pop*1.5
		param	鉄の杖			pop*1.5
		param	鋼鉄の杖		pop*1.5
@@EVENT
	start		50%
	start		-1
	basetime	12h
	plustime	0
	code		priceup-misuriru
	startmsg	ミスリルが不足しています
	endmsg		ミスリル不足が解消されました
	info		ミスリル不足で関連商品の価格が高騰しています
	startfunc	stock_le(6,70)
	#endfunc		stock_ge(6,71)
		param	ミスリル塊			price*2
		param	ミスリルの剣		price*1.5
		param	ミスリルの盾		price*1.5
		param	ミスリルの鎧		price*1.5
		param	ミスリルの杖		price*1.5
		param	ミスリル塊			pop*2
		param	ミスリルの剣		pop*1.5
		param	ミスリルの盾		pop*1.5
		param	ミスリルの鎧		pop*1.5
		param	ミスリルの杖		pop*1.5
@@EVENT
	start		50%
	start		-1
	basetime	12h
	plustime	0
	code		priceup-oriharukon
	startmsg	オリハルコンが不足しています
	endmsg		オリハルコン不足が解消されました
	info		オリハルコン不足で関連商品の価格が高騰しています
	startfunc	stock_le(7,70)
	#endfunc		stock_ge(7,71)
		param	オリハルコン塊			price*2
		param	オリハルコンの剣		price*1.5
		param	オリハルコンの盾		price*1.5
		param	オリハルコンの鎧		price*1.5
		param	オリハルコンの杖		price*1.5
		param	オリハルコン塊			pop*2
		param	オリハルコンの剣		pop*1.5
		param	オリハルコンの盾		pop*1.5
		param	オリハルコンの鎧		pop*1.5
		param	オリハルコンの杖		pop*1.5

@@EVENT
	start		10%
	basetime	48h
	plustime	24h
	code		plusdown-yakusou
	startmsg	薬草栽培業者が薬草の卸を拒否しているようです
	endmsg		薬草栽培業者が薬草の卸を再開しました
	info		市場への薬草供給が止まっています
		param	薬草			plus=-180		#★市場減少
@@EVENT
	start		10%
	basetime	12h
	plustime	12h
	code		plusup-tetu
	startmsg	新たに鉄鉱脈が見つかりました
	endmsg		新しい鉄鉱脈が閉山しました
	info		鉄の流通量が急激に増えています
		param	鉄塊			plus=720		#★市場への入荷ペースが480s。
@@EVENT
	start		7%
	basetime	9h
	plustime	16h
	code		plusup-misuriru
	startmsg	新たにミスリル鉱脈が見つかりました
	endmsg		新しいミスリル鉱脈が閉山しました
	info		ミスリルの流通量が急激に増えています
		param	ミスリル塊			plus=960
@@EVENT
	start		5%
	basetime	6h
	plustime	18h
	code		plusup-oriharukon
	startmsg	新たにオリハルコン鉱脈が見つかりました
	endmsg		新しいオリハルコン鉱脈が閉山しました
	info		オリハルコンの流通量が急激に増えています
		param	オリハルコン塊			plus=1200


# 上位優先で万引きイベント
@@EVENT
	start		100% #old50%
	basetime	0h		#★持続系のイベントではないので時間は0。
	plustime	0h
	code		manbiki
	info		万引き
	startfunc	_local_(400,200)
		#★実はこの関数がイベントの本体になってる
		my($hitproba,$breakproba)=@_;
		#狙われる確率,ロボット破壊確率
		
		foreach my $DT (@DT)
		{
			next if rand(1000)>$hitproba;
			
			if($DT->{item}[@@ITEMNO"店番ロボット"-1])
			{
				return (0,$DT->{shopname}.'へ万引きが入りましたが阻止されました') if rand(1000)>$breakproba;
				
				$DT->{item}[@@ITEMNO"店番ロボット"-1]--;
				return (0,$DT->{shopname}.'へ万引きが入り'.$ITEM[@@ITEMNO"店番ロボット"]->{name}.'が破壊されました');
			}
			
			my $count=0;
			foreach my $idx (0..$DT->{showcasecount}-1)
			{
				my $itemno=$DT->{showcase}[$idx];
				next if !$itemno;
				
				my $cnt=int($DT->{item}[$itemno-1]/10);
				$DT->{item}[$itemno-1]-=$cnt;
				$count+=$cnt*$DT->{price}[$idx];
			}
			return (0,$DT->{shopname}.'が総額'.GetMoneyString($count).'相当の万引き被害に遭いました') if $count;
			return (0,$DT->{shopname}.'に入った万引き犯は何も取らずに逃げました');
		}
		return 0;
	_local_

@@EVENT
	start		20%
	basetime	0h
	plustime	0h
	code		goutou
	info		強盗
	startfunc	_local_(700)
		#★実はこの関数がイベントの本体になってる
		my($hitproba)=@_;
		#狙われる確率
		
		foreach my $DT (@DT)
		{
			next if rand(1000)>$hitproba;
			
			if($DT->{item}[@@ITEMNO"店番ロボット"-1])
			{
				$DT->{item}[@@ITEMNO"店番ロボット"-1]--;
				return (0,$DT->{shopname}.'へ強盗が入り'.$ITEM[@@ITEMNO"店番ロボット"]->{name}.'が破壊されました');
			}
			
			$DT->{rank}-=int($DT->{rank}/5);
			
			my $count=0;
			foreach my $idx (0..$DT->{showcasecount}-1)
			{
				my $itemno=$DT->{showcase}[$idx];
				next if !$itemno;
				
				my $cnt=int($DT->{item}[$itemno-1]/4);
				$DT->{item}[$itemno-1]-=$cnt;
				$count+=$cnt*$DT->{price}[$idx];
			}
			return (0,$DT->{shopname}.'が総額'.GetMoneyString($count).'相当の強盗被害に遭いました') if $count;
			return (0,$DT->{shopname}.'に入った強盗犯は何も取らずに逃げました');
		}
		return 0;
	_local_


# 低資金優先で資金援助イベント
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

# 下位優先で人気アップイベント
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

# 宝くじイベント
@@EVENT
	start		50%
	basetime	0h
	plustime	0h
	code		loto
	info		宝くじ抽選
	startfunc	_local_
		WriteLog(2,0,"宝くじの抽選が行われました");
		foreach my $DT (@DT)
		{
			my $count=$DT->{item}[11-1];
			$DT->{item}[11-1]=0;
			next if !$count;
			
			foreach(1..$count)
			{
				my $rnd=rand(6096454);
				my $hit=0;
				
				$hit=5 if $rnd<152411;
				$hit=4 if $rnd<10000;
				$hit=3 if $rnd<216;
				$hit=2 if $rnd<6;
				$hit=1 if $rnd<1;
				
				if($hit)
				{
					my $getmoney=(0,1000000000,150000000,5000000,100000,10000)[$hit];
					
					$DT->{money}+=$getmoney;
					$DT->{money}=$main::MAX_MONEY if $DT->{money}>$main::MAX_MONEY;
					WriteLog(($hit<=3?1:2),0,$DT->{shopname}."が$hit等".GetMoneyString($getmoney)."を当てました！");
				}
			}
		}
		return 0;
	_local_

@@FUNCINIT
#目利きの真髄を持っている場合、買い物に必要な時間を3/4にする。
$TIME_SEND_ITEM=int($TIME_SEND_ITEM/4*3) if $DT->{item}[@@ITEMNO"目利きの真髄"-1];

#職業が「行商人」の場合、買い物に必要な時間を1/2にする。
$TIME_SEND_ITEM=int($TIME_SEND_ITEM/2) if $DT->{job} eq 'peddle';

@@FUNCITEM
######################################################################
# ★本or地図がボロボロになって破棄するという処理
######################################################################
sub lostbook
{
	my $itemno=$USE->{itemno};
	if(rand(1000)<$USE->{param1})
	{
		UseItem($itemno,1,$ITEM[$itemno]->{name}.'が読めない程ボロボロになりましたので破棄しました');
	}
	return "";
}
######################################################################
# ★人気アップ(汎用)
#   param1 アップポイント
#   param2 最近の出来事用コメント 表示方式:●●商店がparam2
######################################################################
sub popup
{
	my $up=int($USE->{param1}*(2-$DT->{rank}/5000));
	$DT->{rank}+=$up;
	$DT->{rank}=10000 if $DT->{rank}>10000;
	
	my $ret=$USE->{param2}."：人気".int($up/100)."%アップ";
	WriteLog(0,$DT->{id},$ret);
	WriteLog(3,0,$DT->{shopname}."が".$USE->{param2});
	
	return $ret;
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
				['ギフト券',	[[@@ITEMNO "ギフト券", 5],			],],
				['ギフト券',	[[@@ITEMNO "ギフト券", 4],			],],
				['ギフト券',	[[@@ITEMNO "ギフト券", 3],			],],
				['ギフト券',	[[@@ITEMNO "ギフト券", 2],			],],
				['ギフト券',	[[@@ITEMNO "ギフト券", 1],			],],
				['ロボット',	[[@@ITEMNO "店番ロボット", 1],		],],
				['お祝いグッズ',[[@@ITEMNO "七面鳥の丸焼き", 1],	],],
				['お祝いグッズ',[[@@ITEMNO "こだわりのラム酒", 1],	],],
				['お祝いグッズ',[[@@ITEMNO "おしゃれブーツ", 1],	],],
			],
			[
				['ギフト券',	[[@@ITEMNO "ギフト券", 3],			],],
				['ギフト券',	[[@@ITEMNO "ギフト券", 3],			],],
				['ギフト券',	[[@@ITEMNO "ギフト券", 2],			],],
				['ギフト券',	[[@@ITEMNO "ギフト券", 2],			],],
				['ギフト券',	[[@@ITEMNO "ギフト券", 1],			],],
				['禁断の書',	[[@@ITEMNO "禁断の書", 1],			],],
				['お祝いグッズ',[[@@ITEMNO "七面鳥の丸焼き", 1],	],],
				['お祝いグッズ',[[@@ITEMNO "こだわりのラム酒", 1],	],],
				['お祝いグッズ',[[@@ITEMNO "おしゃれブーツ", 1],	],],
			],
			[
				['ギフト券',	[[@@ITEMNO "ギフト券", 2],			],],
				['ギフト券',	[[@@ITEMNO "ギフト券", 2],			],],
				['ギフト券',	[[@@ITEMNO "ギフト券", 2],			],],
				['ギフト券',	[[@@ITEMNO "ギフト券", 1],			],],
				['ギフト券',	[[@@ITEMNO "ギフト券", 1],			],],
				['広告パック',	[[@@ITEMNO "広告パック", 1],		],],
				['お祝いグッズ',[[@@ITEMNO "七面鳥の丸焼き", 1],	],],
				['お祝いグッズ',[[@@ITEMNO "こだわりのラム酒", 1],	],],
				['お祝いグッズ',[[@@ITEMNO "おしゃれブーツ", 1],	],],
			],
			[
				['ギフト券',	[[@@ITEMNO "ギフト券", 2],			],],
				['ギフト券',	[[@@ITEMNO "ギフト券", 1],			],],
				['ギフト券',	[[@@ITEMNO "ギフト券", 1],			],],
				['広告パック',	[[@@ITEMNO "広告パック", 1],		],],
				['広告パック',	[[@@ITEMNO "広告パック", 1],		],],
				['広告パック',	[[@@ITEMNO "広告パック", 1],		],],
				['お祝いグッズ',[[@@ITEMNO "七面鳥の丸焼き", 1],	],],
				['お祝いグッズ',[[@@ITEMNO "こだわりのラム酒", 1],	],],
				['お祝いグッズ',[[@@ITEMNO "おしゃれブーツ", 1],	],],
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
		foreach my $DT (@DT)
		{
			my $expsum=0;
			foreach(values(%{$DT->{exp}}))
			{
				$expsum+=$_;
			}
			#$expsum=5000 if $expsum>5000;
			
			next if $expsum<=4000;
			$expsum-=4000;
			
			foreach my $itemno (@@ITEMNO"鍛冶屋の技術",@@ITEMNO"魔法の知識",@@ITEMNO"解体屋の魂",@@ITEMNO"目利きの真髄")
			{
				if($DT->{item}[$itemno-1] && rand(14000)<$expsum)
				{
					my $msg="初心を忘れ、".$DT->{shopname}."さんの".$ITEM[$itemno]->{name}."が失われました";
					WriteLog(2,0,0,$msg,1);
					WriteLog(0,$DT->{id},0,$ITEM[$itemno]->{name}."を失いました",1);
					$DT->{item}[$itemno-1]--;
				}
			}
		}
	}
}

@@FUNCNEW

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

# $DEFINE_FUNCNEW_NOLOG=1 を設定すると、システム側の最近の出来事新装開店メッセージを抑制します。
# $DEFINE_FUNCNEW_NOLOG=1;
# WriteLog(1,0,0,$DT->{shopname}."がエントリーしました",1);

# その他、新装開店時に独自の処理を追加できます。

@@FUNCSHOPIN

SetUserDataEx($DT,'_so_move_in',$NOW_TIME); # 移転時刻を記録
if($DT->{job} eq 'peddle')
{
	# 行商人(peddle)には移転消費時間の1/2を返還
	$DT->{_MoveTownTime}=int($DT->{_MoveTownTime}/2);
	EditTime($DT,$DT->{_MoveTownTime});
	WriteLog(0,$DT->{id},0,'移転時間が半分の'.GetTime2HMS($DT->{_MoveTownTime}).'で済んだようです',1);
}
if(GetUserDataEx($DT,'_so_present_money'))
{
	WriteLog(0,$DT->{id},0,'移転元の街から餞別として'.GetMoneyString(GetUserDataEx($DT,'_so_present_money')).'をもらいました',1);
	SetUserDataEx($DT,'_so_present_money','');
}

@@FUNCSHOPOUT

if(GetUserDataEx($DT,'_so_move_in'))
{
	my $present_money=int(($NOW_TIME-GetUserDataEx($DT,'_so_move_in'))/86400)*5000;
	EditMoney($DT,$present_money); # 滞在期間1日に付き\5000を餞別として資金へ
	SetUserDataEx($DT,'_so_present_money',$present_money);
	SetUserDataEx($DT,'_so_move_in',''); # $DT->{user}{_so_move_in} を削除
}

@@FUNCBUY
# package item です。
# 
# $item::BUY を利用できます。$item::BUY の構造はマニュアルの @@ITEM funcb をご覧ください。
# 商品毎の処理は @@ITEM funcb を利用してください。

if($BUY->{whole})
{
	# 市場からの仕入の場合、\500000に付き1枚のギフト券を進呈する。
	my $price=$BUY->{num}*$BUY->{price};
	my $count=int $price/500000;
	
	$count=AddItemSub(@@ITEMNO"ギフト券",$count,$BUY->{dt}) if $count;
	WriteLog(0,$BUY->{dt}{id},'市場からギフト券を'.$count.'枚もらいました') if $count;
}

@@END #定義終了宣言(以降コメント扱い)

------------
●簡単な説明
------------

全ての商品/イベントはこのファイルを変換し作成されます。

このファイルをカスタマイズすることで、まったく違う世界の SOLD OUT をも
作ることが出来ます。それこそ、ゲームの方向性をも変えることが出来るはず
です。（例えば、モンスター合成ゲームとか、貿易ゲームとか）

そういう個性的なカスタマイズが出てきたら面白いだろうし嬉しいなあと思い、
スクリプトのフリー公開とカスタマイズ方法を用意した次第です。

この標準アイテムデータは、サンプルという意味合いが強いです。とは言って
もバランス調整は1年にわたって行っていますのでそれなりに遊べるレベルだと
思いますが、システムのポテンシャルを十分に引き出しているとは言えないか
もしれません。

ですので、是非、カスタマイズしてみてください。単純に商品名を変えるだけ
でも面白いですが、独自の商品/開発方法/イベントを追加することも比較的簡
単に出来ます。挑戦してみてください。

商品データの更新は、本ファイルを変更してアップロード後、管理メニューで
「商品データ生成/更新」を行うことで可能です。その際、エラーなどがあれば
表示されます。

データ定義の書式は、説明書の中のカスタマイズドキュメントと実際にこのファ
イルを参照し、研究してみてください。特に、このファイルはサンプルになる
と思います。

プログラム読める人は makeitem.cgi を解析してみてください。商品データを
編集するにあたって不便な点は makeitem.cgi を改造すると楽になるかもしれ
ません。

なお、SOLD OUT はこれからも進化させていくつもりです。その際、定義データ
の互換性が損なわれる可能性があります。もちろん、そのようなことが起こら
ないように努めますが、そういう可能性があるということをご了承下さい。

追伸

カスタマイズに興味を持ってくれるみなさんのおかげで、いろんなタイプの
SOLD OUT を目にするようになりました。大変嬉しく思っています。ありがとう
ございます。
