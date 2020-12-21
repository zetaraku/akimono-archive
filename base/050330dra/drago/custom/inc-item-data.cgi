# ドラゴノーマ版アイテムデータ 2005/01/06 由來

# このファイルはアイテムデータの定義ファイルです。
# 好きなようにカスタマイズできます。詳細はマニュアルをご覧ください。

@@DEFINE
	version	05-01-06(DN)		#★商品データバージョン表記
					# 最後の「DN」はドラゴノーマ版であることを示します。
					# もしあなたが独自アイテムを目玉にした商人物語を作るなら，
					# この記号を変えるのがよいでしょう。

	scale	個			#★デフォルトの数え単位
	type0	全			#全アイテムの集合
	type1	触媒
	type2	魔餌
	type3	火
	type4	水
	type5	土
	type6	風
	type7	聖
	type8	邪
	type9	道具
	
	job	warlock		ウォーロック	#★職業コードは英小文字10文字以内
	job	dtamer		ドラゴンテイマー
	job	dmaster		ドラゴンマスター
	job	btamer		ビーストテイマー
	job	shaman		シャーマン
	job	thunter		トレジャーハンター
	job	peddle		トレードマスター

	MaxMoney	999999999	#★最大資金
	
	set NewShopMoney	100000					#初期資金 (@@FUNCNEWにて使用)
	set NewShopTime		12*60*60				#初期持時間(秒) (@@FUNCNEWにて使用)
	set NewShopItem		陳列棚増築取壊キット:1:ギフト券:1	#初期所持商品 (@@FUNCNEWにて使用) 書式 商品名:個数:商品名:個数:...
	
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
	no		20		#★アイテム番号(重複しないように)
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
		time	90m
		exp		2%
		exptime	30m
		job		ウォーロック	times/1.5
		scale	回
		action	書く
		name	『紀行文』を執筆する
		info	周りの土地を駆け巡った記憶を綴ろうと思います
		okmsg	様々な地図シリーズが書きあがりました
		ngmsg	執筆に失敗しました…
			use		1	本執筆キット
			get		2	近くの洞窟への地図	50%
			get		2	近くの野山への地図	50%
	@@USE
		time	3h
		exp		4%
		exptime	1h
		name	『君子豹変』を執筆する
		info	自分の新たな可能性を本にしようと思います
		okmsg	『職業の秘密』が書きあがりました
		ngmsg	執筆に失敗しました…
			needexp	10%
			use		1	本執筆キット
			get		3	職業の秘密	50%
	@@USE
		time	3h
		exp		4%
		exptime	1h
		name	『召喚研究』を執筆する
		info	召喚の研究成果を本にしようと思います
		okmsg	『触媒の秘法』が書きあがりました
		ngmsg	執筆に失敗しました…
			needexp	20%
			use		1	本執筆キット
			get		4	触媒の秘法	50%
	@@USE
		time	3h
		exp		4%
		exptime	1h
		name	『推理小説』を執筆する
		info	緻密なサスペンスはどこか実用的なようです
		okmsg	『禁断の書』が書きあがりました
		ngmsg	執筆に失敗しました…
			needexp	30%
			use		1	本執筆キット
			get		5	禁断の書	40%
	@@USE
		time	4h
		exp		2%
		exptime	2h
		name	『竜の誕生』を執筆する
		info	竜を誕生させる方法を本にしようと思います
		okmsg	『ドラゴノーマの法典』が書きあがりました
		ngmsg	執筆に失敗しました…
			needjob	ウォーロック
			needexp	50%
			use		1	本執筆キット
			get		2	ドラゴノーマの法典	50%

@@ITEM
	no		1
	type	触媒
	code	dizmal
	name	ディズマル
	info	火の力で召喚するのに用います
	price	120
	limit	1500/500
	pop	10d
	plus	-20m
	base	200/600
	scale	個
	cost	40
	point	50%
	@@use
		time	90m
		exp		2%
		exptime	30m
		job		シャーマン	times/1.5
		scale	回
		action	召喚する
		name	低級召喚魔を呼び出す
		info	火の力で召喚を試みます
		okmsg	ウィスプを召喚しました
		ngmsg	召喚に失敗しました…
			need		1	魔方陣
			use		20	ディズマル
			get		15	ウィスプ	80%
	@@use
		time	1h
		exp		2%
		exptime	20m
		scale	回
		action	召喚する
		name	上級召喚魔を呼び出す
		info	火の力で召喚を試みます
		okmsg	イフリートを召喚しました
		ngmsg	召喚に失敗しました…
			needexp	25%
			need		1	魔方陣
			use		20	ディズマル
			get		10	イフリート	80%
@@ITEM
	no		2
	type	触媒
	code	jemstone
	name	ジェムストーン
	info	水の力で召喚するのに用います
	price	120
	limit	1500/500
	pop	10d
	plus	-20m
	base	200/600
	scale	個
	cost	40
	point	50%
	@@use
		time	90m
		exp		2%
		exptime	30m
		job		シャーマン	times/1.5
		scale	回
		action	召喚する
		name	低級召喚魔を呼び出す
		info	水の力で召喚を試みます
		okmsg	スライムを召喚しました
		ngmsg	召喚に失敗しました…
			need		1	魔方陣
			use		20	ジェムストーン
			get		15	スライム	80%
	@@use
		time	90m
		exp		2%
		exptime	30m
		scale	回
		action	召喚する
		name	上級召喚魔を呼び出す
		info	水の力で召喚を試みます
		okmsg	イエティを召喚しました
		ngmsg	召喚に失敗しました…
			needexp	25%
			need		1	魔方陣
			use		20	ジェムストーン
			get		10	イエティ	80%
@@ITEM
	no		3
	type	触媒
	code	chronime
	name	クロナイム
	info	土の力で召喚するのに用います
	price	120
	limit	1500/500
	pop	10d
	plus	-20m
	base	200/600
	scale	個
	cost	40
	point	50%
	@@use
		time	90m
		exp		2%
		exptime	30m
		job		シャーマン	times/1.5
		scale	回
		action	召喚する
		name	低級召喚魔を呼び出す
		info	土の力で召喚を試みます
		okmsg	ノームを召喚しました
		ngmsg	召喚に失敗しました…
			need		1	魔方陣
			use		20	クロナイム
			get		15	ノーム	80%
	@@use
		time	90m
		exp		2%
		exptime	30m
		scale	回
		action	召喚する
		name	上級召喚魔を呼び出す
		info	土の力で召喚を試みます
		okmsg	ゴーレムを召喚しました
		ngmsg	召喚に失敗しました…
			needexp	25%
			need		1	魔方陣
			use		20	クロナイム
			get		10	ゴーレム	80%
@@ITEM
	no		4
	type	触媒
	code	fiyel
	name	フィエル
	info	風の力で召喚するのに用います
	price	120
	limit	1500/500
	pop	10d
	plus	-20m
	base	200/600
	scale	個
	cost	40
	point	50%
	@@use
		time	90m
		exp		2%
		exptime	30m
		job		シャーマン	times/1.5
		scale	回
		action	召喚する
		name	低級召喚魔を呼び出す
		info	風の力で召喚を試みます
		okmsg	シルフを召喚しました
		ngmsg	召喚に失敗しました…
			need		1	魔方陣
			use		20	フィエル
			get		15	シルフ	80%
	@@use
		time	90m
		exp		2%
		exptime	30m
		scale	回
		action	召喚する
		name	上級召喚魔を呼び出す
		info	風の力で召喚を試みます
		okmsg	グリフォンを召喚しました
		ngmsg	召喚に失敗しました…
			needexp	25%
			need		1	魔方陣
			use		20	フィエル
			get		10	グリフォン	80%
@@ITEM
	no		5
	type	触媒
	code	crystal
	name	クリスタル
	info	聖の力で召喚するのに用います
	price	240
	limit	500/100
	pop	10d
	plus	-20m
	base	100/500
	scale	個
	cost	100
	@@use
		time	90m
		exp		2%
		exptime	30m
		job		シャーマン	times/1.5
		scale	回
		action	召喚する
		name	低級召喚魔を呼び出す
		info	聖なる力で召喚を試みます
		okmsg	スピリットを召喚しました
		ngmsg	召喚に失敗しました…
			needexp	10%
			need		1	魔方陣
			use		10	クリスタル
			get		12	スピリット	80%
	@@use
		time	90m
		exp		2%
		exptime	30m
		scale	回
		action	召喚する
		name	上級召喚魔を呼び出す
		info	聖なる力で召喚を試みます
		okmsg	ユニコーンを召喚しました
		ngmsg	召喚に失敗しました…
			needexp	25%
			need		1	魔方陣
			use		10	クリスタル
			get		10	ユニコーン	80%
@@ITEM
	no		6
	type	触媒
	code	verdure
	name	ヴェルデュール
	info	邪の力で召喚するのに用います
	price	240
	limit	500/100
	pop	10d
	plus	-20m
	base	100/500
	scale	個
	cost	100
	@@use
		time	90m
		exp		2%
		exptime	30m
		job		シャーマン	times/1.5
		scale	回
		action	召喚する
		name	低級召喚魔を呼び出す
		info	邪の力で召喚を試みます
		okmsg	シェイドを召喚しました
		ngmsg	召喚に失敗しました…
			needexp	10%
			need		1	魔方陣
			use		10	ヴェルデュール
			get		12	シェイド	80%
	@@use
		time	90m
		exp		2%
		exptime	30m
		scale	回
		action	召喚する
		name	上級召喚魔を呼び出す
		info	邪の力で召喚を試みます
		okmsg	デーモンを召喚しました
		ngmsg	召喚に失敗しました…
			needexp	25%
			need		1	魔方陣
			use		10	ヴェルデュール
			get		10	デーモン	80%

