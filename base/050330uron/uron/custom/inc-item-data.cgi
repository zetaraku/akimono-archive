# うどん＆そば版アイテムデータ 2005/01/06 由來

# このファイルはアイテムデータの定義ファイルです。
# 好きなようにカスタマイズできます。詳細はマニュアルをご覧ください。

@@DEFINE
	version	05-01-06(URon)		#★商品データバージョン表記
					# 最後の「URon」はうどん＆そば版であることを示します。
					# もしあなたが独自アイテムを目玉にした商人物語を作るなら，
					# この記号を変えるのがよいでしょう。

	scale	杯			#★デフォルトの数え単位
	type0	全			#全アイテムの集合
	type1	人材
	type2	陸産物
	type3	海産物
	type4	うどん
	type5	そば
	type6	ツール
	
	job	agri		農業		#★職業コードは英小文字10文字以内
	job	fish		漁業
	job	temp		天ぷら屋
	job	udon		うどん屋
	job	soba		そば屋
	job	man		人材派遣業
	job	black		裏家業
	
	# 職業別時間短縮用変数設定
	set job_agri_time_rate		1.5	#★職業についていると1.5倍早くなる
	set job_fish_time_rate		1.5
	set job_temp_time_rate		1.5
	set job_udon_time_rate		1.5
	set job_soba_time_rate		1.5
	set job_man_time_rate		2
	set job_black_time_rate		2

	MaxMoney	999999999	#★最大資金
	
	set NewShopMoney	200000					#初期資金 (@@FUNCNEWにて使用)
	set NewShopTime		24*60*60				#初期持時間(秒) (@@FUNCNEWにて使用)
	set NewShopItem		ヒントブック:1	#初期所持商品 (@@FUNCNEWにて使用) 書式 商品名:個数:商品名:個数:...
	
	TimeEditShowcase	10m		#★陳列棚操作時間
	TimeShopping		20m		#★仕入時間(旧SOLD OUTとの互換性確保。今は使用せず)
	TimeSendItem		20m		#★アイテム仕入/送信時間(基本)
	TimeSendItemPlus	20s		#★アイテム仕入/送信時間(1個辺りの追加時間)
	TimeSendMoney		20m		#★資金送信時間(基本)
	TimeSendMoneyPlus	100000		#★入金所要時間計算用金額(この金額につきTimeSendMoney時間を消費)
	
	CostShowcase1		0		#★陳列棚1個時維持費
	CostShowcase2		1000	#陳列棚2個時維持費
	CostShowcase3		2000	#陳列棚3個時維持費
	CostShowcase4		4000	#陳列棚4個時維持費
	CostShowcase5		8000	#陳列棚5個時維持費
	CostShowcase6		16000	#陳列棚6個時維持費
	CostShowcase7		32000	#陳列棚7個時維持費
	CostShowcase8		64000	#陳列棚8個時維持費
	
	ItemUseTimeRate		0.5		#★アイテム使用時時間計算補正倍率(@USE内time,exptimeに有効)
	

#------ ここからアイテム定義 ---------------------------------


@@ITEM
	no		1
	type	人材
	code	man-free
	name	フリーター
	info	可能性を秘めた人材です
	scale	人
	price	5000
	cost	100
	limit	5/5
	plus	2h
	pop	1d
	flag	noshowcase|norequest|human
	@@USE
		time	4h
		exp		1%
		exptime	2h
		job		人材派遣業	times/job_man_time_rate
		scale	人
		action	農業を始める
		name	農業を始める
		info	フリーターは農業を始めます
		okmsg	フリーターは農夫になりました
			use		1	フリーター
			get		1	農夫
			get		10	店力	20%
	@@USE
		time	4h
		exp		1%
		exptime	2h
		job		人材派遣業	times/job_man_time_rate
		scale	人
		action	漁業を始める
		name	漁業を始める
		info	フリーターは漁業を始めます
		okmsg	フリーターは漁師になりました
			use		1	フリーター
			get		1	漁師
			get		10	店力	20%
	@@USE
		time	4h
		exp		1%
		exptime	2h
		job		人材派遣業	times/job_man_time_rate
		scale	人
		action	修行をする
		name	天ぷら職人の修行をする
		info	フリーターは天ぷら職人になる修行をします
		okmsg	フリーターは天ぷら職人になりました
			use		1	フリーター
			get		1	天ぷら職人
			get		10	店力	20%
	@@USE
		time	4h
		exp		1%
		exptime	2h
		job		人材派遣業	times/job_man_time_rate
		scale	人
		action	修行をする
		name	うどん職人の修行をする
		info	フリーターはうどん職人になる修行をします
		okmsg	フリーターはうどん職人になりました
			use		1	フリーター
			use		10	小麦粉
			get		1	うどん職人
			get		10	店力	20%
	@@USE
		time	4h
		exp		1%
		exptime	2h
		job		人材派遣業	times/job_man_time_rate
		scale	人
		action	修行をする
		name	そば職人の修行をする
		info	フリーターはそば職人になる修行をします
		okmsg	フリーターはそば職人になりました
			use		1	フリーター
			use		10	そば粉
			get		1	そば職人
			get		10	店力	20%
	@@USE
		time	4h
		exp		1%
		exptime	2h
		job		人材派遣業	times/job_man_time_rate
		scale	人
		action	便利屋になる
		name	便利屋になる
		info	フリーターは便利屋になります
		okmsg	フリーターは便利屋になりました
			use		1	フリーター
			get		1	便利屋
			get		10	店力	20%
	@@use
		time	4h
		job		人材派遣業	times/job_man_time_rate
		scale	回
		action	働く
		name	チラシ配りで資金稼ぎ
		info	少し稼ぎましょう
		param	7000
		func	_local_
			$DT->{money}+=$USE->{param1}*$count;
			my $ret=GetMoneyString($USE->{param1}*$count).'稼ぎました';
			if (rand(1000)<200)
			{
			UseItem(1,1,$ITEM[1]->{name}.'が資金稼ぎで疲れて店を去りました');
			}
			WriteLog(0,$DT->{id},"バイトし，$ret");
			WriteLog(3,0,$DT->{shopname}."のフリーターがバイトしたようです");
			return $ret;
		_local_
	@@use
		time	9h
		job		人材派遣業	times/job_man_time_rate
		scale	回
		action	働く
		name	コンビニで資金稼ぎ
		info	ちょっときついけどけっこうな稼ぎです
		param	20000
		func	_local_7
	@@USE
		time	6h
		action	人材派遣業の専門家になる
		arg		nocount
		name	人材派遣業の専門家になる
		info	今までの経験を生かして，人材派遣業の専門家になります
			needexp		20%
		func	_local_
			my $ret="";
			main::OutError('現在すでに人材派遣業の専門家です') if ($DT->{job} eq 'man');
			$DT->{job} = 'man';
			$ret="人材派遣業の専門家になりました";
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_

@@ITEM
	no		2
	type	人材
	code	man-nou
	name	農夫
	info	家畜を飼うのも得意です
	scale	人
	price	30000
	cost	1000
	limit	3/0.5
	plus	1d
	pop	1d
	flag	noshowcase|human
	@@USE
		time	3h
		exp		1%
		exptime	1h
		price	20000
		job		農業	times/job_agri_time_rate
		scale	反
		action	畑を手に入れる
		name	畑を手に入れる
		info	手入れのよい畑を探して購入します
		okmsg	すぐに収穫できそうな畑が手に入り，おまけに堆肥も分けてもらいました
			get		1	収穫を待つ畑
			get		100	堆肥
	@@USE
		time	3h
		exp		1%
		exptime	1h
		job		農業	times/job_agri_time_rate
		scale	反
		action	耕して種を植える
		name	畑を耕して種を植える
		info	畑に肥料を与えて耕し，作物の種を植えます
		okmsg	畑はよく耕され，作物の種が植えられました
			use		1	耕す前の畑
			use		100	堆肥
			get		1	よく耕した畑
			get		10	店力	10%
	@@USE
		time	3h
		exp		1%
		exptime	1h
		job		農業	times/job_agri_time_rate
		scale	回
		action	収穫をする
		name	ねぎの収穫をする
		info	ねぎ畑に行って収穫をします
		func	lostman
		param	50
		ngmsg	何も収穫できませんでした‥
			use		1	収穫を待つ畑
			get		100	ねぎ	50%	ねぎを収穫しました
			get		10	とうもろこし	50%	ついでに食べ頃のとうもろこしを取ってきました
			get		1	福引き補助券	01%	畑で福引き補助券を拾いました
			get		1	がちょう	05%	畑に侵入していた野生のがちょうをつかまえました
			get		1	耕す前の畑
			get		10	店力	10%
		funcb	_local_
			# 1/20の確率で収穫量が2倍になる
			return 0 if rand(1000)>50;
			
			my $USE=$_[0];
			
			foreach(@{$USE->{result}->{create}})
			{
				$_->{count}*=2;
			}
			
			$USE->{result}->{message}->{resultok}='今回はかなり豊作でした<br>新しい畑を手に入れました';
			return 0;
		_local_
	@@USE
		time	3h
		exp		1%
		exptime	1h
		job		農業	times/job_agri_time_rate
		scale	回
		action	収穫をする
		name	小麦の収穫をする
		info	小麦畑に行って収穫をします
		func	lostman
		param	50
		ngmsg	何も収穫できませんでした‥
			use		1	収穫を待つ畑
			get		40	小麦粉	50%	小麦を収穫し，さらに製粉しました
			get		10	とうがらし	50%	ついでにとうがらしを取ってきました
			get		1	福引き補助券	01%	畑で福引き補助券を拾いました
			get		1	がちょう	05%	畑に侵入していた野生のがちょうをつかまえました
			get		1	耕す前の畑
			get		10	店力	10%
		funcb	_local_
			return 0 if rand(1000)>50;
			
			my $USE=$_[0];
			
			foreach(@{$USE->{result}->{create}})
			{
				$_->{count}*=2;
			}
			
			$USE->{result}->{message}->{resultok}='今回はかなり豊作でした<br>新しい畑を手に入れました';
			return 0;
		_local_
@@USE
		time	3h
		exp		1%
		exptime	1h
		job		農業	times/job_agri_time_rate
		scale	回
		action	収穫をする
		name	そばの収穫をする
		info	そば畑に行って収穫をします
		func	lostman
		param	50
		ngmsg	何も収穫できませんでした‥
			use		1	収穫を待つ畑
			get		40	そば粉	50%	そばを収穫し，さらに製粉しました
			get		20	とうがらし	50%	ついでにとうがらしを取ってきました
			get		1	福引き補助券	01%	畑で福引き補助券を拾いました
			get		1	豚	05%	畑に侵入していた野生の豚をつかまえました
			get		1	耕す前の畑
			get		10	店力	10%
		funcb	_local_
			return 0 if rand(1000)>50;
			
			my $USE=$_[0];
			
			foreach(@{$USE->{result}->{create}})
			{
				$_->{count}*=2;
			}
			
			$USE->{result}->{message}->{resultok}='今回はかなり豊作でした<br>新しい畑を手に入れました';
			return 0;
		_local_
@@USE
		time	3h
		exp		1%
		exptime	1h
		job		農業	times/job_agri_time_rate
		scale	回
		action	収穫をする
		name	大豆の収穫をする
		info	大豆畑に行って収穫をします
		func	lostman
		param	50
		ngmsg	何も収穫できませんでした‥
			use		1	収穫を待つ畑
			get		40	大豆	50%	大豆を収穫しました
			get		30	ねぎ	50%	ついでにねぎを取ってきました
			get		1	福引き補助券	01%	畑で福引き補助券を拾いました
			get		1	豚	05%	畑に侵入していた野生の豚をつかまえました
			get		1	耕す前の畑
			get		10	店力	10%
		funcb	_local_
			return 0 if rand(1000)>50;
			
			my $USE=$_[0];
			
			foreach(@{$USE->{result}->{create}})
			{
				$_->{count}*=2;
			}
			
			$USE->{result}->{message}->{resultok}='今回はかなり豊作でした<br>新しい畑を手に入れました';
			return 0;
		_local_
@@USE
		time	3h
		exp		1%
		exptime	1h
		job		農業	times/job_agri_time_rate
		scale	回
		action	収穫をする
		name	とうもろこしの収穫をする
		info	とうもろこし畑に行って収穫をします
		func	lostman
		param	50
		ngmsg	何も収穫できませんでした‥
			use		1	収穫を待つ畑
			get		27	とうもろこし	50%	とうもろこしを収穫しました
			get		20	大豆	50%	ついでに大豆を取ってきました
			get		1	福引き補助券	01%	畑で福引き補助券を拾いました
			get		1	がちょう	05%	畑に侵入していた野生のがちょうをつかまえました
			get		1	耕す前の畑
			get		10	店力	10%
		funcb	_local_
			return 0 if rand(1000)>50;
			
			my $USE=$_[0];
			
			foreach(@{$USE->{result}->{create}})
			{
				$_->{count}*=2;
			}
			
			$USE->{result}->{message}->{resultok}='今回はかなり豊作でした<br>新しい畑を手に入れました';
			return 0;
		_local_
	@@USE
		time	3h
		exp		1%
		exptime	1h
		job		農業	times/job_agri_time_rate
		arg		nocount
		action	世話をする
		name	にわとりの世話をする
		info	餌を十分に準備すれば，鶏舎の掃除後ににわとりに食べさせることができます
		param	2
			need		1	にわとり
		func	_local_
			my $val=$USE->{param1}*$count;
			my $ret="";
			my $niwatori=$DT->{item}[20-1];
			my $toumorokosi=$DT->{item}[17-1];

			if ($niwatori*$count>$toumorokosi)
			{
			AddItem(58,$count,);
			$ret='鶏の餌が足りないようなので，鶏舎の掃除だけ済ませました';
			WriteLog(0,$DT->{id},$ret);
			}
			else
			{
			$val*=$DT->{item}[20-1];
			$val=int(rand($val) * 2)+1;
			AddItem(9,$val,);
			AddItem(58,$count,);
			UseItem(17,$niwatori*$count,'にわとり１羽につき，とうもろこしを'.$count.'本食べさせました');
			
			my $useproba=$USE->{param1}*$USE->{param1};
			my $usecount=0;
			foreach(1..$count)
			{
				$usecount++ if rand(1000)<$useproba;
			}
			UseItem(20,$usecount,$ITEM[20]->{name}.'が満腹した後，昇天しました') if $usecount;
			
			$ret='卵が'.$val.'個手に入りました';
			WriteLog(0,$DT->{id},$ret);
			}
			return $ret;
		_local_
	@@USE
		time	3h
		exp		1%
		exptime	1h
		job		農業	times/job_agri_time_rate
		scale	セット
		action	親鳥に卵を抱かせる
		name	卵を孵化させる
		info	卵を親鳥に抱かせ，孵化させてみます
		func	lostman
		param	50
		okmsg	孵化の準備が整いました
			need		1	にわとり
			use		5	卵
			get		5	孵化を待つ卵
			get		10	店力	10%
	@@USE
		time	3h
		exp		1%
		exptime	1h
		job		農業	times/job_agri_time_rate
		scale	羽
		action	世話をする
		name	がちょうの世話をする
		info	がちょうにたっぷり餌を与えてみます
		func	lostman
		param	50
		ngmsg	フォアグラがとれる前に，がちょうが昇天してしまいました‥
		okmsg	高級なフォアグラが手に入りました
			use		1	がちょう
			use		10	とうもろこし
			get		48	フォアグラ	50%
			get		10	店力	15%
	@@USE
		time	3h
		exp		1%
		exptime	1h
		job		農業	times/job_agri_time_rate
		scale	回
		arg		nocount
		action	世話をする
		name	豚の世話をする
		info	餌を十分に用意すれば，豚に食べさせてから山に散歩に連れて行くことができます
		param	1
			need		1	豚
		func	_local_
			my $val=$USE->{param1}*$count;
			my $ret="";
			my $buta=$DT->{item}[22-1];
			my $daizu=$DT->{item}[16-1];

			if ($buta*$count*5>$daizu)
			{
			AddItem(58,$count*2,);
			$ret='餌が足りそうになかったので，豚小屋の掃除だけ済ませました';
			WriteLog(0,$DT->{id},$ret);
			}
			else
			{
			$val*=$DT->{item}[22-1];
			$val=int(rand($val) * 3)+1;
			AddItem(18,$val,);
			AddItem(58,$count,);
			UseItem(16,$buta*$count*5,'豚1頭につき，大豆を'.($count*5).'kg食べさせました');
			
			my $useproba=$USE->{param1}*$USE->{param1};
			my $usecount=0;
			foreach(1..$count)
			{
				$usecount++ if rand(1000)<$useproba;
			}
			UseItem(22,$usecount,$ITEM[22]->{name}.'が山奥に逃げていきました') if $usecount;
			
			$ret='食後の散歩に連れて行った山で，豚がトリュフを'.$val.'個見つけました';
			WriteLog(0,$DT->{id},$ret);
			}
			return $ret;
		_local_
	@@USE
		time	6h
		action	農業の専門家になる
		scale	回
		arg		nocount
		name	農業の専門家になる
		info	今までの経験を生かして，農業の専門家になります
			needexp		20%
		func	_local_
			my $ret="";
			main::OutError('現在すでに農業の専門家です') if ($DT->{job} eq 'agri');
			$DT->{job} = 'agri';
			$ret="農業の専門家になりました";
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_

