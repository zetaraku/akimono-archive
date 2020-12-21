# ワールドアトラス版アイテムデータ 2005/01/20 由來

# このファイルはアイテムデータの定義ファイルです。
# 好きなようにカスタマイズできます。詳細はマニュアルをご覧ください。

@@DEFINE
	version	05-01-20(WA)		#★商品データバージョン表記
					# 最後の「WA」はワールドアトラス版であることを示します。
					# もしあなたが独自アイテムを目玉にした商人物語を作るなら，
					# この記号を変えるのがよいでしょう。

	scale	個			#★デフォルトの数え単位
	type0	全			#全アイテムの集合
	type1	素材
	type2	食品
	type3	調味
	type4	織物
	type5	工芸
	type6	船舶
	type7	船団
	type8	航海
	type9	道具
	
	job	shipb		造船屋		#★職業コードは英小文字10文字以内
	job	pirate		海賊
	job	pros		海軍司令
	job	explore		探検家
	job	trader		貿易商

	MaxMoney	999999999	#★最大資金
	
	set NewShopMoney	200000					#初期資金 (@@FUNCNEWにて使用)
	set NewShopTime		14*60*60				#初期持時間(秒) (@@FUNCNEWにて使用)
	set NewShopItem		陳列棚増築取壊キット:1:ギフト券:10	#初期所持商品 (@@FUNCNEWにて使用) 書式 商品名:個数:商品名:個数:...
	
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


@@ITEM
	no		18
	type	航海
	code	bread
	name	パン
	info	航海の必需品
	price	100
	limit	1000/1000
	pop	20m
	plus	20m
	base	100/100000
	scale	食
	cost	20
	point	5%
@@ITEM
	no		19
	type	航海
	code	lamb
	name	ラム酒
	info	航海の必需品
	price	200
	limit	500/500
	pop	40m
	plus	20m
	base	100/50000
	scale	樽
	cost	20
	point	10%

@@ITEM
	no		20
	type	航海
	code	seaman
	name	水夫
	info	船を動かす人手
	price	1200
	limit	800/800
	pop	1d
	plus	20m
	base	10000/100000
	scale	人
	flag	noshowcase|human|norequest

@@ITEM
	no		1
	type	道具
	code	book-bd
	name	造船指南の書
	info	造船の方法を解説した指南書
	price	10000
	limit	1/0.1
	pop	1d
	plus	2h
	scale	冊
	flag	noshowcase
	@@use
		time	120m
		exp		2%
		exptime	40m
		job		造船屋	times/1.5
		scale	回
		action	製造する
		name	バルカを製造する
		info	バルカを製造します
		okmsg	バルカを製造しました
			use		1	木材
			use		1	帆布
			get		1	バルカ
	@@use
		time	3h
		exp		2%
		exptime	1h
		scale	回
		action	製造する
		name	コッグを製造する
		info	コッグを製造します
		okmsg	コッグを製造しました
		ngmsg	製造に失敗しました…
			needjob	造船屋
			needexp	10%
			use		1	木材
			use		1	帆布
			get		1	コッグ	90%
	@@use
		time	6h
		exp		4%
		exptime	2h
		scale	回
		action	製造する
		name	ガレーを製造する
		info	ガレーを製造します
		okmsg	ガレーを製造しました
		ngmsg	製造に失敗しました…
			needjob	造船屋
			needexp	30%
			use		3	木材
			use		1	帆布
			get		1	ガレー	90%
	@@use
		time	12h
		exp		4%
		exptime	4h
		scale	回
		action	製造する
		name	カラベルを製造する
		info	カラベルを製造します
		okmsg	カラベルを製造しました
		ngmsg	製造に失敗しました…
			needjob	造船屋
			needexp	30%
			use		5	木材
			use		3	帆布
			get		1	カラベル	90%
	@@use
		time	24h
		exp		8%
		exptime	8h
		scale	回
		action	製造する
		name	キャラックを製造する
		info	キャラックを製造します
		okmsg	キャラックを製造しました
		ngmsg	製造に失敗しました…
			needjob	造船屋
			needexp	50%
			use		10	木材
			use		6	帆布
			get		1	キャラック	90%
	@@use
		time	24h
		exp		8%
		exptime	8h
		scale	回
		action	製造する
		name	ガレオンを製造する
		info	ガレオンを製造します
		okmsg	ガレオンを製造しました
		ngmsg	製造に失敗しました…
			needjob	造船屋
			needexp	50%
			use		10	木材
			use		6	帆布
			get		1	ガレオン	90%
	@@use
		time	36h
		exp		10%
		exptime	12h
		scale	回
		action	製造する
		name	ガレアスを製造する
		info	ガレアスを製造します
		okmsg	ガレアスを製造しました
		ngmsg	製造に失敗しました…
			needjob	造船屋
			needexp	60%
			use		18	木材
			use		7	帆布
			get		1	ガレアス	90%

@@ITEM
	no		26
	type	船団
	code	convoy-aa
	name	第一探検船団
	info	探検向け船団
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	欧州の探検に派遣する
		info	欧州に対する海域適性
		param	26,1
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	アフリカの探検に派遣する
		info	アフリカに対する海域適性
		param	26,2
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	中近東の探検に派遣する
		info	中近東に対する海域適性
		param	26,3
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	インドの探検に派遣する
		info	インドに対する海域適性
		param	26,4
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	アジアの探検に派遣する
		info	アジアに対する海域適性
		param	26,5
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	新大陸の探検に派遣する
		info	新大陸に対する海域適性
		param	26,6
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	20m
		exp		0
		scale	回
		action	出迎える
		name	探検船団を出迎える
		info	船団が帰ってきているか港を確認します
		param	26
		funcb	onlyexp
		func	meetexp
		arg	nocount
@@ITEM
	no		27
	type	船団
	code	convoy-ab
	name	第二探検船団
	info	探検向け船団
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	欧州の探検に派遣する
		info	欧州に対する海域適性
		param	27,1
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	アフリカの探検に派遣する
		info	アフリカに対する海域適性
		param	27,2
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	中近東の探検に派遣する
		info	中近東に対する海域適性
		param	27,3
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	インドの探検に派遣する
		info	インドに対する海域適性
		param	27,4
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	アジアの探検に派遣する
		info	アジアに対する海域適性
		param	27,5
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	新大陸の探検に派遣する
		info	新大陸に対する海域適性
		param	27,6
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	20m
		exp		0
		scale	回
		action	出迎える
		name	探検船団を出迎える
		info	船団が帰ってきているか港を確認します
		param	27
		funcb	onlyexp
		func	meetexp
		arg	nocount
@@ITEM
	no		28
	type	船団
	code	convoy-ac
	name	第三探検船団
	info	探検向け船団
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	欧州の探検に派遣する
		info	欧州に対する海域適性
		param	28,1
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	アフリカの探検に派遣する
		info	アフリカに対する海域適性
		param	28,2
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	中近東の探検に派遣する
		info	中近東に対する海域適性
		param	28,3
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	インドの探検に派遣する
		info	インドに対する海域適性
		param	28,4
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	アジアの探検に派遣する
		info	アジアに対する海域適性
		param	28,5
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	新大陸の探検に派遣する
		info	新大陸に対する海域適性
		param	28,6
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	20m
		exp		0
		scale	回
		action	出迎える
		name	探検船団を出迎える
		info	船団が帰ってきているか港を確認します
		param	28
		funcb	onlyexp
		func	meetexp
		arg	nocount
@@ITEM
	no		29
	type	船団
	code	convoy-ad
	name	第四探検船団
	info	探検向け船団
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	欧州の探検に派遣する
		info	欧州に対する海域適性
		param	29,1
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	アフリカの探検に派遣する
		info	アフリカに対する海域適性
		param	29,2
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	中近東の探検に派遣する
		info	中近東に対する海域適性
		param	29,3
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	インドの探検に派遣する
		info	インドに対する海域適性
		param	29,4
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	アジアの探検に派遣する
		info	アジアに対する海域適性
		param	29,5
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	新大陸の探検に派遣する
		info	新大陸に対する海域適性
		param	29,6
		funcb	beforeexp
		func	exploring
		arg	nocount
	@@use
		time	20m
		exp		0
		scale	回
		action	出迎える
		name	探検船団を出迎える
		info	船団が帰ってきているか港を確認します
		param	29
		funcb	onlyexp
		func	meetexp
		arg	nocount

@@ITEM
	no		30
	type	船団
	code	convoy-ba
	name	第一貿易船団
	info	貿易向け船団
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	12h
		exp		10%
		scale	回
		action	に派遣する
		name	欧州の貿易に派遣する
		info	欧州に対する海域適性
		param	30,1
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	に派遣する
		name	アフリカの貿易に派遣する
		info	アフリカに対する海域適性
		param	30,2
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	に派遣する
		name	中近東の貿易に派遣する
		info	中近東に対する海域適性
		param	30,3
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	に派遣する
		name	インドの貿易に派遣する
		info	インドに対する海域適性
		param	30,4
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	に派遣する
		name	アジアの貿易に派遣する
		info	アジアに対する海域適性
		param	30,5
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	に派遣する
		name	新大陸の貿易に派遣する
		info	新大陸に対する海域適性
		param	30,6
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	20m
		exp		0
		scale	回
		action	出迎える
		name	貿易船団を出迎える
		info	船団が帰ってきているか港を確認します
		param	30
		funcb	onlyexp
		func	meetrtp
		arg	nocount
@@ITEM
	no		31
	type	船団
	code	convoy-bb
	name	第二貿易船団
	info	貿易向け船団
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	12h
		exp		10%
		scale	回
		action	に派遣する
		name	欧州の貿易に派遣する
		info	欧州に対する海域適性
		param	31,1
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	に派遣する
		name	アフリカの貿易に派遣する
		info	アフリカに対する海域適性
		param	31,2
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	に派遣する
		name	中近東の貿易に派遣する
		info	中近東に対する海域適性
		param	31,3
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	に派遣する
		name	インドの貿易に派遣する
		info	インドに対する海域適性
		param	31,4
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	に派遣する
		name	アジアの貿易に派遣する
		info	アジアに対する海域適性
		param	31,5
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	に派遣する
		name	新大陸の貿易に派遣する
		info	新大陸に対する海域適性
		param	31,6
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	20m
		exp		0
		scale	回
		action	出迎える
		name	貿易船団を出迎える
		info	船団が帰ってきているか港を確認します
		param	31
		funcb	onlyexp
		func	meetrtp
		arg	nocount
