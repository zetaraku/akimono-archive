# ドラゴンレース設定 2005/03/30 由來

# -------- 設定部分 ---------

# レース設定
@WEATHER=('晴','雨');
@RACERANK=('G1','G2','G3','OP','100下','未勝利');
@FIELDTYPE=('芝生','ダート');

@RACETERM=("登竜レース","重賞レース");

@RACE=(
	# 0名称		1ランク	2ハンデ	3馬場種	4終盤坂	5距離	6１着	7２着	8３着 9定員
	[
	['若葉新竜'	,5	,0	,0	,1	,1600	,50	,30	,20	,10],
	['かさぶらんか杯',4	,20	,0	,0	,1600	,100	,50	,30	,10],
	['かさぶらんかダート杯',4,20	,1	,1	,1600	,100	,50	,30	,10],
	['未勝利2600ダート',5	,0	,1	,0	,2600	,50	,30	,20	,10],
	['あじさいカップ',3	,50	,0	,0	,2800	,150	,70	,50	,10],
	['あじさいダートカップ',3,50	,1	,0	,2800	,150	,70	,50	,10],
	['彩花新竜'	,5	,0	,0	,0	,2200	,50	,30	,20	,10],
	['かえで杯'	,4	,20	,0	,0	,2000	,100	,50	,30	,10],
	['かえでダート杯',4	,20	,1	,1	,2000	,100	,50	,30	,10],
	['未勝利1600ダート',5	,0	,1	,1	,1600	,50	,30	,20	,10],
	['あやめカップ',3	,50	,0	,1	,1400	,150	,70	,50	,10],
	['あやめダートカップ',3	,50	,1	,0	,1400	,150	,70	,50	,10],
	],
	[
	['酒場杯ハンデ'	,2	,100	,0	,0	,2600	,200	,100	,80	,10],
	['水花賞'	,2	,100	,1	,0	,2200	,200	,100	,80	,10],
	['新月杯'	,2	,100	,0	,0	,1600	,200	,100	,80	,10],
	['蒼天杯'	,2	,100	,0	,0	,2000	,200	,100	,80	,10],
	['領主チャレンジカップ',1,200	,0	,1	,2800	,300	,150	,100	,10],
	['桃花賞'	,1	,200	,1	,0	,2200	,300	,150	,100	,10],
	['名月トライアルカップ',1,200	,0	,0	,1400	,300	,150	,100	,10],
	['黄天トライアルカップ',1,200	,0	,1	,2000	,300	,150	,100	,10],
	['新千年国王賞'	,0	,0	,0	,0	,3000	,400	,200	,100	,10],
	['春花賞'	,0	,0	,1	,1	,2400	,400	,200	,100	,10],
	['秋月賞'	,0	,0	,0	,1	,1600	,400	,200	,100	,10],
	['霹靂賞'	,0	,0	,0	,0	,2000	,400	,200	,100	,10],
	],
);

# 牧場
$RCest=1000000;

# 競争ドラゴン
$MYDRmax=3;
$DRbuy=500000;

# 引退
$DRretire=86400 * 10;
$PRentry=300;
$PRcycle=86400 * 3;

# 厩舎
$STest=500000;
$STcost=100000;
$STmax=10;
$STtime=86400 * 50;

# 騎手
$JKest=500000;
$JKmax=20;
$JKtime=86400 * 50;

# 騎手能力
@JKSP=(
	'なし',
	'牝竜の騎乗が得意',
	'牡竜の騎乗が得意',
	'芝のレースに強い',
	'ダートのレースに強い',
	'大舞台に強い',
	'雨のレースに強い',
	'勝利すると竜の成長を促す',
);

# 用語の定義

@STRATE=('逃げ','先行','差し','追込','自在');

@EMPHA=('スピード','勝負根性','瞬発力','パワー','健康','柔軟性');

@VALUE=('Ｅ','Ｄ','Ｃ','Ｂ','Ａ','Ｓ','Ｓ');

@EVALUE=('×','△','○','◎','◎');

@FM=('牡','牝');

@ONRACE=('待機','<b>落選</b>','<SPAN>登録</SPAN>','<SPAN>出走</SPAN>');

@DRCOLOR=('紅毛','青毛','碧毛','芦毛','漆毛');

# 更新時刻 (調教時刻 登竜出走締め 重賞出走締め)

@DRTIMESET=(3,23,22);

# -------- 設定完了 ---------

@DLOG=();

@DRnamelist=qw(
		no birth fm color name town owner stable race apt
		sp spp sr srp ag agp pw pwp hl hlp fl flp
		con wt gr
		prize sdwin g3win g2win g1win
		);

@PRnamelist=qw(
		no birth fm color name town owner apt hr preg
		sp sr ag pw hl fl
		prize sdwin g3win g2win g1win
		);

@RCnamelist=qw(
		no birth name town owner
		prize sdwin g3win g2win g1win
		);

@STnamelist=qw(
		no birth name town owner
		emp tr con wt
		sp sr ag pw hl fl
		sdwin g3win g2win g1win
		);

@JKnamelist=qw(
		no birth name town owner race
		ahead back sp
		sdwin g3win g2win g1win
		);

@RDnamelist=qw(
		no dr birth fm color name ranch rcname stable stname jock jkname prize strate
		sp1 sp2 sp3 sp4
		pop time str lose
		);
1;

sub GetTagImgDra
{
	my($i,$ii,$old)=@_;
	$i++;
	$ii++;
	$i+=2 if $old;
	return qq|<IMG class="i" SRC="$IMAGE_URL/dragon$i$ii$IMAGE_EXT">|;
}

