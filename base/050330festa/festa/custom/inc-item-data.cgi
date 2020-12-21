# キャンパスフェスタ版アイテムデータ 2005/01/29 由來

# このファイルはアイテムデータの定義ファイルです。
# 好きなようにカスタマイズできます。詳細はマニュアルをご覧ください。

@@DEFINE
	version	05-02-17(CF)		#★商品データバージョン表記
					# 最後の「CF」はキャンパスフェスタ版であることを示します。
					# もしあなたが独自アイテムを目玉にした商人物語を作るなら，
					# この記号を変えるのがよいでしょう。

	scale	個			#★デフォルトの数え単位
	type0	全			#全アイテムの集合
	type1	飲食
	type2	芸術
	type3	研究
	type4	催物
	type5	印刷
	type6	道具
	type7	試験
	
	job	art		美術部		#★職業コードは英小文字10文字以内
	job	tea		茶道部
	job	flower		花道部
	job	chemist		化学部
	job	otakkie		パソ部
	job	magic		手品部
	job	show		演劇部
	job	obake		古典部
	job	boss		実行委員会
	
	MaxMoney	999999999	#★最大資金
	
	set NewShopMoney	100000					#初期資金 (@@FUNCNEWにて使用)
	set NewShopTime		12*60*60				#初期持時間(秒) (@@FUNCNEWにて使用)
	set NewShopItem		陳列棚増築取壊キット:1			#初期所持商品 (@@FUNCNEWにて使用) 書式 商品名:個数:商品名:個数:...
	
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
	no		82
	type	道具
	code	gabyou
	name	散らばった画鋲
	info	客が近寄れないうえに価値は全くなし
	price	0
	cost	500
	limit	500/0
	pop	0
	plus	-1m
	flag	noshowcase|norequest

@@ITEM
	no		1
	type	飲食
	code	ice
	name	アイス
	info	屋台の人気デザート
	price	300
	base	1000/100000
	plus	2h
	limit	lv2
	pop	lv3
	point	lv4
	scale	個
@@ITEM
	no		2
	type	飲食
	code	lemonade
	name	ラムネ
	info	屋台の人気ジュース
	price	250
	base	1000/100000
	plus	2h
	limit	lv2
	pop	lv3
	point	lv4
	scale	本
@@ITEM
	no		3
	type	飲食
	code	noodle
	name	中華麺
	info	焼きそばの麺
	price	240
	base	1000/100000
	plus	2h
	limit	lv1
	pop	lv1
	point	lv1
	scale	袋
@@ITEM
	no		4
	type	飲食
	code	yakisauce
	name	焼きそばソース
	info	焼きそばの味を出すソース
	price	200
	base	1000/100000
	plus	2h
	limit	lv1
	pop	lv1
	point	lv1
	scale	袋
@@ITEM
	no		5
	type	飲食
	code	kyabe
	name	キャベツ
	info	食感が勝負の食材
	price	300
	base	1000/100000
	plus	2h
	limit	lv1
	pop	lv1
	point	lv1
	scale	玉
@@ITEM
	no		6
	type	飲食
	code	aonori
	name	青海苔
	info	料理の味付けに
	price	300
	base	1000/100000
	plus	2h
	limit	lv1
	pop	lv1
	point	lv1
	scale	枚
@@ITEM
	no		7
	type	飲食
	code	tako
	name	タコ
	info	歯ごたえのある食材
	price	900
	base	1000/100000
	plus	2h
	limit	lv1
	pop	lv1
	point	lv1
	scale	枚
	scale	kg
@@ITEM
	no		8
	type	飲食
	code	egg
	name	卵
	info	味に広がりが出る
	price	500
	base	1000/100000
	plus	2h
	limit	lv1
	pop	lv1
	point	lv1
	scale	パック
@@ITEM
	no		9
	type	飲食
	code	takonomoto
	name	たこ焼き粉
	info	たこ焼きの素
	price	200
	base	1000/100000
	plus	2h
	limit	lv1
	pop	lv1
	point	lv1
	scale	袋
@@ITEM
	no		10
	type	飲食
	code	takosauce
	name	たこ焼きソース
	info	たこ焼きにかけるソース
	price	200
	base	1000/100000
	plus	2h
	limit	lv1
	pop	lv1
	point	lv1
	scale	本

@@ITEM
	no		11
	type	飲食
	code	yakisoba
	name	焼きそば
	info	屋台の定番料理
	price	500
	plus	-1h
	pop	lv4
	point	lv4
	scale	パック
@@ITEM
	no		12
	type	飲食
	code	takoyaki
	name	たこ焼き
	info	屋台の定番料理
	price	500
	plus	-1h
	pop	lv4
	point	lv4
	scale	パック
@@ITEM
	no		13
	type	飲食
	code	eggfire
	name	卵焼き
	info	そこそこ売れるかも？
	price	300
	plus	-1h
	pop	lv3
	point	lv2
	scale	パック
@@ITEM
	no		14
	type	飲食
	code	yakikyabe
	name	焼きキャベツ
	info	こんなん売れるんだろうか
	price	400
	plus	-1h
	pop	lv2
	point	lv1
	scale	玉

@@ITEM
	no		15
	type	道具
	code	cooktable
	name	調理台
	info	焼きそばを作れそうだ
	price	0
	cost	500
	limit	1
	plus	-1h
	flag	noshowcase|norequest
	scale	台
	@@use
		time	1h
		exp		2%
		exptime	20m
		job	実行委員会	times/1.5
		scale	回
		action	調理する
		name	焼きそばを調理する
		info	焼きそばを作ります
		okmsg	焼きそばを作りました
		ngmsg	調理に失敗しました…
			use		5	中華麺
			use		3	焼きそばソース
			use		1	キャベツ
			use		1	青海苔
			get		48	焼きそば	80%
	@@use
		time	1h
		exp		2%
		exptime	20m
		scale	回
		action	調理する
		name	卵を焼いてみる
		info	卵を焼いてみます
		okmsg	卵焼きができました
		ngmsg	調理に失敗しました…
			use		4	卵
			get		40	卵焼き	80%
	@@use
		time	1h
		exp		2%
		exptime	20m
		scale	回
		action	調理する
		name	キャベツを焼いてみる
		info	キャベツを焼いてみます
		okmsg	焼きキャベツができました
		ngmsg	調理に失敗しました…
			use		6	キャベツ
			get		30	焼きキャベツ	80%

@@ITEM
	no		16
	type	道具
	code	cooktako
	name	たこ焼き器
	info	たこ焼きを作れそうだ
	price	0
	cost	500
	limit	1
	plus	-1h
	flag	noshowcase|norequest
	scale	台
	@@use
		time	1h
		exp		2%
		exptime	20m
		job	実行委員会	times/1.5
		scale	回
		action	調理する
		name	たこ焼きを調理する
		info	たこ焼きを作ります
		okmsg	たこ焼きを作りました
		ngmsg	調理に失敗しました…
			use		1	タコ
			use		1	卵
			use		1	たこ焼き粉
			use		1	たこ焼きソース
			use		1	キャベツ
			use		1	青海苔
			get		48	たこ焼き	80%
	@@use
		time	1h
		exp		2%
		exptime	20m
		scale	回
		action	調理する
		name	卵を焼いてみる
		info	卵を焼いてみます
		okmsg	卵焼きができました
		ngmsg	調理に失敗しました…
			use		4	卵
			get		40	卵焼き	80%
	@@use
		time	1h
		exp		2%
		exptime	20m
		scale	回
		action	調理する
		name	キャベツを焼いてみる
		info	キャベツを焼いてみます
		okmsg	焼きキャベツができました
		ngmsg	調理に失敗しました…
			use		6	キャベツ
			get		30	焼きキャベツ	80%

@@ITEM
	no		24
	type	芸術
	code	posca
	name	ポストカード
	info	絵が描かれているハガキ
	price	1000
	plus	-1h
	pop	lv4
	point	lv7
	scale	枚
@@ITEM
	no		25
	type	芸術
	code	copyart
	name	模写絵
	info	練習がてら模写してみた
	price	3000
	plus	-1h
	pop	lv5
	point	lv6
	scale	枚
@@ITEM
	no		26
	type	芸術
	code	kokucho
	name	彫刻
	info	立体的な芸術
	price	8000
	plus	-1h
	pop	lv6
	point	lv5
	scale	体