@@ITEM
	no		3
	type	人材
	code	man-gyo
	name	漁師
	info	大物を釣るには餌が必要です
	scale	人
	price	30000
	cost	1000
	limit	3/0.5
	plus	1d
	pop	3d
	flag	noshowcase|human
	@@USE
		time	4.5h
		exp		1%
		exptime	1.5h
		job		漁業	times/job_fish_time_rate
		scale	回
		action	釣りをする
		name	釣りをする
		info	近くの海岸で釣りをしてみます
		ngmsg	釣果はありませんでした‥
			get		10	すけとうだら	50%	すけとうだらが釣れました
			get		2	えそ	50%	えそが釣れました
			get		100	えび	60%	えびを捕まえました
			get		40	わかめ	50%	ついでにわかめも採りました
			get		1	がちょう	02%	溺れかけていたがちょうを助けました
			get		10	店力	20%
	@@USE
		time	4h
		exp		1%
		exptime	2h
		job		漁業	times/job_fish_time_rate
		scale	回
		action	漁に出る
		name	漁に出る
		info	船に乗って漁に出てみます
		func	lostman
		param	50
		ngmsg	釣果はありませんでした‥
			use		50	えび
			get		8	すけとうだら	30%	すけとうだらが釣れました
			get		8	えそ	50%	えそが釣れました
			get		10	かつお	50%	かつおが釣れました
			get		2	ちょうざめ	30%	大物のちょうざめが釣れました
			get		1	豚	02%	溺れかけていた豚を助けました
			get		10	店力	20%
	@@USE
		time	2h
		exp		1%
		exptime	1h
		job		漁業	times/job_fish_time_rate
		scale	回
		action	作る
		name	辛子めんたいを作る
		info	すけとうだらの卵を加工して，辛子めんたいを作ります
		func	lostman
		param	50
		ngmsg	辛子めんたい作りに失敗し，材料を無駄にしてしまいました‥
		okmsg	辛子めんたいができました
			use		1	すけとうだら
			use		5	とうがらし
			get		20	辛子めんたい	80%
			get		10	店力	10%
	@@USE
		time	2h
		exp		1%
		exptime	1h
		job		漁業	times/job_fish_time_rate
		scale	回
		action	手に入れる
		name	キャビアを手に入れる
		info	ちょうざめのおなかからキャビアを取り出します
		func	lostman
		param	50
		ngmsg	ちょうざめは♂でした‥
		okmsg	キャビアが手に入りました
			use		1	ちょうざめ
			get		40	キャビア	60%
			get		10	店力	10%
	@@USE
		time	6h
		action	漁業の専門家になる
		scale	回
		arg		nocount
		name	漁業の専門家になる
		info	今までの経験を生かして，漁業の専門家になります
			needexp		20%
		func	_local_
			my $ret="";
			main::OutError('現在すでに漁業の専門家です') if ($DT->{job} eq 'fish');
			$DT->{job} = 'fish';
			$ret="漁業の専門家になりました";
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_

@@ITEM
	no		4
	type	人材
	code	man-ten
	name	天ぷら職人
	info	油揚げやかまぼこも作ります
	scale	人
	price	30000
	cost	1000
	limit	3/0.5
	plus	2d
	pop	3d
	flag	noshowcase|human
	@@USE
		time	90m
		exp	2%
		exptime	30m
		job	天ぷら屋	times/job_temp_time_rate
		scale	回
		action	作る
		name	油揚げを作る
		info	大豆から豆腐を作り，さらに油揚げに加工します
		ngmsg	油揚げ作りに失敗し，材料を無駄にしてしまいました‥
			use		10	大豆
			get		100	油揚げ	80%	油揚げができました
			get		10	店力	20%
	@@USE
		time	90m
		exp	2%
		exptime	30m
		job		天ぷら屋	times/job_temp_time_rate
		scale	回
		action	作る
		name	かまぼこを作る
		info	かまぼこを作ります
		ngmsg	かまぼこ作りに失敗し，材料を無駄にしてしまいました‥
			use		4	すけとうだら
			get		100	かまぼこ	80%	かまぼこができました
			get		10	店力	20%
	@@USE
		time	90m
		exp	2%
		exptime	30m
		job		天ぷら屋	times/job_temp_time_rate
		scale	回
		action	作る
		name	丸天を作る
		info	丸天を作ります
		func	lostman
		param	50
		ngmsg	丸天作りに失敗し，材料を無駄にしてしまいました‥
			use		2	えそ
			get		60	丸天	80%	丸天ができました
			get		10	店力	20%
	@@USE
		time	90m
		exp	2%
		exptime	30m
		job		天ぷら屋	times/job_temp_time_rate
		scale	回
		action	作る
		name	えび天を作る
		info	えび天を作ります
		func	lostman
		param	50
		ngmsg	えび天作りに失敗し，材料を無駄にしてしまいました‥
			use		20	えび
			use		2	小麦粉
			use		10	卵
			get		50	えび天	80%	えび天ができました
			get		10	店力	20%
	@@USE
		time	6h
		action	天ぷら作りの専門家になる
		arg		nocount
		name	天ぷら作りの専門家になる
		info	今までの経験を生かして，天ぷら作りの専門家になります
			needexp		20%
		func	_local_
			my $ret="";
			main::OutError('現在すでに天ぷら作りの専門家です') if ($DT->{job} eq 'temp');
			$DT->{job} = 'temp';
			$ret="天ぷら作りの専門家になりました";
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_

@@ITEM
	no		5
	type	人材
	code	man-udon
	name	うどん職人
	info	各種うどんを1杯ずつ揃えて，新しいうどんの開発を！
	scale	人
	price	30000
	cost	1000
	limit	3/0.3
	plus	2d
	pop	3d
	flag	noshowcase|human
	@@USE
		time	1h
		exp	1%
		exptime	20m
		job	うどん屋	times/job_udon_time_rate
		scale	回
		action	作る
		name	すうどんを作る
		info	すうどんを作ります
		ngmsg	すうどん作りに失敗し，材料を無駄にしてしまいました‥
			use		3	小麦粉
			use		2	ねぎ
			use		2	かまぼこ
			use		40	きれいな丼
			get		40	すうどん	80%	すうどんができました
			get		10	店力	10%
	@@USE
		time	1h
		exp	1%
		exptime	20m
		job	うどん屋	times/job_udon_time_rate
		scale	回
		action	作る
		name	わかめうどんを作る
		info	わかめうどんを作ります
		ngmsg	わかめうどん作りに失敗し，材料を無駄にしてしまいました‥
			use		3	小麦粉
			use		2	ねぎ
			use		5	わかめ
			use		32	きれいな丼
			get		30	わかめうどん	90%	わかめうどんができました
			get		10	店力	10%
	@@USE
		time	1h
		exp	1%
		exptime	20m
		job	うどん屋	times/job_udon_time_rate
		scale	回
		action	作る
		name	きつねうどんを作る
		info	きつねうどんを作ります
		ngmsg	きつねうどん作りに失敗し，材料を無駄にしてしまいました‥
			use		3	小麦粉
			use		2	ねぎ
			use		10	油揚げ
			use		25	きれいな丼
			get		25	きつねうどん	80%	きつねうどんができました
			get		10	店力	10%
	@@USE
		time	1h
		exp	1%
		exptime	20m
		job	うどん屋	times/job_udon_time_rate
		scale	回
		action	作る
		name	丸天うどんを作る
		info	丸天うどんを作ります
		ngmsg	丸天うどん作りに失敗し，材料を無駄にしてしまいました‥
			use		3	小麦粉
			use		2	ねぎ
			use		10	丸天
			use		20	きれいな丼
			get		20	丸天うどん	80%	丸天うどんができました
			get		10	店力	10%
	@@USE
		time	2h
		exp	2%
		exptime	40m
		job	うどん屋	times/job_udon_time_rate
		scale	回
		action	作る
		name	えび天うどんを作る
		info	えび天うどんを作ります
		ngmsg	えび天うどん作りに失敗し，材料を無駄にしてしまいました‥
			use		5	小麦粉
			use		5	ねぎ
			use		20	えび天
			use		20	きれいな丼
			get		20	えび天うどん	80%	えび天うどんができました
			get		20	店力	10%
	@@USE
		time	20m
		exp	0%
		exptime	10m
		job	うどん屋	times/job_udon_time_rate
		scale	セット
		action	作る
		name	うどん三昧を作る
		info	うどん三昧を作ります
		okmsg	うどん三昧ができました
			needexp		20%
			use		10	きつねうどん
			use		10	丸天うどん
			use		10	えび天うどん
			get		10	うどん三昧
	@@USE
		time	3h
		exp	4%
		exptime	1h
		job	うどん屋	times/job_udon_time_rate
		scale	回
		action	作る
		name	キャビアうどんを作る
		info	キャビアうどんを作ります
		func	lostman
		param	50
		ngmsg	キャビアうどん作りに失敗し，材料を無駄にしてしまいました‥
			needexp		40%
			use		3	小麦粉
			use		1	かつお
			use		2	キャビア
			use		8	きれいな丼
			get		8	キャビアうどん	80%	キャビアうどんができました
			get		10	店力	20%
	@@USE
		time	3h
		exp	4%
		exptime	1h
		job	うどん屋	times/job_udon_time_rate
		scale	回
		action	作る
		name	トリュフうどんを作る
		info	トリュフうどんを作ります
		func	lostman
		param	50
		ngmsg	トリュフうどん作りに失敗し，材料を無駄にしてしまいました‥
			needexp		40%
			use		3	小麦粉
			use		1	かつお
			use		2	トリュフ
			use		8	きれいな丼
			get		10	トリュフうどん	60%	トリュフうどんができました
			get		10	店力	20%
	@@USE
		time	3h
		exp	4%
		exptime	1h
		job		うどん屋	times/job_udon_time_rate
		scale	回
		action	作る
		name	フォアグラうどんを作る
		info	フォアグラうどんを作ります
		func	lostman
		param	50
		ngmsg	フォアグラうどん作りに失敗し，材料を無駄にしてしまいました‥
			needexp		40%
			use		3	小麦粉
			use		1	かつお
			use		2	フォアグラ
			use		6	きれいな丼
			get		6	フォアグラうどん	80%	フォアグラうどんができました
			get		10	店力	20%
	@@USE
		time	6h
		exp	5%
		exptime	2h
		job		うどん屋	times/job_udon_time_rate
		scale	回
		action	作る
		name	博多うどんを作る
		info	博多うどんを作ります
		func	lostman
		param	50
		ngmsg	博多うどん作りに失敗し，材料を無駄にしてしまいました‥
			needexp		60%
			use		5	小麦粉
			use		1	豚
			use		2	辛子めんたい
			use		6	きれいな丼
			get		6	博多うどん	80%	博多うどんができました
			get		10	店力	20%
	@@USE
		time	6h
		exp	5%
		exptime	2h
		job		うどん屋	times/job_udon_time_rate
		scale	回
		action	作る
		name	オリジナルうどんを作る
		info	オリジナルうどんを作ります
		ngmsg	オリジナルうどん作りに失敗し，材料を無駄にしてしまいました‥
			needexp		80%
			need		1	オリジナルうどんレシピ
			use		5	小麦粉
			use		1	かつお
			use		1	がちょう
			use		5	とうがらし
			use		3	きれいな丼
			get		5	オリジナルうどん	40%	オリジナルうどんができました
			get		10	店力	20%
		func	_local_
			my $ret="";
			$DT->{user}->{udoncnt}+=1;
			if (rand(1000)<100)
			{
				UseItem(@@ITEMNO"うどん職人",1,"<br>仕事を終えたうどん職人が，黙って去っていきました");
			}
			if ((rand(1000)<100)&&($DT->{user}->{udoncnt}>50))
			{
				$DT->{user}->{udoncnt}=0;
				UseItem(@@ITEMNO"オリジナルうどんレシピ",1,"<br>オリジナルうどんレシピにうっかり火がつき，燃やしてしまいました");
				WriteLog(0,$DT->{id},"オリジナルうどんレシピを失いました");
				WriteLog(2,0,$DT->{shopname}."がオリジナルうどんレシピをうっかり燃やしてしまったようです。");
			}
			return $ret;
		_local_
	@@USE
		time	6h
		exp		1%
		exptime	4h
		job		うどん屋	times/job_udon_time_rate
		action	という名前のうどんを作る
		name	オリジナルうどんを開発する
		info	精魂込めて作るオリジナルうどんに名前をつけます
		arg		nocount|message30
		okmsg	忘れないうちに作り方をメモしておきました
			use		1	すうどん
			use		1	わかめうどん
			use		1	きつねうどん
			use		1	丸天うどん
			use		1	えび天うどん
			use		1	キャビアうどん
			use		1	トリュフうどん
			use		1	フォアグラうどん
			use		1	博多うどん
			get		1	オリジナルうどん
			get		1	オリジナルうどんレシピ
		func	_local_
			# オリジナルうどんを作る
			main::OutError('名前をつけてください') if !$USE->{arg}->{message};
			my $ret;
			$ret='オリジナルうどん【'.$USE->{arg}->{message}.'】が完成しました';	
			WriteLog(3,0,$DT->{shopname}."が特製うどん「".$USE->{arg}->{message}."」を完成させました。");
			WriteLog(0,$DT->{id},$ret);
			$DT->{user}->{udon}=$USE->{arg}->{message};
			return $ret;
		_local_
	@@USE
		time	6h
		action	うどん作りの専門家になる
		arg		nocount
		name	うどん作りの専門家になる
		info	今までの経験を生かして，うどん作りの専門家になります
			needexp		20%
		func	_local_
			my $ret="";
			main::OutError('現在すでにうどん作りの専門家です') if ($DT->{job} eq 'udon');
			$DT->{job} = 'udon';
			$ret="うどん作りの専門家になりました";
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_