@@ITEM
	no		32
	type	船団
	code	convoy-bc
	name	第三貿易船団
	info	貿易向け船団
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	12h
		exp		10%
		scale	回
		action	に派遣する
		name	欧州の貿易に派遣する
		info	欧州に対する海域適性
		param	32,1
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	に派遣する
		name	アフリカの貿易に派遣する
		info	アフリカに対する海域適性
		param	32,2
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	に派遣する
		name	中近東の貿易に派遣する
		info	中近東に対する海域適性
		param	32,3
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	に派遣する
		name	インドの貿易に派遣する
		info	インドに対する海域適性
		param	32,4
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	に派遣する
		name	アジアの貿易に派遣する
		info	アジアに対する海域適性
		param	32,5
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	に派遣する
		name	新大陸の貿易に派遣する
		info	新大陸に対する海域適性
		param	32,6
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	20m
		exp		0
		scale	回
		action	出迎える
		name	貿易船団を出迎える
		info	船団が帰ってきているか港を確認します
		param	32
		funcb	onlyexp
		func	meetrtp
		arg	nocount
@@ITEM
	no		33
	type	船団
	code	convoy-bd
	name	第四貿易船団
	info	貿易向け船団
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	12h
		exp		10%
		scale	回
		action	に派遣する
		name	欧州の貿易に派遣する
		info	欧州に対する海域適性
		param	33,1
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	に派遣する
		name	アフリカの貿易に派遣する
		info	アフリカに対する海域適性
		param	33,2
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	に派遣する
		name	中近東の貿易に派遣する
		info	中近東に対する海域適性
		param	33,3
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	に派遣する
		name	インドの貿易に派遣する
		info	インドに対する海域適性
		param	33,4
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	に派遣する
		name	アジアの貿易に派遣する
		info	アジアに対する海域適性
		param	33,5
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	12h
		exp		10%
		scale	回
		action	に派遣する
		name	新大陸の貿易に派遣する
		info	新大陸に対する海域適性
		param	33,6
		funcb	routesel
		func	route
		arg	nocount|select
	@@use
		time	20m
		exp		0
		scale	回
		action	出迎える
		name	貿易船団を出迎える
		info	船団が帰ってきているか港を確認します
		param	33
		funcb	onlyexp
		func	meetrtp
		arg	nocount

@@ITEM
	no		34
	type	船団
	code	convoy-ca
	name	第一武装艦隊
	info	戦闘向け艦隊
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	欧州へ
		info	欧州に対する海域適性
		param	34,1
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	アフリカへ
		info	アフリカに対する海域適性
		param	34,2
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	中近東へ
		info	中近東に対する海域適性
		param	34,3
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	インドへ
		info	イントに対する海域適性
		param	34,4
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	アジアへ
		info	アジアに対する海域適性
		param	34,5
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	新大陸へ
		info	新大陸に対する海域適性
		param	34,6
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	20m
		exp		0
		scale	回
		action	出迎える
		name	武装艦隊を出迎える
		info	艦隊が帰ってきているか港を確認します
		param	34
		funcb	onlyexp
		func	meetpp
		arg	nocount
@@ITEM
	no		35
	type	船団
	code	convoy-cb
	name	第二武装艦隊
	info	戦闘向け艦隊
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	欧州へ
		info	欧州に対する海域適性
		param	35,1
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	アフリカへ
		info	アフリカに対する海域適性
		param	35,2
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	中近東へ
		info	中近東に対する海域適性
		param	35,3
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	インドへ
		info	イントに対する海域適性
		param	35,4
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	アジアへ
		info	アジアに対する海域適性
		param	35,5
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	新大陸へ
		info	新大陸に対する海域適性
		param	35,6
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	20m
		exp		0
		scale	回
		action	出迎える
		name	武装艦隊を出迎える
		info	艦隊が帰ってきているか港を確認します
		param	35
		funcb	onlyexp
		func	meetpp
		arg	nocount
@@ITEM
	no		36
	type	船団
	code	convoy-cc
	name	第三武装艦隊
	info	戦闘向け艦隊
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	欧州へ
		info	欧州に対する海域適性
		param	36,1
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	アフリカへ
		info	アフリカに対する海域適性
		param	36,2
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	中近東へ
		info	中近東に対する海域適性
		param	36,3
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	インドへ
		info	イントに対する海域適性
		param	36,4
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	アジアへ
		info	アジアに対する海域適性
		param	36,5
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	新大陸へ
		info	新大陸に対する海域適性
		param	36,6
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	20m
		exp		0
		scale	回
		action	出迎える
		name	武装艦隊を出迎える
		info	艦隊が帰ってきているか港を確認します
		param	36
		funcb	onlyexp
		func	meetpp
		arg	nocount
@@ITEM
	no		37
	type	船団
	code	convoy-cd
	name	第四武装艦隊
	info	戦闘向け艦隊
	price	0
	limit	1
	plus	-10m
	pop	0
	scale	個隊
	flag	noshowcase|notrash|norequest
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	欧州へ
		info	欧州に対する海域適性
		param	37,1
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	アフリカへ
		info	アフリカに対する海域適性
		param	37,2
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	中近東へ
		info	中近東に対する海域適性
		param	37,3
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	インドへ
		info	イントに対する海域適性
		param	37,4
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	アジアへ
		info	アジアに対する海域適性
		param	37,5
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	16h
		exp		10%
		scale	回
		action	派遣する
		name	新大陸へ
		info	新大陸に対する海域適性
		param	37,6
		funcb	nowpp
		func	attack
		arg	nocount
	@@use
		time	20m
		exp		0
		scale	回
		action	出迎える
		name	武装艦隊を出迎える
		info	艦隊が帰ってきているか港を確認します
		param	37
		funcb	onlyexp
		func	meetpp
		arg	nocount

@@ITEM
	no		39
	type	航海
	code	discover-a
	name	発見報告書（欧州）
	info	探検で発見した珍しい物
	price	0
	limit	3
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@use
		time	2h
		scale	回
		action	届け出る
		name	王国に届け出る
		info	発見物を王国に届け出ます
		func	disc
		param	1
		arg	nocount
			use		1	発見報告書（欧州）
@@ITEM
	no		40
	type	航海
	code	discover-b
	name	発見報告書（アフリカ）
	info	探検で発見した珍しい物
	price	0
	limit	3
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@use
		time	2h
		scale	回
		action	届け出る
		name	王国に届け出る
		info	発見物を王国に届け出ます
		func	disc
		param	2
		arg	nocount
			use		1	発見報告書（アフリカ）
@@ITEM
	no		41
	type	航海
	code	discover-c
	name	発見報告書（中近東）
	info	探検で発見した珍しい物
	price	0
	limit	3
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@use
		time	2h
		scale	回
		action	届け出る
		name	王国に届け出る
		info	発見物を王国に届け出ます
		func	disc
		param	3
		arg	nocount
			use		1	発見報告書（中近東）
@@ITEM
	no		42
	type	航海
	code	discover-d
	name	発見報告書（インド）
	info	探検で発見した珍しい物
	price	0
	limit	3
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@use
		time	2h
		scale	回
		action	届け出る
		name	王国に届け出る
		info	発見物を王国に届け出ます
		func	disc
		param	4
		arg	nocount
			use		1	発見報告書（インド）
@@ITEM
	no		43
	type	航海
	code	discover-e
	name	発見報告書（アジア）
	info	探検で発見した珍しい物
	price	0
	limit	3
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@use
		time	2h
		scale	回
		action	届け出る
		name	王国に届け出る
		info	発見物を王国に届け出ます
		func	disc
		param	5
		arg	nocount
			use		1	発見報告書（アジア）
@@ITEM
	no		44
	type	航海
	code	discover-f
	name	発見報告書（新大陸）
	info	探検で発見した珍しい物
	price	0
	limit	3
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@use
		time	2h
		scale	回
		action	届け出る
		name	王国に届け出る
		info	発見物を王国に届け出ます
		func	disc
		param	6
		arg	nocount
			use		1	発見報告書（新大陸）

@@ITEM
	no		45
	type	航海
	code	town-a
	name	新都市の地図（欧州）
	info	探検で発見した貿易都市
	price	0
	limit	1
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@USE
		time	2h
		arg	nocount|message18
		argmessage	都市の名前
		scale	回
		action	と名付けて建設
		name	商館を建設する
		info	都市を命名して貿易ができるようにします
		param	1
		func	newtown
			use		1	新都市の地図（欧州）
@@ITEM
	no		46
	type	航海
	code	town-b
	name	新都市の地図（アフリカ）
	info	探検で発見した貿易都市
	price	0
	limit	1
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@USE
		time	2h
		arg	nocount|message18
		argmessage	都市の名前
		scale	回
		action	と名付けて建設
		name	商館を建設する
		info	都市を命名して貿易ができるようにします
		param	2
		func	newtown
			use		1	新都市の地図（アフリカ）
@@ITEM
	no		47
	type	航海
	code	town-c
	name	新都市の地図（中近東）
	info	探検で発見した貿易都市
	price	0
	limit	1
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@USE
		time	2h
		arg	nocount|message18
		argmessage	都市の名前
		scale	回
		action	と名付けて建設
		name	商館を建設する
		info	都市を命名して貿易ができるようにします
		param	3
		func	newtown
			use		1	新都市の地図（中近東）
@@ITEM
	no		48
	type	航海
	code	town-d
	name	新都市の地図（インド）
	info	探検で発見した貿易都市
	price	0
	limit	1
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@USE
		time	2h
		arg	nocount|message18
		argmessage	都市の名前
		scale	回
		action	と名付けて建設
		name	商館を建設する
		info	都市を命名して貿易ができるようにします
		param	4
		func	newtown
			use		1	新都市の地図（インド）
@@ITEM
	no		49
	type	航海
	code	town-e
	name	新都市の地図（アジア）
	info	探検で発見した貿易都市
	price	0
	limit	1
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@USE
		time	2h
		arg	nocount|message18
		argmessage	都市の名前
		scale	回
		action	と名付けて建設
		name	商館を建設する
		info	都市を命名して貿易ができるようにします
		param	5
		func	newtown
			use		1	新都市の地図（アジア）
@@ITEM
	no		50
	type	航海
	code	town-f
	name	新都市の地図（新大陸）
	info	探検で発見した貿易都市
	price	0
	limit	1
	plus	-1h
	pop	0
	scale	通
	flag	noshowcase|norequest
	@@USE
		time	2h
		arg	nocount|message18
		argmessage	都市の名前
		scale	回
		action	と名付けて建設
		name	商館を建設する
		info	都市を命名して貿易ができるようにします
		param	6
		func	newtown
			use		1	新都市の地図（新大陸）