@@ITEM
	no		27
	type	芸術
	code	superart
	name	美しい絵画
	info	美術部最高の作品
	price	50000
	plus	-1h
	pop	lv7
	point	lv4
	scale	枚
@@ITEM
	no		28
	type	道具
	code	toolart
	name	美術用具
	info	絵の具とかもろもろ
	price	0
	cost	500
	limit	1
	plus	-1h
	flag	noshowcase|norequest
	scale	セット
	@@use
		time	2h
		exp		1%
		exptime	30m
		job	美術部	times/1.5
		scale	回
		action	片付ける
		name	部室を片付ける
		info	いろんな材料が見つかるかもしれません
		okmsg	使えそうな材料が出てきました
		ngmsg	なにも見つかりませんでした…
			get		18	ホワイトカード	70%
			get		11	カンバス	70%
			get		3	石膏		50%
			get		1	あやしい雑誌	50%
	@@use
		time	30m
		exp		1%
		exptime	10m
		job	美術部	times/1.5
		scale	回
		action	描く
		name	ポストカードを描く
		info	ハガキに絵を描きます
		okmsg	ポストカードを作りました
		ngmsg	製作に失敗しました…
			use		12	ホワイトカード
			get		12	ポストカード	80%
	@@use
		time	1h
		exp		2%
		exptime	20m
		job	美術部	times/1.5
		scale	回
		action	描く
		name	模写絵を描く
		info	有名な絵をまねて描いてみます
		okmsg	模写絵を作りました
		ngmsg	製作に失敗しました…
			needexp		20%
			use		8	カンバス
			get		8	模写絵	80%
	@@use
		time	1h
		exp		2%
		exptime	20m
		job	美術部	times/1.5
		scale	回
		action	描く
		name	彫刻を彫る
		info	立体的な芸術に挑戦します
		okmsg	彫刻を作りました
		ngmsg	製作に失敗しました…
			needexp		40%
			use		3	石膏
			get		3	彫刻	80%
	@@use
		time	1h
		exp		2%
		exptime	20m
		job	美術部	times/1.5
		scale	回
		action	描く
		name	自分独自の絵を描く
		info	新しい芸術に挑戦します
		okmsg	美しい絵画を作りました
		ngmsg	製作に失敗しました…
			needexp		60%
			use		6	カンバス
			use		1	あやしい雑誌
			get		1	美しい絵画	50%

@@ITEM
	no		29
	type	道具
	code	whitecard
	name	ホワイトカード
	info	何も描かれてないカード
	price	100
	plus	-1h
	pop	10d
	point	10%
	scale	枚
@@ITEM
	no		30
	type	道具
	code	canvas
	name	カンバス
	info	何も描かれてないカンバス
	price	300
	plus	-1h
	pop	10d
	point	10%
	scale	枚
@@ITEM
	no		31
	type	道具
	code	artstone
	name	石膏
	info	固めたり彫ったり
	price	800
	plus	-1h
	pop	10d
	point	10%
	scale	個
@@ITEM
	no		32
	type	道具
	code	magazine
	name	あやしい雑誌
	info	想像力がかきたてられるらしい
	price	300
	plus	-1h
	pop	10d
	point	10%
	scale	冊

@@ITEM
	no		33
	type	芸術
	code	ujicha
	name	桐壺茶
	info	練習用に淹れるお茶
	price	500
	plus	-1h
	pop	lv4
	point	lv7
	scale	服
@@ITEM
	no		34
	type	芸術
	code	youkan
	name	茶菓子
	info	お茶とともに召し上がれ
	price	1500
	plus	-1h
	pop	lv5
	point	lv6
	scale	個
@@ITEM
	no		35
	type	芸術
	code	chagama
	name	茶釜
	info	これぞ茶人の証
	price	4000
	plus	-1h
	pop	lv6
	point	lv5
	scale	体
@@ITEM
	no		36
	type	芸術
	code	supertea
	name	侘び寂びの茶碗
	info	茶道部最高の作品
	price	25000
	plus	-1h
	pop	lv7
	point	lv4
	scale	枚
@@ITEM
	no		37
	type	道具
	code	tooltea
	name	裏千家用具
	info	お茶に必要な道具もろもろ
	price	0
	cost	500
	limit	1
	plus	-1h
	flag	noshowcase|norequest
	scale	セット
	@@use
		time	2h
		exp		1%
		exptime	30m
		job	茶道部	times/1.5
		scale	回
		action	片付ける
		name	部室を片付ける
		info	いろんな材料が見つかるかもしれません
		okmsg	使えそうな材料が出てきました
		ngmsg	なにも見つかりませんでした…
			get		18	茶葉		70%
			get		10	お菓子の食べ残し	70%
			get		3	粘土		50%
			get		1	ホコリ		40%
	@@use
		time	30m
		exp		1%
		exptime	10m
		job	茶道部	times/1.5
		scale	回
		action	淹れる
		name	お茶を淹れる
		info	まずは一献
		okmsg	お茶を淹れました
		ngmsg	製作に失敗しました…
			use		12	茶葉
			get		24	桐壺茶	80%
	@@use
		time	1h
		exp		2%
		exptime	20m
		job	茶道部	times/1.5
		scale	回
		action	作る
		name	茶菓子を作る
		info	残り物を再利用して作ります
		okmsg	茶菓子を作りました
		ngmsg	製作に失敗しました…
			needexp		20%
			use		8	お菓子の食べ残し
			get		16	茶菓子	80%
	@@use
		time	1h
		exp		2%
		exptime	20m
		job	茶道部	times/1.5
		scale	回
		action	焼く
		name	茶釜を焼く
		info	茶釜作りに挑戦します
		okmsg	茶釜を作りました
		ngmsg	製作に失敗しました…
			needexp		40%
			use		3	粘土
			get		6	茶釜	80%
	@@use
		time	1h
		exp		2%
		exptime	20m
		job	茶道部	times/1.5
		scale	回
		action	焼く
		name	自分独自の茶碗を焼く
		info	新しい境地に挑戦します
		okmsg	侘び寂びの茶碗を作りました
		ngmsg	製作に失敗しました…
			needexp		60%
			use		6	粘土
			use		1	ホコリ
			get		1	侘び寂びの茶碗	50%

@@ITEM
	no		38
	type	道具
	code	chaba
	name	茶葉
	info	お茶の葉
	price	100
	plus	-1h
	pop	10d
	point	10%
	scale	杯
@@ITEM
	no		39
	type	道具
	code	kashikuzu
	name	お菓子の食べ残し
	info	再利用できるかも（ぉ
	price	300
	plus	-1h
	pop	10d
	point	10%
	scale	個
@@ITEM
	no		40
	type	道具
	code	nendo
	name	粘土
	info	茶器を作る原料
	price	800
	plus	-1h
	pop	10d
	point	10%
	scale	個
@@ITEM
	no		41
	type	道具
	code	dust
	name	ホコリ
	info	ゴミのようでゴミでないかも
	price	300
	plus	-1h
	pop	10d
	point	10%
	scale	個

@@ITEM
	no		42
	type	芸術
	code	bouquet
	name	ブーケ
	info	初歩的な花束
	price	1000
	plus	-1h
	pop	lv4
	point	lv7
	scale	枚
@@ITEM
	no		43
	type	芸術
	code	prest
	name	プレストブーケ
	info	押し花
	price	1500
	plus	-1h
	pop	lv5
	point	lv6
	scale	枚
@@ITEM
	no		44
	type	芸術
	code	dry
	name	ドライブーケ
	info	保存加工が施されたブーケ
	price	8000
	plus	-1h
	pop	lv6
	point	lv5
	scale	体
@@ITEM
	no		45
	type	芸術
	code	superflower
	name	見事なアレンジ
	info	花道部最高の作品
	price	50000
	plus	-1h
	pop	lv7
	point	lv4
	scale	束