@@ITEM
	no		6
	type	人材
	code	man-soba
	name	そば職人
	info	各種そばを1杯ずつ揃えて，新しいそばの開発を！
	scale	人
	price	30000
	cost	1000
	limit	3/0.3
	plus	2d
	pop	3d
	flag	noshowcase|human
	@@USE
		time	1h
		exp	1%
		exptime	20m
		job	そば屋	times/job_soba_time_rate
		scale	回
		action	作る
		name	かけそばを作る
		info	かけそばを作ります
		ngmsg	かけそば作りに失敗し，材料を無駄にしてしまいました‥
			use		3	そば粉
			use		2	ねぎ
			use		2	かまぼこ
			use		40	きれいな丼
			get		40	かけそば	80%	かけそばができました
			get		10	店力	10%
	@@USE
		time	1h
		exp	1%
		exptime	20m
		job		そば屋	times/job_soba_time_rate
		scale	回
		action	作る
		name	わかめそばを作る
		info	わかめそばを作ります
		ngmsg	わかめそば作りに失敗し，材料を無駄にしてしまいました‥
			use		3	そば粉
			use		2	ねぎ
			use		5	わかめ
			use		32	きれいな丼
			get		30	わかめそば	90%	わかめそばができました
			get		10	店力	10%
	@@USE
		time	1h
		exp	1%
		exptime	20m
		job		そば屋	times/job_soba_time_rate
		scale	回
		action	作る
		name	きつねそばを作る
		info	きつねそばを作ります
		ngmsg	きつねそば作りに失敗し，材料を無駄にしてしまいました‥
			use		3	そば粉
			use		2	ねぎ
			use		10	油揚げ
			use		25	きれいな丼
			get		25	きつねそば	80%	きつねそばができました
			get		10	店力	10%
	@@USE
		time	1h
		exp	1%
		exptime	20m
		job	そば屋	times/job_soba_time_rate
		scale	回
		action	作る
		name	丸天そばを作る
		info	丸天そばを作ります
		ngmsg	丸天そば作りに失敗し，材料を無駄にしてしまいました‥
			use		3	そば粉
			use		2	ねぎ
			use		10	丸天
			use		20	きれいな丼
			get		20	丸天そば	80%	丸天そばができました
			get		10	店力	10%
	@@USE
		time	2h
		exp	2%
		exptime	40m
		job	そば屋	times/job_soba_time_rate
		scale	回
		action	作る
		name	えび天そばを作る
		info	えび天そばを作ります
		ngmsg	えび天そば作りに失敗し，材料を無駄にしてしまいました‥
			use		5	そば粉
			use		5	ねぎ
			use		20	えび天
			use		20	きれいな丼
			get		20	えび天そば	80%	えび天そばができました
			get		20	店力	10%
	@@USE
		time	20m
		exp	0%
		exptime	10m
		job		そば屋	times/job_soba_time_rate
		scale	セット
		action	作る
		name	そば三昧を作る
		info	そば三昧を作ります
		okmsg	そば三昧ができました
			needexp		20%
			use		10	きつねそば
			use		10	丸天そば
			use		10	えび天そば
			get		10	そば三昧
	@@USE
		time	3h
		exp	4%
		exptime	1h
		job	そば屋	times/job_soba_time_rate
		scale	回
		action	作る
		name	キャビアそばを作る
		info	キャビアそばを作ります
		func	lostman
		param	50
		ngmsg	キャビアそば作りに失敗し，材料を無駄にしてしまいました‥
			needexp		40%
			use		3	そば粉
			use		1	かつお
			use		2	キャビア
			use		8	きれいな丼
			get		8	キャビアそば	80%	キャビアそばができました
			get		10	店力	20%
	@@USE
		time	3h
		exp	4%
		exptime	1h
		job	そば屋	times/job_soba_time_rate
		scale	回
		action	作る
		name	トリュフそばを作る
		info	トリュフそばを作ります
		func	lostman
		param	50
		ngmsg	トリュフそば作りに失敗し，材料を無駄にしてしまいました‥
			needexp		40%
			use		3	そば粉
			use		1	かつお
			use		2	トリュフ
			use		8	きれいな丼
			get		10	トリュフそば	60%	トリュフそばができました
			get		10	店力	20%
	@@USE
		time	3h
		exp	4%
		exptime	1h
		job	そば屋	times/job_soba_time_rate
		scale	回
		action	作る
		name	フォアグラそばを作る
		func	lostman
		param	50
		info	フォアグラそばを作ります
		ngmsg	フォアグラそば作りに失敗し，材料を無駄にしてしまいました‥
			needexp		40%
			use		3	そば粉
			use		1	かつお
			use		2	フォアグラ
			use		6	きれいな丼
			get		6	フォアグラそば	80%	フォアグラそばができました
			get		10	店力	20%
	@@USE
		time	6h
		exp	5%
		exptime	2h
		job	そば屋	times/job_soba_time_rate
		scale	回
		action	作る
		name	博多そばを作る
		info	博多そばを作ります
		func	lostman
		param	50
		ngmsg	博多そば作りに失敗し，材料を無駄にしてしまいました‥
			needexp		60%
			use		5	そば粉
			use		1	豚
			use		2	辛子めんたい
			use		6	きれいな丼
			get		6	博多そば	80%	博多そばができました
			get		10	店力	20%
	@@USE
		time	6h
		exp	5%
		exptime	2h
		job	そば屋	times/job_soba_time_rate
		scale	回
		action	作る
		name	オリジナルそばを作る
		info	オリジナルそばを作ります
		ngmsg	オリジナルそば作りに失敗し，材料を無駄にしてしまいました‥
			needexp		80%
			need		1	オリジナルそばレシピ
			use		5	そば粉
			use		1	かつお
			use		1	ちょうざめ
			use		15	卵
			use		3	きれいな丼
			get		5	オリジナルそば	40%	オリジナルそばができました
			get		10	店力	30%
		func	_local_
			my $ret="";
			$DT->{user}->{sobacnt}+=1;
			if (rand(1000)<100)
			{
				UseItem(@@ITEMNO"そば職人",1,"<br>仕事を終えたそば職人が，黙って去っていきました");
			}
			if ((rand(1000)<100)&&($DT->{user}->{sobacnt}>50))
			{
				$DT->{user}->{sobacnt}=0;
				UseItem(@@ITEMNO"オリジナルそばレシピ",1,"<br>オリジナルそばレシピにうっかり火がつき，燃やしてしまいました");
				WriteLog(0,$DT->{id},"オリジナルそばレシピを失いました");
				WriteLog(2,0,$DT->{shopname}."がオリジナルそばレシピをうっかり燃やしてしまったようです。");
			}
			return $ret;
		_local_
	@@USE
		time	6h
		exp		1%
		exptime	4h
		job		そば屋	times/job_soba_time_rate
		action	という名前のそばを作る
		name	オリジナルそばを開発する
		info	精魂込めて作るオリジナルそばに名前をつけます
		arg		nocount|message30
		okmsg	忘れないうちに作り方をメモしておきました
			use		1	かけそば
			use		1	わかめそば
			use		1	きつねそば
			use		1	丸天そば
			use		1	えび天そば
			use		1	キャビアそば
			use		1	トリュフそば
			use		1	フォアグラそば
			use		1	博多そば
			get		1	オリジナルそば
			get		1	オリジナルそばレシピ
		func	_local_
			# オリジナルそばを作る
			main::OutError('名前をつけてください') if !$USE->{arg}->{message};
			my $ret;
			$ret='オリジナルそば【'.$USE->{arg}->{message}.'】が完成しました';	
			WriteLog(3,0,$DT->{shopname}."が特製そば「".$USE->{arg}->{message}."」を完成させました。");
			WriteLog(0,$DT->{id},$ret);
			$DT->{user}->{soba}=$USE->{arg}->{message};
			return $ret;
		_local_
	@@USE
		time	6h
		action	そば作りの専門家になる
		arg		nocount
		name	そば作りの専門家になる
		info	今までの経験を生かして，そば作りの専門家になります
			needexp		20%
		func	_local_
			my $ret="";
			main::OutError('現在すでにそば作りの専門家です') if ($DT->{job} eq 'soba');
			$DT->{job} = 'soba';
			$ret="そば作りの専門家になりました";
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_

@@ITEM
	no		7
	type	人材
	code	man-benri
	name	便利屋
	info	棚作りや丼洗いなどが得意です
	scale	人
	price	30000
	cost	1000
	limit	5/0.5
	plus	2h
	pop		3d
	flag	noshowcase|human
	@@USE
		time	1h
		job		人材派遣業	times/job_man_time_rate
		scale	回
		action	作業する
		price	0
		name	陳列棚を1つにする
		info	陳列棚を1つにする
		arg		nocount
		param	1
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
			WriteLog(3,0,$DT->{shopname}."の陳列棚が$DT->{showcasecount}個になりました");
			
			return $ret;
		_local_
	@@USE
		time	2h
		job		人材派遣業	times/job_man_time_rate
		price	10000
		name	陳列棚を2つにする
		info	陳列棚を2つにする
		func	_local_1
		arg		nocount
		param	2
	@@USE
		time	4h
		job		人材派遣業	times/job_man_time_rate
		price	50000
		name	陳列棚を3つにする
		info	陳列棚を3つにする
		func	_local_1
		arg		nocount
		param	3
			need	2	便利屋
	@@USE
		time	6h
		job		人材派遣業	times/job_man_time_rate
		price	100000
		name	陳列棚を4つにする
		info	陳列棚を4つにする
		func	_local_1
		arg		nocount
		param	4
			need	2	便利屋
	@@USE
		time	10h
		job		人材派遣業	times/job_man_time_rate
		price	200000
		name	陳列棚を5つにする
		info	陳列棚を5つにする
		func	_local_1
		arg		nocount
		param	5
			need	3	便利屋
	@@USE
		time	12h
		job		人材派遣業	times/job_man_time_rate
		price	500000
		name	陳列棚を6つにする
		info	陳列棚を6つにする
		func	_local_1
		arg		nocount
		param	6
			need	3	便利屋
	@@USE
		time	14h
		job		人材派遣業	times/job_man_time_rate
		price	1000000
		name	陳列棚を7つにする
		info	陳列棚を7つにする
		func	_local_1
		arg		nocount
		param	7
			need	4	便利屋
	@@USE
		time	16h
		job		人材派遣業	times/job_man_time_rate
		price	2000000
		name	陳列棚を8つにする
		info	陳列棚を8つにする
		func	_local_1
		arg		nocount
		param	8
			need	5	便利屋
	@@USE
		time	30m
		exp		1%
		exptime	10m
		job		人材派遣業	times/job_man_time_rate
		scale	回
		action	洗う
		name	丼洗いをする
		info	汚れた丼を洗います
		func	lostman
		param	10
		ngmsg	丼を全部割ってしまいました‥
			use		10	汚れた丼
			get		10	きれいな丼	90%	丼がピカピカになりました
			get		10	店力	02%
	@@USE
		time	1h
		exp		1%
		exptime	30m
		job		人材派遣業	times/job_man_time_rate
		scale	回
		action	セットする
		name	食器洗い機で丼洗いをする
		info	汚れた丼を食器洗い機にセットします
		func	lostman
		param	50
		ngmsg	丼を全部割ってしまいました‥
			need		1	食器洗い機
			use		50	汚れた丼
			get		50	きれいな丼	95%	丼がピカピカになりました
			get		10	店力	05%
	@@use
		time	10h
		exp		5%
		exptime	6h
		job		人材派遣業	times/job_man_time_rate
		action	広告を流す
		name	[新聞]に広告を流す
		info	下のフォームに文を書き込んでボタンをクリックすると<br>[新聞]に広告が流れます
		param	300
		arg		nocount|message100
			use	1	便利屋
		func	_local_
			main::OutError('広告文をご記入ください') if !$USE->{arg}->{message};
			my $ret;
			my $up=int($USE->{param1}*(2-$DT->{rank}/5000));
			$DT->{rank}+=$up;
			$DT->{rank}=10000 if $DT->{rank}>10000;

			$ret='[新聞]に広告を流して注目され，人気'.int($up/100)."%アップ";
			WriteLog(2,0,"【広告】".$USE->{arg}{message});
			WriteLog(0,$DT->{id},$ret);	
			return $ret;
		_local_
	@@USE
		time	6h
		action	看板を下ろす
		arg		nocount
		name	看板を下ろす
		info	専門職の看板を下ろします
		func	_local_
			my $ret="";
			main::OutError('専門職の看板はあがっていません') if ($DT->{job} eq '');
			$DT->{money}+=30000;
			$DT->{job}='';	
			$ret='看板を下ろし，慰労金\30000を受け取りました';
			WriteLog(0,$DT->{id},"看板を下ろし，慰労金を受け取りました");
			WriteLog(3,0,"専門職の看板を下ろした".$DT->{shopname}."に，商店会から慰労金が支給されたようです");
			return $ret;
		_local_