@@ITEM
	no		51
	type	工芸
	code	coin
	name	金貨
	info	王国発行の金貨。販売して換金
	price	10000
	limit	500
	base	10/20
	plus	-1h
	pop	2h
	scale	枚
	point	75%
@@ITEM
	no		52
	type	食品
	code	wine
	name	ワイン
	info	欧州特産の食品
	price	10000
	limit	100
	base	10/20
	plus	-1h
	pop	16h
	scale	樽
	point	300%
@@ITEM
	no		53
	type	食品
	code	cheese
	name	チーズ
	info	欧州特産の食品
	price	2000
	limit	500
	base	10/20
	plus	-1h
	pop	3h
	scale	樽
	point	60%
@@ITEM
	no		54
	type	調味
	code	olive
	name	オリーブ油
	info	欧州特産の調味料
	price	1000
	limit	1000
	base	10/20
	plus	-1h
	pop	90m
	scale	樽
	point	30%
@@ITEM
	no		55
	type	織物
	code	woolen
	name	毛織物
	info	欧州特産の織物
	price	5000
	limit	200
	base	10/20
	plus	-1h
	pop	8h
	scale	箱
	point	150%
@@ITEM
	no		56
	type	工芸
	code	stained
	name	ステンドグラス
	info	欧州特産の工芸品
	price	8000
	limit	120
	base	10/20
	plus	-1h
	pop	12h
	scale	箱
	point	200%
@@ITEM
	no		57
	type	工芸
	code	sculpture
	name	彫刻
	info	欧州特産の工芸品
	price	4000
	limit	250
	base	10/20
	plus	-1h
	pop	6h
	scale	箱
	point	120%
@@ITEM
	no		58
	type	工芸
	code	gun
	name	鉄砲
	info	欧州特産の工芸品
	price	3000
	limit	300
	base	10/20
	plus	-1h
	pop	5h
	scale	箱
	point	80%

@@ITEM
	no		59
	type	素材
	code	gold
	name	金
	info	アフリカ特産の素材
	price	5000
	limit	200
	base	10/20
	plus	-1h
	pop	10h
	scale	箱
	point	300%
@@ITEM
	no		60
	type	素材
	code	diamond
	name	ダイヤモンド
	info	アフリカ特産の素材
	price	10000
	limit	100
	base	10/20
	plus	-1h
	pop	20h
	scale	箱
	point	600%
@@ITEM
	no		61
	type	素材
	code	coral
	name	珊瑚
	info	アフリカ特産の素材
	price	2500
	limit	400
	base	10/20
	plus	-1h
	pop	5h
	scale	箱
	point	140%
@@ITEM
	no		62
	type	素材
	code	ivory
	name	象牙
	info	アフリカ特産の素材
	price	1000
	limit	1000
	base	10/20
	plus	-1h
	pop	2h
	scale	箱
	point	50%
@@ITEM
	no		63
	type	食品
	code	coffee
	name	コーヒー
	info	アフリカ特産の食品
	price	500
	limit	2000
	base	10/20
	plus	-1h
	pop	1h
	scale	箱
	point	40%
@@ITEM
	no		64
	type	調味
	code	salt
	name	塩
	info	アフリカ特産の調味料
	price	400
	limit	2500
	base	10/20
	plus	-1h
	pop	40m
	scale	箱
	point	15%
@@ITEM
	no		65
	type	調味
	code	tamarindo
	name	タマリンド
	info	アフリカ特産の調味料
	price	500
	limit	2000
	base	10/20
	plus	-1h
	pop	1h
	scale	箱
	point	30%

@@ITEM
	no		66
	type	素材
	code	ironore
	name	鉄鉱石
	info	中近東特産の素材
	price	1000
	limit	1000
	base	10/20
	plus	-1h
	pop	2h
	scale	箱
	point	50%
@@ITEM
	no		67
	type	素材
	code	sulfur
	name	硫黄
	info	中近東特産の素材
	price	1000
	limit	1000
	base	10/20
	plus	-1h
	pop	2h
	scale	箱
	point	50%
@@ITEM
	no		68
	type	食品
	code	honey
	name	蜂蜜
	info	中近東特産の食品
	price	500
	limit	2000
	base	10/20
	plus	-1h
	pop	1h
	scale	箱
	point	25%
@@ITEM
	no		69
	type	調味
	code	sugar
	name	砂糖
	info	中近東特産の調味料
	price	500
	limit	2000
	base	10/20
	plus	-1h
	pop	1h
	scale	箱
	point	25%
@@ITEM
	no		70
	type	織物
	code	carpet
	name	絨毯
	info	中近東特産の織物
	price	2500
	limit	400
	base	10/20
	plus	-1h
	pop	5h
	scale	箱
	point	180%
@@ITEM
	no		71
	type	織物
	code	hemptext
	name	麻織物
	info	中近東特産の織物
	price	2000
	limit	500
	base	10/20
	plus	-1h
	pop	4h
	scale	箱
	point	120%
@@ITEM
	no		72
	type	工芸
	code	bicornis
	name	犀角
	info	中近東特産の工芸品
	price	2000
	limit	500
	base	10/20
	plus	-1h
	pop	4h
	scale	箱
	point	100%

@@ITEM
	no		73
	type	素材
	code	saltpeter
	name	硝石
	info	インド特産の素材
	price	1000
	limit	1000
	base	10/20
	plus	-1h
	pop	2h
	scale	箱
	point	50%
@@ITEM
	no		74
	type	素材
	code	sapphire
	name	サファイア
	info	インド特産の素材
	price	5000
	limit	200
	base	10/20
	plus	-1h
	pop	10h
	scale	箱
	point	300%
@@ITEM
	no		75
	type	調味
	code	pepper
	name	胡椒
	info	インド特産の調味料
	price	2500
	limit	400
	base	10/20
	plus	-1h
	pop	200m
	scale	箱
	point	150%
@@ITEM
	no		76
	type	調味
	code	cinnamon
	name	シナモン
	info	インド特産の調味料
	price	500
	limit	2000
	base	10/20
	plus	-1h
	pop	1h
	scale	箱
	point	25%
@@ITEM
	no		77
	type	織物
	code	cottonfab
	name	綿織物
	info	インド特産の織物
	price	1000
	limit	1000
	base	10/20
	plus	-1h
	pop	2h
	scale	箱
	point	50%
@@ITEM
	no		78
	type	織物
	code	printing
	name	更紗
	info	インド特産の織物
	price	2000
	limit	500
	base	10/20
	plus	-1h
	pop	4h
	scale	箱
	point	100%
@@ITEM
	no		79
	type	工芸
	code	tortoiseshell
	name	鼈甲
	info	インド特産の工芸品
	price	2000
	limit	500
	base	10/20
	plus	-1h
	pop	4h
	scale	箱
	point	100%

@@ITEM
	no		80
	type	素材
	code	pearl
	name	真珠
	info	アジア特産の素材
	price	5000
	limit	200
	base	10/20
	plus	-1h
	pop	10h
	scale	箱
	point	250%
@@ITEM
	no		81
	type	食品
	code	sake
	name	清酒
	info	アジア特産の食品
	price	5000
	limit	200
	base	10/20
	plus	-1h
	pop	10h
	scale	樽
	point	250%
@@ITEM
	no		82
	type	食品
	code	greentea
	name	茶
	info	アジア特産の食品
	price	1000
	limit	1000
	base	10/20
	plus	-1h
	pop	2h
	scale	箱
	point	50%
@@ITEM
	no		83
	type	織物
	code	silkfab
	name	絹織物
	info	アジア特産の織物
	price	10000
	limit	100
	base	10/20
	plus	-1h
	pop	20h
	scale	箱
	point	750%
@@ITEM
	no		84
	type	工芸
	code	ukiyoe
	name	浮世絵
	info	アジア特産の工芸品
	price	2000
	limit	500
	base	10/20
	plus	-1h
	pop	4h
	scale	箱
	point	120%
@@ITEM
	no		85
	type	工芸
	code	lacquer
	name	漆器
	info	アジア特産の工芸品
	price	4000
	limit	250
	base	10/20
	plus	-1h
	pop	8h
	scale	箱
	point	200%
@@ITEM
	no		86
	type	工芸
	code	katana
	name	刀
	info	アジア特産の工芸品
	price	8000
	limit	120
	base	10/20
	plus	-1h
	pop	16h
	scale	箱
	point	400%

@@ITEM
	no		17
	type	素材
	code	silver
	name	銀
	info	新大陸特産の素材
	price	4000
	limit	250
	base	10/20
	plus	-1h
	pop	8h
	scale	箱
	point	200%
@@ITEM
	no		12
	type	素材
	code	emerald
	name	エメラルド
	info	新大陸特産の素材
	price	10000
	limit	100
	base	10/20
	plus	-1h
	pop	20h
	scale	箱
	point	500%
@@ITEM
	no		13
	type	食品
	code	cacao
	name	カカオ
	info	新大陸特産の食品
	price	500
	limit	2000
	base	10/20
	plus	-1h
	pop	1h
	scale	樽
	point	25%
@@ITEM
	no		14
	type	食品
	code	corn
	name	トウモロコシ
	info	新大陸特産の食品
	price	500
	limit	2000
	base	10/20
	plus	-1h
	pop	1h
	scale	樽
	point	25%
@@ITEM
	no		38
	type	食品
	code	tamato
	name	トマト
	info	新大陸特産の食品
	price	500
	limit	2000
	base	10/20
	plus	-1h
	pop	1h
	scale	樽
	point	25%
@@ITEM
	no		23
	type	食品
	code	tobacco
	name	タバコ
	info	新大陸特産の食品
	price	2000
	limit	500
	base	10/20
	plus	-1h
	pop	4h
	scale	箱
	point	150%
@@ITEM
	no		21
	type	食品
	code	pumpkin
	name	かぼちゃ
	info	新大陸特産の食品
	price	500
	limit	2000
	base	10/20
	plus	-1h
	pop	1h
	scale	樽
	point	25%

@@ITEM
	no		5
	type	船舶
	code	ship-a
	name	バルカ
	info	小規模帆船。
	price	20000
	limit	50
	base	5/10
	plus	-1h
	pop	32h
	scale	隻
	point	2h
@@ITEM
	no		6
	type	船舶
	code	ship-c
	name	コッグ
	info	小規模帆船。
	price	40000
	limit	25
	base	5/10
	plus	-1h
	pop	72h
	scale	隻
	point	4h
@@ITEM
	no		7
	type	船舶
	code	ship-b
	name	ガレー
	info	中規模漕船。
	price	60000
	limit	16
	base	5/10
	plus	-1h
	pop	108h
	scale	隻
	point	6h