@@ITEM
	no		46
	type	道具
	code	toolflower
	name	花道用具
	info	花鋏とかもろもろ
	price	0
	cost	500
	limit	1
	plus	-1h
	flag	noshowcase|norequest
	scale	セット
	@@use
		time	2h
		exp		1%
		exptime	30m
		job	花道部	times/1.5
		scale	回
		action	片付ける
		name	部室を片付ける
		info	いろんな材料が見つかるかもしれません
		okmsg	使えそうな材料が出てきました
		ngmsg	なにも見つかりませんでした…
			get		45	花		70%
			get		3	額縁		70%
			get		3	花器		52%
			get		3	カラーテープ	70%
	@@use
		time	30m
		exp		1%
		exptime	10m
		job	花道部	times/1.5
		scale	回
		action	作る
		name	ブーケを作る
		info	花をアレンジしてブーケにします
		okmsg	ブーケを作りました
		ngmsg	製作に失敗しました…
			use		12	花
			get		12	ブーケ	80%
	@@use
		time	1h
		exp		2%
		exptime	20m
		job	花道部	times/1.5
		scale	回
		action	作る
		name	プレストブーケを作る
		info	押し花にして額に飾ります
		okmsg	プレストブーケを作りました
		ngmsg	製作に失敗しました…
			needexp		20%
			use		12	花
			use		4	額縁
			get		16	プレストブーケ	80%
	@@use
		time	1h
		exp		2%
		exptime	20m
		job	花道部	times/1.5
		scale	回
		action	作る
		name	ドライブーケを作る
		info	花を容器で保存できるようにします
		okmsg	ドライブーケを作りました
		ngmsg	製作に失敗しました…
			needexp		40%
			use		12	花
			use		3	花器
			get		3	ドライブーケ	80%
	@@use
		time	1h
		exp		2%
		exptime	20m
		job	花道部	times/1.5
		scale	回
		action	作る
		name	自分独自のアレンジを作る
		info	新しい芸術に挑戦します
		okmsg	見事なアレンジを作りました
		ngmsg	製作に失敗しました…
			needexp		60%
			use		12	花
			use		4	カラーテープ
			get		1	見事なアレンジ	50%

@@ITEM
	no		47
	type	道具
	code	flower
	name	花
	info	部室に埋もれていたけど枯れてない
	price	100
	plus	-1h
	pop	10d
	point	10%
	scale	輪
@@ITEM
	no		48
	type	道具
	code	gaku
	name	額縁
	info	花を入れて飾る
	price	300
	plus	-1h
	pop	10d
	point	10%
	scale	枚
@@ITEM
	no		49
	type	道具
	code	flwerglass
	name	花器
	info	花を入れて保存する容器
	price	400
	plus	-1h
	pop	10d
	point	10%
	scale	個
@@ITEM
	no		50
	type	道具
	code	colortape
	name	カラーテープ
	info	アレンジのまずさをごまかす
	price	300
	plus	-1h
	pop	10d
	point	10%
	scale	個


@@ITEM
	no		51
	type	研究
	code	shoppai
	name	塩化ナトリウム
	info	要するに塩
	price	1000
	plus	-1h
	pop	lv4
	point	lv7
	scale	kg
@@ITEM
	no		52
	type	研究
	code	goodwater
	name	アルカリイオン水
	info	おいしい水
	price	3000
	plus	-1h
	pop	lv5
	point	lv6
	scale	kl
@@ITEM
	no		53
	type	研究
	code	sakana
	name	ドコサヘキサエン酸
	info	食べると頭がよくなる
	price	8000
	plus	-1h
	pop	lv6
	point	lv5
	scale	ml
@@ITEM
	no		54
	type	研究
	code	superche
	name	不思議な化合物
	info	化学部最高の作品
	price	50000
	plus	-1h
	pop	lv7
	point	lv4
	scale	枚
@@ITEM
	no		55
	type	道具
	code	toolche
	name	科学セット
	info	試験管とかもろもろ
	price	0
	cost	500
	limit	1
	plus	-1h
	flag	noshowcase|norequest
	scale	セット
	@@use
		time	2h
		exp		1%
		exptime	30m
		job	化学部	times/1.5
		scale	回
		action	片付ける
		name	部室を片付ける
		info	いろんな材料が見つかるかもしれません
		okmsg	使えそうな材料が出てきました
		ngmsg	なにも見つかりませんでした…
			get		11	クエン酸	70%
			get		18	シリコン化ナトリウム	70%
			get		9	バケツの水	70%
			get		3	パンくず	70%
			get		1	アレ	50%
	@@use
		time	30m
		exp		1%
		exptime	10m
		job	化学部	times/1.5
		scale	回
		action	化合する
		name	塩化ナトリウムを化合する
		info	化学反応により塩化ナトリウムを作ります
		okmsg	塩化ナトリウムを作りました
		ngmsg	製作に失敗しました…
			use		6	クエン酸
			use		6	シリコン化ナトリウム
			get		12	塩化ナトリウム	80%
	@@use
		time	1h
		exp		2%
		exptime	20m
		job	化学部	times/1.5
		scale	回
		action	化合する
		name	アルカリイオン水を化合する
		info	化学反応によりアルカリイオン水を作ります
		okmsg	アルカリイオン水を作りました
		ngmsg	製作に失敗しました…
			needexp		20%
			use		12	シリコン化ナトリウム
			use		4	バケツの水
			get		8	アルカリイオン水	80%
	@@use
		time	1h
		exp		2%
		exptime	20m
		job	化学部	times/1.5
		scale	回
		action	化合する
		name	ドコサヘキサエン酸を化合する
		info	化学反応によりドコサヘキサエン酸を作ります
		okmsg	ドコサヘキサエン酸を作りました
		ngmsg	製作に失敗しました…
			needexp		40%
			use		4	バケツの水
			use		4	パンくず
			get		3	ドコサヘキサエン酸	80%
	@@use
		time	1h
		exp		2%
		exptime	20m
		job	化学部	times/1.5
		scale	回
		action	化合する
		name	自分独自の化学反応を起こす
		info	新しい化合物に挑戦します
		okmsg	不思議な化合物を作りました
		ngmsg	製作に失敗しました…
			needexp		60%
			use		6	クエン酸
			use		4	バケツの水
			use		1	アレ
			get		1	不思議な化合物	50%

@@ITEM
	no		56
	type	道具
	code	noteat
	name	クエン酸
	info	お約束ですが食えません
	price	100
	plus	-1h
	pop	10d
	point	10%
	scale	mg
@@ITEM
	no		57
	type	道具
	code	sna
	name	シリコン化ナトリウム
	info	シリコン化したナトリウム
	price	100
	plus	-1h
	pop	10d
	point	10%
	scale	mg
@@ITEM
	no		58
	type	道具
	code	washwater
	name	バケツの水
	info	前の掃除のときに片付けてなかった
	price	300
	plus	-1h
	pop	10d
	point	10%
	scale	kl
@@ITEM
	no		59
	type	道具
	code	breadtrash
	name	パンくず
	info	給食の残り
	price	300
	plus	-1h
	pop	10d
	point	10%
	scale	mg
@@ITEM
	no		60
	type	道具
	code	are
	name	アレ
	info	ごっきー
	price	300
	plus	-1h
	pop	10d
	point	10%
	scale	匹


@@ITEM
	no		61
	type	研究
	code	scsaver
	name	スクリーンセーバー
	info	初歩的なプログラム
	price	1000
	plus	-1h
	pop	lv4
	point	lv7
	scale	CPUs
@@ITEM
	no		62
	type	研究
	code	akihako
	name	商人諸島
	info	ありふれたCGIゲーム
	price	3000
	plus	-1h
	pop	lv5
	point	lv6
	scale	CPUs
@@ITEM
	no		63
	type	研究
	code	virus
	name	ウイルス製造プログラム
	info	なぜか大人気
	price	8000
	plus	-1h
	pop	lv6
	point	lv5
	scale	CPUs
@@ITEM
	no		64
	type	研究
	code	superota
	name	オタッキーなゲーム
	info	パソ部最高の作品
	price	50000
	plus	-1h
	pop	lv7
	point	lv4
	scale	CPUs