@@ITEM
	no		8
	type	人材
	code	man-black
	name	ブラック工作員
	info	たまった店力を使って裏工作をします
	scale	人
	price	50000
	cost	2500
	limit	2/0.2
	plus	2d
	flag	noshowcase|human
	@@use
		time	6h
		exp	5%
		exptime	4h
		job		裏家業	times/job_black_time_rate
		scale	回
		action	仲間を呼ぶ
		name	仲間を呼ぶ
		info	仲間が来る確率は50%です
		ngmsg	仲間は来ませんでした
		okmsg	仲間がやってきました
		arg		nocount
			get		1	ブラック工作員	50%
	@@use
		time	1h
		exp	1%
		exptime	30m
		job		裏家業	times/job_black_time_rate
		scale	回
		action	作る
		name	闇うどんを作る
		info	ありあわせの材料で適当にうどんを作ってみます
		func	lostman
		param	50
		ngmsg	闇うどん作りに失敗しました‥
			use		10	汚れた丼
			get		10	闇うどん	95%	闇うどんを作りました
			get		10	店力	07%
	@@use
		time	1h
		exp	1%
		exptime	30m
		job		裏家業	times/job_black_time_rate
		scale	回
		action	作る
		name	闇そばを作る
		info	ありあわせの材料で適当にそばを作ってみます
		func	lostman
		param	50
		ngmsg	闇そば作りに失敗しました‥
			use		10	汚れた丼
			get		10	闇そば	95%	闇そばを作りました
			get		10	店力	07%
	@@use
		time	4h
		exp	5%
		exptime	2h
		job		裏家業	times/job_black_time_rate
		scale	回
		action	実行する
		name	すり替え作戦を実行する
		info	他店の陳列棚の商品を，こっそり他の商品とすり替えます
		arg		target|nocount
			use		1	ブラック工作員
			use		50	闇うどん
			use		50	闇そば
			use		10	店力
		func	_local_
		# ★すり替え作戦を実行する
			my $cnt=int(rand(100))+1;
			my $ret="すり替え作戦は失敗し，店の人気が下がりました";
			if(rand(1000)<900)
			{
				if($DTS->{item}[@@ITEMNO"警報機"-1])
				{
					if(rand(1000)<200)
					{
					$DTS->{showcase}[0]=57; # 闇そばのアイテム番号
					$DTS->{price}[0]=20; # 闇そばの価格
					$DTS->{item}[@@ITEMNO"闇そば"-1]+=$cnt;
					$DTS->{item}[@@ITEMNO"闇そば"-1]=2000 if $DTS->{item}[$itemno2-1]>2000;
					$ret="すり替え作戦は成功しました";
					$DTS->{item}[@@ITEMNO"警報機"-1]--;
					WriteLog(2,0,$DTS->{shopname}."の陳列棚の商品が闇そばにすり替えられ，怒った店主が警報機をたたき壊しました");
					}
					elsif(rand(1000)<700)
					{
					$DT->{rank}-=int($DT->{rank}/3);
					$DTS->{item}[@@ITEMNO"警報機"-1]--;
					WriteLog(3,0,$DTS->{shopname}."に侵入した".$DT->{shopname}."のブラック工作員が，警報機を破壊しましたが結局捕まりました");
					}
					else
					{
					$DT->{rank}-=int($DT->{rank}/3);
					WriteLog(3,0,$DTS->{shopname}."の警報機が鳴り響き，侵入していた".$DT->{shopname}."のブラック工作員が捕まりました");
					}
				}
				else
				{
				$DTS->{showcase}[0]=45; # 闇うどんのアイテムナンバー
				$DTS->{price}[0]=20; # 闇うどんの価格
				$DTS->{item}[@@ITEMNO"闇うどん"-1]+=$cnt;
				$DTS->{item}[@@ITEMNO"闇うどん"-1]=2000 if $DTS->{item}[$itemno-1]>2000;
				$ret="すり替え作戦は成功しました";
				WriteLog(2,0,$DTS->{shopname}."の陳列棚の商品が闇うどんにすり替えられました");
				}
			}
			else
			{
			$ret="すり替え作戦は失敗しました";
			WriteLog(3,0,$DTS->{shopname}."に現れたブラック工作員が，なぜか何もせずに去っていきました");
			}
			WriteLog(0,$DT->{id},$ret);
			return $ret;
			_local_
	@@use
		time	4h
		exp	10%
		job		裏家業	times/job_black_time_rate
		scale	回
		action	万引きをする
		name	万引きをする
		info	警報機のある店は危険！？
		arg		target|nocount
			use		50	店力
		func	_local_
			# ★万引き作戦（成功時はイベントと同じメッセージを出力）
			
			my $ret="万引きは失敗し，お店の人気が下がりました";
			if(rand(1000)<700)
			{
				if($DTS->{item}[@@ITEMNO"警報機"-1])
				{
					$DT->{rank}-=int($DT->{rank}/2);
					if(rand(1000)<700)
					{
						$DTS->{item}[@@ITEMNO"警報機"-1]--;
						WriteLog(3,0,$DT->{shopname}."のブラック工作員が".$DTS->{shopname}."へ万引きに入り，$ITEM[@@ITEMNO"警報機"]->{name}を破壊しましたが結局捕まりました。");
					}
					else
					{
						WriteLog(3,0,$DT->{shopname}."のブラック工作員が".$DTS->{shopname}."へ万引きに入りましたが失敗しました。");
					}
				}
				else
				{
					my $manbiki_count=0;
					foreach my $idx (0..$DTS->{showcasecount}-1)
					{
						my $itemno=$DTS->{showcase}[$idx];
						if($itemno)
						{
							my $cnt=int($DTS->{item}[$itemno-1]/4);
							$cnt=$ITEM[$itemno]->{limit}-$DT->{item}[$itemno-1] if $DT->{item}[$itemno-1]+$cnt>$ITEM[$itemno]->{limit};
							$DTS->{item}[$itemno-1]-=$cnt;
							$DT->{item}[$itemno-1]+=$cnt;
							$manbiki_count+=$cnt*$DTS->{price}[$idx];
						}
					}
					$ret="万引きは成功しました";
					$ret="ブラック工作員は気が変わって万引きをやめました" if !$manbiki_count;
					WriteLog(2,0,$DTS->{shopname}."が総額".GetMoneyString($manbiki_count)."の万引き被害に遭いました。") if $manbiki_count;
					WriteLog(2,0,$DTS->{shopname}."に入った万引き犯は何も取らずに逃げました。") if !$manbiki_count;
				}
			}
			else
			{
				$DT->{rank}-=int($DT->{rank}/3);
				WriteLog(3,0,$DT->{shopname}."のブラック工作員が".$DTS->{shopname}."へ万引きに入りましたが失敗しました。");
			}
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_
	@@use
		time	10h
		exp	10%
		job		裏家業	times/job_black_time_rate
		scale	回
		action	悪い噂を流す
		name	店舗の悪い噂を流す
		info	根も葉もない噂を流し，他店の人気を下げます
		arg		target|nocount
			use		1	ブラック工作員
			use		100	店力
		func	_local_
			# ★悪い噂を流す作戦
			my $ret;
			if(rand(1000)<750)
			{
				$DTS->{rank}-=int($DTS->{rank}/4);
				$ret=$DTS->{shopname}.'の悪い噂を流す作戦が成功しました。';
				WriteLog(0,$DT->{id},$ret);
				WriteLog(3,0,$DTS->{shopname}.'の悪い噂が広まり人気が下がりました。');
			}
			else
			{
				$DT->{rank}-=int($DT->{rank}/2);
				$ret=$DTS->{shopname}.'の悪い噂を流す作戦が失敗しました';
				WriteLog(0,$DT->{id},$ret);
				WriteLog(3,0,$DT->{shopname}."のブラック工作員が".$DTS->{shopname}.'の悪い噂を流そうと画策していたようです。');
			}
			return $ret;
			_local_
	@@use
		time	2h
		exp	10%
		job		裏家業	times/job_black_time_rate
		action	解放する
		name	店力を解放する
		info	店力をすべて解放し，店の人気を上げます
		arg		nocount
		func	_local_
			main::OutError('店力が100以上ないと解放できません') if ($DT->{item}[@@ITEMNO"店力"-1]<100);
			my $ret="";
			my $power;
			my $cnt=$DT->{item}[@@ITEMNO"店力"-1];
			$power=$DT->{item}[@@ITEMNO"店力"-1]*3;
			my $up=int($power*(2-$DT->{rank}/5000));

			$DT->{rank}+=$up;
			$DT->{rank}=10000 if $DT->{rank}>10000;
			$ret="店力をすべて解放しました（人気".int($up/100)."%アップ）";
			UseItem(@@ITEMNO"店力",$cnt);
			WriteLog(0,$DT->{id},$ret);
			WriteLog(3,0,$DT->{shopname}."がすべての店力を解放しました。");
			return $ret;
			_local_
	@@USE
		time	0m
		action	時間操作をする
		scale	回
		name	時間操作をする
		info	成功すれば時間を取り戻せる！
			use		2	ブラック工作員
		arg		nocount
		func	_local_
			# ★持ち時間増加
			my $ret;
			my $cnt=int(rand(6))+1;

			if(rand(1000)<100)
			{
				$ret='時間操作は失敗しました';
				WriteLog(3,0,$DT->{shopname}.'のブラック工作員が，時間操作をしくじったようです。');
				AddItem(8,1,'ブラック工作員の1人が，時空の割れ目から戻ってきました');
				WriteLog(0,$DT->{id},'時間操作は失敗しました');
			}
			else
			{
				$DT->{time}-=3600*($cnt);
				$DT->{user}->{black}+=1;
				$ret='時間操作は成功しました　（＋'.($cnt).'時間）';
				WriteLog(3,0,$DT->{shopname}.'のブラック工作員が，時間操作をおこなったようです。');
				WriteLog(0,$DT->{id},'時間操作の結果，持ち時間が増えました');
			}					
			return $ret;
		_local_
	@@USE
		time	6h
		action	裏工作のプロになる
		arg		nocount
		name	裏工作のプロになる
		info	今までの経験を生かして，裏工作のプロフェッショナルになります
			needexp		20%
		func	_local_
			my $ret="";
			main::OutError('現在すでに裏工作のプロフェッショナルです') if ($DT->{job} eq 'black');
			$DT->{job} = 'black';
			$ret="裏工作のプロフェッショナルになりました";
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_

@@ITEM
	no		9
	type	陸産物
	code	riku-tamagoa
	name	卵
	info	栄養価の高い食品です
	scale	個
	price	100
	cost	10
	limit	5000/50
	base	2500/10000
	plus	5h
	pop	40m
	point	20%
	@@USE
		time	1m
		action	コンポストに入れる
		name	コンポストに入れる
		info	古くなった食品をコンポストに入れ，堆肥を作ります
		ngmsg	堆肥作りに失敗しました
			use		1	卵
			get		10	堆肥	15%	上質の堆肥ができました

@@ITEM
	no		10
	type	陸産物
	code	riku-tamagob
	name	孵化を待つ卵
	info	栄養価の高い食品です
	scale	個
	price	100
	cost	50
	limit	50/0
	pop	10d
	funct	_local_
		my($ITEM,@DT)=@_;
		my $gabirth_per_day=3;  # 1日にがちょうが3羽産まれるような確率(?)の設定
		my $nibirth_per_day=30;  # 1日ににわとりが30羽産まれるような確率(?)の設定
		my $val          =1;  # 一度に産まれる基本数

		my $gabirth_rate=$gabirth_per_day && (86400/$gabirth_per_day); # 0で割るのを阻止
		my $nibirth_rate=$nibirth_per_day && (86400/$nibirth_per_day);
		foreach my $DT (@DT)
		{
			next if !$DT->{item}[@@ITEMNO"孵化を待つ卵"-1];
			if(rand($gabirth_rate)<$TIMESPAN) # 1店舗につき「1日に$gabirth_per_day回」の確率で条件が真になる(ハズ…)
			{
				UseItemSub(@@ITEMNO"孵化を待つ卵",$val,$DT);
				AddItemSub(@@ITEMNO"がちょう",$val,$DT);
				WriteLog(0,$DT->{id},'なんと！卵からがちょうが生まれました');
			}
			if(rand($nibirth_rate)<$TIMESPAN)
			{
				UseItemSub(@@ITEMNO"孵化を待つ卵",$val,$DT);
				AddItemSub(@@ITEMNO"にわとり",$val,$DT);
			}
		}
	_local_ 

@@ITEM
	no		11
	type	陸産物
	code	riku-age
	name	油揚げ
	info	俗にキツネの好物といわれる食品です
	scale	枚
	price	300
	cost	10
	limit	10000/10
	base	500/2000
	plus	5h
	pop	40m
	point	20%
	@@USE
		time	1m
		action	コンポストに入れる
		name	コンポストに入れる
		info	古くなった食品をコンポストに入れ，堆肥を作ります
		ngmsg	堆肥作りに失敗しました
			use		1	油揚げ
			get		10	堆肥	20%	上質の堆肥ができました

@@ITEM
	no		12
	type	陸産物
	code	riku-negi
	name	ねぎ
	info	うどんやそばには欠かせない薬味です
	scale	把
	price	200
	limit	5000/10
	base	500/2000
	plus	3h
	pop	1h
	point	10%
	@@USE
		time	1m
		action	コンポストに入れる
		name	コンポストに入れる
		info	古くなった食品をコンポストに入れ，堆肥を作ります
		ngmsg	堆肥作りに失敗しました
			use		1	ねぎ
			get		10	堆肥	25%	上質の堆肥ができました

@@ITEM
	no		13
	type	陸産物
	code	riku-komugi
	name	小麦粉
	info	うどんや天ぷらの材料になります
	scale	kg
	price	500
	cost	10
	limit	1000/10
	base	500/1000
	plus	4h
	pop	4h
	point	30%
	@@USE
		time	1m
		action	コンポストに入れる
		name	コンポストに入れる
		info	古くなった食品をコンポストに入れ，堆肥を作ります
		ngmsg	堆肥作りに失敗しました
			use		1	小麦粉
			get		10	堆肥	30%	上質の堆肥ができました

@@ITEM
	no		14
	type	陸産物
	code	riku-soba
	name	そば粉
	info	そばの材料になります
	scale	kg
	price	500
	cost	10
	limit	1000/10
	base	500/1000
	plus	4h
	pop	4h
	point	30%
	@@USE
		time	1m
		action	コンポストに入れる
		name	コンポストに入れる
		info	古くなった食品をコンポストに入れ，堆肥を作ります
		ngmsg	堆肥作りに失敗しました
			use		1	そば粉
			get		10	堆肥	30%	上質の堆肥ができました

@@ITEM
	no		15
	type	陸産物
	code	riku-tougarasi
	name	とうがらし
	info	博多名物『辛子めんたい』の味付けに使います
	scale	kg
	price	800
	limit	1000/10
	base	500/1000
	plus	-1d
	pop	5h
	@@USE
		time	1m
		action	コンポストに入れる
		name	コンポストに入れる
		info	古くなった食品をコンポストに入れ，堆肥を作ります
		ngmsg	堆肥作りに失敗しました
			use		1	とうがらし
			get		10	堆肥	35%	上質の堆肥ができました

@@ITEM
	no		16
	type	陸産物
	code	riku-daizu
	name	大豆
	info	加工品の一つに『油揚げ』があります
	scale	kg
	price	400
	limit	1500/20
	base	1000/2000
	plus	-1d
	pop	5h
	@@USE
		time	1m
		action	コンポストに入れる
		name	コンポストに入れる
		info	古くなった食品をコンポストに入れ，堆肥を作ります
		ngmsg	堆肥作りに失敗しました
			use		1	大豆
			get		10	堆肥	35%	上質の堆肥ができました

@@ITEM
	no		17
	type	陸産物
	code	riku-toukibi
	name	とうもろこし
	info	家畜の餌にもなります
	scale	kg
	price	600
	limit	1000/10
	base	500/1000
	plus	-1d
	pop	4h
	point	50%
	@@USE
		time	1m
		action	コンポストに入れる
		name	コンポストに入れる
		info	古くなった食品をコンポストに入れ，堆肥を作ります
		ngmsg	堆肥作りに失敗しました
			use		1	とうもろこし
			get		10	堆肥	35%	上質の堆肥ができました

@@ITEM
	no		18
	type	陸産物
	code	riku-toryuhu
	name	トリュフ
	info	めずらしいきのこです
	scale	個
	price	2000
	limit	500
	base	50/200
	plus	-1d
	pop	8h
	@@USE
		time	1m
		action	コンポストに入れる
		name	コンポストに入れる
		info	古くなった食品をコンポストに入れ，堆肥を作ります
		ngmsg	堆肥作りに失敗しました
			use		1	トリュフ
			get		10	堆肥	35%	上質の堆肥ができました

@@ITEM
	no		19
	type	陸産物
	code	riku-foagura
	name	フォアグラ
	info	肥大させたがちょうの肝臓です
	scale	個
	price	2000
	limit	500
	base	50/200
	plus	-1d
	pop	8h
	@@USE
		time	1m
		action	コンポストに入れる
		name	コンポストに入れる
		info	古くなった食品をコンポストに入れ，堆肥を作ります
		ngmsg	堆肥作りに失敗しました
			use		1	フォアグラ
			get		10	堆肥	35%	上質の堆肥ができました

@@ITEM
	no		20
	type	陸産物
	code	riku-niwatori
	name	にわとり
	info	卵を産ませるには餌が必要です
	scale	羽
	price	5000
	limit	30/3
	base	30/300
	plus	1d
	pop	10d
	@@USE
		time	30m
		action	交換する
		scale	回
		name	がちょうと交換する
		info	養育場に行って鶏をがちょうと交換します
		okmsg	がちょうを手に入れました
			use		2	にわとり
			get		1	がちょう
	@@USE
		time	30m
		action	交換する
		scale	回
		name	豚と交換する
		info	養育場に行って鶏を豚と交換します
		okmsg	豚を手に入れました
			use		3	にわとり
			get		1	豚