@@ITEM
	no		8
	type	船舶
	code	ship-d
	name	カラベル
	info	中規模帆船。
	price	80000
	limit	12
	base	5/10
	plus	-1h
	pop	150h
	scale	隻
	point	8h
@@ITEM
	no		9
	type	船舶
	code	ship-e
	name	キャラック
	info	大規模帆船。
	price	160000
	limit	10
	base	5/10
	plus	-1h
	pop	300h
	scale	隻
	point	16h
@@ITEM
	no		10
	type	船舶
	code	ship-f
	name	ガレオン
	info	大規模帆船。
	price	320000
	limit	10
	base	5/10
	plus	-1h
	pop	600h
	scale	隻
	point	50h
@@ITEM
	no		11
	type	船舶
	code	ship-g
	name	ガレアス
	info	巨大漕船。
	price	480000
	limit	10
	base	5/10
	plus	-1h
	pop	900h
	scale	隻
	point	80h

@@ITEM
	no		15
	type	道具
	code	wood
	name	木材
	info	船の材料
	price	5000
	limit	100/100
	pop	10d
	plus	10m
	base	100/10000
	scale	束
	cost	100
@@ITEM
	no		16
	type	道具
	code	cloth
	name	帆布
	info	マストの材料
	price	3000
	limit	100/100
	pop	10d
	plus	10m
	base	100/10000
	scale	枚
	cost	100

@@ITEM
	no		2
	type	道具
	code	jobchange
	name	職業の秘密
	info	様々なジョブに就くための本
	price	25000
	limit	1/1
	pop	0
	base	10/200
	scale	冊
	plus	2h
	@@USE
		time	20m
		scale	回
		action	確認する
		name	現在の職業不足状況を見る
		info	いま不足している職業が一目で分かります
		arg	nocount
		func	jobwant
	@@USE
		time	6h
		action	ジョブチェンジ
		scale	回
		arg		nocount
		name	造船屋になる
		info	造船屋にジョブチェンジします
		param	1,26:27:28:29:30:31:32:33:34:35:36:37,0.2,shipb
		funcb	jobcheck
			need		1	造船指南の書
			use		1	職業の秘密
		func	jobport
	@@USE
		time	6h
		action	ジョブチェンジ
		scale	回
		arg		nocount
		name	貿易商になる
		info	貿易商にジョブチェンジします
		param	30,1:26:27:28:29:34:35:36:37,0.2,trader
		funcb	jobcheck
			use		1	職業の秘密
		func	jobport
	@@USE
		time	6h
		action	ジョブチェンジ
		scale	回
		arg		nocount
		name	探検家になる
		info	探検家にジョブチェンジします
		param	26,1:30:31:32:33:34:35:36:37,0.2,explore
		funcb	jobcheck
			use		1	職業の秘密
		func	jobport
	@@USE
		time	6h
		action	ジョブチェンジ
		scale	回
		arg		nocount
		name	海賊になる
		info	海賊にジョブチェンジします
		param	34,1:26:27:28:29:30:31:32:33,0.2,pirate
		funcb	jobcheck
			use		1	職業の秘密
		func	jobport
	@@USE
		time	6h
		action	ジョブチェンジ
		scale	回
		arg		nocount
		name	海軍司令になる
		info	海軍司令にジョブチェンジします
		param	34,1:26:27:28:29:30:31:32:33,0.2,pros
		funcb	jobcheck
			use		1	職業の秘密
		func	jobport

@@ITEM
	no		3
	type	道具
	code	cm
	name	広告パック
	info	人気を上げられますが失敗することも…
	price	100000
	limit	1/0.1
	pop	10d
	plus	5d
	base	10/50
	scale	パック
	cost	10000
	@@use
		time	10h
		exp	10%
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
	no		4
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
	no		22
	type	道具
	code	book-help
	name	困ったときに読む本
	info	悩み事がこれで解決されるかも
	price	0
	limit	1/1
	pop	0
	plus	4h
	scale	冊
	flag	noshowcase
	@@USE
		time	20m
		scale	回
		action	確認する
		name	どの職業が狙い目なのかを知りたい
		info	いま不足している職業が一目で分かります
		arg	nocount
		func	jobwant
	@@use
		time	40m
		scale	回
		action	仕入れる
		price	1200
		name	パンが市場に出ていなくて買えない
		info	パンを特別ルートで仕入れます（10箱単位）
		okmsg	パンを調達しました
			get		10	パン
	@@use
		time	40m
		scale	回
		action	仕入れる
		price	2400
		name	ラム酒が市場に出ていなくて買えない
		info	ラム酒を特別ルートで仕入れます（10樽単位）
		okmsg	ラム酒を調達しました
			get		10	ラム酒
	@@use
		time	40m
		scale	回
		action	雇い入れる
		price	15000
		name	水夫が市場に出ていなくて雇えない
		info	水夫を特別ルートで雇います（10人単位）
		okmsg	水夫を雇い入れました
			get		10	水夫
	@@use
		time	10m
		scale	回
		action	売りさばく
		name	金貨が売れずに大量に余ってしまう
		info	金貨を特別ルートで売りさばきます
		okmsg	金貨を売りさばきました
			use		1	金貨
		func	_local_
			$DT->{money}+=8000 * $count;
			return "換金額：".GetMoneyString(8000 * $count);
		_local_
	@@use
		time	8h
		scale	回
		action	働く
		name	資金不足で困っている
		info	日雇い土木作業で金貨を稼ぎましょう
		okmsg	めいっぱい働いて金貨をもらいました
			get		2	金貨

@@ITEM
	no		24
	type	道具
	code	gift
	name	ギフト券
	info	欲しいものを手に入れよう！
	price	10000
	cost	10
	limit	10/0
	scale	枚
	@@USE
		time	20m
		scale	回
		action	アドバイスをもらう
		name	ギフト券を交換してしまう前に
		info	海を知り尽くした男にアドバイスをもらいます
		arg	nocount
		func	advice
			need		10	ギフト券
	@@USE
		time	20m
		scale	回
		action	確認する
		name	現在の職業不足状況を見る
		info	いま不足している職業が一目で分かります
		arg	nocount
		func	jobwant
			need		10	ギフト券
	@@USE
		time	20m
		scale	回
		action	引き換え
		name	造船グッズと引き換え
		info	造船屋として暮らすのに必要なグッズです
		okmsg	ご利用ありがとうございました
			use		10	ギフト券
			get		1	造船指南の書
	@@USE
		time	20m
		scale	回
		action	引き換え
		name	貿易グッズと引き換え
		info	貿易商として暮らすのに必要なグッズです
		okmsg	ご利用ありがとうございました
			use		10	ギフト券
			get		5	バルカ
			get		20	金貨
			get		1	職業の秘密
			get		1	困ったときに読む本
	@@USE
		time	20m
		scale	回
		action	引き換え
		name	探検グッズと引き換え
		info	探検家として暮らすのに必要なグッズです
		okmsg	ご利用ありがとうございました
			use		10	ギフト券
			get		5	バルカ
			get		20	金貨
			get		1	職業の秘密
			get		1	困ったときに読む本
	@@USE
		time	20m
		scale	回
		action	引き換え
		name	海賊グッズと引き換え
		info	海賊として暮らすのに必要なグッズです
		okmsg	ご利用ありがとうございました
			use		10	ギフト券
			get		5	バルカ
			get		10	金貨
			get		1	職業の秘密
			get		1	困ったときに読む本
	@@USE
		time	20m
		scale	回
		action	引き換え
		name	海軍グッズと引き換え
		info	海軍司令として暮らすのに必要なグッズです
		okmsg	ご利用ありがとうございました
			use		10	ギフト券
			get		5	バルカ
			get		10	金貨
			get		1	職業の秘密
			get		1	困ったときに読む本

@@ITEM
	no		25
	type	道具
	code	slot
	name	くじ引き券
	info	珍しいアイテムが当たるかも
	price	20000
	cost	100
	limit	10/1.2
	plus	-10h
	scale	枚
	pop	10d
	flag	noshowcase
	@@use
		time	20m
		scale	回
		action	引く
		name	くじ引きをしてみる
		info	当たるも当たらぬも運次第
		arg		nocount
		ngmsg	何も当たりませんでした…
			use		1	くじ引き券
			get		1	ギフト券		5%		ギフト券が当たりました！
			get		1	広告パック		10%		広告パックが当たりました！
			get		1	職業の秘密		5%		職業の秘密が当たりました！
			get		1	番犬			5%		番犬が当たりました！
			get		1	禁断のハッピーベリィ	10%		禁断のハッピーベリィが当たりました！
			get		1	パン			5%		パンが当たりました！
			get		1	ラム酒			5%		ラム酒が当たりました！

@@ITEM
	no		87
	type	道具
	code	defence-manbiki
	name	番犬
	info	店番ができる高級血統犬
	price	500000
	cost	5000
	limit	1/0.5
	pop	1d
	plus	30m
	scale	匹
	flag	noshowcase|onlysend|human

@@ITEM
	no		88
	type	道具
	code	badgossip
	name	禁断のハッピーベリィ
	info	禁断の果実は甘い香り
	price	50000
	cost	5000
	limit	1/1
	pop	0
	plus	1d
	scale	冊
	@@use
		time	10h
		exp	20%
		exptime	8h
		scale	回
		price	50000
		scale	回
		action	仕掛ける
		price	0
		name	ムートさんの隠し日記
		info	成功すれば相手のお店の人気を下げられますが，失敗することも…
		arg	target|nocount
			needpoint	20000
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
		name	ラビくんのパクリ
		info	そこまで追い込まれてるのなら，しょうがないね…
			needpoint	20000
		func	stole
		arg		target|nocount


#------------------------------イベント
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

@@EVENT
	start		150%
	basetime	0h
	plustime	0h
	code		message
	info		メッセージ
	startfunc	_local_
		my @message=(
		'哲学者「この大地は，下で大男が手を広げて支えているのだ。」',
		'宗教家「世界は，体長500kmもある亀が支えているのだよ。」',
		'天文学者「大地は丸い球のような形をしているに違いない。」',
		'冒険家「世界は丸い。ここから西に行けばすぐインドに着くはずだ。」',
		'水夫「あんまり西へ行くと，大地から落っこっちまうぜ。」',
		'酒場娘「大地が丸かったら，裏側にいる人は下に転落してしまうでしょ。」',
		'航海士「はるか東には，何もかもが黄金でできた国があるらしいぞ。」',
		'航海士「はるか西の森には，キリストの楽園があるらしいぞ。」',
		'水夫「南の岬にいる妖精は，その歌声で船を沈めてしまうんだ。」',
		'水夫「熱のない光を放つ船に注意しろ。それは幽霊船だぜ。」',
		'冒険家「船よりも大きいタコが襲ってきて，船が沈むことがあるのさ。」',
		);
		my $cnt=int(rand(scalar(@message)));
		return (0,$message[$cnt]);
	_local_