@@ITEM
	no		21
	type	道具
	code	book-dk
	name	近くの洞窟への地図
	info	触媒調達にはもってこいの洞窟です
	price	10000
	limit	100/1
	pop	24h
	plus	2h
	base	50/150
	scale	冊
	cost	1000
	point	500%
	@@use
		time	2h
		exp		2%
		exptime	30m
		job		トレジャーハンター	times/1.5
		scale	往復
		action	探索しに行く
		name	溶岩鉱を探索
		info	いろんな触媒が調達できるかもしれません
		ngmsg	なにも見つかりませんでした…
			get		40	ディズマル	90%	ディズマルがたくさん見つかりました
			get		2	クロナイム	90%
			get		3	ヴェルデュール	45%
	@@use
		time	2h
		exp		2%
		exptime	30m
		scale	往復
		action	探索しに行く
		name	地下水脈を探索
		info	いろんな触媒が調達できるかもしれません
		ngmsg	なにも見つかりませんでした…
			get		40	ジェムストーン	90%	ジェムストーンがたくさん見つかりました
			get		2	フィエル	90%
			get		3	クリスタル	45%
	@@use
		time	2h
		exp		2%
		exptime	30m
		scale	往復
		action	探索しに行く
		name	掘削地を探索
		info	いろんな触媒が調達できるかもしれません
		ngmsg	なにも見つかりませんでした…
			get		2	ディズマル	90%
			get		40	クロナイム	90%	クロナイムがたくさん見つかりました
			get		3	ヴェルデュール	45%
	@@use
		time	2h
		exp		2%
		exptime	30m
		scale	往復
		action	探索しに行く
		name	通風孔を探索
		info	いろんな触媒が調達できるかもしれません
		ngmsg	なにも見つかりませんでした…
			get		2	ジェムストーン	90%
			get		40	フィエル	90%	フィエルがたくさん見つかりました
			get		3	クリスタル	45%
	@@use
		time	2h
		exp		2%
		exptime	30m
		scale	往復
		action	探索しに行く
		name	鍾乳洞を探索
		info	いろんな触媒が調達できるかもしれません
		ngmsg	なにも見つかりませんでした…
			needexp	10%
			get		2	ジェムストーン	90%
			get		2	フィエル	90%
			get		40	クリスタル	45%	クリスタルがたくさん見つかりました
	@@use
		time	2h
		exp		2%
		exptime	30m
		scale	往復
		action	探索しに行く
		name	封魔壁を探索
		info	いろんな触媒が調達できるかもしれません
		ngmsg	なにも見つかりませんでした…
			needexp	10%
			get		2	ディズマル	90%
			get		2	クロナイム	90%
			get		40	ヴェルデュール	45%	ヴェルデュールがたくさん見つかりました
	
@@ITEM
	no		22
	type	道具
	code	book-ny
	name	近くの野山への地図
	info	モンスターの好物が採取できそうです
	price	10000
	limit	100/1
	pop	24h
	plus	-1h
	base	50/150
	scale	冊
	cost	1000
	point	500%
	@@use
		time	2h
		exp		2%
		exptime	30m
		job		トレジャーハンター	times/1.5
		scale	往復
		action	探索しに行く
		name	野原を探索
		info	いろんな餌が調達できるかもしれません
		ngmsg	なにも見つかりませんでした…
			get		60	へびいちご	70%	へびいちごがたくさん見つかりました
			get		3	ツキノハナワラビ	70%
			get		3	雪だるまの昆布	35%
			get		3	トカゲのしっぽ	35%
			get		3	ネコのひげ	35%
	@@use
		time	2h
		exp		2%
		exptime	30m
		scale	往復
		action	探索しに行く
		name	森林を探索
		info	いろんな餌が調達できるかもしれません
		ngmsg	なにも見つかりませんでした…
			get		3	へびいちご	70%
			get		60	ツキノハナワラビ	70%	ツキノハナワラビがたくさん見つかりました
			get		3	雪だるまの昆布	35%
			get		3	トカゲのしっぽ	35%
			get		3	ネコのひげ	35%
	@@use
		time	2h
		exp		2%
		exptime	30m
		scale	往復
		action	探索しに行く
		name	海辺を探索
		info	いろんな餌が調達できるかもしれません
		ngmsg	なにも見つかりませんでした…
			get		3	へびいちご	70%
			get		3	ツキノハナワラビ	70%
			get		30	雪だるまの昆布	70%	雪だるまの昆布がたくさん見つかりました
			get		3	トカゲのしっぽ	35%
			get		3	ネコのひげ	35%
	@@use
		time	2h
		exp		2%
		exptime	30m
		scale	往復
		action	探索しに行く
		name	岩山を探索
		info	いろんな餌が調達できるかもしれません
		ngmsg	なにも見つかりませんでした…
			get		3	へびいちご	70%
			get		3	ツキノハナワラビ	70%
			get		3	雪だるまの昆布	35%
			get		30	トカゲのしっぽ	70%	トカゲのしっぽをたくさん手に入れました
			get		3	ネコのひげ	35%
	@@use
		time	2h
		exp		2%
		exptime	30m
		scale	往復
		action	探索しに行く
		name	公園を探索
		info	いろんな餌が調達できるかもしれません
		ngmsg	なにも見つかりませんでした…
			get		3	へびいちご	70%
			get		3	ツキノハナワラビ	70%
			get		3	雪だるまの昆布	35%
			get		3	トカゲのしっぽ	35%
			get		30	ネコのひげ	70%	ネコのひげをたくさん手に入れました


@@ITEM
	no		7
	type	火
	code	wisp
	name	ウィスプ
	info	低級召喚魔。浮遊する火の玉
	price	1200
	limit	600
	base	50/100
	plus	-1h
	pop	3h
	scale	匹
	point	120%
	flag	norequest
@@ITEM
	no		8
	type	水
	code	slime
	name	スライム
	info	低級召喚魔。ねばねばした液体
	price	1200
	limit	600
	base	50/100
	plus	-1h
	pop	3h
	scale	匹
	point	120%
	flag	norequest
@@ITEM
	no		9
	type	土
	code	gnome
	name	ノーム
	info	低級召喚魔。親指ほどの小人
	price	1200
	limit	600
	base	50/100
	plus	-1h
	pop	3h
	scale	匹
	point	120%
	flag	norequest
@@ITEM
	no		10
	type	風
	code	sylph
	name	シルフ
	info	低級召喚魔。小さな妖精
	price	1200
	limit	600
	base	50/100
	plus	-1h
	pop	3h
	scale	匹
	point	120%
	flag	norequest
@@ITEM
	no		11
	type	聖
	code	spirit
	name	スピリット
	info	低級召喚魔。浮遊する霊体
	price	1500
	limit	500
	base	50/100
	plus	-1h
	pop	225m
	scale	匹
	point	150%
	flag	norequest
@@ITEM
	no		12
	type	邪
	code	shade
	name	シェイド
	info	低級召喚魔。闇が実体化し浮遊するもの
	price	1500
	limit	500
	base	50/100
	plus	-1h
	pop	225m
	scale	匹
	point	150%
	flag	norequest

@@ITEM
	no		13
	type	火
	code	efreet
	name	イフリート
	info	上級召喚魔。灼熱の魔神
	price	2400
	limit	300
	base	50/100
	plus	-1h
	pop	6h
	scale	匹
	point	200%
	flag	norequest
	@@use
		time	2h
		job		ビーストテイマー	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をイフリートが割ります
		param	卵からサラマンダーが誕生しました！
			use		1	産まれそうな卵
			get		1	サラマンダー
		arg		nocount
		func	memo
@@ITEM
	no		14
	type	水
	code	yeti
	name	イエティ
	info	上級召喚魔。氷河に棲む白い魔獣
	price	2400
	limit	300
	base	50/100
	plus	-1h
	pop	6h
	scale	匹
	point	200%
	flag	norequest
	@@use
		time	2h
		job		ビーストテイマー	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をイエティが割ります
		param	卵からヨルムンガンドが誕生しました！
			use		1	産まれそうな卵
			get		1	ヨルムンガンド
		arg		nocount
		func	memo
@@ITEM
	no		15
	type	土
	code	golem
	name	ゴーレム
	info	上級召喚魔。土で作られた巨人
	price	2400
	limit	300
	base	50/100
	plus	-1h
	pop	6h
	scale	匹
	point	200%
	flag	norequest
	@@use
		time	2h
		job		ビーストテイマー	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をゴーレムが割ります
		param	卵からバジリスクが誕生しました！
			use		1	産まれそうな卵
			get		1	バジリスク
		arg		nocount
		func	memo
@@ITEM
	no		16
	type	風
	code	griffin
	name	グリフォン
	info	上級召喚魔。獅子の胴体に鷲の頭と羽を持つ
	price	2400
	limit	300
	base	50/100
	plus	-1h
	pop	6h
	scale	匹
	point	200%
	flag	norequest
	@@use
		time	2h
		job		ビーストテイマー	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をグリフォンが割ります
		param	卵からテュポーンが誕生しました！
			use		1	産まれそうな卵
			get		1	テュポーン
		arg		nocount
		func	memo
@@ITEM
	no		17
	type	聖
	code	unicorn
	name	ユニコーン
	info	上級召喚魔。長い角を持つ白馬
	price	2400
	limit	300
	base	50/100
	plus	-1h
	pop	6h
	scale	匹
	point	200%
	flag	norequest
	@@use
		time	2h
		job		ビーストテイマー	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をユニコーンが割ります
		param	卵からホワイトスネイクが誕生しました！
			use		1	産まれそうな卵
			get		1	ホワイトスネイク
		arg		nocount
		func	memo
@@ITEM
	no		18
	type	邪
	code	demon
	name	デーモン
	info	上級召喚魔。地獄に棲む魔物
	price	2400
	limit	300
	base	50/100
	plus	-1h
	pop	6h
	scale	匹
	point	200%
	flag	norequest
	@@use
		time	2h
		job		ビーストテイマー	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をデーモンが割ります
		param	卵からプチヒュドラが誕生しました！
			use		1	産まれそうな卵
			get		1	プチヒュドラ
		arg		nocount
		func	memo

@@ITEM
	no		31
	type	火
	code	salamander
	name	サラマンダー
	info	基礎竜。炎に包まれた怪蛇
	price	6000
	limit	150
	base	20/40
	plus	-1h
	pop	12h
	scale	匹
	point	400%
	flag	norequest
	@@use
		time	600
		exp		1%
		exptime	200
		job		ビーストテイマー	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をサラマンダーが割ります
		okmsg	卵からサラマンダーが誕生しました
			use		1	産まれそうな卵
			get		1	サラマンダー
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	積み木遊びを教える
		info	積み木で遊ぶことを教えます
		ngmsg	あまり積み木には興味がないようです…
			need		1	積み木
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	飛行の方法を教える
		info	空を飛ぶことを教えます
		param	31,37,空を飛ぶこと
		func	education
			need		1	飛行のテクニック
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	国際的会話を教える
		info	異文化コミュニケーションを教えます
		ngmsg	あまり会話には興味がないようです…
			need		1	基礎から学ぶＡＢＣ