@@ITEM
	no		21
	type	陸産物
	code	riku-gatyou
	name	がちょう
	info	餌をたっぷりやって太らせましょう
	scale	羽
	price	7500
	limit	20/2
	base	20/200
	plus	-1d
	pop	10d

@@ITEM
	no		22
	type	陸産物
	code	riku-buta
	name	豚
	info	面倒をよく見ていると，恩返しをするかもしれません
	scale	頭
	price	10000
	limit	20/2
	plus	1d
	pop	10d

@@ITEM
	no		23
	type	海産物
	code	umi-ebi
	name	えび
	info	プリッと身の引き締まった，近海物のえびです
	scale	匹
	price	100
	limit	5000/20
	base	1000/4000
	plus	3h
	pop	1h
	point	10%
	@@USE
		time	1m
		action	コンポストに入れる
		name	コンポストに入れる
		info	古くなった食品をコンポストに入れ，堆肥を作ります
		ngmsg	堆肥作りに失敗しました
			use		1	えび
			get		10	堆肥	25%	上質の堆肥ができました

@@ITEM
	no		24
	type	海産物
	code	umi-wakame
	name	わかめ
	info	ミネラルたっぷりの海藻です
	scale	kg
	price	200
	limit	2500/10
	base	100/2000
	plus	4h
	pop	1h
	point	10%
	@@USE
		time	1m
		action	コンポストに入れる
		name	コンポストに入れる
		info	古くなった食品をコンポストに入れ，堆肥を作ります
		ngmsg	堆肥作りに失敗しました
			use		1	わかめ
			get		10	堆肥	30%	上質の堆肥ができました

@@ITEM
	no		25
	type	海産物
	code	umi-kama
	name	かまぼこ
	info	ピンクのかまぼこです
	scale	本
	price	300
	limit	1500/10
	plus	4h
	pop	90m
	point	30%
	@@USE
		time	1m
		action	コンポストに入れる
		name	コンポストに入れる
		info	古くなった食品をコンポストに入れ，堆肥を作ります
		ngmsg	堆肥作りに失敗しました
			use		1	かまぼこ
			get		10	堆肥	30%	上質の堆肥ができました

@@ITEM
	no		26
	type	海産物
	code	umi-maruten
	name	丸天
	info	厚みのある丸天です
	scale	枚
	price	500
	limit	1000/10
	plus	6h
	pop	150m
	point	50%
	@@USE
		time	1m
		action	コンポストに入れる
		name	コンポストに入れる
		info	古くなった食品をコンポストに入れ，堆肥を作ります
		ngmsg	堆肥作りに失敗しました
			use		1	丸天
			get		10	堆肥	35%	上質の堆肥ができました

@@ITEM
	no		27
	type	海産物
	code	umi-ebiten
	name	えび天
	info	カラッと揚がったえびの天ぷらです
	scale	匹
	price	600
	limit	1000
	plus	-1h
	pop	180m
	point	50%
	@@USE
		time	1m
		action	コンポストに入れる
		name	コンポストに入れる
		info	古くなった食品をコンポストに入れ，堆肥を作ります
		ngmsg	堆肥作りに失敗しました
			use		1	えび天
			get		10	堆肥	35%	上質の堆肥ができました

@@ITEM
	no		28
	type	海産物
	code	umi-suke
	name	すけとうだら
	info	かまぼこの原料になる魚で，卵は加工できます
	scale	匹
	price	1000
	limit	1000/10
	base	500/5000
	plus	5h
	pop	9h
	@@USE
		time	1m
		action	コンポストに入れる
		name	コンポストに入れる
		info	古くなった食品をコンポストに入れ，堆肥を作ります
		ngmsg	堆肥作りに失敗しました
			use		1	すけとうだら
			get		10	堆肥	50%	上質の堆肥ができました

@@ITEM
	no		29
	type	海産物
	code	umi-eso
	name	えそ
	info	丸天の原料になる魚です
	scale	匹
	price	2000
	limit	500/5
	base	250/5000
	plus	7h
	pop	18h
	@@USE
		time	1m
		action	コンポストに入れる
		name	コンポストに入れる
		info	古くなった食品をコンポストに入れ，堆肥を作ります
		ngmsg	堆肥作りに失敗しました
			use		1	えそ
			get		10	堆肥	50%	上質の堆肥ができました

@@ITEM
	no		32
	type	海産物
	code	umi-katuo
	name	かつお
	info	高級うどん（そば）のだし作りに欠かせません
	scale	匹
	price	2000
	limit	500
	base	250/5000
	plus	-1m
	pop	18h
	point	200%
	@@USE
		time	1m
		action	コンポストに入れる
		name	コンポストに入れる
		info	古くなった食品をコンポストに入れ，堆肥を作ります
		ngmsg	堆肥作りに失敗しました
			use		1	かつお
			get		10	堆肥	50%	上質の堆肥ができました

@@ITEM
	no		33
	type	海産物
	code	umi-tyouzame
	name	ちょうざめ
	info	海の宝と呼ばれる魚です
	scale	匹
	price	8000
	limit	100
	base	250/5000
	plus	-1m
	pop	4d
	point	200%
	@@USE
		time	1m
		action	コンポストに入れる
		name	コンポストに入れる
		info	古くなった食品をコンポストに入れ，堆肥を作ります
		ngmsg	堆肥作りに失敗しました
			use		1	ちょうざめ
			get		10	堆肥	80%	上質の堆肥ができました

@@ITEM
	no		30
	type	海産物
	code	umi-mentai
	name	辛子めんたい
	info	すけとうだらの卵をとうがらし汁に漬けこんだ，博多名物のひとつです
	scale	kg
	price	3000
	limit	300
	base	50/200
	plus	-1d
	pop	12h
	@@USE
		time	1m
		action	コンポストに入れる
		name	コンポストに入れる
		info	古くなった食品をコンポストに入れ，堆肥を作ります
		ngmsg	堆肥作りに失敗しました
			use		1	辛子めんたい
			get		10	堆肥	35%	上質の堆肥ができました

@@ITEM
	no		31
	type	海産物
	code	umi-kyabia
	name	キャビア
	info	黒いダイヤと呼ばれて珍重される，ちょうざめの卵です
	scale	kg
	price	2000
	limit	500
	base	50/200
	plus	-1d
	pop	8h
	@@USE
		time	1m
		action	コンポストに入れる
		name	コンポストに入れる
		info	古くなった食品をコンポストに入れ，堆肥を作ります
		ngmsg	堆肥作りに失敗しました
			use		1	キャビア
			get		10	堆肥	35%	上質の堆肥ができました

@@ITEM
	no		34
	type	うどん
	code	udon-su
	name	すうどん
	info	通好みのシンプルうどん
	price	500
	limit	1000/0
	pop	75m
	point	40%
	@@USE
		time	5m
		action	食べる
		name	食べる
		info	熱々のうどんを食べます
		okmsg	とても美味しかったです
			use		1	すうどん
			get		1	汚れた丼
			get		10	店力	20%

@@ITEM
	no		35
	type	うどん
	code	udon-wakame
	name	わかめうどん
	info	髪の毛つやつやヘルシーうどん
	price	600
	limit	1000/0
	pop	90m
	point	50%
	@@USE
		time	5m
		action	食べる
		name	食べる
		info	熱々のうどんを食べます
		okmsg	とても美味しかったです
			use		1	わかめうどん
			get		1	汚れた丼
			get		10	店力	20%

@@ITEM
	no		36
	type	うどん
	code	udon-kitune
	name	きつねうどん
	info	味のしみこんだ油揚げが絶品のうどん
	price	800
	limit	1000/0
	pop	120m
	point	60%
	@@USE
		time	5m
		action	食べる
		name	食べる
		info	熱々のうどんを食べます
		okmsg	とても美味しかったです
			use		1	きつねうどん
			get		1	汚れた丼
			get		10	店力	20%

@@ITEM
	no		37
	type	うどん
	code	udon-maruten
	name	丸天うどん
	info	食べ応えのある丸天がのったうどん
	price	1000
	limit	1000/0
	pop	120m
	point	75%
	@@USE
		time	5m
		action	食べる
		name	食べる
		info	熱々のうどんを食べます
		okmsg	とても美味しかったです
			use		1	丸天うどん
			get		1	汚れた丼
			get		10	店力	20%

@@ITEM
	no		38
	type	うどん
	code	udon-ebiten
	name	えび天うどん
	info	からっと揚がったえびが二匹のったうどん
	price	2000
	limit	500/0
	pop	240m
	@@USE
		time	5m
		action	食べる
		name	食べる
		info	熱々のうどんを食べます
		okmsg	とても美味しかったです
			use		1	えび天うどん
			get		1	汚れた丼
			get		10	店力	20%

@@ITEM
	no		39
	type	うどん
	code	udon-zanmai
	name	うどん三昧
	info	おすすめうどん三種セット
	scale	セット
	price	5000
	limit	200
	pop	8h
	point	500%
	@@USE
		time	5m
		action	食べる
		name	食べる
		info	熱々のうどんを食べます
		okmsg	とても美味しかったです
			use		1	うどん三昧
			get		3	汚れた丼
			get		10	店力	30%

@@ITEM
	no		40
	type	うどん
	code	udon-kyabia
	name	キャビアうどん
	info	世界三大珍味うどんのひとつ
	price	7500
	limit	120/0
	pop	12h
	@@USE
		time	5m
		action	食べる
		name	食べる
		info	熱々のうどんを食べます
		okmsg	びっくりするほど美味しかったです
			use		1	キャビアうどん
			get		1	汚れた丼
			get		10	店力	50%

@@ITEM
	no		41
	type	うどん
	code	udon-toryuhu
	name	トリュフうどん
	info	世界三大珍味うどんのひとつ
	price	8000
	limit	120/0
	pop	13h
	@@USE
		time	5m
		action	食べる
		name	食べる
		info	熱々のうどんを食べます
		okmsg	びっくりするほど美味しかったです
			use		1	トリュフうどん
			get		1	汚れた丼
			get		10	店力	50%

@@ITEM
	no		42
	type	うどん
	code	udon-foagura
	name	フォアグラうどん
	info	世界三大珍味うどんのひとつ
	price	10000
	limit	100/0
	pop	15h
	@@USE
		time	5m
		action	食べる
		name	食べる
		info	熱々のうどんを食べます
		okmsg	びっくりするほど美味しかったです
			use		1	フォアグラうどん
			get		1	汚れた丼
			get		10	店力	50%

@@ITEM
	no		43
	type	うどん
	code	udon-hakata
	name	博多うどん
	info	博多の味の特製うどん
	price	20000
	limit	50
	pop	25h
	point	200%
	@@USE
		time	5m
		action	食べる
		name	食べる
		info	熱々のうどんを食べます
		okmsg	びっくりするほど美味しかったです
			use		1	博多うどん
			get		1	汚れた丼
			get		10	店力	70%

@@ITEM
	no		44
	type	うどん
	code	udon-origi
	name	オリジナルうどん
	info	精魂込めて作ったオリジナルうどん
	price	50000
	limit	20/0
	pop	60h
	point	200%
	@@USE
		time	5m
		action	食べる
		name	食べる
		info	熱々のうどんを食べます
		okmsg	夢のように美味しかったです
			use		1	オリジナルうどん
			get		1	汚れた丼
			get		20	店力	50%

@@ITEM
	no		45
	type	うどん
	code	udon-yami
	name	闇うどん
	info	ブラック工作員が作ったまずいうどん
	price	100
	limit	5000/0
	pop	1h
	point	-10%
	@@USE
		time	5m
		action	食べる
		name	食べる
		info	熱々のうどんを食べます
		okmsg	お世辞にも美味しいとはいえませんでした
			use		1	闇うどん
			get		1	汚れた丼

@@ITEM
	no		46
	type	そば
	code	soba-kake
	name	かけそば
	info	通好みのシンプルそば
	price	500
	limit	1000/0
	pop	75m
	point	40%
	@@USE
		time	5m
		action	食べる
		name	食べる
		info	熱々のそばを食べます
		okmsg	とても美味しかったです
			use		1	かけそば
			get		1	汚れた丼
			get		10	店力	20%

@@ITEM
	no		47
	type	そば
	code	soba-wakame
	name	わかめそば
	info	髪の毛つやつやヘルシーそば
	price	600
	limit	1000/0
	pop	90m
	point	50%
	@@USE
		time	5m
		action	食べる
		name	食べる
		info	熱々のそばを食べます
		okmsg	とても美味しかったです
			use		1	わかめそば
			get		1	汚れた丼
			get		10	店力	20%

@@ITEM
	no		48
	type	そば
	code	soba-kitune
	name	きつねそば
	info	味のしみこんだ油揚げが絶品のそば
	price	800
	limit	1000/0
	pop	120m
	point	60%
	@@USE
		time	5m
		action	食べる
		name	食べる
		info	熱々のそばを食べます
		okmsg	とても美味しかったです
			use		1	きつねそば
			get		1	汚れた丼
			get		10	店力	20%

@@ITEM
	no		49
	type	そば
	code	soba-maruten
	name	丸天そば
	info	食べ応えのある丸天がのったそば
	price	1000
	limit	1000/0
	pop	120m
	point	75%
	@@USE
		time	5m
		action	食べる
		name	食べる
		info	熱々のそばを食べます
		okmsg	とても美味しかったです
			use		1	丸天そば
			get		1	汚れた丼
			get		10	店力	20%

@@ITEM
	no		50
	type	そば
	code	soba-ebiten
	name	えび天そば
	info	からっと揚がったえびが二匹のったそば
	price	2000
	limit	500/0
	pop	240m
	@@USE
		time	5m
		action	食べる
		name	食べる
		info	熱々のそばを食べます
		okmsg	とても美味しかったです
			use		1	えび天そば
			get		1	汚れた丼
			get		10	店力	20%

@@ITEM
	no		51
	type	そば
	code	soba-zanmai
	name	そば三昧
	info	おすすめそば三種セット
	scale	セット
	price	5000
	limit	200
	pop	8h
	point	500%
	@@USE
		time	5m
		action	食べる
		name	食べる
		info	熱々のそばを食べます
		okmsg	とても美味しかったです
			use		1	そば三昧
			get		3	汚れた丼
			get		10	店力	30%

@@ITEM
	no		52
	type	そば
	code	soba-kyabia
	name	キャビアそば
	info	世界三大珍味そばのひとつ
	price	7500
	limit	120/0
	pop	12h
	@@USE
		time	5m
		action	食べる
		name	食べる
		info	熱々のそばを食べます
		okmsg	びっくりするほど美味しかったです
			use		1	キャビアそば
			get		1	汚れた丼
			get		10	店力	50%

@@ITEM
	no		53
	type	そば
	code	soba-toryuhu
	name	トリュフそば
	info	世界三大珍味そばのひとつ
	price	8000
	limit	120/0
	pop	13h
	@@USE
		time	5m
		action	食べる
		name	食べる
		info	熱々のそばを食べます
		okmsg	びっくりするほど美味しかったです
			use		1	トリュフそば
			get		1	汚れた丼
			get		10	店力	50%

@@ITEM
	no		54
	type	そば
	code	soba-foagura
	name	フォアグラそば
	info	世界三大珍味そばのひとつ
	price	10000
	limit	100/0
	pop	15h
	@@USE
		time	5m
		action	食べる
		name	食べる
		info	熱々のそばを食べます
		okmsg	びっくりするほど美味しかったです
			use		1	フォアグラそば
			get		1	汚れた丼
			get		10	店力	50%