@@FUNCINIT
#職業が「探検家」の場合、買い物に必要な時間を1/2にする。
$TIME_SEND_ITEM=int($TIME_SEND_ITEM/2) if $DT->{job} eq 'explore';

@@FUNCITEM
######################################################################
# ★ジョブチェンジチェック
######################################################################
sub jobcheck
{
my($USE)=@_;
return 1 if ($DT->{job} eq $USE->{param4});
return 0;
}

######################################################################
# ★ジョブチェンジ
######################################################################
sub jobport
{
	$DT->{job}=$USE->{param4};
	WriteLog(3,0,$DT->{shopname}.'のジョブが「'.$main::JOBTYPE{$USE->{param4}}.'」になりました。');
	main::RequireFile('inc-sea.cgi');

	my $ret;
	my $exp1=$DT->{exp}{$USE->{param1}};
	my $exp2=0;
	$ret.="本を片手に転職の神殿へと向かった。<br><br>";
	$ret.="<TABLE><tr><td>";
	$ret.=main::GetTagImgKao('アムザ','amza')."神官アムザ：<br>";
	$ret.="…ふむ。".$main::JOBTYPE{$USE->{param4}}."になりたいというのですね。<br>";
	$ret.='さすれば，全知全能の神よ！<br>いまここに<b>'.$DT->{shopname}."</b>が<br>";
	$ret.=$main::JOBTYPE{$USE->{param4}}."の道を歩むことを許したまえ！";
	$ret.="</td></tr></table><br>";
	$ret.="ジョブが".$main::JOBTYPE{$USE->{param4}}."になりました。<br>";
	
	foreach my $exps (split(/:/,$USE->{param2}))
	{
		my $exp=$DT->{exp}{$exps};
		next if (!$DT->{item}[$exps-1] && !$exp);
		$exp2+=$exp;
		delete($DT->{exp}{$exps});
		main::DeleteSeaSub("$DT->{id}-abi$exps");
		main::DeleteSeaSub("$DT->{id}-exp$exps");
		my $msg=$ITEM[$exps]->{name}.'は失われました';
		if ($DT->{item}[$exps-1])
			{
			$DT->{item}[$exps-1]=0;
			$msg.="（引き取り料 ".GetMoneyString(50000)."）";
			$DT->{money}+=50000;
			}
		$msg.="。";
		WriteLog(0,$DT->{id},$msg);
		$ret.=$msg."<br>";
	}
	$exp2=int($exp2*$USE->{param3});
	$exp1+=$exp2;
	$exp1=1000 if $exp1>1000;
	$msg=$ITEM[$USE->{param1}]->{name}."の熟練度が ".int($exp1/10)."% になりました。";
	WriteLog(0,$DT->{id},$msg);
	$ret.=$msg."<br>";
	$DT->{exp}{$USE->{param1}}=$exp1;
	return $ret;
}

######################################################################
#★探検船団の派遣
######################################################################
sub exploring
{
	my $itemno=$USE->{param1};	#派遣する船
	my $data=$USE->{param2};	#派遣海域
	my $ability=$ship[$data+4];	#能力
	main::ReadSea($data);
	my @subdata;
	$subdata[0]=$main::NOW_TIME + 3600*11 + int(rand(7200));
	$subdata[1]=$data;

	# 生き残り判定
	if ($main::Pir * 12 > 100 + rand(1900 - $DT->{exp}{$itemno}))
		{
		$subdata[2]=1;	#海の藻屑
		}
		else
		{
		$subdata[2]=0;
		
		# 発見物判定
		if ($main::Civ + 20 < rand($ability) + int($DT->{exp}{$itemno} / 50))
			{
			$subdata[3]=1;
			$main::Civ+=int(rand(3) + 1);
			$main::Civ=100 if ($main::Civ > 100);
			}
		# 都市発見判定
		$subdata[4]=1 if (rand(100)+ ($main::Townnum * 12) < $ability + int($DT->{exp}{$itemno} / 50));
		}
	main::WriteSea($data);
	main::WriteSeaSub("$DT->{id}-exp$itemno",@subdata);
	my $ret;
	$ret.=qq|<IMG width="112" height="150" SRC="$main::IMAGE_URL/map/ship1.png"><br>|;
	my @AREA=("","欧州","アフリカ","中近東","インド","アジア","新大陸");
	$ret.=$AREA[$data]."に探検船団を派遣しました。";
	WriteLog(0,0,$DT->{shopname}."が".$AREA[$data]."に探検船団を派遣しました。");
	return $ret;
}

######################################################################
# ★探検船団派遣前チェック
######################################################################
sub beforeexp
{
my($USE)=@_;
my $itemno=$USE->{param1};	#派遣する船
my $data=$USE->{param2};	#派遣海域
return 1 if ($DT->{job} ne 'explore');
return 1 if -e(main::GetPath($main::SUBDATA_DIR,$DT->{id}."-exp".$itemno));
if (!$ship[0])
	{
	main::RequireFile('inc-sea.cgi');
	@ship=main::ReadSeaSub("$DT->{id}-abi$itemno");
	}
return 1 if $ship[$data+4] < 1;
$USE->{info}.="<b>".$ship[$data+4]."</b>%";
$USE->{use}[0]->{no}=@@ITEMNO "パン";
$USE->{use}[0]->{count}=$ship[11];
$USE->{use}[0]->{proba}=1000;
$USE->{use}[1]->{no}=@@ITEMNO "ラム酒";
$USE->{use}[1]->{count}=$ship[12];
$USE->{use}[1]->{proba}=1000;
$USE->{use}[2]->{no}=@@ITEMNO "水夫";
$USE->{use}[2]->{count}=$ship[13];
$USE->{use}[2]->{proba}=1000;
return 0;
}

######################################################################
# ★派遣中のときだけ可
######################################################################
sub onlyexp
{
my($USE)=@_;
my $itemno=$USE->{param1};	#派遣した船
return 0 if -e(main::GetPath($main::SUBDATA_DIR,$DT->{id}."-exp".$itemno));
return 1;
}

######################################################################
#★探検船団の出迎え
######################################################################
sub meetexp
{
	my $itemno=$USE->{param1};	#派遣した船
	main::RequireFile('inc-sea.cgi');
	my @subdata=main::ReadSeaSub("$DT->{id}-exp$itemno");
	my @ship=main::ReadSeaSub("$DT->{id}-abi$itemno");
	my $seaman=$ship[13];		#水夫
	my $ret;
	$ret.=qq|<TABLE cellpadding="26" width="570"><tr>|;
	$ret.=qq|<TD style="background-repeat : repeat-x;background-image : url($main::IMAGE_URL/harbor.png);" valign="top"><br><br>|;

	if ($main::NOW_TIME < $subdata[0])
		{
		$ret.="港に出てみたが，まだ船団が帰ってくる気配はないようだ。<br>";
		$ret.="もう少し気長に待ってみよう。</tr></table>";
		return $ret;
		}
	main::DeleteSeaSub("$DT->{id}-exp$itemno");
	if ($subdata[2])
		{
		$ret.=qq|<IMG width="112" height="150" align="left" SRC="$main::IMAGE_URL/map/ship2.png">|;
		$ret.="もうそろそろ，船団が戻ってもよいころだ。<br>";
		$ret.="しかし，いくら待っても船団の姿は見えなかった。<br><br>";
		$ret.="どうやら，海の藻屑と消えていったようだ。<br>";
		$ret.="海賊にでもやられたのだろうか・・・。<br>";
		$ret.="</tr></table>";
		UseItem($itemno,1);
		delete $DT->{exp}{$itemno};
		main::DeleteSeaSub("$DT->{id}-abi$itemno");
		WriteLog(2,0,$DT->{shopname}.'の探検船団は海の藻屑と消えました。');
		return $ret;
		}
	$seaman=int($seaman * (70 + rand(30)) / 100);
	AddItem(@@ITEMNO "水夫",$seaman);
	$ret.=qq|<IMG width="112" height="150" align="left" SRC="$main::IMAGE_URL/map/ship1.png">|;
	$ret.=main::GetTagImgKao('提督','exp','align="left" ')."<SPAN>提督</SPAN>：おお，ちょうど今到着したところだ。<br>";
	$ret.="台風やら海賊やら危険な目には遭ったが，<br>$seaman人の水夫が無事だ。<br>";
	if ($subdata[3])
		{
		$ret.="今回の航海の途中，珍しい物を発見したぜ。<br>";
		$ret.="<SPAN>報告書</SPAN>を書いておいたから，ぜひ読んでおいてくんな。<br>";
		AddItem((38 + $subdata[1]),1);
		}
		else
		{
		$ret.="今回の航海では，とくに珍しい物は見つからなかったぜ。<br>";
		}
	if ($subdata[4])
		{
		$ret.="それより重要なことは，<b>新しい陸地を発見した</b>ということだ。<br>";
		$ret.="<SPAN>新しい貿易都市</SPAN>を建設できそうだぜ！<br>";
		AddItem((44 + $subdata[1]),1);
		}
		else
		{
		$ret.="今回の航海では，とくに新しい陸地は見つからなかったぜ。<br>";
		}
	$ret.="これにて報告は終わりだ。次の航海まで少し休ませてくれよ。";
	$ret.="</tr></table>";
	return $ret;
}