@@ITEM
	no		32
	type	水
	code	jormungand
	name	ヨルムンガンド
	info	基礎竜。海中に棲む巨大な毒蛇
	price	6000
	limit	150
	base	20/40
	plus	-1h
	pop	12h
	scale	匹
	point	400%
	flag	norequest
	@@use
		time	600
		exp		1%
		exptime	200
		job		ビーストテイマー	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をヨルムンガンドが割ります
		okmsg	卵からヨルムンガンドが誕生しました
			use		1	産まれそうな卵
			get		1	ヨルムンガンド
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	積み木遊びを教える
		info	積み木で遊ぶことを教えます
		ngmsg	あまり積み木には興味がないようです…
			need		1	積み木
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	おしゃれを教える
		info	カガミを使っておしゃれを教えます
		ngmsg	あまりカガミには興味がないようです…
			need		1	カガミ
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	トイレのしつけを教える
		info	おまるの使い方を教えます
		param	32,38,トイレのしつけ
		func	education
			need		1	おまる
@@ITEM
	no		33
	type	土
	code	basilisk
	name	バジリスク
	info	基礎竜。砂漠に棲み石化視線を放つ凶蛇
	price	6000
	limit	150
	base	20/40
	plus	-1h
	pop	12h
	scale	匹
	point	400%
	flag	norequest
	@@use
		time	600
		exp		1%
		exptime	200
		job		ビーストテイマー	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をバジリスクが割ります
		okmsg	卵からバジリスクが誕生しました
			use		1	産まれそうな卵
			get		1	バジリスク
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	積み木遊びを教える
		info	積み木で遊ぶことを教えます
		param	33,39,積み木遊び
		func	education
			need		1	積み木
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	おしゃれを教える
		info	カガミを使っておしゃれを教えます
			need		1	カガミ
			get		50	クロナイム
		func	_local_
			my $ret;
			$ret.="バジリスクはカガミにより自分を石化させてしまいました！";
			UseItem(33,1);
			return $ret;
		_local_
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	飛行の方法を教える
		info	空を飛ぶことを教えます
		ngmsg	あまり飛行には興味がないようです…
			need		1	飛行のテクニック
@@ITEM
	no		34
	type	風
	code	typhon
	name	テュポーン
	info	基礎竜。突風を引き起こす異形の巨蛇
	price	6000
	limit	150
	base	20/40
	plus	-1h
	pop	12h
	scale	匹
	point	400%
	flag	norequest
	@@use
		time	600
		exp		1%
		exptime	200
		job		ビーストテイマー	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をテュポーンが割ります
		okmsg	卵からテュポーンが誕生しました
			use		1	産まれそうな卵
			get		1	テュポーン
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	積み木遊びを教える
		info	積み木で遊ぶことを教えます
		ngmsg	あまり積み木には興味がないようです…
			need		1	積み木
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	トイレのしつけを教える
		info	おまるの使い方を教えます
		ngmsg	あまりおまるには興味がないようです…
			need		1	おまる
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	おしゃれを教える
		info	カガミを使っておしゃれを教えます
		param	34,40,おしゃれ
		func	education
			need		1	カガミ
@@ITEM
	no		35
	type	聖
	code	whitesnake
	name	ホワイトスネイク
	info	基礎竜。幸運をもたらす白蛇
	price	6000
	limit	150
	base	20/40
	plus	-1h
	pop	12h
	scale	匹
	point	400%
	flag	norequest
	@@use
		time	600
		exp		1%
		exptime	200
		job		ビーストテイマー	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をホワイトスネイクが割ります
		okmsg	卵からホワイトスネイクが誕生しました
			use		1	産まれそうな卵
			get		1	ホワイトスネイク
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	トイレのしつけを教える
		info	おまるの使い方を教えます
		ngmsg	あまりおまるには興味がないようです…
			need		1	おまる
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	歩行の方法を教える
		info	あんよの仕方を教えます
		ngmsg	あまりあんよには興味がないようです…
			need		1	あんよがじょうずの本
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	飛行の方法を教える
		info	空を飛ぶことを教えます
		param	35,41,空を飛ぶこと
		func	education
			need		1	飛行のテクニック
@@ITEM
	no		36
	type	邪
	code	petithydra
	name	プチヒュドラ
	info	基礎竜。多数の首を持つ毒蛇
	price	6000
	limit	150
	base	20/40
	plus	-1h
	pop	12h
	scale	匹
	point	400%
	flag	norequest
	@@use
		time	600
		exp		1%
		exptime	200
		job		ビーストテイマー	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をプチヒュドラが割ります
		okmsg	卵からプチヒュドラが誕生しました
			use		1	産まれそうな卵
			get		1	プチヒュドラ
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	歩行の方法を教える
		info	あんよの仕方を教えます
		ngmsg	あまりあんよには興味がないようです…
			need		1	あんよがじょうずの本
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	飛行の方法を教える
		info	空を飛ぶことを教えます
		ngmsg	あまり飛行には興味がないようです…
			need		1	飛行のテクニック
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	国際的会話を教える
		info	異文化コミュニケーションを教えます
		param	36,42,会話の仕方
		func	education
			need		1	基礎から学ぶＡＢＣ
@@ITEM
	no		37
	type	火
	code	lesserropros
	name	レッサーロプロス
	info	中級竜。炎を吐き大空を駆ける翼竜
	price	9600
	limit	100
	base	10/30
	plus	-1h
	pop	18h
	scale	匹
	point	360%
	flag	norequest
	@@use
		time	750
		exp		1%
		exptime	250
		job		ビーストテイマー	times/1.5
		job		ドラゴンテイマー	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をレッサーロプロスが割ります
		okmsg	卵からレッサーロプロスが誕生しました
			use		1	産まれそうな卵
			get		1	レッサーロプロス
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	おしゃれを教える
		info	カガミを使っておしゃれを教えます
		ngmsg	あまりカガミには興味がないようです…
			need		1	カガミ
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	歩行の方法を教える
		info	あんよの仕方を教えます
		ngmsg	あまりあんよには興味がないようです…
			need		1	あんよがじょうずの本
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	国際的会話を教える
		info	異文化コミュニケーションを教えます
		param	37,43,会話の仕方
		func	education
			need		1	基礎から学ぶＡＢＣ
@@ITEM
	no		38
	type	水
	code	leviathan
	name	リヴァイアサン
	info	中級竜。煙を吐く巨大な海竜
	price	9600
	limit	100
	base	10/30
	plus	-1h
	pop	18h
	scale	匹
	point	360%
	flag	norequest
	@@use
		time	750
		exp		1%
		exptime	250
		job		ビーストテイマー	times/1.5
		job		ドラゴンテイマー	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をリヴァイアサンが割ります
		okmsg	卵からリヴァイアサンが誕生しました
			use		1	産まれそうな卵
			get		1	リヴァイアサン
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	歩行の方法を教える
		info	あんよの仕方を教えます
		ngmsg	あまりあんよには興味がないようです…
			need		1	あんよがじょうずの本
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	飛行の方法を教える
		info	空を飛ぶことを教えます
		ngmsg	あまり飛行には興味がないようです…
			need		1	飛行のテクニック
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	高次方程式を教える
		info	高度な数学を教えます
		param	38,44,高度な数学
		func	education
			need		1	高次方程式の解法
@@ITEM
	no		39
	type	土
	code	stoorworm
	name	ストーアウォーム
	info	中級竜。足や翼を持たないが炎を吐く地竜
	price	9600
	limit	100
	base	10/30
	plus	-1h
	pop	18h
	scale	匹
	point	360%
	flag	norequest
	@@use
		time	750
		exp		1%
		exptime	250
		job		ビーストテイマー	times/1.5
		job		ドラゴンテイマー	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をストーアウォームが割ります
		okmsg	卵からストーアウォームが誕生しました
			use		1	産まれそうな卵
			get		1	ストーアウォーム
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	おしゃれを教える
		info	カガミを使っておしゃれを教えます
		ngmsg	あまりカガミには興味がないようです…
			need		1	カガミ
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	歩行の方法を教える
		info	あんよの仕方を教えます
		param	39,45,歩行の方法
		func	education
			need		1	あんよがじょうずの本
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	高次方程式を教える
		info	高度な数学を教えます
		ngmsg	あまり数学には興味がないようです…
			need		1	高次方程式の解法
@@ITEM
	no		40
	type	風
	code	thunderhawk
	name	サンダーホーク
	info	中級竜。鈍色の鱗に稲妻をまとう翼竜
	price	9600
	limit	100
	base	10/30
	plus	-1h
	pop	18h
	scale	匹
	point	360%
	flag	norequest
	@@use
		time	750
		exp		1%
		exptime	250
		job		ビーストテイマー	times/1.5
		job		ドラゴンテイマー	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をサンダーホークが割ります
		okmsg	卵からサンダーホークが誕生しました
			use		1	産まれそうな卵
			get		1	サンダーホーク
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	トイレのしつけを教える
		info	おまるの使い方を教えます
		param	40,46,トイレのしつけ
		func	education
			need		1	おまる
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	国際的会話を教える
		info	異文化コミュニケーションを教えます
		ngmsg	あまり会話には興味がないようです…
			need		1	基礎から学ぶＡＢＣ
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	高次方程式を教える
		info	高度な数学を教えます
		ngmsg	あまり数学には興味がないようです…
			need		1	高次方程式の解法
@@ITEM
	no		41
	type	聖
	code	lindwurm
	name	リンドブルム
	info	中級竜。天空に棲む飛竜
	price	9600
	limit	100
	base	10/30
	plus	-1h
	pop	18h
	scale	匹
	point	360%
	flag	norequest
	@@use
		time	750
		exp		1%
		exptime	250
		job		ビーストテイマー	times/1.5
		job		ドラゴンテイマー	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をリンドブルムが割ります
		okmsg	卵からリンドブルムが誕生しました
			use		1	産まれそうな卵
			get		1	リンドブルム
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	積み木遊びを教える
		info	積み木で遊ぶことを教えます
		ngmsg	あまり積み木には興味がないようです…
			need		1	積み木
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	おしゃれを教える
		info	カガミを使っておしゃれを教えます
		param	41,47,おしゃれ
		func	education
			need		1	カガミ
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	国際的会話を教える
		info	異文化コミュニケーションを教えます
		ngmsg	あまり会話には興味がないようです…
			need		1	基礎から学ぶＡＢＣ