@@ITEM
	no		55
	type	そば
	code	soba-hakata
	name	博多そば
	info	博多の味の特製そば
	price	20000
	limit	50
	pop	25h
	point	200%
	@@USE
		time	5m
		action	食べる
		name	食べる
		info	熱々のそばを食べます
		okmsg	びっくりするほど美味しかったです
			use		1	博多そば
			get		1	汚れた丼
			get		10	店力	70%

@@ITEM
	no		56
	type	そば
	code	soba-origi
	name	オリジナルそば
	info	精魂込めて作ったオリジナルそば
	price	50000
	limit	20/0
	pop	60h
	point	200%
	@@USE
		time	5m
		action	食べる
		name	食べる
		info	熱々のそばを食べます
		okmsg	夢のように美味しかったです
			use		1	オリジナルそば
			get		1	汚れた丼
			get		20	店力	50%

@@ITEM
	no		57
	type	そば
	code	soba-yami
	name	闇そば
	info	ブラック工作員が作ったまずいそば
	price	100
	limit	5000/0
	pop	1h
	point	-10%
	@@USE
		time	5m
		action	食べる
		name	食べる
		info	熱々のそばを食べます
		okmsg	お世辞にも美味しいとはいえませんでした
			use		1	闇そば

@@ITEM
	no		58
	type	ツール
	code	tool-tikara
	name	店力
	info	いざというときに真価を発揮するかもしれない[みせぢから]
	scale	力
	price	0
	limit	1000/0
	pop		0
	flag	noshowcase|norequest|notrash
	@@use
		time	10m
		scale	回
		action	浴びる
		name	浴びる
		info	祈りを込めて店力を頭から浴びてみます
		arg		nocount
			use		500	店力
		func	_local_
			my $ret='祈りが通じて店力が不思議な力を発揮したようです';

			if ((rand(1000)<20) && !$DT->{item}[@@ITEMNO"オリジナルうどんレシピ"-1])
			{
				AddItem(@@ITEMNO"オリジナルうどんレシピ",1,"突風で飛んできた紙切れをよく見ると，なんと！どこかの店の「オリジナルうどんレシピ」でした");
				WriteLog(0,$DT->{id},'オリジナルうどんレシピを手に入れました');
			}
			elsif((rand(1000)<20) && !$DT->{item}[@@ITEMNO"オリジナルそばレシピ"-1])
			{
				AddItem(@@ITEMNO"オリジナルそばレシピ",1,"突風で飛んできた紙切れをよく見ると，なんと！どこかの店の「オリジナルそばレシピ」でした");
				WriteLog(0,$DT->{id},'オリジナルそばレシピを手に入れました');
			}
			elsif ((rand(1000)<100) && ($DT->{item}[@@ITEMNO"豚"-1]<=10))
			{
				AddItem(@@ITEMNO"豚",10,"野生の豚集団が店に飛び込んできました");
				WriteLog(0,$DT->{id},'豚を手に入れました');
			}
			elsif ((rand(1000)<100) && ($DT->{item}[@@ITEMNO"がちょう"-1]<=10))
			{
				AddItem(@@ITEMNO"がちょう",10,"野生のがちょう集団が店に飛び込んできました");
				WriteLog(0,$DT->{id},'がちょうを手に入れました');
			}
			elsif ((rand(1000)<100) && ($DT->{item}[@@ITEMNO"とうがらし"-1]<=500))
			{
				AddItem(@@ITEMNO"とうがらし",500,"遠い親戚からとうがらしの小包が送ってきました");
				WriteLog(0,$DT->{id},'とうがらしを手に入れました');
			}
			elsif((rand(1000)<100) && $DT->{item}[@@ITEMNO"にわとり"-1] && ($DT->{item}[@@ITEMNO"卵"-1]<=2700))
			{
				AddItem(@@ITEMNO"卵",$DT->{item}[@@ITEMNO"にわとり"-1]*10,"飼っているにわとりが一斉に卵を10個ずつ産みました");
				WriteLog(0,$DT->{id},'卵を手に入れました');
			}
			elsif((rand(1000)<100) && $DT->{item}[@@ITEMNO"豚"-1] && ($DT->{item}[@@ITEMNO"トリュフ"-1]<=50))
			{
				AddItem(@@ITEMNO"トリュフ",$DT->{item}[@@ITEMNO"豚"-1]*5,"飼っている豚が皆，トリュフを5個ずつくわえてきました");
				WriteLog(0,$DT->{id},'トリュフを手に入れました');
			}
			elsif ((rand(1000)<100) && ($DT->{item}[@@ITEMNO"ブラック工作員"-1]<2))
			{
				AddItem(@@ITEMNO"ブラック工作員",1,"ブラック工作員がこっそり店に入ってきて，雇ってほしいと言いました");
				WriteLog(0,$DT->{id},'ブラック工作員を手に入れました');
			}
			elsif((rand(1000)<20) && $DT->{user}->{udon} && ($DT->{user}->{udon}ne'トンヌラうどん') && ($DT->{user}->{udon}ne'ハイパーグレートＵＤＯＮ'))
			{
				if (rand(1000)<500)
				{
					$ret.='<br>突然ひらめいて，開発したオリジナルうどんの名前を「トンヌラうどん」に変えました<br>';
					$DT->{user}->{udon}='トンヌラうどん';
				}
				else
				{
					$ret.='<br>突然ひらめいて，開発したオリジナルうどんの名前を「ハイパーグレートＵＤＯＮ」に変えました<br>';
					$DT->{user}->{udon}='ハイパーグレートＵＤＯＮ';
				}
				WriteLog(0,$DT->{id},'オリジナルうどんの名前を変更しました');
				WriteLog(3,0,$DT->{shopname}.'の店主が店力を浴びてひらめき，オリジナルうどんの名前を変更したようです');
			}
			elsif((rand(1000)<20) && $DT->{user}->{soba} && ($DT->{user}->{soba}ne'愛の貧乏脱出そば') && ($DT->{user}->{soba}ne'ぬらりひょんソバ'))
			{
				if (rand(1000)<500)
				{
					$ret.='<br>突然ひらめいて，開発したオリジナルそばの名前を「愛の貧乏脱出そば」に変えました<br>';
					$DT->{user}->{soba}='愛の貧乏脱出そば';
				}
				else
				{
					$ret.='<br>突然ひらめいて，開発したオリジナルそばの名前を「ぬらりひょんソバ」に変えました<br>';
					$DT->{user}->{soba}='ぬらりひょんソバ';
				}
				WriteLog(0,$DT->{id},'オリジナルそばの名前を変更しました');
				WriteLog(3,0,$DT->{shopname}.'の店主が店力を浴びてひらめき，オリジナルそばの名前を変更したようです');
			}
			else
			{
				$ret.='<br>店力によって時のエネルギーが増幅され，活動できる時間が増えました';
				my $cnt=int(rand(6))+5;
				$DT->{time}-=3600*($cnt);
				$ret.='（＋'.($cnt).'時間）<br>';
				WriteLog(0,$DT->{id},'店力を頭から浴びた結果，持ち時間が増えました');
			}
			return $ret;
		_local_

@@ITEM
	no		59
	type	ツール
	code	tool-huku
	name	福引き補助券
	info	5枚で1回抽選ができます
	scale	枚
	price	0
	limit	1000/0
	pop		0
	@@USE
		time	5m
		action	福引きをする
		name	福引きをする
		info	集めた福引き補助券で福引きをします
		scale	回
			use		5	福引き補助券
		func	_local_
			# ★福引き
			my $ret;
			my $hit1=0; #手に入る特等景品の個数
			my $hit2=0; #手に入る1等景品の個数
			my $hit3=0; #手に入る2等景品の個数
			my $hit4=0; #手に入る3等景品の個数
			my $hit5=0; #手に入る4等景品の個数
			my $hit6=0; #手に入る5等景品の個数
			my $hit7=0; #手に入る残念賞の個数

			foreach(1..$count)
			{
				if(rand(1000)<1)
				{
					$hit1+=1;
				}
				elsif(rand(1000)<3)
				{
					$hit2+=1;
				}
				elsif(rand(1000)<10)
				{
					$hit3+=1;
				}
				elsif(rand(1000)<50)
				{
					$hit4+=1;
				}
				elsif(rand(1000)<100)
				{
					$hit5+=1;
				}
				elsif(rand(1000)<200)
				{
					$hit6+=1;
				}
			}
			$hit7=$count-($hit1+$hit2+$hit3+$hit4+$hit5+$hit6);
			AddItem(83,$hit1,'なんと！特等の金の招き猫が'.$hit1.'回当たりました') if ($hit1>=1);
			AddItem(82,$hit2,'なんと！1等の自動車が'.$hit2.'回当たりました') if ($hit2>=1);
			AddItem(80,$hit3,'2等の食器洗い機が'.$hit3.'回当たりました') if ($hit3>=1);
			AddItem(79,$hit4,'3等の自転車が'.$hit4.'回当たりました') if ($hit4>=1);
			AddItem(67,$hit5,'4等のヒントブックが'.$hit5.'回当たりました') if ($hit5>=1);
			AddItem(66,$hit6,'5等の商品券が'.$hit6.'回当たりました') if ($hit6>=1);
			AddItem(64,$hit7,'残念賞のきれいな丼が'.$hit7.'回分です') if ($hit7>=1);
			$ret='福引きははずれました';
			$ret='福引きで景品を当てました' if ($hit7<$count);
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_

@@ITEM
	no		60
	type	ツール
	code	tool-udon
	name	オリジナルうどんレシピ
	info	オリジナルうどんの作り方が書いてあります
	scale	枚
	price	0
	limit	1/0
	pop		0
	@@USE
		time	1m
		action	見る
		name	レシピを見る
		info	オリジナルうどんの材料と作り方を忘れたときのために
		scale	回
		arg		nocount
		ngmsg	【オリジナルうどんの作り方】<br>材料<br>・小麦粉<br>・かつお<br>・がちょう<br>・とうがらし<br>・きれいな丼<br><br>作り方<br><b>　　秘密</b>
	@@USE
		time	4h
		job		うどん屋	times/job_udon_time_rate
		action	という名前に変える
		name	オリジナルうどんの名前を変える
		info	オリジナルうどんの名前を変更します
		arg		nocount|message30
		func	_local_
			# オリジナルうどんの名前を変える
			main::OutError('まずオリジナルうどんを開発してください') if !$DT->{user}->{udon};
			main::OutError('名前をつけてください') if !$USE->{arg}->{message};
			my $ret;
			$ret='オリジナルうどんの名前を【'.$USE->{arg}->{message}.'】に変更しました';	
			WriteLog(3,0,$DT->{shopname}."がオリジナルうどんの名前を変えたようです");
			WriteLog(0,$DT->{id},$ret);
			$DT->{user}->{udon}=$USE->{arg}->{message};
			return $ret;
		_local_

@@ITEM
	no		61
	type	ツール
	code	tool-soba
	name	オリジナルそばレシピ
	info	オリジナルそばの作り方が書いてあります
	scale	枚
	price	0
	limit	1/0
	pop		0
	@@USE
		time	1m
		action	見る
		name	レシピを見る
		info	オリジナルそばの材料と作り方を忘れたときのために
		scale	回
		arg		nocount
		ngmsg	【オリジナルそばの作り方】<br>材料<br>・そば粉<br>・かつお<br>・ちょうざめ<br>・たまご<br>・きれいな丼<br><br>作り方<br><b>　　秘密</b>
	@@USE
		time	4h
		job		そば屋	times/job_soba_time_rate
		action	という名前に変える
		name	オリジナルそばの名前を変える
		info	オリジナルそばの名前を変更します
		arg		nocount|message30
		func	_local_
			main::OutError('まずオリジナルそばを開発してください') if !$DT->{user}->{soba};
			main::OutError('名前をつけてください') if !$USE->{arg}->{message};
			my $ret;
			$ret='オリジナルそばの名前を【'.$USE->{arg}->{message}.'】に変更しました';	
			WriteLog(3,0,$DT->{shopname}."がオリジナルそばの名前を変えたようです");
			WriteLog(0,$DT->{id},$ret);
			$DT->{user}->{soba}=$USE->{arg}->{message};
			return $ret;
		_local_

@@ITEM
	no		62
	type	ツール
	code	tool-taihi
	name	堆肥
	info	畑の肥料です
	scale	kg
	price	5
	cost	0
	limit	5000/1000
	base	100/20000
	plus	20m
	pop		20m
	point	10%

@@ITEM
	no		63
	type	ツール
	code	tool-yogore
	name	汚れた丼
	info	使った後の丼です
	scale	個
	price	10
	cost	0
	limit	10000/0
	pop		0

@@ITEM
	no		64
	type	ツール
	code	tool-kirei
	name	きれいな丼
	info	きれいに洗った丼です
	scale	個
	price	50
	cost	10
	limit	3000/2000
	base	10000/100000
	plus	1h
	pop	10d

@@ITEM
	no		65
	type	ツール
	code	tool-takara
	name	宝くじ
	info	一攫千金を夢見て‥
	scale	枚
	price	1000
	cost	10
	limit	100/20
	plus	3h
	pop		2h
	flag	noshowcase|norequest

@@ITEM
	no		66
	type	ツール
	code	tool-syou
	name	商品券
	info	希望の商品と交換できます
	scale	枚
	price	5000
	cost	10
	limit	500/0
	pop		0
	@@USE
		time	10m
		action	交換する
		scale	回
		name	堆肥と交換する
		info	商品券を希望の商品と交換します
		okmsg	堆肥を手に入れました
			use		1	商品券
			get		250	堆肥
	@@USE
		time	10m
		action	交換する
		scale	回
		name	きれいな丼と交換する
		info	商品券を希望の商品と交換します
		okmsg	きれいな丼を手に入れました
			use		1	商品券
			get		100	きれいな丼
	@@USE
		time	10m
		action	交換する
		scale	回
		name	ヒントブックと交換する
		info	商品券を希望の商品と交換します
		okmsg	ヒントブックを手に入れました
			use		2	商品券
			get		1	ヒントブック
	@@USE
		time	10m
		action	交換する
		scale	回
		name	警報機と交換する
		info	商品券を希望の商品と交換します
		okmsg	警報機を手に入れました
			use		40	商品券
			get		1	警報機
	@@USE
		time	10m
		action	交換する
		scale	回
		name	自動車と交換する
		info	商品券を希望の商品と交換します
		okmsg	自動車を手に入れました
			use		100	商品券
			get		1	自動車
	@@USE
		time	10m
		action	交換する
		scale	回
		name	金の招き猫と交換する
		info	商品券を希望の商品と交換します
		okmsg	金の招き猫を手に入れました
			use		200	商品券
			get		1	金の招き猫
	@@use
		time	10m
		scale	枚
		action	換金する
		name	換金する
		info	商品券を金券ショップに引き取ってもらいます
		param	500,2500
			use		1	商品券
		func	_local_
			my $ret;
			if (rand(1000)<300)
			{
				$DT->{money}+=$USE->{param1}*$count;
				$ret='金券ショップのおやじに買いたたかれたようです<br>';
				$ret.=GetMoneyString($USE->{param1}*$count).'で引き取ってもらいました';
			}
			else
			{
			$DT->{money}+=$USE->{param2}*$count;
			$ret=GetMoneyString($USE->{param2}*$count).'で引き取ってもらいました';
			}
			WriteLog(0,$DT->{id},"商品券を換金しました");
			return $ret;
		_local_