######################################################################
#★発見物
######################################################################
sub disc
{
	my $no=$USE->{param1} - 1;
	my @DISCOVER=(
		[
		['錬金術','あらゆる物を金へと変化させる技術。ただ，材料が手に入らない。',55],
		['ミノタウロスの斧','猛獣ミノタウルスが使っていた斧。取っ手の部分がうなり声を上げる。',72],
		['フランク王のサーベル','フランク王が使っていたサーベル。宝石がちりばめられている。',75],
		['ユダの魔衣','キリストを裏切ったユダが着ていた衣。持つ者を呪う。',65],
		['アッティラの鎧','アッティラ王が着ていた鎧。重くて持ち上げることができない。',65],
		['逆周りの懐中時計','反時計回りに針が進む時計。ねじを巻かなくとも自分の意思で動く。',75],
		['滅びの十字架','キリストが処刑の際に体を打ちつけられた十字架。',60],
		['ストーンヘンジ','石柱を輪のようにめぐらせた遺跡。',60],
		],
		[
		['麒麟','体から五色の燐光を発する霊獣。牛の尾と馬の蹄を持ち，腹の下は黄色である。',90],
		['人草','地面に生えている人間の種族。',65],
		['目だけ頭','頭の部分がすべて目になった人間の種族。',70],
		['歩行ブナ','歩行するブナの木。姿を見かけると縁起がいい。',75],
		['ハマペッガの剣','古代の王の剣。すべて純金でできている。',100],
		['邪神の像','蛇の姿をした邪神を祭った像。',60],
		['スフィンクス','半人半獅子の魔獣。謎かけを好み，解けない人間を食らう。',70],
		['ビクトリア瀑布','大地の裂け目へと注ぐ巨大な滝。',60],
		],
		[
		['サラディンの鎧','古代の王の鎧。質素だが，いかなる攻撃も受け付けない。',60],
		['天球儀','星空の様子を丸い球体に描き出した芸術品。',80],
		['クレオパトラの絨毯','美しい刺繍の絨毯。絶世の美女がこれにくるまっていたという。',100],
		['ランプの大男','ランプの中で暮らす人間の種族。',75],
		['コーラン','この地域の民族が形見とする書物。何か大切なことが書かれているらしい。',50],
		['シュメールの粘土板','古代の人間が記した文字。我々の言語によく似ている。',50],
		['布巻き人','全身を布でぐるぐる巻きにした人間の種族。',60],
		['十字軍の宝剣','十字軍の隊長が遠征の際に用いた宝剣。',80],
		],
		[
		['象','鼻の長い巨大な霊獣。胴体は太く，足が８本ある。',80],
		['首長族','首の部分が１メートル近くある人間の種族。',60],
		['金喰虫','金を食べ物にしている虫。',60],
		['金斗雲','人を乗せて飛ぶことのできる雲。',75],
		['ストゥーバ','石でできた巨大な塔。中に現地の神が祀られている。',50],
		['ムガルの宝盾','古代王国に伝わる伝説の盾。サファイアが散りばめられている。',100],
		['勇者のシミター','古代の英雄が用いたというシミター。',80],
		['タージマハール','古代の王が女性を祀るために建てた巨大寺院。',70],
		],
		[
		['そろばん','この地域の民族の遊び道具。玉を弾いて遊ぶ。',90],
		['妖刀村正','妖気を帯びた剣。持ち主の心を支配し，復讐心に駆り立てる。',70],
		['浦島の玉手箱','海中の楽園から持ち帰った宝物。この近くに竜宮城があるようだ。',100],
		['ハラキリ人','腹を自ら切るのが好きな人間の種族。',75],
		['桃源郷の地図','伝説の楽園の位置を示した地図。この近くに桃源郷があるようだ。',100],
		['冬虫夏草','半虫半植物。冬には虫の姿をしているが，夏になると草に変化する。',80],
		['高麗人参','万病を癒すという伝説のにんじん。',80],
		['万里の長城','古代の王が外敵の侵入を防ぐために築いた壁。',70],
		],
		[
		['金のカエル','生きているカエルだが，体が黄金でできている。',90],
		['挫折の遺跡','キリストを祀った施設の残骸。伝説の聖地プレステ・ジョアンのなれの果てのようだ。',120],
		['黄金の川','水の代わりに黄金が流れてくる川。近くに黄金の国エル・ドラドがあるようだ。',100],
		['ナスカの地上絵','地上に描かれた巨大な鳥の絵。',75],
		['モアイの石像','海岸に並べられた巨大な人の顔の石像。',100],
		['入れ墨の人','顔や体を，青や赤などで塗るのが好きな人間の種族。',75],
		['人魚','腰から下が魚になっている人間の種族。',90],
		['空中遺跡','空中に存在する都市の遺跡。人は死滅している。',80],
		],
	);
	my @MYDIS=@{$DISCOVER[$no]};
	my $num=int(rand(scalar(@MYDIS))) + 0;
	my @msg=@{$MYDIS[$num]};
	my $ret;
	$ret.=qq|<TABLE cellpadding="26" width="455"><tr>|;
	$ret.=qq|<TD style="background-repeat : repeat-x;background-image : url($main::IMAGE_URL/discover.png);" valign="top"><br><br>|;
	$no++;
	$num++;
	$ret.=qq|<IMG width="60" height="80" align="left" SRC="$main::IMAGE_URL/disc/$no-$num.png">|;
	$ret.="<SPAN>$msg[0]</SPAN><br><br>";
	$ret.="$msg[1]</tr></table>";
	$ret.="<br>褒美として王様から".main::GetTagImgItemType(51)."金貨".($msg[2])."</b>枚頂いた。";
	AddItem(51,$msg[2]);
	return $ret;
}