@@ITEM
	no		42
	type	邪
	code	Ladon
	name	ラドン
	info	中級竜。多数の首を持つ毒竜
	price	9600
	limit	100
	base	10/30
	plus	-1h
	pop	18h
	scale	匹
	point	360%
	flag	norequest
	@@use
		time	750
		exp		1%
		exptime	250
		job		ビーストテイマー	times/1.5
		job		ドラゴンテイマー	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をラドンが割ります
		okmsg	卵からラドンが誕生しました
			use		1	産まれそうな卵
			get		1	ラドン
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	積み木遊びを教える
		info	積み木で遊ぶことを教えます
		param	42,48,積み木遊び
		func	education
			need		1	積み木
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	飛行の方法を教える
		info	空を飛ぶことを教えます
		ngmsg	あまり飛行には興味がないようです…
			need		1	飛行のテクニック
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	高次方程式を教える
		info	高度な数学を教えます
		ngmsg	あまり数学には興味がないようです…
			need		1	高次方程式の解法
@@ITEM
	no		43
	type	火
	code	firedragon
	name	ファイアドラゴン
	info	上級竜。炎のブレスを吐く竜
	price	15000
	limit	60
	base	10/20
	plus	-1h
	pop	22h
	scale	匹
	point	240%
	flag	norequest
	@@use
		time	900
		exp		1%
		exptime	300
		job		ドラゴンテイマー	times/1.5
		job		ドラゴンマスター	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をファイアドラゴンが割ります
		okmsg	卵からファイアドラゴンが誕生しました
			use		1	産まれそうな卵
			get		1	ファイアドラゴン
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	おしゃれを教える
		info	カガミを使っておしゃれを教えます
		ngmsg	あまりカガミには興味がないようです…
			need		1	カガミ
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	国際的会話を教える
		info	異文化コミュニケーションを教えます
		ngmsg	あまり会話には興味がないようです…
			need		1	基礎から学ぶＡＢＣ
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	高次方程式を教える
		info	高度な数学を教えます
		param	43,49,高度な数学
		func	education
			need		1	高次方程式の解法
@@ITEM
	no		44
	type	水
	code	colddragon
	name	コールドドラゴン
	info	上級竜。冷気のブレスを吐く竜
	price	15000
	limit	60
	base	10/20
	plus	-1h
	pop	22h
	scale	匹
	point	240%
	flag	norequest
	@@use
		time	900
		exp		1%
		exptime	300
		job		ドラゴンテイマー	times/1.5
		job		ドラゴンマスター	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をコールドドラゴンが割ります
		okmsg	卵からコールドドラゴンが誕生しました
			use		1	産まれそうな卵
			get		1	コールドドラゴン
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	積み木遊びを教える
		info	積み木で遊ぶことを教えます
		ngmsg	あまり積み木には興味がないようです…
			need		1	積み木
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	トイレのしつけを教える
		info	おまるの使い方を教えます
		ngmsg	あまりおまるには興味がないようです…
			need		1	おまる
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	おしゃれを教える
		info	カガミを使っておしゃれを教えます
		param	44,50,おしゃれ
		func	education
			need		1	カガミ
@@ITEM
	no		45
	type	土
	code	earthdragon
	name	アースドラゴン
	info	上級竜。石化のブレスを吐く竜
	price	15000
	limit	60
	base	10/20
	plus	-1h
	pop	22h
	scale	匹
	point	240%
	flag	norequest
	@@use
		time	900
		exp		1%
		exptime	300
		job		ドラゴンテイマー	times/1.5
		job		ドラゴンマスター	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をアースドラゴンが割ります
		okmsg	卵からアースドラゴンが誕生しました
			use		1	産まれそうな卵
			get		1	アースドラゴン
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	トイレのしつけを教える
		info	おまるの使い方を教えます
		ngmsg	あまりおまるには興味がないようです…
			need		1	おまる
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	飛行の方法を教える
		info	空を飛ぶことを教えます
		param	45,51,空を飛ぶこと
		func	education
			need		1	飛行のテクニック
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	高次方程式を教える
		info	高度な数学を教えます
		ngmsg	あまり数学には興味がないようです…
			need		1	高次方程式の解法
@@ITEM
	no		46
	type	風
	code	thunderdragon
	name	サンダードラゴン
	info	上級竜。麻痺のブレスを吐く竜
	price	15000
	limit	60
	base	10/20
	plus	-1h
	pop	22h
	scale	匹
	point	240%
	flag	norequest
	@@use
		time	900
		exp		1%
		exptime	300
		job		ドラゴンテイマー	times/1.5
		job		ドラゴンマスター	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をサンダードラゴンが割ります
		okmsg	卵からサンダードラゴンが誕生しました
			use		1	産まれそうな卵
			get		1	サンダードラゴン
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	歩行の方法を教える
		info	あんよの仕方を教えます
		param	46,52,歩行の方法
		func	education
			need		1	あんよがじょうずの本
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	国際的会話を教える
		info	異文化コミュニケーションを教えます
		ngmsg	あまり会話には興味がないようです…
			need		1	基礎から学ぶＡＢＣ
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	高次方程式を教える
		info	高度な数学を教えます
		ngmsg	あまり数学には興味がないようです…
			need		1	高次方程式の解法
@@ITEM
	no		47
	type	聖
	code	holydragon
	name	ホーリードラゴン
	info	上級竜。誘惑のブレスを吐く竜
	price	15000
	limit	60
	base	10/20
	plus	-1h
	pop	22h
	scale	匹
	point	240%
	flag	norequest
	@@use
		time	900
		exp		1%
		exptime	300
		job		ドラゴンテイマー	times/1.5
		job		ドラゴンマスター	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をホーリードラゴンが割ります
		okmsg	卵からホーリードラゴンが誕生しました
			use		1	産まれそうな卵
			get		1	ホーリードラゴン
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	おしゃれを教える
		info	カガミを使っておしゃれを教えます
		ngmsg	あまりカガミには興味がないようです…
			need		1	カガミ
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	トイレのしつけを教える
		info	おまるの使い方を教えます
		ngmsg	あまりおまるには興味がないようです…
			need		1	おまる
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	国際的会話を教える
		info	異文化コミュニケーションを教えます
		param	47,53,会話の仕方
		func	education
			need		1	基礎から学ぶＡＢＣ
@@ITEM
	no		48
	type	邪
	code	deathdragon
	name	デスドラゴン
	info	上級竜。即死のブレスを吐く竜
	price	15000
	limit	60
	base	10/20
	plus	-1h
	pop	22h
	scale	匹
	point	240%
	flag	norequest
	@@use
		time	900
		exp		1%
		exptime	300
		job		ドラゴンテイマー	times/1.5
		job		ドラゴンマスター	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をデスドラゴンが割ります
		okmsg	卵からデスドラゴンが誕生しました
			use		1	産まれそうな卵
			get		1	デスドラゴン
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	積み木遊びを教える
		info	積み木で遊ぶことを教えます
		ngmsg	あまり積み木には興味がないようです…
			need		1	積み木
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	おしゃれを教える
		info	カガミを使っておしゃれを教えます
		ngmsg	あまりカガミには興味がないようです…
			need		1	カガミ
	@@use
		time	2h
		exp		1%
		arg	nocount
		scale	回
		action	教育する
		name	トイレのしつけを教える
		info	おまるの使い方を教えます
		param	48,54,トイレのしつけ
		func	education
			need		1	おまる
@@ITEM
	no		49
	type	火
	code	flarebrass
	name	フレアブラス
	info	最上級竜。吐く炎は一瞬にして辺りを灼熱に包む
	price	24000
	limit	40
	base	6/12
	plus	-1h
	pop	32h
	scale	匹
	point	200%
	flag	norequest
	@@use
		time	960
		exp		1%
		exptime	320
		job		ドラゴンマスター	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をフレアブラスが割ります
		okmsg	卵からフレアブラスが誕生しました
			use		1	産まれそうな卵
			get		1	フレアブラス
	@@USE
		time	6h
		exp	1%
		arg	nocount|message20
		scale	回
		action	というドラゴンを開発
		name	新種を開発する
		info	様々な教育によりオリジナルドラゴンへと育てます
		param	dmaster,49,55		# ドラゴンマスターのアビリティ
		func	newdragon
			needjob	ドラゴンマスター
			need		1	積み木
			need		1	カガミ
			need		1	おまる
			need		1	あんよがじょうずの本
			need		1	飛行のテクニック
			need		1	基礎から学ぶＡＢＣ
			need		1	高次方程式の解法
@@ITEM
	no		50
	type	水
	code	luciferclaw
	name	ルシファークロー
	info	最上級竜。爪の一掻きは辺りを一瞬で凍えさせる
	price	24000
	limit	40
	base	6/12
	plus	-1h
	pop	32h
	scale	匹
	point	200%
	flag	norequest
	@@use
		time	960
		exp		1%
		exptime	320
		job		ドラゴンマスター	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をルシファークローが割ります
		okmsg	卵からルシファークローが誕生しました
			use		1	産まれそうな卵
			get		1	ルシファークロー
	@@USE
		time	6h
		exp	1%
		arg	nocount|message20
		argmessage	ドラゴンの名前
		scale	回
		action	というドラゴンを開発
		name	新種を開発する
		info	様々な教育によりオリジナルドラゴンへと育てます
		param	dmaster,50,56		# ドラゴンマスターのアビリティ
		func	newdragon
			needjob	ドラゴンマスター
			need		1	積み木
			need		1	カガミ
			need		1	おまる
			need		1	あんよがじょうずの本
			need		1	飛行のテクニック
			need		1	基礎から学ぶＡＢＣ
			need		1	高次方程式の解法
@@ITEM
	no		51
	type	土
	code	zahhaku
	name	ザッハーク
	info	最上級竜。その力はあらゆるものを破壊しつくす
	price	24000
	limit	40
	base	6/12
	plus	-1h
	pop	32h
	scale	匹
	point	200%
	flag	norequest
	@@use
		time	960
		exp		1%
		exptime	320
		job		ドラゴンマスター	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をザッハークが割ります
		okmsg	卵からザッハークが誕生しました
			use		1	産まれそうな卵
			get		1	ザッハーク
	@@USE
		time	6h
		exp	1%
		arg	nocount|message20
		argmessage	ドラゴンの名前
		scale	回
		action	というドラゴンを開発
		name	新種を開発する
		info	様々な教育によりオリジナルドラゴンへと育てます
		param	dmaster,51,57		# ドラゴンマスターのアビリティ
		func	newdragon
			needjob	ドラゴンマスター
			need		1	積み木
			need		1	カガミ
			need		1	おまる
			need		1	あんよがじょうずの本
			need		1	飛行のテクニック
			need		1	基礎から学ぶＡＢＣ
			need		1	高次方程式の解法