@@ITEM
	no		65
	type	道具
	code	toolota
	name	ノーパソ
	info	パソ一式
	price	0
	cost	500
	limit	1
	plus	-1h
	flag	noshowcase|norequest
	scale	セット
	@@use
		time	2h
		exp		1%
		exptime	30m
		job	パソ部	times/1.5
		scale	回
		action	片付ける
		name	部室を片付ける
		info	いろんな材料が見つかるかもしれません
		okmsg	使えそうな材料が出てきました
		ngmsg	なにも見つかりませんでした…
			get		18	ロウソク	70%
			get		10	ジーピーエル	70%
			get		3	ムチ		50%
			get		1	メイド型人形	50%
	@@use
		time	30m
		exp		1%
		exptime	10m
		job	パソ部	times/1.5
		scale	回
		action	開発する
		name	スクリーンセーバーを開発する
		info	初歩的なプログラムをあやつります
		okmsg	スクリーンセーバーを作りました
		ngmsg	製作に失敗しました…
			use		12	ロウソク
			get		12	スクリーンセーバー	80%
	@@use
		time	1h
		exp		2%
		exptime	20m
		job	パソ部	times/1.5
		scale	回
		action	開発する
		name	商人諸島を開発する
		info	最近話題のperlをあやつります
		okmsg	商人諸島を作りました
		ngmsg	製作に失敗しました…
			needexp		20%
			use		8	ジーピーエル
			get		8	商人諸島	80%
	@@use
		time	1h
		exp		2%
		exptime	20m
		job	パソ部	times/1.5
		scale	回
		action	開発する
		name	ウイルス製造プログラムを開発する
		info	世の中を混沌に陥れます
		okmsg	ウイルス製造プログラムを作りました
		ngmsg	製作に失敗しました…
			needexp		40%
			use		3	ムチ
			get		3	ウイルス製造プログラム	80%
	@@use
		time	1h
		exp		2%
		exptime	20m
		job	パソ部	times/1.5
		scale	回
		action	開発する
		name	自分独自のゲームを開発する
		info	新しいプログラムに挑戦します
		okmsg	オタッキーなゲームを作りました
		ngmsg	製作に失敗しました…
			needexp		60%
			use		6	ジーピーエル
			use		1	メイド型人形
			get		1	オタッキーなゲーム	50%

@@ITEM
	no		66
	type	道具
	code	joousama
	name	ロウソク
	info	刺激を得られる
	price	100
	plus	-1h
	pop	10d
	point	10%
	scale	本
@@ITEM
	no		67
	type	道具
	code	gnugpl
	name	ジーピーエル
	info	意味不明な文章が並んだ契約書
	price	300
	plus	-1h
	pop	10d
	point	10%
	scale	通
@@ITEM
	no		68
	type	道具
	code	odamari
	name	ムチ
	info	強い刺激を得られる
	price	800
	plus	-1h
	pop	10d
	point	10%
	scale	本
@@ITEM
	no		69
	type	道具
	code	moemoe
	name	メイド型人形
	info	想像力がかきたてられるらしい
	price	300
	plus	-1h
	pop	10d
	point	10%
	scale	体


@@ITEM
	no		70
	type	催物
	code	ticketmagic
	name	手品公演券
	info	手品公演を見るためのチケット
	price	5000
	plus	-1h
	pop	lv10
	point	lv-1
	scale	枚
@@ITEM
	no		71
	type	道具
	code	toolmagic
	name	手品グッズ
	info	手品のタネがいっぱい
	price	0
	cost	500
	limit	1
	plus	-1h
	flag	noshowcase|norequest
	scale	セット
	@@use
		time	12h
		exp		10%
		arg	nocount|message20
		job	手品部	times/1.5
		scale	回
		action	という公演を企画する
		name	新しい手品公演を企画する
		info	手品公演のネタを考えます
		func	newmagic
	@@use
		time	1h
		exp	0%
		exptime	20m
		job	手品部	times/1.5
		scale	回
		action	印刷する
		name	手品公演券を印刷する
		info	チケットを作ります
		okmsg	手品公演券を作りました
		ngmsg	印刷に失敗しました…
		price	2400
		funcb	ptcheck
			get		8	手品公演券	80%
	@@use
		time	8h
		exp		3%
		job	手品部	times/1.5
		scale	回
		action	開催する
		name	手品公演を行う
		info	用意した手品公演を行います
		funcb	ptcheck
		func	showing

@@ITEM
	no		72
	type	催物
	code	ticketshow
	name	演劇公演券
	info	演劇公演を見るためのチケット
	price	5000
	plus	-1h
	pop	lv10
	point	lv-1
	scale	枚
@@ITEM
	no		73
	type	道具
	code	toolshow
	name	舞台セット
	info	演劇の必需品がいっぱい
	price	0
	cost	500
	limit	1
	plus	-1h
	flag	noshowcase|norequest
	scale	セット
	@@use
		time	12h
		exp		10%
		arg	nocount|message20
		job	演劇部	times/1.5
		scale	回
		action	という公演を企画する
		name	新しい演劇の脚本を企画する
		info	演劇公演のストーリーを考えます
		func	newshow
	@@use
		time	1h
		exp	0%
		exptime	20m
		job	演劇部	times/1.5
		scale	回
		action	印刷する
		name	演劇公演券を印刷する
		info	チケットを作ります
		okmsg	演劇公演券を作りました
		ngmsg	印刷に失敗しました…
		price	2400
		funcb	ptcheck
			get		8	演劇公演券	80%
	@@use
		time	8h
		exp		3%
		job	演劇部	times/1.5
		scale	回
		action	開催する
		name	演劇公演を行う
		info	用意した手品公演を行います
		funcb	ptcheck
		func	showing

@@ITEM
	no		74
	type	催物
	code	ticketobake
	name	お化け屋敷入場券
	info	お化け屋敷に入るためのチケット
	price	5000
	plus	-1h
	pop	lv10
	point	lv-1
	scale	枚
@@ITEM
	no		75
	type	道具
	code	toolobake
	name	お化け変装グッズ
	info	これを使っておどかします
	price	0
	cost	500
	limit	1
	plus	-1h
	flag	noshowcase|norequest
	scale	セット
	@@use
		time	12h
		exp		10%
		arg	nocount|message20
		job	古典部	times/1.5
		scale	回
		action	というお化け屋敷を設営する
		name	新しいお化け屋敷を設営する
		info	お化けの出現ポイントなどを調整します
		func	newobake
	@@use
		time	1h
		exp	0%
		exptime	20m
		job	古典部	times/1.5
		scale	回
		action	印刷する
		name	お化け屋敷入場券を印刷する
		info	チケットを作ります
		okmsg	お化け屋敷入場券を作りました
		ngmsg	印刷に失敗しました…
		price	2400
		funcb	ptcheck
			get		8	お化け屋敷入場券	80%
	@@use
		time	8h
		exp		3%
		job	古典部	times/1.5
		scale	回
		action	開催する
		name	お化け特別ショーを行う
		info	お化けの舞うイベントを行います
		funcb	ptcheck
		func	obaking

@@ITEM
	no		76
	type	道具
	code	invitecard
	name	招待状
	info	これを持っていると催物が見られます
	price	0
	cost	500
	limit	3
	plus	-1h
	flag	noshowcase|norequest
	scale	枚

@@ITEM
	no		77
	type	印刷
	code	toiletticket
	name	トイレ利用券
	info	これがないとトイレに入れない
	price	1000
	plus	-1h
	pop	lv3
	point	lv5
	scale	枚
@@ITEM
	no		78
	type	印刷
	code	parkticket
	name	駐車場利用券
	info	これがないと駐車場を使えない
	price	3000
	plus	-1h
	pop	lv3
	point	lv4
	scale	枚
@@ITEM
	no		79
	type	印刷
	code	panf
	name	パンフレット
	info	文化祭を見て回るのに役立つ
	price	8000
	plus	-1h
	pop	lv4
	point	lv4
	scale	冊
@@ITEM
	no		80
	type	印刷
	code	cm
	name	ポスター
	info	貼ると広告になる
	price	50000
	plus	-1h
	pop	lv4
	point	lv3
	scale	枚
	@@use
		time	10h
		exp	10%
		job		実行委員会	times/1.5
		scale	回
		action	広告する
		name	自店の広告を出す
		info	自分の店の人気を上げられます
		arg		nocount
			use		1	ポスター
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
			use		1	ポスター
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
			use		1	ポスター
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
	no		81
	type	道具
	code	ghq
	name	大本営
	info	すべての権力がここに集まる
	price	0
	cost	500
	limit	1
	plus	-1h
	flag	noshowcase|norequest
	scale	セット
	@@use
		time	30m
		exp		1%
		exptime	10m
		job	実行委員会	times/1.5
		scale	回
		action	印刷する
		name	トイレ利用券を印刷する
		info	大本営のコピー機で印刷します
		okmsg	トイレ利用券を作りました
		ngmsg	製作に失敗しました…
		price	1200
			get		12	トイレ利用券	80%
	@@use
		time	1h
		exp		2%
		exptime	20m
		scale	回
		action	印刷する
		name	駐車場利用券を印刷する
		info	大本営のコピー機で印刷します
		okmsg	駐車場利用券を作りました
		ngmsg	製作に失敗しました…
			needexp		20%
		price	2400
			get		8	駐車場利用券	80%
	@@use
		time	1h
		exp		2%
		exptime	20m
		scale	回
		action	印刷する
		name	パンフレットを印刷する
		info	大本営のコピー機で印刷します
		okmsg	パンフレットを作りました
		ngmsg	製作に失敗しました…
			needexp		40%
		price	2400
			get		3	パンフレット	80%
	@@use
		time	1h
		exp		2%
		exptime	20m
		scale	回
		action	印刷する
		name	ポスターを印刷する
		info	大本営のコピー機で印刷します
		okmsg	ポスターを作りました
		ngmsg	製作に失敗しました…
			needexp		60%
		price	2400
			get		1	ポスター	50%