@@ITEM
	no		67
	type	ツール
	code	tool-hint
	name	ヒントブック
	info	<b>注意！★印のヒントを読むとヒントブックが消滅します</b>
	scale	冊
	price	10000
	cost	10
	limit	5/0
	pop		0
	flag	noshowcase|norequest
	@@USE
		time	1m
		action	ヒントを読む
		name	初めての方へ
		info	まず何をしたらよいのかわからない場合のヒントです
		arg		nocount
		ngmsg	（「図書館」を見てから）<br><br>農夫か漁師を1人，市場か相場から購入してみましょう。<br>（どちらもない場合は，フリーターを買って農夫か漁師にしてください）<br>漁師の場合はすぐに釣りが始められます。<br>農夫は畑を手に入れると，収穫をすることができるようになります。<br>収穫した畑は「耕す前の畑」に戻り，1反につき堆肥100kgで<br>「よく耕した畑」にすることができ，さらにある程度の時間経過によって<br>順次「収穫を待つ畑」に変化します。
	@@USE
		time	10m
		action	ヒントを読む
		name	★フリーターの秘密
		info	人材派遣業を極めてみたい方へ
		arg		nocount
		ngmsg	・うどん職人の修行をするには，フリーターと小麦粉が必要です。<br>・そば職人の修行をするには，フリーターとそば粉が必要です。
			use		1	ヒントブック
	@@USE
		time	10m
		action	ヒントを読む
		name	★農夫の秘密
		info	農業を極めてみたい方へ
		arg		nocount
		ngmsg	・エサで動物を育てましょう。にわとりとがちょうのエサはとうもろこし，豚のエサは大豆です。<br>・卵がいくつかあるときは，にわとりの親鳥に卵を抱かせ，孵化させることができます。<br>（孵化を待つ卵は，時間が経過すると順次親鳥になります）<br>・にわとりを使用すると，がちょうや豚と取りかえることができます。
			use		1	ヒントブック
	@@USE
		time	10m
		action	ヒントを読む
		name	★漁師の秘密
		info	漁業を極めてみたい方へ
		arg		nocount
		ngmsg	・えびをたくさん用意すると，漁に出られるようになります。<br>・すけとうだらと，とうがらしを準備すれば，辛子めんたいが作れます。
			use		1	ヒントブック
	@@USE
		time	10m
		action	ヒントを読む
		name	★天ぷら職人の秘密
		info	天ぷら屋を極めてみたい方へ
		arg		nocount
		ngmsg	・大豆から油揚げを作ることができます。<br>・すけとうだらからかまぼこが作れます。<br>・えそから丸天が作れます。<br>・えびと小麦粉，卵を用意すれば，えび天を作ることができます。
			use		1	ヒントブック
	@@USE
		time	10m
		action	ヒントを読む
		name	★うどん職人の秘密
		info	うどん屋を極めてみたい方へ
		arg		nocount
		ngmsg	・作ることのできるうどんは，標準価格の安い順に「すうどん」「わかめうどん」「きつねうどん」<br>「丸天うどん」「えび天うどん」「うどん三昧」「キャビアうどん」「トリュフうどん」「フォアグラうどん」<br>「博多うどん」「オリジナルうどん」の11種類です。<br>・すうどんの材料は，小麦粉とねぎ，かまぼこときれいな丼です（うどん作りの基本）。<br>・うどん三昧は特定のうどん3種類を，セットにすることによって作ります。<br>・高級なうどんにはかつおが必要なものが多いです。<br>・博多うどんは豚骨味で，ある博多名物の海産物加工品がのっています。
			use		1	ヒントブック
	@@USE
		time	10m
		action	ヒントを読む
		name	★そば職人の秘密
		info	そば屋を極めてみたい方へ
		arg		nocount
		ngmsg	・作ることのできるそばは，標準価格の安い順に「かけそば」「わかめそば」「きつねそば」<br>「丸天そば」「えび天そば」「そば三昧」「キャビアそば」「トリュフそば」「フォアグラそば」<br>「博多そば」「オリジナルそば」の11種類です。<br>・かけそばの材料は，そば粉とねぎ，かまぼこときれいな丼です（そば作りの基本）。<br>・そば三昧は特定のそば3種類を，セットにすることによって作ります。<br>・高級なそばにはかつおが必要なものが多いです。<br>・博多そばは豚骨味で，ある博多名物の海産物加工品がのっています。
			use		1	ヒントブック
	@@USE
		time	10m
		action	ヒントを読む
		name	★便利屋の秘密
		info	人材派遣業を極めてみたい方へ
		arg		nocount
		ngmsg	・フリーターが人材派遣の専門家になることによって，便利屋の各種作業時間も短くなります。<br>・食器洗い機を手に入れると，短い時間でたくさんの汚れた丼が洗えるようになります。<br>・専門職の看板を下ろすと，商店会から慰労金が支給されます。
			use		1	ヒントブック
	@@USE
		time	10m
		action	ヒントを読む
		name	★ブラック工作員の秘密
		info	裏家業を極めてみたい方へ
		arg		nocount
		ngmsg	・汚れた丼がある程度あると，闇うどんと闇そばを作ることができます。<br>・闇うどんと闇そばがたくさん揃っているときに，店力が少しあれば，すり替え作戦を実行できます。<br>・悪い噂を流すためには，店力が100必要です。<br>・ブラック工作員が2人いて，さらに店力が100あると時間操作を行うことができます。<br>（時間操作によって，持ち時間がランダムに増加します）
			use		1	ヒントブック
	@@USE
		time	1m
		action	ヒントを読む
		name	陳列棚について
		info	陳列棚の増改築と維持費についての説明です
		arg		nocount
		ngmsg	陳列棚の数を変えるには，便利屋を使います。<br>ただし，便利屋1人では陳列棚を２つまでしか増やすことができず，<br>それ以上増やしたいときには，便利屋の数がもっと必要です。<br>陳列棚の維持費は，棚が増えると次第にかかるようになってきます。
	@@USE
		time	1m
		action	ヒントを読む
		name	店力について
		info	店力に関する説明です
		arg		nocount
		ngmsg	店力（みせぢから）とは，生産的な行動をとったり<br>うどんやそばを食べることによって手にはいるもので<br>ブラック工作員や金の招き猫によって，その力を使用することができます。
	@@USE
		time	1m
		action	ヒントを読む
		name	オリジナルうどん（そば）について
		info	オリジナルうどん（そば）の作り方の説明です
		arg		nocount
		ngmsg	うどん（そば）三昧とオリジナルうどん（そば）を除く全種類のうどん（そば）を1杯ずつ用意すると，<br>うどん（そば）職人はオリジナルうどん（そば）を開発することができるようになります。<br>オリジナルうどん（そば）には，好きな名前を付けられます。<br>この名前はショウウインドウ（陳列棚1）で販売したときに，ランキング中に表示されます。
	@@USE
		time	1m
		action	ヒントを読む
		name	汚れた丼について
		info	汚れた丼についての説明です
		arg		nocount
		ngmsg	うどんやそばが売れると，汚れた丼が倉庫にたまってきます。<br>（他店舗から買われたときには，丼は戻ってきません）<br>ただし，闇うどんと闇そばは例外で<br>一般市民も「ま，まずい！」と怒ったうえ，丼を叩き割ってしまうのです。
	@@USE
		time	1m
		action	ヒントを読む
		name	ヒントブックについて
		info	ヒントブックの手に入れ方に関する説明です
		arg		nocount
		ngmsg	ヒントブックは，商品券と交換できます。<br>商品券は決算時の賞品としてもらえることがあります。<br>また，ヒントブックは福引きの景品で当たることもあります。<br>福引き補助券は，市場で買い物をするともらえることがあります。
	@@use
		time	10m
		scale	冊
		action	換金する
		name	換金する
		info	ヒントブックを金券ショップに引き取ってもらいます
		param	1000,5000
			use		1	ヒントブック
		func	_local_
			my $ret;
			if (rand(1000)<300)
			{
				$DT->{money}+=$USE->{param1}*$count;
				$ret='金券ショップのおやじに買いたたかれたようです<br>';
				$ret.=GetMoneyString($USE->{param1}*$count).'で引き取ってもらいました';
			}
			else
			{
			$DT->{money}+=$USE->{param2}*$count;
			$ret=GetMoneyString($USE->{param2}*$count).'で引き取ってもらいました';
			}
			WriteLog(0,$DT->{id},"ヒントブックを換金しました");
			return $ret;
		_local_

@@ITEM
	no		68
	type	ツール
	code	tool-paintr
	name	赤の塗料
	info	（使用できないアイテムです。破棄してください）
	scale	缶
	price	10000
	cost	100
	limit	1/0
	pop	1d

@@ITEM
	no		69
	type	ツール
	code	tool-paintb
	name	青の塗料
	info	（使用できないアイテムです。破棄してください）
	scale	缶
	price	10000
	cost	100
	limit	1/0
	pop	1d

@@ITEM
	no		70
	type	ツール
	code	tool-painto
	name	オレンジの塗料
	info	（使用できないアイテムです。破棄してください）
	scale	缶
	price	10000
	cost	100
	limit	1/0
	pop	1d

@@ITEM
	no		71
	type	ツール
	code	tool-painty
	name	黄色の塗料
	info	（使用できないアイテムです。破棄してください）
	scale	缶
	price	10000
	cost	100
	limit	1/0
	pop	1d

@@ITEM
	no		72
	type	ツール
	code	tool-paintg
	name	緑の塗料
	info	（使用できないアイテムです。破棄してください）
	scale	缶
	price	10000
	cost	100
	limit	1/0
	pop	1d

@@ITEM
	no		73
	type	ツール
	code	tool-paintp
	name	ピンクの塗料
	info	（使用できないアイテムです。破棄してください）
	scale	缶
	price	10000
	cost	100
	limit	1/0
	pop	1d

@@ITEM
	no		74
	type	ツール
	code	tool-painte
	name	紫の塗料
	info	（使用できないアイテムです。破棄してください）
	scale	缶
	price	10000
	cost	100
	limit	1/0
	pop	1d

@@ITEM
	no		75
	type	ツール
	code	tool-paintk
	name	黒の塗料
	info	（使用できないアイテムです。破棄してください）
	scale	缶
	price	10000
	cost	100
	limit	1/0
	pop	1d

@@ITEM
	no		76
	type	ツール
	code	tool-hatakea
	name	耕す前の畑
	info	肥料をたっぷり与えましょう
	scale	反
	price	5000
	limit	40/2
	plus	1d
	pop		2d
	flag	noshowcase|onlysend

@@ITEM
	no		77
	type	ツール
	code	tool-hatakeb
	name	よく耕した畑
	info	しばらくすると収穫できるようになります
	scale	反
	price	10000
	limit	20/0
	pop		1d
	flag	noshowcase|onlysend
	funct	_local_
		my($ITEM,@DT)=@_;
		my $birth_per_day=40;  # 1日に収穫を待つ畑が40になる確率の設定
		my $val          =1;  # 一度に収穫を待つ畑になる基本数
		
		my $birth_rate=$birth_per_day && (86400/$birth_per_day); # 0で割るのを阻止
		foreach my $DT (@DT)
		{
			next if !$DT->{item}[@@ITEMNO"よく耕した畑"-1];
			if(rand($birth_rate)<$TIMESPAN) # 1店舗につき「1日に$birth_per_day回」の確率で条件が真になる(ハズ…)
			{
				UseItemSub(@@ITEMNO"よく耕した畑",$val,$DT);
				AddItemSub(@@ITEMNO"収穫を待つ畑",$val,$DT);
			}
		}
	_local_ 

@@ITEM
	no		78
	type	ツール
	code	tool-hatakec
	name	収穫を待つ畑
	info	いろいろな収穫物が期待できそうです
	scale	反
	price	20000
	limit	20/0
	pop		1d
	flag	noshowcase|onlysend

@@ITEM
	no		79
	type	ツール
	code	tool-ziten
	name	自転車
	info	買い物がちょっと楽になります
	scale	台
	price	30000
	cost	1000
	limit	1/0.5
	plus	10d
	pop		3d
	flag	noshowcase|onlysend

@@ITEM
	no		80
	type	ツール
	code	tool-syokki
	name	食器洗い機
	info	食器洗いが手早くできます
	scale	台
	price	100000
	cost	3000
	limit	1/0.8
	plus	10d
	pop		10d
	flag	noshowcase|onlysend

@@ITEM
	no		81
	type	ツール
	code	tool-keihou
	name	警報機
	info	店の安全対策に‥
	scale	台
	price	200000
	cost	5000
	limit	1/0.5
	plus	10d
	pop		20d
	flag	noshowcase|onlysend

@@ITEM
	no		82
	type	ツール
	code	tool-kuruma
	name	自動車
	info	買い物がかなり楽になります
	scale	台
	price	500000
	cost	5000
	limit	1/0.3
	plus	10d
	pop	30d
	flag	noshowcase|onlysend

@@ITEM
	no		83
	type	ツール
	code	tool-neko
	name	金の招き猫
	info	店の守り神です
	scale	体
	price	1000000
	cost	1000
	limit	1/0.2
	plus	10d
	pop		50d
	flag	noshowcase|onlysend
	@@use
		time	3m
		scale	回
		action	拝む
		name	拝む
		info	商売繁盛を願って，金の招き猫を拝みます
			use		1	店力
		func	_local_
			my $val=$count;
			my $ret="";
			
			if($count>=50)
			{
				$DT->{rank}-=$count*2;
				$DT->{rank}=0 if $DT->{rank}<0;
				WriteLog(2,0,$DT->{shopname}.'の店主が気を失って，救急車で運ばれました。');
				WriteLog(2,0,'一度に'.$count.'回も金の招き猫を拝むなんて，正気の沙汰ではありません。');
				$ret="‥気が付いたら病院のベッドの上でした";
			}
			elsif($count>=20)
			{
				$ret='貧血を起こしてしまいました　一度に'.$count.'回は拝み過ぎです。';
				WriteLog(0,$DT->{id},$ret);
			}
			else
			{
				$DT->{rank}+=int(rand($count+1))+$count;
				$DT->{rank}=10000 if $DT->{rank}>10000;
				$ret='金の招き猫を拝んで，今日も商売が順調にいく気がしました。';
				WriteLog(0,$DT->{id},$ret);
			}
			return $ret;
		_local_

@@EVENT
	start		50%
	basetime	0h
	plustime	0h
	code		loto
	startfunc	loto
	info		宝くじ抽選