@@ITEM
	no		52
	type	風
	code	quetzalcoatl
	name	ケツァルコアトル
	info	最上級竜。その翼はあらゆるものを吹き飛ばす
	price	24000
	limit	40
	base	6/12
	plus	-1h
	pop	32h
	scale	匹
	point	200%
	flag	norequest
	@@use
		time	960
		exp		1%
		exptime	320
		job		ドラゴンマスター	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をケツァルコアトルが割ります
		okmsg	卵からケツァルコアトルが誕生しました
			use		1	産まれそうな卵
			get		1	ケツァルコアトル
	@@USE
		time	6h
		exp	1%
		arg	nocount|message20
		argmessage	ドラゴンの名前
		scale	回
		action	というドラゴンを開発
		name	新種を開発する
		info	様々な教育によりオリジナルドラゴンへと育てます
		param	dmaster,52,58		# ドラゴンマスターのアビリティ
		func	newdragon
			needjob	ドラゴンマスター
			need		1	積み木
			need		1	カガミ
			need		1	おまる
			need		1	あんよがじょうずの本
			need		1	飛行のテクニック
			need		1	基礎から学ぶＡＢＣ
			need		1	高次方程式の解法
@@ITEM
	no		53
	type	聖
	code	bahamut
	name	バハムート
	info	最上級竜。その光はあらゆるものを畏怖させる
	price	24000
	limit	40
	base	6/12
	plus	-1h
	pop	32h
	scale	匹
	point	200%
	flag	norequest
	@@use
		time	960
		exp		1%
		exptime	320
		job		ドラゴンマスター	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をバハムートが割ります
		okmsg	卵からバハムートが誕生しました
			use		1	産まれそうな卵
			get		1	バハムート
	@@USE
		time	6h
		exp	1%
		arg	nocount|message20
		argmessage	ドラゴンの名前
		scale	回
		action	というドラゴンを開発
		name	新種を開発する
		info	様々な教育によりオリジナルドラゴンへと育てます
		param	dmaster,53,59		# ドラゴンマスターのアビリティ
		func	newdragon
			needjob	ドラゴンマスター
			need		1	積み木
			need		1	カガミ
			need		1	おまる
			need		1	あんよがじょうずの本
			need		1	飛行のテクニック
			need		1	基礎から学ぶＡＢＣ
			need		1	高次方程式の解法
@@ITEM
	no		54
	type	邪
	code	tiamat
	name	ティアマット
	info	最上級竜。無限の魔法はあらゆるものを滅ぼす
	price	24000
	limit	40
	base	6/12
	plus	-1h
	pop	32h
	scale	匹
	point	200%
	flag	norequest
	@@use
		time	960
		exp		1%
		exptime	320
		job		ドラゴンマスター	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をティアマットが割ります
		okmsg	卵からティアマットが誕生しました
			use		1	産まれそうな卵
			get		1	ティアマット
	@@USE
		time	6h
		exp	1%
		arg	nocount|message20
		argmessage	ドラゴンの名前
		scale	回
		action	というドラゴンを開発
		name	新種を開発する
		info	様々な教育によりオリジナルドラゴンへと育てます
		param	dmaster,54,60		# ドラゴンマスターのアビリティ
		func	newdragon
			needjob	ドラゴンマスター
			need		1	積み木
			need		1	カガミ
			need		1	おまる
			need		1	あんよがじょうずの本
			need		1	飛行のテクニック
			need		1	基礎から学ぶＡＢＣ
			need		1	高次方程式の解法
@@ITEM
	no		55
	type	火
	code	original-fire
	name	オリジナルドラゴン（火）
	info	オリジナルドラゴン
	price	30000
	limit	30
	base	5/10
	plus	-1h
	pop	40h
	scale	匹
	point	300%
	flag	norequest
	@@use
		time	960
		exp		1%
		exptime	320
		job		ドラゴンマスター	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をオリジナルドラゴン（火）が割ります
		okmsg	卵からオリジナルドラゴン（火）が誕生しました
			use		1	産まれそうな卵
			get		1	オリジナルドラゴン（火）
@@ITEM
	no		56
	type	水
	code	original-cold
	name	オリジナルドラゴン（水）
	info	オリジナルドラゴン
	price	30000
	limit	30
	base	5/10
	plus	-1h
	pop	40h
	scale	匹
	point	300%
	flag	norequest
	@@use
		time	960
		exp		1%
		exptime	320
		job		ドラゴンマスター	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をオリジナルドラゴン（水）が割ります
		okmsg	卵からオリジナルドラゴン（水）が誕生しました
			use		1	産まれそうな卵
			get		1	オリジナルドラゴン（水）
@@ITEM
	no		57
	type	土
	code	original-earth
	name	オリジナルドラゴン（土）
	info	オリジナルドラゴン
	price	30000
	limit	30
	base	5/10
	plus	-1h
	pop	40h
	scale	匹
	point	300%
	flag	norequest
	@@use
		time	960
		exp		1%
		exptime	320
		job		ドラゴンマスター	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をオリジナルドラゴン（土）が割ります
		okmsg	卵からオリジナルドラゴン（土）が誕生しました
			use		1	産まれそうな卵
			get		1	オリジナルドラゴン（土）
@@ITEM
	no		58
	type	風
	code	original-thunder
	name	オリジナルドラゴン（風）
	info	オリジナルドラゴン
	price	30000
	limit	30
	base	5/10
	plus	-1h
	pop	40h
	scale	匹
	point	300%
	flag	norequest
	@@use
		time	960
		exp		1%
		exptime	320
		job		ドラゴンマスター	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をオリジナルドラゴン（風）が割ります
		okmsg	卵からオリジナルドラゴン（風）が誕生しました
			use		1	産まれそうな卵
			get		1	オリジナルドラゴン（風）
@@ITEM
	no		59
	type	聖
	code	original-holy
	name	オリジナルドラゴン（聖）
	info	オリジナルドラゴン
	price	30000
	limit	30
	base	5/10
	plus	-1h
	pop	40h
	scale	匹
	point	300%
	flag	norequest
	@@use
		time	960
		exp		1%
		exptime	320
		job		ドラゴンマスター	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をオリジナルドラゴン（聖）が割ります
		okmsg	卵からオリジナルドラゴン（聖）が誕生しました
			use		1	産まれそうな卵
			get		1	オリジナルドラゴン（聖）
@@ITEM
	no		60
	type	邪
	code	original-death
	name	オリジナルドラゴン（邪）
	info	オリジナルドラゴン
	price	30000
	limit	30
	base	5/10
	plus	-1h
	pop	40h
	scale	匹
	point	300%
	flag	norequest
	@@use
		time	960
		exp		1%
		exptime	320
		job		ドラゴンマスター	times/1.5
		scale	個
		action	開始
		name	卵の殻を割ってもらう
		info	産まれそうな卵の殻をオリジナルドラゴン（邪）が割ります
		okmsg	卵からオリジナルドラゴン（邪）が誕生しました
			use		1	産まれそうな卵
			get		1	オリジナルドラゴン（邪）

@@ITEM
	no		61
	type	道具
	code	wonderegg
	name	不思議な卵
	info	秘術によりもたらされた竜の卵
	price	900
	limit	500/1
	pop	1d
	plus	-1h
	base	200/1000
	scale	個
	@@USE
		time	20m
		scale	回
		action	調べる
		arg	nocount
		name	卵をかえす方法を調べる
		info	どうやってドラゴンを育成するか知りたいときに
		func	_local_
			my $ret;
			$ret.="突然，卵の背後からモクモクと煙が噴き出し，老人が現れた。<br><br>";
			$ret.="<TABLE><tr><td>";
			$ret.=main::GetTagImgKao('ラムウ','ram')."不思議な老人：<br>";
			$ret.="…ふむ，卵からドラゴンを育てたいというのじゃな。<br>";
			$ret.="ある草を敷いて卵を温めると，やがて卵はかえるはずじゃ。<br>";
			$ret.="その後のことは，図書館に行って自分で勉強せい。<br>";
			$ret.="さもないと，育てるのに失敗して大変なことになるぞい。";
			$ret.="</td></tr></table><br>";
			$ret.="一通り話し終えると，老人は煙の中に消えていった。";
			return $ret;
		_local_
	@@use
		time	9m
		exp		1%
		exptime	3m
		job		ビーストテイマー	times/1.5
		scale	個
		action	開始
		name	卵を温める
		info	草を敷いて卵を温めます
		okmsg	後はこのまま卵がかえるのを待つばかりです
			use		1	不思議な卵
			use		1	ツキノハナワラビ
			get		1	温められている卵
@@ITEM
	no		62
	type	道具
	code	warmedegg
	name	温められている卵
	info	もう少し待てばヒナが生まれそうです
	price	0
	limit	500
	pop	10d
	plus	-1h
	scale	個
	cost	100
	flag	noshowcase|norequest
@@ITEM
	no		63
	type	道具
	code	borneegg
	name	産まれそうな卵
	info	魔獣が殻を割ってあげる必要があります
	price	0
	limit	500
	pop	10d
	plus	-1h
	scale	個
	cost	100
	flag	noshowcase|norequest

@@ITEM
	no	19
	type	道具
	code	circle
	name	魔方陣
	info	触媒を使って召喚魔を呼び出すのに必要です
	price	0
	cost	500
	limit	1/1
	pop	0
	scale	個
	plus	2h
	flag	noshowcase|norequest
	@@USE
		time	20m
		scale	回
		action	調べる
		arg	nocount
		name	召喚の仕方を調べる
		info	どうやってモンスターを召喚するか知りたいときに
		func	_local_
			my $ret;
			$ret.="突然，魔方陣からモクモクと煙が噴き出し，老人が現れた。<br><br>";
			$ret.="<TABLE><tr><td>";
			$ret.=main::GetTagImgKao('ラムウ','ram')."不思議な老人：<br>";
			$ret.="…召喚の仕方が分からんじゃと。図書館に書いてあるのにのう。<br>";
			$ret.="ひとまず，近くの洞窟への地図を使って触媒を集めなされ。<br>";
			$ret.="そして，集めた触媒を使用して，召喚を行うのじゃ。<br>";
			$ret.="詳しくは[城下町]にある図書館でよく調べるとよいぞ。";
			$ret.="</td></tr></table><br>";
			$ret.="一通り話し終えると，老人は煙の中に消えていった。";
			return $ret;
		_local_