@@ITEM
	no		17
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
	no		23
	type	印刷
	code	comejoinus
	name	入部届
	info	クラブに入るための申請書
	price	1000
	limit	1/1
	pop	lv0.1
	point	lv0.1
	plus	1h
	scale	枚
	flag	noshowcase
	@@USE
		time	6h
		action	入部する
		scale	回
		arg		nocount
		name	美術部に入る
		info	美術部に入部します
		param	28,37:46:55:65:71:73:75:81,0.2,art
		funcb	jobcheck
			use		1	入部届
		func	jobport
	@@USE
		time	6h
		action	入部する
		scale	回
		arg		nocount
		name	茶道部に入る
		info	茶道部に入部します
		param	37,28:46:55:65:71:73:75:81,0.2,tea
		funcb	jobcheck
			use		1	入部届
		func	jobport
	@@USE
		time	6h
		action	入部する
		scale	回
		arg		nocount
		name	花道部に入る
		info	花道部に入部します
		param	46,28:37:55:65:71:73:75:81,0.2,flower
		funcb	jobcheck
			use		1	入部届
		func	jobport
	@@USE
		time	6h
		action	入部する
		scale	回
		arg		nocount
		name	化学部に入る
		info	化学部に入部します
		param	55,28:37:46:65:71:73:75:81,0.2,chemist
		funcb	jobcheck
			use		1	入部届
		func	jobport
	@@USE
		time	6h
		action	入部する
		scale	回
		arg		nocount
		name	パソ部に入る
		info	パソ部に入部します
		param	65,28:37:46:55:71:73:75:81,0.2,otakkie
		funcb	jobcheck
			use		1	入部届
		func	jobport
	@@USE
		time	6h
		action	入部する
		scale	回
		arg		nocount
		name	手品部に入る
		info	手品部に入部します
		param	71,28:37:46:55:65:73:75:81,0.2,magic
		funcb	jobcheck
			use		1	入部届
		func	jobport
	@@USE
		time	6h
		action	入部する
		scale	回
		arg		nocount
		name	演劇部に入る
		info	演劇部に入部します
		param	73,28:37:46:55:65:71:75:81,0.2,show
		funcb	jobcheck
			use		1	入部届
		func	jobport
	@@USE
		time	6h
		action	入部する
		scale	回
		arg		nocount
		name	古典部に入る
		info	古典部に入部します
		param	75,28:37:46:55:65:71:73:81,0.2,obake
		funcb	jobcheck
			use		1	入部届
		func	jobport
	@@USE
		time	6h
		action	入部する
		scale	回
		arg		nocount
		name	実行委員会に入る
		info	実行委員会に入部します
		param	81,28:37:46:55:65:71:73:75,0.2,boss
		funcb	jobcheck
			use		1	入部届
		func	jobport


@@ITEM
	no		18
	type	道具
	code	defence-manbiki
	name	生活委員
	info	いじめを見つけて先生にちくってくれる
	price	500000
	cost	5000
	limit	1/0.5
	pop	lv0.1
	point	lv0.1
	plus	30m
	scale	人
	flag	noshowcase|onlysend|human

