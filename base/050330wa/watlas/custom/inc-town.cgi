# 城下町設定ファイル 2003/10/08 由來

# 城下町の風景をカスタマイズできます。
# ただし，「領主邸」と，最下段の「商店街」「現在活動中の店」の位置は変更できません。
# 場所の番号は，次のようになっています。
#
#   [No.0]  [   領主邸   ] [No.1]
#   [No.2]  [No.3]  [No.4] [No.5]
#   [No.6]  [No.7]  [No.8] [No.9]
#                 ・
#                 ・
#   [   商店街   ] [ 活動中の店 ]
#   
#  ※No.10以下を定義すれば，さらに道路が増えて下に伸ばせます。

#  ＜記述文法＞
#  ・「名前」，「画像」，「リンク」，「ゲスト権限でのリンク」の順です。
#  ・画像では，$i[0]（通常建物），$i[1]（店舗建物），$space（小さい空間），$vspace（大きな空間）が有効です。
#  ・リンクは，サブプログラム名のほかアドレスを指定可能です。空欄だとリンクをつくりません。
#  ・何も定義しない場所は，樹木と解釈します。

# --- No.0 の場所定義 ---

($Pname[0],$Pimage[0],$Plink[0],$Pguest[0])=(
	"競技場",
	qq|<IMG WIDTH=16 HEIGHT=64 SRC="$IMAGE_URL/map/mapsignslime.png">$i[0]|,
	"slime",
	"slime"
	);

# --- No.1 の場所定義 ---

# 樹木のため省略

# --- No.2 の場所定義 ---

($Pname[2],$Pimage[2],$Plink[2],$Pguest[2])=(
	"依頼所",
	qq|$space<IMG WIDTH=16 HEIGHT=64 SRC=\"$IMAGE_URL/map/mapsignrequest.png\">$i[1]|,
	"req",
	"req"
	);

# --- No.3 の場所定義 ---

($Pname[3],$Pimage[3],$Plink[3],$Pguest[3])=(
	"市場",
	qq|$space<IMG WIDTH=16 HEIGHT=64 SRC=\"$IMAGE_URL/map/mapsignmarket.png\">$i[1]|,
	"shop-m",
	"shop-m"
	);

# --- No.4 の場所定義 ---

# 樹木のため省略

# --- No.5 の場所定義 ---

($Pname[5],$Pimage[5],$Plink[5],$Pguest[5])=(
	"ギルド",
	qq|<IMG WIDTH=16 HEIGHT=64 SRC="$IMAGE_URL/map/mapsignguild.png">$i[0]|,
	"gd",
	"gd"
	);

# --- No.6 の場所定義 ---

# 樹木のため省略

# --- No.7 の場所定義 ---

($Pname[7],$Pimage[7],$Plink[7],$Pguest[7])=(
	"兵士駐屯所",
	qq|<IMG WIDTH=16 HEIGHT=64 SRC="$IMAGE_URL/map/mapsignarmy.png">$i[0]|,
	"army",
	""
	);

# --- No.8 の場所定義 ---

($Pname[8],$Pimage[8],$Plink[8],$Pguest[8])=(
	"図書館",
	qq|$space<IMG WIDTH=112 HEIGHT=80 SRC="$IMAGE_URL/map/house1c.png">|,
	"action.cgi?key=library",
	"action.cgi?key=library"
	);

# --- No.9 の場所定義 ---

($Pname[9],$Pimage[9],$Plink[9],$Pguest[9])=(
	"掲示板",
	qq|<br><br><IMG WIDTH=32 HEIGHT=32 SRC="$IMAGE_URL/map/mapboard.png">|.GetTime2FormatTime((stat($COMMON_DIR.'/treelog.cgi'))[9]+0,1),
	"treebbs",
	""
	);

# --- 以下，No.10，11…と増やしていくことができます。


# --- キャラクターのセリフ ---
# 見よう見まねでカスタマイズしてください（ぉ

sub CharaDefine
{
@chara=();
	if ($DTevent{rebel})
		{
		$chara[1]=TagChara('大変だ・・・。援軍を呼ばないと！',"d2");
		$chara[2]=TagChara('反乱だ！加勢に行くぞっ',"d1");
		$chara[5]=TagChara('領主を倒せっ',"d1")."<br>".TagChara('一気にケリをつけようっ',"d1");
		return;
		}
my $i=int($NOW_TIME / 3600) % 4;
	if ($i == 0)
		{
		$chara[0]=TagChara("うちのスライムまた負けちゃった・・・","e1").$vspace.$vspace;
		$chara[4]=$space.TagChara("食事の材料買いに行かなくっちゃ。","e2");
		}
	elsif ($i == 1)
		{
		$chara[7]=$vspace.$vspace.TagChara("図書館の情報は重要だよっ","b2").$space
			.TagChara("掲示板のチェックも大切だね。ふむふむ・・・","b1");
		}
	elsif ($i == 2)
		{
		$chara[4]=$vspace.TagChara("ぽかぽかして気持ちええのぉ・・・","c2");
		$chara[6]=TagChara("買い物はやっぱり".$DT[0]->{shopname}."よねっ","c1").$space;
		}
	elsif ($STATE->{safety} < 4000)
		{
		my $lid=$id2idx{$STATE->{leader}};
		$chara[0]=TagChara(($STATE->{leader} ? $DT[$lid]->{name} : $BAL_NAME).'の暴政に断固ハンターイ！',"a1")
			.TagChara('もっと市民の安全を考えろーっ',"a2");
		}
}
1;