######################################################################
#★都市建設
######################################################################
sub newtown
{
	my $data=$USE->{param1};	#派遣海域
	$name=$USE->{arg}->{message};
	main::RequireFile('inc-sea.cgi');
	main::ReadSea($data);
	my $ret;
	if ($main::Townnum > 9)
		{
		$ret.='何と，新しく発見したこの都市には，すでに商館が建設されている。<br>';
		$ret.='どうやら，商館の建設で先を越されてしまったようだ。<br>';
		$ret.='誰だ！先に建設した奴は！';
		return $ret;
		}
	main::OutError('都市の名前をつけてください。') if !$name;
	main::OutError('都市の名前に使用できない文字が使われています。') if ($name =~ /([,:;\t\r\n<>&])/);
	my @TOWN=(
		[
		[@@ITEMNO "ワイン",20,10],
		[@@ITEMNO "チーズ",15,10],
		[@@ITEMNO "オリーブ油",25,5],
		[@@ITEMNO "毛織物",10,15],
		[@@ITEMNO "ステンドグラス",20,10],
		[@@ITEMNO "彫刻",20,10],
		[@@ITEMNO "鉄砲",15,10],
		],
		[
		[@@ITEMNO "金",10,5],
		[@@ITEMNO "ダイヤモンド",10,10],
		[@@ITEMNO "珊瑚",15,10],
		[@@ITEMNO "象牙",15,15],
		[@@ITEMNO "コーヒー",10,10],
		[@@ITEMNO "塩",20,10],
		[@@ITEMNO "タマリンド",20,10],
		],
		[
		[@@ITEMNO "鉄鉱石",10,10],
		[@@ITEMNO "硫黄",10,10],
		[@@ITEMNO "蜂蜜",15,10],
		[@@ITEMNO "砂糖",15,15],
		[@@ITEMNO "絨毯",8,7],
		[@@ITEMNO "麻織物",10,5],
		[@@ITEMNO "犀角",5,15],
		],
		[
		[@@ITEMNO "硝石",10,10],
		[@@ITEMNO "サファイア",10,5],
		[@@ITEMNO "胡椒",1,4],
		[@@ITEMNO "シナモン",10,15],
		[@@ITEMNO "綿織物",15,10],
		[@@ITEMNO "更紗",10,10],
		[@@ITEMNO "鼈甲",10,5],
		],
		[
		[@@ITEMNO "真珠",10,10],
		[@@ITEMNO "清酒",10,10],
		[@@ITEMNO "茶",5,10],
		[@@ITEMNO "絹織物",5,15],
		[@@ITEMNO "浮世絵",10,5],
		[@@ITEMNO "漆器",5,15],
		[@@ITEMNO "刀",5,10],
		],
		[
		[@@ITEMNO "銀",5,10],
		[@@ITEMNO "エメラルド",5,10],
		[@@ITEMNO "カカオ",5,15],
		[@@ITEMNO "トウモロコシ",5,15],
		[@@ITEMNO "トマト",10,5],
		[@@ITEMNO "タバコ",5,5],
		[@@ITEMNO "かぼちゃ",5,10],
		],
	);
	$no=$data - 1;
	my @MYDIS=@{$TOWN[$no]};
	my $num=int(rand(scalar(@MYDIS))) + 0;
	my @msg=@{$MYDIS[$num]};
	my $price=int($ITEM[$msg[0]]->{price} * ($msg[1] + rand($msg[2])) / 100);
	my $life=$main::NOW_TIME + 86400*8 + int(rand(86400) * 4);
	foreach(1..$#main::SEA)
		{
		my @buf=split(',',$main::SEA[$_]);
		$life++ if $buf[0] == $life;
		main::OutError('同じ名前の都市があります。違う名前にしてください。') if $buf[1] eq $name;
		}
	push (@main::SEA,"$life,$name,$DT->{id},$msg[0],$price,0\n");
	$main::Civ+=int(rand(3));
	$main::Civ=100 if ($main::Civ > 100);
	$main::Pir+=int(rand(4));
	$main::Pir=100 if ($main::Pir > 100);
	main::WriteSea($data);
	$ret.=qq|<IMG width="255" height="153" SRC="$main::IMAGE_URL/map/trade.jpg"><br><br>|;
	$ret.='商館を建設しました。<br>都市「<b>'.$USE->{arg}->{message}.'</b>」と貿易可能になりました。';
	WriteLog(2,0,$DT->{shopname}.'が都市「'.$USE->{arg}->{message}.'」を発見しました。');
	return $ret;
}

######################################################################
# ★貿易船団派遣前チェック
######################################################################
sub routesel
{
my($USE)=@_;
my $itemno=$USE->{param1};	#派遣する船
my $data=$USE->{param2};	#派遣海域
return 1 if ($DT->{job} ne 'trader');
return 1 if -e(main::GetPath($main::SUBDATA_DIR,$DT->{id}."-exp".$itemno));
if (!$ship[0])
	{
	main::RequireFile('inc-sea.cgi');
	@ship=main::ReadSeaSub("$DT->{id}-abi$itemno");
	}
return 1 if $ship[$data+4] < 1;
$USE->{info}.="<b>".$ship[$data+4]."</b>%";
main::ReadSea($data);
return 1 if $main::Townnum < 1;
$USE->{argselect}=';';
foreach(1..$main::Townnum)
	{
	my($date,$name,$other)=split(',',$main::SEA[$_],3);
	$USE->{argselect}.=$_.';'.$name.';';
	}
$USE->{use}[0]->{no}=@@ITEMNO "パン";
$USE->{use}[0]->{count}=$ship[11];
$USE->{use}[0]->{proba}=1000;
$USE->{use}[1]->{no}=@@ITEMNO "ラム酒";
$USE->{use}[1]->{count}=$ship[12];
$USE->{use}[1]->{proba}=1000;
$USE->{use}[2]->{no}=@@ITEMNO "水夫";
$USE->{use}[2]->{count}=$ship[13];
$USE->{use}[2]->{proba}=1000;
return 0;
}

######################################################################
#★貿易船団の派遣
######################################################################
sub route
{
	my $itemno=$USE->{param1};	#派遣した船
	my $data=$USE->{param2};	#派遣海域
	my $ability=int($ship[$data+4] / 2);	#積載量（ｘ万円相当）
	my $sel=$USE->{arg}->{select};

	#派遣数を増やす
	my @buf=split(',',$main::SEA[$sel]);
	main::OutError("「$buf[1]」の産物は底を突いているので，派遣できません。<br>派遣先を変更してください。") if ($buf[0] < $main::NOW_TIME);
	$main::SEA[$sel]="$buf[0],$buf[1],$buf[2],$buf[3],$buf[4],".($buf[5] + 1)."\n";
	main::WriteSea($data);

	my @subdata;
	$subdata[0]=$main::NOW_TIME + 3600*11 + int(rand(7200));

	# 生き残り判定
	$subdata[1]=1 if ($main::Pir * 12 > 100 + rand(1900 - $DT->{exp}{$itemno}));

	#貿易量
	$subdata[2]=$buf[1];
	$subdata[3]=$buf[3];
	$subdata[4]=int($ITEM[$buf[3]]->{limit} * $ability / 100);
	$subdata[5]=$buf[4] * $subdata[4];

	# 発見者に利益発生
	if (defined($main::id2idx{$buf[2]}))
		{
		$DT[$main::id2idx{$buf[2]}]->{money}+=int($subdata[5] / 2);
		$DT[$main::id2idx{$buf[2]}]->{saletoday}+=int($subdata[5] / 2);
		}
	main::WriteSeaSub("$DT->{id}-exp$itemno",@subdata);
	my $ret;
	$ret.=qq|<IMG width="112" height="150" SRC="$main::IMAGE_URL/map/ship1.png"><br>|;
	$ret.="「$buf[1]」へ貿易船団を派遣しました。";
	return $ret;
}

######################################################################
#★貿易船団の出迎え
######################################################################
sub meetrtp
{
	my $itemno=$USE->{param1};	#派遣した船
	main::RequireFile('inc-sea.cgi');
	my @subdata=main::ReadSeaSub("$DT->{id}-exp$itemno");
	my @ship=main::ReadSeaSub("$DT->{id}-abi$itemno");
	my $seaman=$ship[13];		#水夫
	my $ret;
	$ret.=qq|<TABLE cellpadding="26" width="570"><tr>|;
	$ret.=qq|<TD style="background-repeat : repeat-x;background-image : url($main::IMAGE_URL/harbor.png);" valign="top"><br><br>|;

	if ($main::NOW_TIME < $subdata[0])
		{
		$ret.="港に出てみたが，まだ船団が帰ってくる気配はないようだ。<br>";
		$ret.="もう少し気長に待ってみよう。</tr></table>";
		return $ret;
		}
	main::DeleteSeaSub("$DT->{id}-exp$itemno");
	if ($subdata[1])
		{
		$ret.=qq|<IMG width="112" height="150" align="left" SRC="$main::IMAGE_URL/map/ship2.png">|;
		$ret.="もうそろそろ，船団が戻ってもよいころだ。<br>";
		$ret.="しかし，いくら待っても船団の姿は見えなかった。<br><br>";
		$ret.="どうやら，海の藻屑と消えていったようだ。<br>";
		$ret.="海賊にでもやられたのだろうか・・・。<br>";
		$ret.="</tr></table>";
		UseItem($itemno,1);
		delete $DT->{exp}{$itemno};
		main::DeleteSeaSub("$DT->{id}-abi$itemno");
		WriteLog(2,0,$DT->{shopname}.'の貿易船団は海の藻屑と消えました。');
		return $ret;
		}
	$seaman=int($seaman * (70 + rand(30)) / 100);
	AddItem(@@ITEMNO "水夫",$seaman);
	$ret.=qq|<IMG width="112" height="150" align="left" SRC="$main::IMAGE_URL/map/ship1.png">|;
	$ret.=main::GetTagImgKao('提督','rtp','align="left" ')."<SPAN>提督</SPAN>：どうも，ただいま帰還いたしました。<br>";
	$ret.="途中，台風や海賊に悩まされましたが，<br>$seaman人の水夫が無事です。<br>";
	$ret.="今回の貿易では，都市「$subdata[2]」より，<br>";
	$ret.=main::GetTagImgItemType($subdata[3]).$ITEM[$subdata[3]]->{name}."を ";
	$ret.=$subdata[4].$ITEM[$subdata[3]]->{scale}."仕入れることができました。<br>";
	$ret.="仕入れの費用として，".GetMoneyString($subdata[5])."かかりました。<br>";
	$DT->{money}-=$subdata[5];
	$DT->{paytoday}+=$subdata[5];
	AddItem($subdata[3],$subdata[4]);
	$ret.="報告は以上の通りです。";
	$ret.="</tr></table>";
	return $ret;
}

######################################################################
# ★武装艦隊派遣前チェック
######################################################################
sub nowpp
{
my($USE)=@_;
my $itemno=$USE->{param1};	#派遣した船
my $data=$USE->{param2};	#派遣海域
if ($DT->{job} eq 'pirate') {$USE->{name}.="掠奪に派遣する";}
elsif ($DT->{job} eq 'pros') {$USE->{name}.="偵察に派遣する";}
else {return 0;}
return 1 if -e(main::GetPath($main::SUBDATA_DIR,$DT->{id}."-exp".$itemno));
if (!$ship[0])
	{
	main::RequireFile('inc-sea.cgi');
	@ship=main::ReadSeaSub("$DT->{id}-abi$itemno");
	}
return 1 if $ship[$data+4] < 1;
$USE->{info}.="<b>".$ship[$data+4]."</b>%";
$USE->{use}[0]->{no}=@@ITEMNO "パン";
$USE->{use}[0]->{count}=$ship[11];
$USE->{use}[0]->{proba}=1000;
$USE->{use}[1]->{no}=@@ITEMNO "ラム酒";
$USE->{use}[1]->{count}=$ship[12];
$USE->{use}[1]->{proba}=1000;
$USE->{use}[2]->{no}=@@ITEMNO "水夫";
$USE->{use}[2]->{count}=$ship[13];
$USE->{use}[2]->{proba}=1000;
return 0;
}

######################################################################
#★武装艦隊の派遣
######################################################################
sub attack
{
	my $itemno=$USE->{param1};	#派遣する船
	my $data=$USE->{param2};	#派遣海域
	my $ability=$ship[$data+4];	#能力
	main::ReadSea($data);
	my @subdata;
	$subdata[0]=$main::NOW_TIME + 3600*11 + int(rand(7200));
	$subdata[1]=$data;
	my $ret;
	$ret.=qq|<IMG width="112" height="150" SRC="$main::IMAGE_URL/map/ship1.png"><br>|;
	my @AREA=("","欧州","アフリカ","中近東","インド","アジア","新大陸");

	if ($DT->{job} eq 'pros')
	{
	# 海軍の処理
	# 生き残り判定
	if ($main::Pir * 6 > 100 + rand(1900 - $DT->{exp}{$itemno}))
		{
		$subdata[2]=1;	#海の藻屑
		}
		else
		{
		# 海賊出現率低下
		$main::Pir-=int(rand(5)) + 6;
		$main::Pir=0 if ($main::Pir < 0);
		# 海軍偵察率上昇
		$main::Pro+=int(rand(5)) + 4;
		$main::Pro=100 if ($main::Pro > 100);
		}
	$ret.=$AREA[$data]."に海軍を派遣しました。";
	WriteLog(0,0,$DT->{shopname}."が".$AREA[$data]."に海軍を派遣しました。");
	}
	else
	{
	# 海賊の処理
	# 生き残り判定
	if ($main::Pro * 16 > 100 + rand(1900 - $DT->{exp}{$itemno}))
		{
		$subdata[2]=1;	#海の藻屑
		}
		else
		{
		# 海賊出現率上昇
		$main::Pir+=int(rand(5)) + 4;
		$main::Pir=100 if ($main::Pir > 100);
		}
	$ret.=$AREA[$data]."に海賊船を派遣しました。";
	WriteLog(2,0,$AREA[$data]."にて海賊が出没しているようです。");
	}
	if (!$subdata[2])
		{
		$subdata[2]=0;
		# 金貨
		$subdata[3]=int(($ability / 4) + ($DT->{exp}{$itemno} / 100) + rand(5));
		# 貿易品
		if ($main::Townnum > 0 && $main::Pir > rand(20))
			{
			my $sel=int(rand($main::Townnum)) + 1;
			my @buf=split(',',$main::SEA[$sel]);
			$subdata[4]=$buf[3];
			$subdata[5]=int($ITEM[$buf[3]]->{limit} * $ability / 200);
			}
		}
	main::WriteSea($data);
	main::WriteSeaSub("$DT->{id}-exp$itemno",@subdata);
	return $ret;
}

######################################################################
#★武装艦隊の出迎え
######################################################################
sub meetpp
{
	my $itemno=$USE->{param1};	#派遣した船
	main::RequireFile('inc-sea.cgi');
	my @subdata=main::ReadSeaSub("$DT->{id}-exp$itemno");
	my @ship=main::ReadSeaSub("$DT->{id}-abi$itemno");
	my $seaman=$ship[13];		#水夫
	my $ret;
	$ret.=qq|<TABLE cellpadding="26" width="570"><tr>|;
	$ret.=qq|<TD style="background-repeat : repeat-x;background-image : url($main::IMAGE_URL/harbor.png);" valign="top"><br><br>|;

	if ($main::NOW_TIME < $subdata[0])
		{
		$ret.="港に出てみたが，まだ艦隊が帰ってくる気配はないようだ。<br>";
		$ret.="もう少し気長に待ってみよう。</tr></table>";
		return $ret;
		}
	main::DeleteSeaSub("$DT->{id}-exp$itemno");
	if ($DT->{job} eq 'pros')
	{
	# 海軍の処理
	if ($subdata[2])
		{
		$ret.=qq|<IMG width="112" height="150" align="left" SRC="$main::IMAGE_URL/map/ship2.png">|;
		$ret.="もうそろそろ，艦隊が戻ってもよいころだ。<br>";
		$ret.="しかし，いくら待っても艦隊の姿は見えなかった。<br><br>";
		$ret.="どうやら，海の藻屑と消えていったようだ。<br>";
		$ret.="海賊に敗れてしまったのだろうか・・・。<br>";
		$ret.="</tr></table>";
		UseItem($itemno,1);
		delete $DT->{exp}{$itemno};
		main::DeleteSeaSub("$DT->{id}-abi$itemno");
		WriteLog(2,0,$DT->{shopname}.'の海軍は海賊に敗れ，沈みました。');
		return $ret;
		}
	$seaman=int($seaman * (40 + rand(30)) / 100);
	AddItem(@@ITEMNO "水夫",$seaman);
	$ret.=qq|<IMG width="112" height="150" align="left" SRC="$main::IMAGE_URL/map/ship1.png">|;
	$ret.=main::GetTagImgKao('提督','pro','align="left" ')."<SPAN>提督</SPAN>：おぉ，ただいま帰還した所である。<br>";
	$ret.="途中，台風や戦闘に巻き込まれたが，<br>$seaman人の水夫が無事だ。<br>";

	if ($subdata[3])
		{
		$ret.="今回，海賊の宿営地を発見，掃討した。<br>";
		$ret.=main::GetTagImgItemType(51)."金貨 $subdata[3]枚を没収した。<br>";
		AddItem(51,$subdata[3]);
		}
	if ($subdata[4])
		{
		$ret.="途中通りかかった海賊船を攻撃，これを討伐したので，<br>";
		$ret.=main::GetTagImgItemType($subdata[4]).$ITEM[$subdata[4]]->{name}."を ";
		$ret.=$subdata[5].$ITEM[$subdata[4]]->{scale}."没収した。<br>";
		AddItem($subdata[4],$subdata[5]);
		}
	$ret.="以上で報告を終わる。治安に貢献できたことを誇りに思う。";
	$ret.="</tr></table>";
	return $ret;
	}
	# 海賊の処理
	if ($subdata[2])
		{
		$ret.=qq|<IMG width="112" height="150" align="left" SRC="$main::IMAGE_URL/map/ship2.png">|;
		$ret.="もうそろそろ，艦隊が戻ってもよいころだ。<br>";
		$ret.="しかし，いくら待っても艦隊の姿は見えなかった。<br><br>";
		$ret.="どうやら，海の藻屑と消えていったようだ。<br>";
		$ret.="海軍にでもやられたのだろうか・・・。<br>";
		$ret.="</tr></table>";
		UseItem($itemno,1);
		delete $DT->{exp}{$itemno};
		main::DeleteSeaSub("$DT->{id}-abi$itemno");
		WriteLog(2,0,$DT->{shopname}.'の海賊船は海軍に討伐されました。');
		return $ret;
		}
	$seaman=int($seaman * (40 + rand(30)) / 100);
	AddItem(@@ITEMNO "水夫",$seaman);
	$ret.=qq|<IMG width="112" height="150" align="left" SRC="$main::IMAGE_URL/map/ship1.png">|;
	$ret.=main::GetTagImgKao('提督','pir','align="left" ')."<SPAN>提督</SPAN>：いよう，ちょうど帰還したところだぜ。<br>";
	$ret.="途中，台風やら戦闘やらもあったが，<br>$seaman人の水夫が無事だ。<br>";

	if ($subdata[3])
		{
		$ret.="今回，探検にうろついてた船団を沈めてやったぜ。<br>";
		$ret.=main::GetTagImgItemType(51)."金貨 $subdata[3]枚を頂戴した。<br>";
		AddItem(51,$subdata[3]);
		}
	if ($subdata[4])
		{
		$ret.="途中通りかかった貿易船からは，帰るところを見計らって，<br>";
		$ret.=main::GetTagImgItemType($subdata[4]).$ITEM[$subdata[4]]->{name}."を ";
		$ret.=$subdata[5].$ITEM[$subdata[4]]->{scale}."頂いたぜ。<br>";
		AddItem($subdata[4],$subdata[5]);
		}
	$ret.="どうだい，俺の仕事ぶりは？ この味は忘れられねえな！";
	$ret.="</tr></table>";
	return $ret;
}

######################################################################
#★開始時のアドバイス
######################################################################
sub advice
{
	my $ret;
	$ret.=qq|<TABLE cellpadding="26" width="570"><tr>|;
	$ret.=qq|<TD style="background-repeat : repeat-x;background-image : url($main::IMAGE_URL/harbor.png);" valign="top"><br><br>|;
	$ret.=main::GetTagImgKao('ハイレディン','bal','align="left" ')."<SPAN>ハイレディン</SPAN>：ワシに相談に来るとはいい度胸だな。<br>";
	$ret.="いいか，このギフト券交換は，<BIG>非常に重大な選択</BIG>だ。<br>";
	$ret.="初めの人生がこれで決まっちまうから，いま何の職業が有利かを見極めるんだ。<br><br>";
	$ret.="１．<BIG>造船</BIG>は初心者向けだが，他に<b>同業者</b>が多すぎると行き詰まる。<br>";
	$ret.="２．<BIG>貿易</BIG>は，欧州の<b>海賊出現率</b>が高すぎては赤字になる。<br>";
	$ret.="３．<BIG>探検</BIG>は，欧州の<b>海賊出現率</b>が低く，<b>未踏破領域</b>が高いとよい。<br>";
	$ret.="４．<BIG>海賊</BIG>は，欧州の<b>海軍偵察率</b>が高いなら成り立たない。<br>";
	$ret.="５．<BIG>海軍</BIG>は，欧州の<b>海賊出現率</b>が低すぎては赤字だ。<br>";
	$ret.="<br>分かったか？それと，失敗しない最大のコツは，<SPAN>図書館</SPAN>をよく読むことだ。";
	$ret.="</tr></table>";
	return $ret;
}

######################################################################
#★職業不足・飽和状況
######################################################################
sub jobwant
{
	my %jobwant;
	my $sum;
	foreach my $DT(@DT)
		{
		next if !$DT->{job};
		$jobwant{$DT->{job}}++;
		$sum++;
		}
	my $ret;
	$ret.=qq|<TABLE cellpadding="26" width="570"><tr>|;
	$ret.=qq|<TD style="background-repeat : repeat-x;background-image : url($main::IMAGE_URL/harbor.png);" valign="top" align="center"><br><br>|;
	$ret.=$main::TB;

	my %jobneed=qw(shipb 10 explore 15 trader 55 pirate 10 pros 10);
	foreach("shipb","explore","trader","pirate","pros")
		{
		$ret.=$main::TR.$main::TDB.$main::JOBTYPE{$_};
		my $i=($sum) ? ($jobwant{$_} / $sum / $jobneed{$_} * 100 * 100) : 100;
		$ret.=$main::TD.main::GetMarketStatusGraph($i).$main::TRE;
		}
	$ret.="</tr></table></tr></table>";
	return $ret;
}

######################################################################
#★万引き
######################################################################
sub stole
{
	return '自分から万引きすることはできません。万引きは失敗です。' if  ($DT->{id} eq $DTS->{id});
	my $ret="万引きは失敗しました。賠償金".GetMoneyString(500000)."を取られてしまいました。";
	if($DTS->{item}[@@ITEMNO"番犬"-1])
	{
		$DT->{rank}-=int($DT->{rank}/4);
		$DTS->{money}+=500000;
		$DTS->{saletoday}+=500000;
		$DT->{money}-=500000;
		$DT->{paytoday}+=500000;
		WriteLog(3,0,$DT->{shopname}."が".$DTS->{shopname}."へ万引きに入りましたが番犬に見つかりました。");
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
				['禁断のハッピーベリィ',	[[@@ITEMNO "禁断のハッピーベリィ", 1],			],],
				['番犬',	[[@@ITEMNO "番犬", 1],			],],
				['パン',	[[@@ITEMNO "パン", 400],			],],
				['ラム酒',	[[@@ITEMNO "ラム酒", 200],			],],
				['広告パック',	[[@@ITEMNO "広告パック", 1],			],],
				['ギフト券',	[[@@ITEMNO "ギフト券", 5],			],],
				['くじ引き券',	[[@@ITEMNO "くじ引き券", 5],			],],
			],
			[
				['禁断のハッピーベリィ',	[[@@ITEMNO "禁断のハッピーベリィ", 1],			],],
				['パン',	[[@@ITEMNO "パン", 400],			],],
				['ラム酒',	[[@@ITEMNO "ラム酒", 200],			],],
				['広告パック',	[[@@ITEMNO "広告パック", 1],			],],
				['ギフト券',	[[@@ITEMNO "ギフト券", 4],			],],
				['くじ引き券',	[[@@ITEMNO "くじ引き券", 4],			],],
			],
			[
				['職業の秘密',	[[@@ITEMNO "職業の秘密", 1],			],],
				['パン',	[[@@ITEMNO "パン", 200],			],],
				['ラム酒',	[[@@ITEMNO "ラム酒", 100],			],],
				['広告パック',	[[@@ITEMNO "広告パック", 1],			],],
				['ギフト券',	[[@@ITEMNO "ギフト券", 3],			],],
				['くじ引き券',	[[@@ITEMNO "くじ引き券", 3],			],],
			],
			[
				['職業の秘密',	[[@@ITEMNO "職業の秘密", 1],			],],
				['パン',	[[@@ITEMNO "パン", 100],			],],
				['ラム酒',	[[@@ITEMNO "ラム酒", 50],			],],
				['ギフト券',	[[@@ITEMNO "ギフト券", 2],			],],
				['くじ引き券',	[[@@ITEMNO "くじ引き券", 2],			],],
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
			WriteLog(0,0,0,$msg,1);
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
	foreach my $DT (@DT)
		{
		$DT->{profitstock}=5000000 if ($DT->{profitstock} > 5000000);
		$DT->{profitstock}=-1000000 if ($DT->{profitstock} < -1000000);
		if ($DT->{money} > 50000000)
			{
			$DT->{money} -= int( ($DT->{money} - 20000000)/2 );
			$DT->{rank} += int( (10000 - $DT->{rank})/2 );
			$DT->{rank}=10000 if $DT->{rank}>10000;
			PushLog(2,0,$DT->{shopname}.'にて祝賀会が行われました。');
			}
		}
	main::RequireFile('inc-atlas.cgi');
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
	if (rand(1000) > 990 && $BUY->{num} > 10)
	{
	$count=AddItemSub(@@ITEMNO"ギフト券",1,$BUY->{dt});
	WriteLog(0,$BUY->{dt}{id},'市場の抽選でギフト券が'.$count.'枚あたりました。');
	$main::ret.='<br>抽選でギフト券が'.$count.'枚あたりました！';
	}
}

@@END #定義終了宣言(以降コメント扱い)