@@ITEM
	no		19
	type	道具
	code	badgossip
	name	いじめマニュアル
	info	やってはならないがやらなくてはならないときに…
	price	25000
	limit	1/0.5
	pop	lv0.1
	point	lv0.1
	plus	1h
	base	40/100
	scale	冊
	@@use
		time	10h
		exp	20%
		exptime	8h
		job		実行委員会	times/1.5
		price	50000
		scale	回
		action	仕掛ける
		name	黒板消しを仕掛ける
		info	成功すれば相手のお店の人気を下げられますが，失敗することも…
		arg	target|nocount
			needpoint	20000
		func	_local_
			my $ret;
			if(rand(1000)<800 && !$DTS->{exp}{@@ITEMNO"ポスター"})
			{
				$DTS->{rank}-=int($DTS->{rank}/3);
				$ret=$DTS->{shopname}.'に黒板消しを仕掛ける作戦が成功しました';
				WriteLog(0,$DT->{id},$ret);
				WriteLog(2,0,$DTS->{shopname}.'にて黒板消しが客の頭上に落ち，人気が下がりました。');
			}
			else
			{
				$DTS->{exp}{@@ITEMNO"ポスター"}-=100;
				$DTS->{exp}{@@ITEMNO"ポスター"}=0 if ($DTS->{exp}{@@ITEMNO"ポスター"} < 0);
				$DT->{rank}-=int($DT->{rank}/4);
				$ret=$DTS->{shopname}.'に黒板消しを仕掛ける作戦は失敗しました';
				WriteLog(0,$DT->{id},$ret);
				WriteLog(3,0,$DT->{shopname}."が".$DTS->{shopname}.'に黒板消しを仕掛けていたようです。');
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
	@@use
		time	14h
		exp	20%
		exptime	12h
		price	50000
		scale	回
		action	仕掛ける
		name	画鋲をばらまく
		info	他店の陳列棚に画鋲をばらまきます
		func	fire
		arg	target|nocount
			needpoint	20000

@@ITEM
	no		20
	type	試験
	code	testeng
	name	英語
	info	英語の試験成績
	price	0
	limit	100/0
	pop	0
	plus	-1h
	flag	noshowcase|norequest|notrash
	scale	点
	@@use
		time	2h
		exp		5%
		scale	回
		action	勉強する
		name	英語を勉強する
		info	英語を勉強します
		func	study

@@ITEM
	no		21
	type	試験
	code	testmat
	name	数学
	info	数学の試験成績
	price	0
	limit	100/0
	pop	0
	plus	-1h
	flag	noshowcase|norequest|notrash
	scale	点
	@@use
		time	2h
		exp		5%
		scale	回
		action	勉強する
		name	数学を勉強する
		info	数学を勉強します
		func	study

@@ITEM
	no		22
	type	試験
	code	testtan
	name	国語
	info	国語の試験成績
	price	0
	limit	100/0
	pop	0
	plus	-1h
	flag	noshowcase|norequest|notrash
	scale	点
	@@use
		time	2h
		exp		5%
		scale	回
		action	勉強する
		name	国語を勉強する
		info	国語を勉強します
		func	study


# アイスじゃおなかいっぱいにならないイベント
@@EVENT
	start		100%
	code		icejataranai
	info		アイスじゃおなかいっぱいにならない
	startfunc	_local_
		foreach(@DT)
		{
			next if $_->{money}<100000;
			next if !$_->{item}[@@ITEMNO"アイス"-1];
			next if $_->{item}[@@ITEMNO"調理台"-1];
			my $flag;					#アイス陳列チェック
			foreach my $idx (0..$_->{showcasecount}-1)
			{
			my $itemno=$_->{showcase}[$idx];
			$flag=1 if ($itemno==@@ITEMNO"アイス");
			}
			next if !$flag;

			$_->{money}-=50000;
			$_->{paytoday}+=50000;
			$_->{item}[@@ITEMNO"調理台"-1]++;
			return (0,$_->{shopname}.'にて，アイスじゃおなかいっぱいにならない事件が発生しました。?code'.$_->{id}.':1');
		}
		return 0;
	_local_

# 100％タコなんですイベント
@@EVENT
	start		100%
	code		takonandesu
	info		うちは100％タコなんです
	startfunc	_local_
		foreach(@DT)
		{
			next if $_->{money}<100000;
			next if !$_->{item}[@@ITEMNO"タコ"-1];
			next if $_->{item}[@@ITEMNO"たこ焼き器"-1];
			my $flag;					#タコ陳列チェック
			foreach my $idx (0..$_->{showcasecount}-1)
			{
			my $itemno=$_->{showcase}[$idx];
			$flag=1 if ($itemno==@@ITEMNO"タコ");
			}
			next if !$flag;

			$_->{money}-=50000;
			$_->{paytoday}+=50000;
			$_->{item}[@@ITEMNO"たこ焼き器"-1]++;
			return (0,$_->{shopname}.'にて，100％タコなんです事件が発生しました。?code'.$_->{id}.':2');
		}
		return 0;
	_local_

# 青海苔で自滅イベント
@@EVENT
	start		100%
	code		aonoride
	info		青海苔で自滅
	startfunc	_local_
		foreach(@DT)
		{
			next if !$_->{item}[@@ITEMNO"青海苔"-1];
			my $flag;					#青海苔陳列チェック
			foreach my $idx (0..$_->{showcasecount}-1)
			{
			my $itemno=$_->{showcase}[$idx];
			$flag=1 if ($itemno==@@ITEMNO"青海苔");
			}
			next if !$flag;

			$_->{rank}-=int($_->{rank}/6);
			return (0,$_->{shopname}.'にて，青海苔で自滅事件が発生しました。?code'.$_->{id}.':3');
		}
		return 0;
	_local_

# 美術部勧誘イベント
@@EVENT
	start		100%
	code		artinvite
	info		美術部勧誘
	startfunc	_local_
		foreach(reverse@DT)
		{
			next if ($_->{job} eq "art");
			next if ($_->{item}[@@ITEMNO"英語"-1] > 40);
			next if ($_->{item}[@@ITEMNO"数学"-1] > 40);
			next if ($_->{item}[@@ITEMNO"国語"-1] > 40);
			main::ReadDTSub($_,"data");
			next if ($_->{_data}->{club} =~ /art:/);
			$_->{_data}->{club}.="art:";
			main::WriteDTSub($_,"data");
			return (0,$_->{shopname}.'にて，美術部勧誘事件が発生しました。?code'.$_->{id}.':4');
		}
		return 0;
	_local_

# 茶道部勧誘イベント
@@EVENT
	start		100%
	code		teainvite
	info		茶道部勧誘
	startfunc	_local_
		foreach(reverse@DT)
		{
			next if ($_->{job} eq "tea");
			next if ($_->{item}[@@ITEMNO"国語"-1] < 80);
			next if !$_->{item}[@@ITEMNO"アイス"-1];
			my $flag;					#アイス陳列チェック
			foreach my $idx (0..$_->{showcasecount}-1)
			{
			my $itemno=$_->{showcase}[$idx];
			$flag=1 if ($itemno==@@ITEMNO"アイス");
			}
			next if !$flag;
			main::ReadDTSub($_,"data");
			next if ($_->{_data}->{club} =~ /tea:/);
			$_->{_data}->{club}.="tea:";
			main::WriteDTSub($_,"data");
			return (0,$_->{shopname}.'にて，茶道部勧誘事件が発生しました。?code'.$_->{id}.':5');
		}
		return 0;
	_local_

# 花道部勧誘イベント
@@EVENT
	start		100%
	code		flowerinvite
	info		花道部勧誘
	startfunc	_local_
		foreach(reverse@DT)
		{
			next if ($_->{job} eq "flower");
			next if ($_->{item}[@@ITEMNO"英語"-1] < 80);
			next if ($_->{item}[@@ITEMNO"数学"-1] > 40);
			main::ReadDTSub($_,"data");
			next if ($_->{_data}->{club} =~ /flower:/);
			$_->{_data}->{club}.="flower:";
			main::WriteDTSub($_,"data");
			return (0,$_->{shopname}.'にて，花道部勧誘事件が発生しました。?code'.$_->{id}.':6');
		}
		return 0;
	_local_

# 化学部勧誘イベント
@@EVENT
	start		100%
	code		cheinvite
	info		化学部勧誘
	startfunc	_local_
		foreach(reverse@DT)
		{
			next if ($_->{job} eq "chemist");
			next if ($_->{item}[@@ITEMNO"数学"-1] < 80);
			next if ($_->{item}[@@ITEMNO"国語"-1] > 40);
			main::ReadDTSub($_,"data");
			next if ($_->{_data}->{club} =~ /chemist:/);
			$_->{_data}->{club}.="chemist:";
			main::WriteDTSub($_,"data");
			return (0,$_->{shopname}.'にて，化学部勧誘事件が発生しました。?code'.$_->{id}.':7');
		}
		return 0;
	_local_

# パソ部勧誘イベント
@@EVENT
	start		100%
	code		otainvite
	info		パソ部勧誘
	startfunc	_local_
		foreach(reverse@DT)
		{
			next if ($_->{job} eq "otakkie");
			next if ($_->{item}[@@ITEMNO"英語"-1] < 80);
			next if ($_->{item}[@@ITEMNO"数学"-1] < 80);
			main::ReadDTSub($_,"data");
			next if ($_->{_data}->{club} =~ /otakkie:/);
			$_->{_data}->{club}.="otakkie:";
			main::WriteDTSub($_,"data");
			return (0,$_->{shopname}.'にて，パソ部勧誘事件が発生しました。?code'.$_->{id}.':8');
		}
		return 0;
	_local_

# 手品部勧誘イベント
@@EVENT
	start		70%
	code		magicinvite
	info		手品部勧誘
	startfunc	_local_
		foreach(reverse@DT)
		{
			next if ($_->{job} eq "magic");
			next if ($_->{item}[@@ITEMNO"数学"-1] < 80);
			next if !$_->{item}[@@ITEMNO"たこ焼き"-1];
			my $flag;					#たこ焼き陳列チェック
			foreach my $idx (0..$_->{showcasecount}-1)
			{
			my $itemno=$_->{showcase}[$idx];
			$flag=1 if ($itemno==@@ITEMNO"たこ焼き");
			}
			next if !$flag;
			main::ReadDTSub($_,"data");
			next if ($_->{_data}->{club} =~ /magic:/);
			$_->{_data}->{club}.="magic:";
			main::WriteDTSub($_,"data");
			return (0,$_->{shopname}.'にて，手品部勧誘事件が発生しました。?code'.$_->{id}.':9');
		}
		return 0;
	_local_

# 演劇部勧誘イベント
@@EVENT
	start		70%
	code		showinvite
	info		演劇部勧誘
	startfunc	_local_
		foreach(reverse@DT)
		{
			next if ($_->{job} eq "show");
			next if ($_->{item}[@@ITEMNO"数学"-1] > 40);
			next if ($_->{item}[@@ITEMNO"国語"-1] < 80);
			main::ReadDTSub($_,"data");
			next if ($_->{_data}->{club} =~ /show:/);
			$_->{_data}->{club}.="show:";
			main::WriteDTSub($_,"data");
			return (0,$_->{shopname}.'にて，演劇部勧誘事件が発生しました。?code'.$_->{id}.':10');
		}
		return 0;
	_local_

# 古典部勧誘イベント
@@EVENT
	start		70%
	code		obakeinvite
	info		古典部勧誘
	startfunc	_local_
		foreach(reverse@DT)
		{
			next if ($_->{job} eq "obake");
			next if ($_->{item}[@@ITEMNO"英語"-1] < 80);
			next if ($_->{item}[@@ITEMNO"数学"-1] < 80);
			next if ($_->{item}[@@ITEMNO"国語"-1] < 80);
			main::ReadDTSub($_,"data");
			next if ($_->{_data}->{club} =~ /obake:/);
			$_->{_data}->{club}.="obake:";
			main::WriteDTSub($_,"data");
			return (0,$_->{shopname}.'にて，古典部勧誘事件が発生しました。?code'.$_->{id}.':11');
		}
		return 0;
	_local_

# 実行委員会勧誘イベント
@@EVENT
	start		70%
	code		bossinvite
	info		実行委員会勧誘
	startfunc	_local_
		return if grep($_->{job} eq "boss",@DT);
		foreach(reverse@DT)
		{
			next if ($_->{item}[@@ITEMNO"英語"-1] < 85);
			next if ($_->{item}[@@ITEMNO"数学"-1] < 85);
			next if ($_->{item}[@@ITEMNO"国語"-1] < 85);
			main::ReadDTSub($_,"data");
			next if ($_->{_data}->{club} =~ /boss:/);
			$_->{_data}->{club}.="boss:";
			main::WriteDTSub($_,"data");
			return (0,$_->{shopname}.'にて，実行委員会勧誘事件が発生しました。?code'.$_->{id}.':12');
		}
		return 0;
	_local_

@@FUNCINIT
#部活が「実行委員会」の場合、買い物に必要な時間を3/4にする。
$TIME_SEND_ITEM=int($TIME_SEND_ITEM/4*3) if $DT->{job} eq 'boss';

@@FUNCITEM
######################################################################
# ★入部チェック
######################################################################
sub jobcheck
{
my($USE)=@_;
main::ReadDTSub($DT,"data");
return 1 if ($DT->{job} eq $USE->{param4});
return 0 if ($DT->{_data}->{club} =~ /$USE->{param4}:/);
return 1;
}

######################################################################
# ★ジョブチェンジ
######################################################################
sub jobport
{
	$DT->{job}=$USE->{param4};
	WriteLog(3,0,$DT->{shopname}.'が「'.$main::JOBTYPE{$USE->{param4}}.'」に入部しました。');

	my $ret;
	my $exp1=$DT->{exp}{$USE->{param1}};
	my $exp2=0;
	$ret.="入部届を提出しに学園事務局へと向かった。<br><br>";
	$ret.="<TABLE><tr><td>";
	$ret.=main::GetTagImgKao('アムザ','amza')."事務員アムザ：<br>";
	$ret.="…ふむ。".$main::JOBTYPE{$USE->{param4}}."に入りたいというのですね。<br>";
	$ret.='さすれば，全知全能の校長よ！<br>いまここに<b>'.$DT->{shopname}."</b>が<br>";
	$ret.=$main::JOBTYPE{$USE->{param4}}."の道を歩むことを許したまえ！";
	$ret.="</td></tr></table><br>";
	$ret.="部活が".$main::JOBTYPE{$USE->{param4}}."になりました。<br>";
	
	foreach my $exps (split(/:/,$USE->{param2}))
	{
		my $exp=$DT->{exp}{$exps};
		next if (!$DT->{item}[$exps-1] && !$exp);
		$exp2+=$exp;
		delete($DT->{exp}{$exps});
		my $msg=$ITEM[$exps]->{name}.'は失われました。';
		$DT->{item}[$exps-1]=0 if ($DT->{item}[$exps-1]);
		WriteLog(0,$DT->{id},$msg);
		$ret.=$msg."<br>";
	}
	$exp2=int($exp2*$USE->{param3});
	$exp1+=$exp2;
	$exp1=1000 if $exp1>1000;
	$msg=$ITEM[$USE->{param1}]->{name}."の熟練度が ".int($exp1/10)."% になりました。";
	WriteLog(0,$DT->{id},$msg);
	$ret.=$msg."<br>";
	$DT->{item}[$USE->{param1}-1]=1;	# アイテムがもらえる。
	$DT->{exp}{$USE->{param1}}=$exp1;
	delete $DT->{user}->{pt};
	delete $DT->{user}->{tt};
	return $ret;
}

######################################################################
#★勉強
######################################################################
sub study
{
	my $ret;
	if($count>7)
	{
	$ret.="よし！今日は，バリバリ勉強しちゃる・・・と思って始めたのだが。<br><br>";
	$ret.="<TABLE><tr><td>";
	$ret.=main::GetTagImgKao('お手伝い','help')."<td><SPAN>お手伝い</SPAN>：";
	$ret.="ご主人様！ しっかりしてください！<br>";
	$ret.="どう考えても勉強のしすぎですよ…。";
	$ret.="</td></tr></table><br>";
	WriteLog(0,0,$DT->{shopname}.'が，勉強しすぎて保健室に運ばれました。');
	$ret.="どうやら勉強しすぎてぶっ倒れてしまったようだ。<br>気が付いたら保健室のベッドの上だった。汗";
	}
	else
	{
	$ret.="勉強のことは<SPAN>お手伝い</SPAN>に習うのが一番だ。<br><br>";
	$ret.="<TABLE><tr><td>";
	$ret.=main::GetTagImgKao('お手伝い','help')."<td><SPAN>お手伝い</SPAN>：";
	my $i=int(rand(3));
	if ($i == 1)
		{
		$ret.="ですからー。そこはまず慎重に問題文を読むんですってば。<br>";
		$ret.="あーもう，その問題は私が解くから！ 次！次！";
		}
	elsif ($i == 2)
		{
		$ret.="うーん。当てずっぽうで答え言ってません？<br>";
		$ret.="勘を磨いてどうするんですかー。もー。";
		}
	else
		{
		$ret.="あー。なんか教えるのめんどくさくなってきた・・・。<br>";
		$ret.="・・・はっ。何でもないですよ何でも。";
		}
	$ret.="</td></tr></table><br>";
	$ret.="少しは分かってきたかもしんない。";
	}
	return $ret;
}

######################################################################
# ★公演チェック
######################################################################
sub ptcheck
{
my($USE)=@_;
return 1 if (!$DT->{user}->{pt});
return 0;
}

######################################################################
#★新しい手品公演
######################################################################
sub newmagic
{
	main::OutError('公演タイトルをつけてください。') if !$USE->{arg}->{message};
	my $ret;
	$ret.="新しいネタを<SPAN>お手伝い</SPAN>に見てもらった。<br><br>";
	$ret.="<TABLE><tr><td>";
	$ret.=main::GetTagImgKao('お手伝い','help')."<td><SPAN>お手伝い</SPAN>：";
	my $i=int(rand(3));
	if ($i == 1)
		{
		$ret.="・・・ぐー。・・・ぐー。・・・ふにゃっ。<br>";
		$ret.="・・・はっ。あ，面白かったですよ！ とても。";
		}
	elsif ($i == 2)
		{
		$ret.="あれ，その手品ってどこかで見ませんでした？<br>";
		$ret.="おかしいなあ・・・デジャブ？";
		}
	else
		{
		$ret.="思うんですけど，そのいっつも出てくるハトって，<br>";
		$ret.="飼ってるんですか？ いやもーそれがひたすら気になって。";
		}
	$ret.="</td></tr></table><br>";
	$ret.="新しい手品公演「".$USE->{arg}->{message}."」を開発した。";

	$DT->{user}->{tt}=$USE->{arg}->{message};
	$DT->{user}->{pt}=2000 + int($DT->{exp}{@@ITEMNO"手品グッズ"} * 4 + rand(500));

	WriteLog(1,0,$DT->{shopname}.'で新しい手品「'.$USE->{arg}->{message}.'」が開幕です。');

	foreach my $DTS (@DT) { AddItemSub(@@ITEMNO"招待状",1,$DTS); }
	return $ret;
}

######################################################################
#★新しい演劇公演
######################################################################
sub newshow
{
	main::OutError('公演タイトルをつけてください。') if !$USE->{arg}->{message};
	my $ret;
	$ret.="新しいネタを<SPAN>お手伝い</SPAN>に見てもらった。<br><br>";
	$ret.="<TABLE><tr><td>";
	$ret.=main::GetTagImgKao('お手伝い','help')."<td><SPAN>お手伝い</SPAN>：";
	my $i=int(rand(3));
	if ($i == 1)
		{
		$ret.="うーん，オチがないですね。<br>";
		$ret.="あれ，コメディですよねそれ。違いました？";
		}
	elsif ($i == 2)
		{
		$ret.="その演劇，私も出られないんですかー？<br>";
		$ret.="あ，樹木１とかは勘弁ですよ。";
		}
	else
		{
		$ret.="・・・ぐー。・・・ぐー。・・・ふにゃっ。<br>";
		$ret.="・・・はっ。あ，面白かったですよ！ とても。";
		}
	$ret.="</td></tr></table><br>";
	$ret.="新しい演劇公演「".$USE->{arg}->{message}."」を開発した。";

	$DT->{user}->{tt}=$USE->{arg}->{message};
	$DT->{user}->{pt}=2000 + int($DT->{exp}{@@ITEMNO"舞台セット"} * 4 + rand(500));

	WriteLog(1,0,$DT->{shopname}.'で新しい演劇「'.$USE->{arg}->{message}.'」が開幕です。');

	foreach my $DTS (@DT) { AddItemSub(@@ITEMNO"招待状",1,$DTS); }
	return $ret;
}

######################################################################
#★新しいお化け屋敷
######################################################################
sub newobake
{
	main::OutError('お化け屋敷の名前をつけてください。') if !$USE->{arg}->{message};
	my $ret;
	$ret.="新しいお化け屋敷を<SPAN>お手伝い</SPAN>に体験してもらった。<br><br>";
	$ret.="<TABLE><tr><td>";
	$ret.=main::GetTagImgKao('お手伝い','help')."<td><SPAN>お手伝い</SPAN>：";
	my $i=int(rand(3));
	if ($i == 1)
		{
		$ret.="きゃーーーーーーー！<br>";
		$ret.="あ，あの花子さん，本物です！！";
		}
	elsif ($i == 2)
		{
		$ret.="あちゃー，びっくりしてつい，<br>";
		$ret.="お化け役の人ぶっ飛ばしちゃいました。てへ。";
		}
	else
		{
		$ret.="あのー，お化け役の人が眠ってるみたいで<br>";
		$ret.="何も起こりませんでしたよー。";
		}
	$ret.="</td></tr></table><br>";
	$ret.="新しいお化け屋敷「".$USE->{arg}->{message}."」を開発した。";

	$DT->{user}->{tt}=$USE->{arg}->{message};
	$DT->{user}->{pt}=2000 + int($DT->{exp}{@@ITEMNO"お化け変装グッズ"} * 4 + rand(500));

	WriteLog(1,0,$DT->{shopname}.'で新しいお化け屋敷「'.$USE->{arg}->{message}.'」が開幕です。');

	foreach my $DTS (@DT) { AddItemSub(@@ITEMNO"招待状",1,$DTS); }
	return $ret;
}

######################################################################
#★公演を実施
######################################################################
sub showing
{
	my $up=int($DT->{user}->{pt}*(2-$DT->{rank}/5000)/5);
	$up=$up * $USE->{result}->{count};
	$DT->{rank}+=$up;
	$DT->{rank}=10000 if $DT->{rank}>10000;
	my $ret="公演を行いました：人気".int($up/100)."%アップ";
	WriteLog(0,$DT->{id},$ret);
	WriteLog(3,0,$DT->{shopname}.'で「'.$DT->{user}->{tt}.'」が公演されました。');

	if ($USE->{result}->{count} > rand(10))
		{
		$cnt=($DT->{user}->{pt} + int(rand(5))) * 1000;
		$DT->{money}+=$cnt;
		$DT->{saletoday}+=$cnt;
		$ret.="<br>".GetMoneyString($cnt)."の臨時収入がありました。";
		}
	return $ret;
}

######################################################################
#★公演を実施
######################################################################
sub obaking
{
	my $up=int($DT->{user}->{pt}*(2-$DT->{rank}/5000)/10);
	$up=$up * $USE->{result}->{count};
	$DT->{rank}+=$up;
	$DT->{rank}=10000 if $DT->{rank}>10000;
	my $ret="特別ショーを行いました：人気".int($up/100)."%アップ";
	WriteLog(0,$DT->{id},$ret);
	WriteLog(3,0,$DT->{shopname}.'で「'.$DT->{user}->{tt}.'」の特別ショーが行われました。');

	if ($USE->{result}->{count} > rand(10))
		{
		$cnt=($DT->{user}->{pt} + int(rand(5))) * 1000;
		$DT->{money}+=$cnt;
		$DT->{saletoday}+=$cnt;
		$ret.="<br>".GetMoneyString($cnt)."の臨時収入がありました。";
		}
	return $ret;
}

######################################################################
#★万引き
######################################################################
sub stole
{
	return '自分から万引きすることはできません。万引きは失敗です。' if  ($DT->{id} eq $DTS->{id});
	my $ret="万引きは失敗しました。賠償金".GetMoneyString(500000)."を取られてしまいました。";
	if($DTS->{item}[@@ITEMNO"生活委員"-1])
	{
		$DT->{rank}-=int($DT->{rank}/4);
		$DTS->{money}+=500000;
		$DTS->{saletoday}+=500000;
		$DT->{money}-=500000;
		$DT->{paytoday}+=500000;
		WriteLog(3,0,$DT->{shopname}."が".$DTS->{shopname}."へ万引きに入りましたが生活委員に見つかりました。");
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

######################################################################
#★画鋲
######################################################################
sub fire
{
	my $ret;

if ( (rand(1000)>800) || ($DTS->{item}[@@ITEMNO"生活委員"-1]) )
{
	$DT->{rank}-=int($DT->{rank}/10);
	$ret=$DTS->{shopname}.'への画鋲ばらまきに失敗しました';
	WriteLog(0,$DT->{id},$ret);
	WriteLog(3,0,$DT->{shopname}."が".$DTS->{shopname}.'に画鋲をばらまこうとしていたようです。');
	return $ret;
}

my $cnt=int(rand(50))+45;	#画鋲の数ランダムに45～95
my $price=10000;		#陳列されると強制的に\10000になる
$DTS->{item}[82-1]=$cnt;

foreach my $idx (0..$DTS->{showcasecount}-1)
{
my $itemno=$DTS->{showcase}[$idx];
$DTS->{item}[$itemno-1]=0 if ($itemno);
$DTS->{showcase}[$idx]=82;	#画鋲のアイテムNo.
$DTS->{price}[$idx]=$price;
}

$ret=$DTS->{shopname}.'への画鋲ばらまきに成功しました';
WriteLog(0,$DT->{id},$ret);
WriteLog(3,0,$DTS->{shopname}.'の陳列棚に画鋲がばらまかれました。');

return $ret;
}



@@FUNCUPDATE
sub UpdateResetBefore #決算直前の処理(関数名固定)
{
	foreach my $DT (@DT)
	{
		$DT->{testpoint}=0;
		foreach my $itemno(@@ITEMNO"英語",@@ITEMNO"数学",@@ITEMNO"国語")
		{
		$DT->{item}[$itemno-1]+=int(($DT->{exp}{$itemno}/5 - $DT->{item}[$itemno-1])/3 + rand(5));
		$DT->{item}[$itemno-1]=90 + int(rand(10)) if $DT->{item}[$itemno-1]>95;
		$DT->{item}[$itemno-1]=1 if $DT->{item}[$itemno-1]<1;
		$DT->{exp}{$itemno}=int($DT->{exp}{$itemno}/2);
		$DT->{testpoint}+=$DT->{item}[$itemno-1];
		}
	}
	my @DTS=sort{$b->{testpoint}<=>$a->{testpoint}}@DT;
	PushLog(1,0,"定期試験の総合トップは".$DTS[0]->{shopname}.'さんの'.$DTS[0]->{testpoint}."点でした。");
	my $i=int(rand(4))+3;
	$DTS[0]->{time}-=3600*$i;
	PushLog(2,0,"トップの".$DTS[0]->{shopname}.'さんには'.$i."時間の自由時間が与えられました。");

	@DTS=reverse(@DTS);
	PushLog(1,0,"定期試験の総合ビリは".$DTS[0]->{shopname}.'さんの'.$DTS[0]->{testpoint}."点でした。");
	PushLog(1,0,"また総合ブービーは".$DTS[1]->{shopname}.'さんの'.$DTS[1]->{testpoint}."点でした。");
	$i=int(rand(5))+3;
	$DTS[0]->{time}+=3600*$i;
	PushLog(2,0,"ビリの".$DTS[0]->{shopname}.'さんは'.$i."時間居残り勉強させられました。");
	$i=int(rand(4))+2;
	$DTS[1]->{time}+=3600*$i;
	PushLog(2,0,"ブービーの".$DTS[1]->{shopname}.'さんは'.$i."時間居残り勉強させられました。");
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
$DEFINE_FUNCNEW_NOLOG=1;
WriteLog(1,0,0,"入学おめでとうございます。".$DT->{shopname}."が開店しました。",1);

# その他、新装開店時に独自の処理を追加できます。

foreach my $itemno(@@ITEMNO"英語",@@ITEMNO"数学",@@ITEMNO"国語")
{
	$DT->{item}[$itemno-1]=45+int(rand(10));
}

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

@@END #定義終了宣言(以降コメント扱い)