@@ITEM
	no		30
	type	道具
	code	catalyst-trans
	name	触媒の秘法
	info	修行により触媒の熟練度を移動させます
	price	25000
	limit	50/2
	pop	48h
	base	80/200
	scale	冊
	plus	-1h
	point	500%
	@@USE
		time	6h
		scale	回
		action	修行開始
		arg	nocount
		name	ディズマルへ移動させる
		info	他の触媒の熟練度を捨て，ディズマルの熟練度にします
		okmsg	ディズマルの扱い方が分かったような気がします
		param	1,2:3:4:5:6,0.5
			use		1	触媒の秘法
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
			return $ret;
		_local_
	@@USE
		time	6h
		action	修行開始
		arg	nocount
		name	ジェムストーンへ移動させる
		info	他の触媒の熟練度を捨て，ジェムストーンの熟練度にします
		okmsg	ジェムストーンの扱い方が分かったような気がします
		func	_local_1
		param	2,1:3:4:5:6,0.5
			use		1	触媒の秘法
	@@USE
		time	6h
		action	修行開始
		arg	nocount
		name	クロナイムへ移動させる
		info	他の触媒の熟練度を捨て，クロナイムの熟練度にします
		okmsg	クロナイムの扱い方が分かったような気がします
		func	_local_1
		param	3,1:2:4:5:6,0.5
			use		1	触媒の秘法
	@@USE
		time	6h
		action	修行開始
		arg	nocount
		name	フィエルへ移動させる
		info	他の触媒の熟練度を捨て，フィエルの熟練度にします
		okmsg	フィエルの扱い方が分かったような気がします
		func	_local_1
		param	4,1:2:3:5:6,0.5
			use		1	触媒の秘法
	@@USE
		time	6h
		action	修行開始
		arg	nocount
		name	クリスタルへ移動させる
		info	他の触媒の熟練度を捨て，クリスタルの熟練度にします
		okmsg	クリスタルの扱い方が分かったような気がします
		func	_local_1
		param	5,1:2:3:4:6,0.5
			use		1	触媒の秘法
	@@USE
		time	6h
		action	修行開始
		arg	nocount
		name	ヴェルデュールへ移動させる
		info	他の触媒の熟練度を捨て，ヴェルデュールの熟練度にします
		okmsg	ヴェルデュールの扱い方が分かったような気がします
		func	_local_1
		param	6,1:2:3:4:5,0.5
			use		1	触媒の秘法

@@ITEM
	no		64
	type	道具
	code	dragonomabook
	name	ドラゴノーマの法典
	info	竜を生む方法が記された最先端研究書
	price	50000
	cost	1000
	limit	25/1.2
	pop	80h
	plus	-1h
	base	40/100
	scale	冊
	point	500%
	@@USE
		time	20m
		scale	回
		action	調べる
		arg	nocount
		name	竜を生む方法を調べる
		info	どうやってドラゴンを育成するか知りたいときに
		func	_local_
			my $ret;
			$ret.="突然，本の中からモクモクと煙が噴き出し，老人が現れた。<br><br>";
			$ret.="<TABLE><tr><td>";
			$ret.=main::GetTagImgKao('ラムウ','ram')."不思議な老人：<br>";
			$ret.="…ふむ，ドラゴンの育成を始めたいというのじゃな。<br>";
			$ret.="まずは，卵を召喚してみたらどうじゃ。<br>";
			$ret.="触媒が一通り揃っておるならば，この本を使って，<br>";
			$ret.="魔方陣から卵を呼び出すことができるはずだがのう。";
			$ret.="</td></tr></table><br>";
			$ret.="一通り話し終えると，老人は煙の中に消えていった。";
			return $ret;
		_local_
	@@USE
		time	20m
		scale	回
		action	調べる
		arg	nocount
		name	餌の量を確認する
		info	ドラゴンの餌が十分にあるか調べます
		func	feedcheck
	@@use
		time	1h
		exp		2%
		exptime	20m
		job		シャーマン	times/1.5
		job		ウォーロック	times/1.5
		scale	回
		action	生み出す
		name	竜の卵を生み出す
		info	魔法の力で竜の卵を生み出します
		okmsg	不思議な卵を生み出しました
		ngmsg	何も起こりませんでした…
			need		1	魔方陣
			use		3	ディズマル
			use		3	ジェムストーン
			use		3	クロナイム
			use		3	フィエル
			use		3	クリスタル
			use		3	ヴェルデュール
			get		20	不思議な卵	85%

@@ITEM
	no		65
	type	道具
	code	jobchange
	name	職業の秘密
	info	様々なジョブに就くための本
	price	25000
	limit	50/2
	pop	48h
	base	80/200
	scale	冊
	plus	-1h
	point	500%
	@@USE
		time	6h
		action	ジョブチェンジ
		scale	回
		arg		nocount
		name	ウォーロック
		info	ウォーロックにジョブチェンジします
		param	0,20,warlock,base
		funcb	jobcheck
			use		1	職業の秘密
		func	jobport
	@@USE
		time	6h
		action	ジョブチェンジ
		scale	回
		arg		nocount
		name	シャーマン
		info	シャーマンにジョブチェンジします
		param	0,1:2:3:4:5:6,shaman,base
		funcb	jobcheck
			use		1	職業の秘密
		func	jobport
	@@USE
		time	6h
		action	ジョブチェンジ
		scale	回
		arg		nocount
		name	トレジャーハンター
		info	トレジャーハンターにジョブチェンジします
		param	0,21:22,thunter,base
		funcb	jobcheck
			use		1	職業の秘密
		func	jobport
	@@USE
		time	6h
		action	ジョブチェンジ
		scale	回
		arg		nocount
		name	トレードマスター
		info	トレードマスターにジョブチェンジします
		param	0,23,peddle,base
		funcb	jobcheck
			use		1	職業の秘密
		func	jobport
	@@USE
		time	6h
		action	ジョブチェンジ
		scale	回
		arg		nocount
		name	ビーストテイマー
		info	ビーストテイマーにジョブチェンジします
		param	0,31:32:33:34:35:36,btamer,base
		funcb	jobcheck
			use		1	職業の秘密
		func	jobport
	@@USE
		time	6h
		action	ジョブチェンジ
		scale	回
		arg		nocount
		name	ドラゴンテイマー
		info	ドラゴンテイマーにジョブチェンジします
		param	0,37:38:39:40:41:42,dtamer,btamer
		funcb	jobcheck
			use		1	職業の秘密
		func	jobport
	@@USE
		time	6h
		action	ジョブチェンジ
		scale	回
		arg		nocount
		name	ドラゴンマスター
		info	ドラゴンマスターにジョブチェンジします
		param	0,49:50:51:52:53:54,dmaster,dtamer
		funcb	jobcheck
			use		1	職業の秘密
		func	jobport

@@ITEM
	no		66
	type	魔餌
	code	strawberry
	name	へびいちご
	info	野原に生える小さないちご
	price	100
	limit	2000/500
	pop	10d
	plus	-20m
	base	100/700
	scale	個
	cost	30
	point	50%
@@ITEM
	no		67
	type	魔餌
	code	bracken
	name	ツキノハナワラビ
	info	森林に生える小さなシダ
	price	100
	limit	2000/500
	pop	10d
	plus	-20m
	base	100/700
	scale	本
	cost	30
	point	50%
@@ITEM
	no		68
	type	魔餌
	code	seatangle
	name	雪だるまの昆布
	info	浅瀬に生える小さな昆布
	price	200
	limit	1000/250
	pop	10d
	plus	-20m
	base	100/700
	scale	枚
	cost	50
	point	50%
@@ITEM
	no		69
	type	魔餌
	code	lizard
	name	トカゲのしっぽ
	info	トカゲの落とし物
	price	200
	limit	1000/250
	pop	10d
	plus	-20m
	base	100/700
	scale	本
	cost	50
	point	50%
@@ITEM
	no		70
	type	魔餌
	code	mustache
	name	ネコのひげ
	info	ネコの落とし物
	price	200
	limit	1000/250
	pop	10d
	plus	-20m
	base	100/700
	scale	本
	cost	50
	point	50%
@@ITEM
	no		71
	type	魔餌
	code	brownrice
	name	玄米フレーク
	info	住人も好んで食べる
	price	400
	limit	800/800
	pop	80m
	plus	2h
	base	100/10000
	scale	食
	cost	20
@@ITEM
	no		72
	type	魔餌
	code	curry
	name	カレーライス
	info	住人も好んで食べる
	price	400
	limit	800/800
	pop	80m
	plus	2h
	base	100/10000
	scale	食
	cost	20


@@ITEM
	no		23
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
		job		トレードマスター	times/1.5
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
	no		24
	type	道具
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
		job		トレードマスター	times/1.5
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
		job		トレードマスター	times/1.5
		scale	回
		action	働く
		name	日雇い土木作業で資金稼ぎ
		info	ちょっときついけどそこそこの稼ぎです
		param	10000
		func	_local_1

@@ITEM
	no		25
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
	no		26
	type	道具
	code	badgossip
	name	禁断の書
	info	やってはならないがやらなくてはならないときに…
	price	25000
	limit	50/1.2
	pop	40h
	plus	-1h
	base	40/100
	scale	冊
	point	500%
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
		func	stole
		arg		target|nocount
			needpoint	20000

@@ITEM
	no		27
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
			get		1	ギフト券			10%		ギフト券が当たりました！
			get		1	広告パック			10%		広告パックが当たりました！
			get		1	積み木				10%		積み木が当たりました！
			get		1	カガミ				10%		カガミが当たりました！
			get		1	おまる				10%		おまるが当たりました！
			get		1	あんよがじょうずの本		10%		あんよがじょうずの本が当たりました！
			get		1	飛行のテクニック		10%		飛行のテクニックが当たりました！
			get		1	基礎から学ぶＡＢＣ		10%		基礎から学ぶＡＢＣが当たりました！
			get		1	高次方程式の解法		10%		高次方程式の解法が当たりました！