@@EVENT
	start		30%
	basetime	0h
	plustime	0h
	code		luckyneko
	info		金の招き猫の招運
	startfunc	_local_(200)
		my($hitproba)=@_;
		
		foreach my $DT (@main'DT)
		{
			next if rand(1000)>$hitproba;
			{
			foreach my $itemno (@@ITEMNO"金の招き猫")
			{			
			if ($DT->{item}[@@ITEMNO"金の招き猫"-1])
			{
				$DT->{item}[@@ITEMNO"金の招き猫"-1]=0;
				my $up=int(1000*(2-$DT->{rank}/5000));
				$DT->{rank}+=$up;
				$DT->{rank}=10000 if $DT->{rank}>10000;
				WriteLog(2,0,$DT->{shopname}."の金の招き猫が，お店に幸運をもたらし天に昇っていきました。");
				WriteLog(0,$DT->{id},"金の招き猫の不思議な力で，お店の人気が".int($up/100)."%上がりました");			}
			}		
			}
		}
		return 0;
	_local_

@@EVENT
	start		100%
	basetime	0h
	plustime	0h
	code		yogoredon
	info		汚れた丼の悪臭
	startfunc	_local_(500)
		my($hitproba)=@_;
		
		foreach my $DT (@main'DT)
		{
			next if rand(1000)>$hitproba;
			{
			foreach my $itemno (@@ITEMNO"汚れた丼")
			{			
			if ($DT->{item}[@@ITEMNO"汚れた丼"-1]>=1000)
			{
				my $down=int($DT->{rank}/5);
				$DT->{rank}-=$down;
				$DT->{rank}=0 if $DT->{rank}<0;
				WriteLog(2,0,$DT->{shopname}."にたまっている汚れた丼から悪臭が発生し，店の人気が下がりました。");
				WriteLog(0,$DT->{id},"汚れた丼のせいで，お店の人気が".int($down/100)."%下がりました");			}
			}		
			}
		}
		return 0;
	_local_

# オリジナルうどんで人気アップ
@@EVENT
	start		50%
	basetime	0h
	plustime	0h
	code		udonpop
	info		オリジナルうどん人気沸騰
	startfunc	_local_
		foreach(reverse(@DT))
		{
			next if rand(1000)>200;
			if ($_->{user}->{udon}&&($_->{user}->{udon} ne 'n'))
			{
			my $up=int(300*(2-$_->{rank}/5000));
			$_->{rank}+=$up;
			$_->{rank}=10000 if $_->{rank}>10000;
			return (0,$_->{shopname}.'特製うどん「'.$_->{user}->{udon}.'」が巷で噂になり，店の前は期待に胸を膨らませた客でいっぱいです。') ;
			}
		}
		return 0;
	_local_

# オリジナルそばで人気アップ
@@EVENT
	start		50%
	basetime	0h
	plustime	0h
	code		sobapop
	info		オリジナルそば人気沸騰
	startfunc	_local_
		foreach(reverse(@DT))
		{
			next if rand(1000)>200;
			if ($_->{user}->{soba}&&($_->{user}->{soba} ne 'n'))
			{
			my $up=int(300*(2-$_->{rank}/5000));
			$_->{rank}+=$up;
			$_->{rank}=10000 if $_->{rank}>10000;
			return (0,$_->{shopname}.'特製そば「'.$_->{user}->{soba}.'」が人気沸騰し，噂を聞きつけた客が店の前に行列をつくっています。') ;
			}
		}
		return 0;
	_local_

@@EVENT
	start		30%
	basetime	0h
	plustime	0h
	code		syokkiarai
	info		食器洗い機の寿命
	startfunc	_local_(100)
		my($hitproba)=@_;
		
		foreach my $DT (@DT)
		{			
			next if rand(1000)>$hitproba;
			{
			foreach my $itemno (@@ITEMNO"食器洗い機")
			{
				if ($DT->{item}[@@ITEMNO"食器洗い機"-1]==1)					{
				$DT->{item}[@@ITEMNO"食器洗い機"-1]=0;
				WriteLog(2,0,$DT->{shopname}."の食器洗い機が故障したようです。");
				WriteLog(0,$DT->{id},"故障した食器洗い機を廃棄しました");
				}
			}
			}
		}
		return 0;
	_local_

@@EVENT
	start		30%
	basetime	0h
	plustime	0h
	code		haisya
	info		廃車
	startfunc	_local_(100)
		my($hitproba)=@_;
		
		foreach my $DT (@DT)
		{			
			next if rand(1000)>$hitproba;
			{
			foreach my $itemno (@@ITEMNO"自動車")
			{
				if ($DT->{item}[@@ITEMNO"自動車"-1]==1)	{
				$DT->{item}[@@ITEMNO"自動車"-1]=0;
				WriteLog(2,0,$DT->{shopname}."が故障の多い自動車を廃車したようです。");
				WriteLog(0,$DT->{id},"自動車を廃車しました");
				}
			}
			}
		}
		return 0;
	_local_

#祝福イベントを大売り出しイベントに変更
@@event
	start		20%
	basetime	5h
	plustime	5h
	code		happy
	startmsg	商店街の大売り出しが始まりました。
	endmsg		大売り出しが終わりました。
	info		大売り出しで商店街は活気にあふれています。
	func		_local_
		my $time=$TIMESPAN;
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
	basetime	6h
	plustime	24h
	code		udon-boom
	startmsg	巷ではうどんがブームのようです。
	endmsg		うどんブームが終わりました。
	info		うどんの人気が高まっています。
		param	すうどん			pop/1.5
		param	わかめうどん			pop/1.5
		param	きつねうどん			pop/1.5
		param	丸天うどん			pop/1.5
		param	えび天うどん			pop/2
		param	うどん三昧			pop/2
		param	キャビアうどん			pop/2
		param	トリュフうどん			pop/2
		param	フォアグラうどん		pop/2
		param	博多うどん			pop/2
		param	オリジナルうどん		pop/2

@@EVENT
	start		10%
	basetime	6h
	plustime	24h
	code		soba-boom
	startmsg	巷ではそばがブームのようです。
	endmsg		そばブームが終わりました。
	info		そばの人気が高まっています。
		param	かけそば			pop/1.5
		param	わかめそば			pop/1.5
		param	きつねそば			pop/1.5
		param	丸天そば			pop/1.5
		param	えび天そば			pop/2
		param	そば三昧			pop/2
		param	キャビアそば			pop/2
		param	トリュフそば			pop/2
		param	フォアグラそば			pop/2
		param	博多そば			pop/2
		param	オリジナルそば			pop/2

@@EVENT
	start		5%
	basetime	9h
	plustime	16h
	code		plusup-katuo
	group		sui
	startmsg	かつおが豊漁です。
	endmsg		かつおの流通が平常に戻りました。
	info		かつおの流通量が増えています。
		param	かつお				plus=300

@@EVENT
	start		1%
	basetime	6h
	plustime	18h
	code		plusup-tyouzame
	group		sui
	startmsg	ちょうざめの大群が浜にうち寄せました。
	endmsg		ちょうざめの流通が平常に戻りました。
	info		ちょうざめの流通量が増えています。
		param	ちょうざめ			plus=500

# 低資金優先でギルド未加盟店に資金援助イベント
@@EVENT
	start		30%
	code		getmoney
	info		資金援助
	startfunc	_local_(100000)
		my($money)=@_;
		
		foreach(reverse(@DT))
		{
			next if rand(1000)>300;

			if ($_->{guild} eq '')
			{
			$_->{money}+=$money;
			$_->{money}=$main::MAX_MONEY if $_->{money}>$main::MAX_MONEY;
			return (0,"商店会から".$_->{shopname}.'へ'.GetMoneyString($money).'の補助金が支給されました');
			}
		}
		return 0;
	_local_

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
			
			if($DT->{item}[@@ITEMNO"警報機"-1])
			{
				return (0,$DT->{shopname}.'へ万引きが入りましたが阻止されました。') if rand(1000)>$breakproba;
				
				$DT->{item}[@@ITEMNO"警報機"-1]--;
				return (0,$DT->{shopname}.'へ万引きが入り，'.$ITEM[@@ITEMNO"警報機"]->{name}.'が破壊されました。');
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
			return (0,$DT->{shopname}.'が総額'.GetMoneyString($count).'相当の万引き被害に遭いました。') if $count;
			return (0,$DT->{shopname}.'に入った万引き犯は，何も取らずに逃げました。');
		}
		return 0;
	_local_

@@EVENT
	start		30% #old15%
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
			
			if($DT->{item}[@@ITEMNO"警報機"-1])
			{
				$DT->{item}[@@ITEMNO"警報機"-1]--;
				return (0,$DT->{shopname}.'へ強盗が入り，'.$ITEM[@@ITEMNO"警報機"]->{name}.'が破壊されました。');
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
			return (0,$DT->{shopname}.'が総額'.GetMoneyString($count).'相当の強盗被害に遭いました。') if $count;
			return (0,$DT->{shopname}.'に入った強盗犯は，何も取らずに逃げました。');
		}
		return 0;
	_local_

@@EVENT
	start		15%
	basetime	0h
	plustime	0h
	code		blacktime
	info		時の渦
	startfunc	_local_(700)
		my($hitproba)=@_;
		foreach my $DT (@DT)
		{
			next if rand(1000)>$hitproba;
			
			if($DT->{user}->{black}>10)
			{
				my $blackcnt=int($DT->{user}->{black}/10);
				my $cnt=int(rand(10))+$blackcnt;
				$cnt=12 if $cnt>12;
				$DT->{time}+=3600*$cnt;
				$DT->{user}->{black}=0;
				WriteLog(0,$DT->{id},'時の渦に時間を吸い込まれました　－'.$cnt.'時間');
				return (0,'度重なる時間操作のために時の渦が発生し，'.$DT->{shopname}.'の時間を吸い込んだようです。');
			}
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
			return (0,$_->{shopname}.'が雑誌で紹介され，人気が上がったようです。');
		}
		return 0;
	_local_

@@FUNCEVENT
######################################################################
# ★宝くじイベント
# usage:  loto
# return: 0 固定
######################################################################
sub loto
{
	WriteLog(2,0,"宝くじの抽選が行われました。");
	foreach my $DT (@main'DT)
	{
		my $count=$DT->{item}[65-1];
		$DT->{item}[65-1]=0;
		my $hit1=0;
		my $hit2=0;
		my $hit3=0;
		my $hit4=0;
		my $hit5=0;
		next if !$count;
		
		foreach(1..$count)
		{
			my $rnd=rand(6096454);
			my $hit=0;
			
			if ($rnd<152411) {$hit=5;$hit5++;}
			elsif ($rnd<10000) {$hit=4;$hit4++;}
			elsif ($rnd<216) {$hit=3;$hit3++;}
			elsif ($rnd<6) {$hit=2;$hit2++;}
			elsif ($rnd<1) {$hit=1;$hit1++;}
			
			if($hit)
			{
				my $getmoney=(0,1000000000,150000000,5000000,100000,10000)[$hit];
				
				$DT->{moneystock}+=$getmoney;
				$DT->{money}=$main'MAX_MONEY if $DT->{money}>$main'MAX_MONEY;
			}
		}
		my $hitlog=5;
		$hitlog=1;
		WriteLog(($hitlog<=3?1:2),0,$DT->{shopname}."が1等".GetMoneyString(1000000000)."を当てました！") if $hit1>0;
		$hitlog=2;
		WriteLog(($hitlog<=3?1:2),0,$DT->{shopname}."が2等".GetMoneyString(150000000)."を$hit2本当てました") if $hit2>0;
		$hitlog=3;
		WriteLog(($hitlog<=3?1:2),0,$DT->{shopname}."が3等".GetMoneyString(5000000)."を$hit3本当てました") if $hit3>0;
		$hitlog=4;
		WriteLog(($hitlog<=3?1:2),0,$DT->{shopname}."が4等".GetMoneyString(100000)."を$hit4本当てました") if $hit4>0;
		my $hitlog=5;
		WriteLog(($hitlog<=3?1:2),0,$DT->{shopname}."が5等".GetMoneyString(10000)."を$hit5本当てました") if $hit5>0;
	}
	return 0;
}

@@FUNCINIT
#自転車を持っている場合，買い物に必要な時間を3/4にする。
$TIME_SEND_ITEM=int($TIME_SEND_ITEM/4*3) if (($DT->{item}[@@ITEMNO"自転車"-1])&&(!$DT->{item}[@@ITEMNO"自動車"-1]));

#自動車を持っている場合，買い物に必要な時間を1/4にする。
$TIME_SEND_ITEM=int($TIME_SEND_ITEM/4) if $DT->{item}[@@ITEMNO"自動車"-1];

@@FUNCITEM
######################################################################
# ★人材が店を去る
######################################################################
sub lostman
{
	my $itemno=$USE->{itemno};
	if(rand(1000)<$USE->{param1})
	{
		UseItem($itemno,1,'<br>仕事を終えた'.$ITEM[$itemno]->{name}.'が，黙って去っていきました');
	}
	return "";
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
				['商品券',	[[@@ITEMNO "商品券", 5],			],],
				['商品券',	[[@@ITEMNO "商品券", 4],			],],
				['商品券',	[[@@ITEMNO "商品券", 3],			],],
				['福引き補助券',	[[@@ITEMNO "福引き補助券", 5],		],],
				['防犯用品',	[[@@ITEMNO "警報機", 1],		],],
				['肥料トラック1台分',[[@@ITEMNO "堆肥", 1000],	],],
				['食器',[[@@ITEMNO "きれいな丼", 500],	],],
			],
			[
				['商品券',	[[@@ITEMNO "商品券", 3],			],],
				['商品券',	[[@@ITEMNO "商品券", 2],			],],
				['福引き補助券',	[[@@ITEMNO "福引き補助券", 3],		],],
				['食器',[[@@ITEMNO "きれいな丼", 300],	],],
			],
			[
				['福引き補助券',	[[@@ITEMNO "福引き補助券", 2],		],],
				['商品券',	[[@@ITEMNO "商品券", 2],			],],
				['商品券',	[[@@ITEMNO "商品券", 1],			],],
				['食器',[[@@ITEMNO "きれいな丼", 200],	],],
			],
			[
				['商品券',	[[@@ITEMNO "商品券", 2],			],],
				['商品券',	[[@@ITEMNO "商品券", 1],			],],
				['福引き補助券',	[[@@ITEMNO "福引き補助券", 1],		],],
			],
		);
		
		TopGetItem($DT[0],$TOP123[0],"みごと優勝の") if defined($DT[0]);
		TopGetItem($DT[1],$TOP123[1],"惜しくも2位の") if defined($DT[1]);
		TopGetItem($DT[2],$TOP123[2],"3位入賞の") if defined($DT[2]);
	
		for(my $i=9; $i<$#DT; $i+=10)
		{
			TopGetItem($DT[$i],$TOP123[3],"ジャスト".($i+1)."位の") if defined($DT[$i]);
		}
		
		sub TopGetItem
		{
			my($DT,$itemlist,$head)=@_;
			
			my @list=@{$itemlist};
			my @getitem=@{$list[int(rand($#list+1))]};
			
			my $msg=$head.$DT->{shopname}."には，商店会より".$getitem[0]."が贈られました。";
			WriteLog(2,0,0,$msg,1);
			foreach (@{$getitem[1]})
			{
				my @itemnocount=@{$_};
				
				my $cnt=AddItem($DT,$itemnocount[0],$itemnocount[1]);
				my $ITEM=$ITEM[$itemnocount[0]];
				WriteLog(0,$DT->{id},0,$head."賞品として".$ITEM->{name}."を".$itemnocount[1].$ITEM->{scale}."獲得しました。",1);
				$cnt=$itemnocount[1]-$cnt;
				WriteLog(0,$DT->{id},0,"しかし最大所持数以上だったので".$cnt.$ITEM->{scale}."破棄しました",1) if $cnt;
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

# $DEFINE_FUNCNEW_NOLOG=1 を設定すると，システム側の最近の出来事新装開店メッセージを抑制します。
$DEFINE_FUNCNEW_NOLOG=1;
WriteLog(1,0,0,$DT->{shopname}."がリアカーを引いて，この街に現れました。",1);

# その他，新装開店時に独自の処理を追加できます。

@@FUNCSHOPIN

SetUserDataEx($DT,'_so_move_in',$NOW_TIME); # 移転時刻を記録

$DT->{item}[67-1]=1;	# ヒントブックをプレゼント
if($DT->{job} eq 'man')
{
	# 人材派遣業(man)には移転消費時間の1/2を返還
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
	# 市場からの仕入の場合，\500000に付き1枚の福引き補助券を進呈する。
	my $price=$BUY->{num}*$BUY->{price};
	my $count=int $price/500000;
	
	$count=AddItemSub(@@ITEMNO"福引き補助券",$count,$BUY->{dt}) if $count;
	WriteLog(0,$BUY->{dt}{id},'市場から福引き補助券を'.$count.'枚もらいました') if $count;
}

@@END #定義終了宣言(以降コメント扱い)


