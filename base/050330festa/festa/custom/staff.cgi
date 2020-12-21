# スタッフロール 2005/03/30 由來
#
# 各種著作権表示用です。新たな素材・プログラムを組み込む際に，ここに追加しましょう。
# HTMLの知識があれば，見よう見まねでできると思います。
#
# スタッフロールへのリンクを外したり，目立たなくしてはいけません。
# 著作権表示は目立つよう適切に行う必要があり，これを怠ると法的問題になる場合があります。

DataRead();
CheckUserPass(1);
OutError("パスワード漏れの危険があるので表示中止します。") if $Q{u};
$disp.="<BIG>●開発スタッフロール</BIG><br><br>";
$disp.=$TB.$TR.$TD.GetTagImgKao("案内人","guide").$TD;
$disp.='ゲームの各部分についての著作権は，それぞれ下記の方々に帰属します。<br>';
$disp.='なお，素材をゲームから直接取り出して利用しないでください。'.$TRE.$TBE;
$disp.="<br>".$TBT.$TRT.$TD;

# ----------- ここから下をいろいろ書き換える。-----------------------------

$disp.=<<"HTML";
<SPAN>製作・著作</SPAN> ： 由來 ... <A HREF="http://akimono.org/" target="_blank">商人物語</A>
<br><br>
<SPAN>原作</SPAN> ： MU 様 ... <A HREF="http://mutoys.com/" target="_blank">MUTOYS</A>
<br><br>
<SPAN>アイコン（アイコン）</SPAN> ： せんた 様  ,  <SPAN>ギルド状態アイコン</SPAN> ：  アシュ 様
<br><br>
<SPAN>アイコン（種類・ジョブ）</SPAN> ： YOU 様 ... <A HREF="http://foryou.cside.com/" target="_blank">Net-you's Homepage</A>
<br><br>
<SPAN>マップ・キャラ</SPAN> ： REFMAP 様 ... <A HREF="http://www.mogunet.net/~fsm/" target="_blank">FIRST SEED MATERIAL</A>
<br><br>
<SPAN>音楽</SPAN> ： 氷石 彩亜 様 ... <A HREF="http://fhouse.s17.xrea.com/" target="_blank">FREEDOM HOUSE 2nd</A>
HTML

# ----------- ここまで。最後の「HTML」を消さないよう注意。-----------------

require "skin.pl" if -e "skin.pl";
$disp.=$TRE.$TBE;
OutSkin();
1;