@@ITEM
	no		28
	type	道具
	code	gift
	name	ギフト券
	info	欲しいものを手に入れよう！
	price	50000
	cost	10
	limit	10/0
	scale	枚
	pop	10d
	flag	noshowcase
	@@USE
		time	20m
		action	引き換え
		name	召喚セットと引き換え
		info	召喚に必要な物の詰め合わせです
		okmsg	ご利用ありがとうございました
			use		1	ギフト券
			get		1	近くの洞窟への地図
			get		1	魔方陣
	@@USE
		time	20m
		action	引き換え
		name	くじ引き券と引き換え
		info	ギャンブルに走りたい人へ
		okmsg	ご利用ありがとうございました
			use		2	ギフト券
			get		5	くじ引き券
	@@USE
		time	20m
		action	引き換え
		name	広告パックと引き換え
		info	もっと人気を得たい人へ
		okmsg	ご利用ありがとうございました
			use		2	ギフト券
			get		1	広告パック
	@@USE
		time	20m
		action	引き換え
		name	遊び道具と引き換え
		info	ドラゴンに遊びを教えたい人へ
		okmsg	ご利用ありがとうございました
			use		2	ギフト券
			get		1	積み木
	@@USE
		time	20m
		action	引き換え
		name	しつけ道具と引き換え
		info	ドラゴンにしつけを教えたい人へ
		okmsg	ご利用ありがとうございました
			use		3	ギフト券
			get		1	おまる
			get		1	カガミ
	@@USE
		time	20m
		action	引き換え
		name	練習道具と引き換え
		info	ドラゴンに運動を教えたい人へ
		okmsg	ご利用ありがとうございました
			use		3	ギフト券
			get		1	あんよがじょうずの本
			get		1	飛行のテクニック
	@@USE
		time	20m
		action	引き換え
		name	勉強道具と引き換え
		info	ドラゴンに勉強を教えたい人へ
		okmsg	ご利用ありがとうございました
			use		3	ギフト券
			get		1	基礎から学ぶＡＢＣ
			get		1	高次方程式の解法

@@ITEM
	no		29
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
	no		73
	type	道具
	code	tsumiki
	name	積み木
	info	ドラゴンの遊び道具
	price	100000
	limit	1/1
	pop	0
	plus	-2m
	base	200/400
	scale	個
	cost	100
@@ITEM
	no		74
	type	道具
	code	kagami
	name	カガミ
	info	ドラゴンのおしゃれ道具
	price	100000
	limit	1/1
	pop	0
	plus	-2m
	base	200/400
	scale	個
	cost	100
@@ITEM
	no		75
	type	道具
	code	omaru
	name	おまる
	info	ドラゴンのしつけ道具
	price	100000
	limit	1/1
	pop	0
	plus	-2m
	base	200/400
	scale	個
	cost	100
@@ITEM
	no		76
	type	道具
	code	anyojouzu
	name	あんよがじょうずの本
	info	ドラゴンの歩行練習道具
	price	100000
	limit	1/1
	pop	0
	plus	-2m
	base	200/400
	scale	冊
	cost	100
@@ITEM
	no		77
	type	道具
	code	flytech
	name	飛行のテクニック
	info	ドラゴンの飛行練習道具
	price	100000
	limit	1/1
	pop	0
	plus	-2m
	base	200/400
	scale	冊
	cost	100
@@ITEM
	no		78
	type	道具
	code	abcbook
	name	基礎から学ぶＡＢＣ
	info	ドラゴンの勉強道具
	price	100000
	limit	1/1
	pop	0
	plus	-2m
	base	200/400
	scale	冊
	cost	100
@@ITEM
	no		79
	type	道具
	code	houteishiki
	name	高次方程式の解法
	info	ドラゴンの勉強道具
	price	100000
	limit	1/1
	pop	0
	plus	-2m
	base	200/400
	scale	冊
	cost	100


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
	start		30%
	basetime	6h
	plustime	24h
	code		fire-sale
	group		sale
	startmsg	暖かい火属性のモンスターが話題になっています。
	info		火属性の需要が高まっています。
		param	ウィスプ		pop/2
		param	イフリート		pop/2
		param	サラマンダー		pop/2
		param	レッサーロプロス	pop/3
		param	ファイアドラゴン	pop/3
		param	フレアブラス		pop/3
		param	オリジナルドラゴン（火）	pop/3
@@EVENT
	start		30%
	basetime	6h
	plustime	24h
	code		cold-sale
	group		sale
	startmsg	冷たい水属性のモンスターが話題になっています。
	info		水属性の需要が高まっています。
		param	スライム		pop/2
		param	イエティ		pop/2
		param	ヨルムンガンド		pop/2
		param	リヴァイアサン		pop/3
		param	コールドドラゴン	pop/3
		param	ルシファークロー	pop/3
		param	オリジナルドラゴン（水）	pop/3
@@EVENT
	start		30%
	basetime	6h
	plustime	24h
	code		earth-sale
	group		sale
	startmsg	鈍重な土属性のモンスターが話題になっています。
	info		土属性の需要が高まっています。
		param	ノーム			pop/2
		param	ゴーレム		pop/2
		param	バジリスク		pop/2
		param	ストーアウォーム	pop/3
		param	アースドラゴン		pop/3
		param	ザッハーク		pop/3
		param	オリジナルドラゴン（土）	pop/3
@@EVENT
	start		30%
	basetime	6h
	plustime	24h
	code		thunder-sale
	group		sale
	startmsg	爽快な風属性のモンスターが話題になっています。
	info		風属性の需要が高まっています。
		param	シルフ			pop/2
		param	グリフォン		pop/2
		param	テュポーン		pop/2
		param	サンダーホーク		pop/3
		param	サンダードラゴン	pop/3
		param	ケツァルコアトル	pop/3
		param	オリジナルドラゴン（風）	pop/3

@@EVENT
	start		30%
	basetime	6h
	plustime	24h
	code		sale-item
	group		bazar
	startmsg	市場でバザーが始まりました。
	info		市場でバザーが行われています。
		param	積み木			plus=2400		#★市場への入荷ペース。
		param	カガミ			plus=2400
		param	おまる			plus=2400

@@EVENT
	start		30%
	basetime	6h
	plustime	24h
	code		sale-book
	group		bazar
	startmsg	市場でセールが始まりました。
	info		市場でセールが行われています。
		param	あんよがじょうずの本			plus=2400		#★市場への入荷ペース。
		param	飛行のテクニック			plus=2400
		param	基礎から学ぶＡＢＣ			plus=2400
		param	高次方程式の解法			plus=2400

@@EVENT
	start		150%
	basetime	0h		#★持続系のイベントではないので時間は0。
	plustime	0h
	code		dragonborn
	info		ドラゴン誕生
	startfunc	_local_
		#★実はこの関数がイベントの本体になってる
		my $itemno=@@ITEMNO"温められている卵";
		my $itemto=@@ITEMNO"産まれそうな卵";
		foreach my $DT (@DT)
		{
			next if !$DT->{item}[$itemno-1];
			my $cnt=$DT->{item}[$itemno-1];
			$cnt=$ITEM[$itemto]->{limit}-$DT->{item}[$itemto-1] if $DT->{item}[$itemto-1]+$cnt>$ITEM[$itemto]->{limit};
			$DT->{item}[$itemno-1]-=$cnt;
			$DT->{item}[$itemto-1]+=$cnt;	#産まれそうな卵
		}
		return 0;
	_local_


@@FUNCINIT
#目利きの真髄を持っている場合、買い物に必要な時間を3/4にする。
#$TIME_SEND_ITEM=int($TIME_SEND_ITEM/4*3) if $DT->{item}[@@ITEMNO"目利きの真髄"-1];

#職業が「トレードマスター」の場合、買い物に必要な時間を1/2にする。
$TIME_SEND_ITEM=int($TIME_SEND_ITEM/2) if $DT->{job} eq 'peddle';

@@FUNCITEM
######################################################################
# ★ジョブチェンジチェック
######################################################################
sub jobcheck
{
my($USE)=@_;
return 1 if ($DT->{job} eq $USE->{param3});
return 1 if ($USE->{param4} ne "base")&&($DT->{job} eq '');
return 1 if ($USE->{param4} ne "base")&&($USE->{param4} !~ /$DT->{job}/);
foreach my $exps (split(/:/,$USE->{param2}))
	{
	return 0 if ($DT->{exp}{$exps} > 750);
	}
return 1;
}

######################################################################
# ★ジョブチェンジ
######################################################################
sub jobport
{
	$DT->{job}=$USE->{param3};
	WriteLog(3,0,$DT->{shopname}.'のジョブが「'.$main::JOBTYPE{$USE->{param3}}.'」になりました。');

	my $ret;
	$ret.="本を片手に転職の神殿へと向かった。<br><br>";
	$ret.="<TABLE><tr><td>";
	$ret.=main::GetTagImgKao('アムザ','amza')."神官アムザ：<br>";
	$ret.="…ふむ。".$main::JOBTYPE{$USE->{param3}}."になりたいというのですね。<br>";
	$ret.='さすれば，全知全能の神よ！<br>いまここに<b>'.$DT->{shopname}."</b>が<br>";
	$ret.=$main::JOBTYPE{$USE->{param3}}."の道を歩むことを許したまえ！";
	$ret.="</td></tr></table><br>";

	$ret.="ジョブが".$main::JOBTYPE{$USE->{param3}}."になりました。";
	return $ret;
}

######################################################################
#★お手伝いひとくちメモ
######################################################################
sub memo
{
	my $ret;
	$ret.=$USE->{param1}."<br><br>";
	$ret.="<TABLE><tr><td>";
	$ret.=main::GetTagImgKao('お手伝い','help')."お手伝い：<br>";
	$ret.="店長さま，新しいドラゴンの誕生おめでとうございます。<br>";
	$ret.="一度ドラゴンの新種が誕生してしまえば，どうやら<br>";
	$ret.="そのドラゴンが卵の殻を割ることで，同じ種類の<br>";
	$ret.="ドラゴンをどんどん増やせるようですよ。";
	$ret.="</td></tr></table>";
	return $ret;
}

######################################################################
#★お手伝いエサチェック
######################################################################
sub feedcheck
{
	my @FEED=(
		[
			@@ITEMNO "へびいちご",
			[@@ITEMNO "ホワイトスネイク",@@ITEMNO "リンドブルム",@@ITEMNO "ホーリードラゴン",
			@@ITEMNO "ケツァルコアトル",@@ITEMNO "オリジナルドラゴン（聖）",]
		],
		[
			@@ITEMNO "雪だるまの昆布",
			[@@ITEMNO "ヨルムンガンド",@@ITEMNO "ラドン",@@ITEMNO "デスドラゴン",
			@@ITEMNO "ルシファークロー",@@ITEMNO "オリジナルドラゴン（邪）",]
		],
		[
			@@ITEMNO "トカゲのしっぽ",
			[@@ITEMNO "サラマンダー",@@ITEMNO "リヴァイアサン",@@ITEMNO "アースドラゴン",
			@@ITEMNO "バハムート",@@ITEMNO "オリジナルドラゴン（風）",]
		],
		[
			@@ITEMNO "ネコのひげ",
			[@@ITEMNO "プチヒュドラ",@@ITEMNO "レッサーロプロス",@@ITEMNO "コールドドラゴン",
			@@ITEMNO "フレアブラス",@@ITEMNO "オリジナルドラゴン（土）",]
		],
		[
			@@ITEMNO "玄米フレーク",
			[@@ITEMNO "バジリスク",@@ITEMNO "サンダーホーク",@@ITEMNO "サンダードラゴン",
			@@ITEMNO "ティアマット",@@ITEMNO "オリジナルドラゴン（火）",]
		],
		[
			@@ITEMNO "カレーライス",
			[@@ITEMNO "テュポーン",@@ITEMNO "ストーアウォーム",@@ITEMNO "ファイアドラゴン",
			@@ITEMNO "ザッハーク",@@ITEMNO "オリジナルドラゴン（水）",]
		],
	);
	my $nofeed=0;
	my $msg="";
	my $dragonexist=0;
	foreach(@FEED)
		{
		my @list=@{$_};
		my @needfeed=@{$list[1]};
		my $moneyrate=0;
		foreach(@needfeed)
			{
			$moneyrate+=($DT->{item}[$_-1] * $ITEM[$_]->{price});
			}
		next if $moneyrate < 500;
		$moneyrate=int($moneyrate / $ITEM[$list[0]]->{price} / 12 + 0.9);
		$dragonexist=1;
		next if $DT->{item}[$list[0]-1] >= $moneyrate;
		$msg.=$ITEM[$list[0]]->{name}."が".($moneyrate - $DT->{item}[$list[0]-1]).$ITEM[$list[0]]->{scale}."不足しています。<br>";
		$nofeed=1;
		}
	my $ret;
	$ret.="<TABLE><tr><td>";
	$ret.=main::GetTagImgKao('お手伝い','help')."お手伝い：<br>";
	if (!$dragonexist)
		{
		$ret.="…店長さま，うちの店はドラゴンが一匹もいませんので，<br>";
		$ret.="餌の量を確認する必要はありませんでした。<br>";
		$ret.="召喚魔には餌はいらないみたいです。";
		}
	elsif (!$nofeed)
		{
		$ret.="店長さま，うちの店にいるドラゴンは，みんなうれしそうに<br>";
		$ret.="していますよ。次の決算までは，餌の量は心配ないみたいです。";
		}
	else
		{
		$ret.="店長さま，うちの店にいるドラゴンは，少し不機嫌みたいです。<br>";
		$ret.=$msg."次の決算までには調達しておく必要がありそうですよ。";
		}
		$ret.="</td></tr></table>";
		return $ret;
}

######################################################################
#★ドラゴンの教育
######################################################################
sub education
{
	my $itemno=$USE->{param1};
	my $ret;
	if (rand(4000) > $DT->{exp}{$itemno})
	{
	$ret.=$ITEM[$itemno]->{name}."は，熱心に学習しているようです。<br>";
	$ret.="ただ，まだ".$USE->{param3}."を身につけるには至っていません。";
	return $ret;
	}
	my $itemto=$USE->{param2};
	$ret.="学習により".$USE->{param3}."を身につけました。<br>";
	$ret.=$ITEM[$itemno]->{name}."は，".$ITEM[$itemto]->{name}."へと成長しました！";

	if ($DT->{item}[$itemto-1])
	{
	$ret.="<br>しかし，".$ITEM[$itemto]->{name}."はすでに育成してあるので，逃がすことにしました。";
	}
	else
	{
	$ret=qq|<IMG width="108" height="72" SRC="$main::IMAGE_URL/newpet.jpg"><br><br>|.$ret;
	AddItem($itemto,1);
	WriteLog(2,0,$DT->{shopname}.'が'.$ITEM[$itemto]->{name}.'の育成に成功しました。');
	}
	UseItem($itemno,1);
	return $ret;
}

######################################################################
#★ドラゴンの新種誕生
######################################################################
sub newdragon
{
	my $cnt=0;
	foreach(55..60) { $cnt+=$DT->{item}[$_-1];}
	main::OutError('開発できるオリジナルドラゴンは１種類だけです。<br>すでにオリジナルドラゴンが存在しています。') if $cnt;
	main::OutError('新種の名前をつけてください。') if !$USE->{arg}->{message};
	my $itemno=$USE->{param2};
	my $itemto=$USE->{param3};
	my $ret;
	$DT->{user}->{ori}=$USE->{arg}->{message};
	$ret.=qq|<IMG width="108" height="72" SRC="$main::IMAGE_URL/newpet.jpg"><br><br>|;
	$ret.=$ITEM[$itemno]->{name}."は，ドラゴンに必要な学習をすべて身につけました。<br>";
	$ret.="今ここに，オリジナルドラゴン「".$USE->{arg}->{message}."」が誕生しました！";
	AddItem($itemto,1);
	WriteLog(1,0,$DT->{shopname}.'が新種「'.$USE->{arg}->{message}.'」を誕生させました。');
	UseItem($itemno,1);
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
				['ギフト券',	[[@@ITEMNO "ギフト券", 5],			],],
				['くじ引き券',	[[@@ITEMNO "くじ引き券", 5],			],],
			],
			[
				['ギフト券',	[[@@ITEMNO "ギフト券", 4],			],],
				['くじ引き券',	[[@@ITEMNO "くじ引き券", 4],			],],
			],
			[
				['ギフト券',	[[@@ITEMNO "ギフト券", 3],			],],
				['くじ引き券',	[[@@ITEMNO "くじ引き券", 3],			],],
			],
			[
				['ギフト券',	[[@@ITEMNO "ギフト券", 2],			],],
				['基礎から学ぶＡＢＣ',[[@@ITEMNO "基礎から学ぶＡＢＣ", 1],	],],
				['高次方程式の解法',[[@@ITEMNO "高次方程式の解法", 1],	],],
				['くじ引き券',	[[@@ITEMNO "くじ引き券", 1],			],],
				['積み木',	[[@@ITEMNO "積み木", 1],			],],
				['カガミ',	[[@@ITEMNO "カガミ", 1],			],],
				['おまる',	[[@@ITEMNO "おまる", 1],			],],
				['あんよがじょうずの本',[[@@ITEMNO "あんよがじょうずの本", 1],	],],
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
	my @FEED=(
		[
			@@ITEMNO "へびいちご",
			[@@ITEMNO "ホワイトスネイク",@@ITEMNO "リンドブルム",@@ITEMNO "ホーリードラゴン",
			@@ITEMNO "ケツァルコアトル",@@ITEMNO "オリジナルドラゴン（聖）",]
		],
		[
			@@ITEMNO "雪だるまの昆布",
			[@@ITEMNO "ヨルムンガンド",@@ITEMNO "ラドン",@@ITEMNO "デスドラゴン",
			@@ITEMNO "ルシファークロー",@@ITEMNO "オリジナルドラゴン（邪）",]
		],
		[
			@@ITEMNO "トカゲのしっぽ",
			[@@ITEMNO "サラマンダー",@@ITEMNO "リヴァイアサン",@@ITEMNO "アースドラゴン",
			@@ITEMNO "バハムート",@@ITEMNO "オリジナルドラゴン（風）",]
		],
		[
			@@ITEMNO "ネコのひげ",
			[@@ITEMNO "プチヒュドラ",@@ITEMNO "レッサーロプロス",@@ITEMNO "コールドドラゴン",
			@@ITEMNO "フレアブラス",@@ITEMNO "オリジナルドラゴン（土）",]
		],
		[
			@@ITEMNO "玄米フレーク",
			[@@ITEMNO "バジリスク",@@ITEMNO "サンダーホーク",@@ITEMNO "サンダードラゴン",
			@@ITEMNO "ティアマット",@@ITEMNO "オリジナルドラゴン（火）",]
		],
		[
			@@ITEMNO "カレーライス",
			[@@ITEMNO "テュポーン",@@ITEMNO "ストーアウォーム",@@ITEMNO "ファイアドラゴン",
			@@ITEMNO "ザッハーク",@@ITEMNO "オリジナルドラゴン（水）",]
		],
	);

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

		my $nofeed=0;
		foreach(@FEED)
			{
			my @list=@{$_};
			my @needfeed=@{$list[1]};
			my $moneyrate=0;
			foreach(@needfeed)
				{
				$moneyrate+=($DT->{item}[$_-1] * $ITEM[$_]->{price});
				}
			next if $moneyrate < 500;
			$moneyrate=int($moneyrate / $ITEM[$list[0]]->{price} / 12 + 0.9);
			$DT->{item}[$list[0]-1] -= $moneyrate;
			next if $DT->{item}[$list[0]-1] > 0;
			$nofeed=1;
			$DT->{item}[$list[0]-1] = 0;
			foreach(@needfeed) { $DT->{item}[$_-1]=0; }
			}
		if ($nofeed)
			{
			PushLog(0,0,$DT->{shopname}.'にいたドラゴンは，餌が足りないため脱走しました。') if $nofeed;
			$DT->{rank} = int($DT->{rank} / 2);
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
	if (rand(1000) > 990 && $BUY->{num} > 10)
	{
	$count=AddItemSub(@@ITEMNO"ギフト券",1,$BUY->{dt});
	WriteLog(0,$BUY->{dt}{id},'市場の抽選でギフト券が'.$count.'枚あたりました。');
	$main::ret.='<br>抽選でギフト券が'.$count.'枚あたりました！';
	}
}

@@END #定義終了宣言(以降コメント扱い)

