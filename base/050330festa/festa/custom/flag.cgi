# イベントテラー 2003/10/10 由來
# キャンパスフェスタ独自

DataRead();
CheckUserPass(1);

$disp.=GetMenuTag('log',	'[速報]')
	.GetMenuTag('log',	'[入賞]','&t=3')
	.GetMenuTag('log',	'[順位]','&t=4')
	.GetMenuTag('log',	'[爵位]','&t=5');
$disp.="<hr width=500 noshade size=1>";
$disp.="<BIG>●新聞：三面記事</BIG><br><br>";

OutError('数値に不正があります') if (crypt($Q{class},$Q{mode}) ne $Q{check});
my $functionname="story".$Q{mode};
OutError('現在の状態ではこのコマンドを実行できません') if !defined(&$functionname);
&$functionname if defined(&$functionname);

OutSkin();
1;

sub story1
{
	my $idx=$id2idx{$Q{class}};
	my $shopname="<SPAN>".$DT[$idx]->{shopname}."</SPAN>";
	my $name="<SPAN>".$DT[$idx]->{name}."</SPAN>";
	my $icon=GetTagImgKao($DT[$idx]->{name},$DT[$idx]->{icon});
	my $people=GetTagImgKao("お客","st1");

	$disp.=<<STR;
<TABLE cellpadding="26" width="570">$TR$TD
アイスを販売している$shopnameの店主$nameのもとに，あるときこんなお客がやってきた。<br><br>
$people<SPAN>お客</SPAN>：すいませーん。<br>
$icon$name：いらっしゃーい。アイスですか？<br>
$people<SPAN>お客</SPAN>：んと，アイスはもうたくさん食べたんだけど…<br>
$icon$name：む？（じゃあ，どっかいけよ。）<br>
$people<SPAN>お客</SPAN>：おなかがいっぱいにならないので，何かありませんか？<br>
$icon$name：じゃあ，もっとアイスをどうぞ。<br>
$people<SPAN>お客</SPAN>：アイスじゃおなかいっぱいにならないよー。びえーん。<br>
$icon$name：うーん。じゃあ何が食べたいんでしょう？（クレーマーかこいつは。）<br>
$people<SPAN>お客</SPAN>：焼きそば食べたいよー。びえーん。<br>
$icon$name：あー，焼きそばは売ってないです。作る機材がないんで。<br>
$people<SPAN>お客</SPAN>：ひどいよー。びえーん。先生にいいつけてやる。<br>
$icon$name：・・・。（鼻炎なのかこいつは。）<br><br>
先生にいいつけられるのは困るので，<br>
$nameは焼きそば用の<SPAN>調理台</SPAN>を
STR
	$disp.=GetMoneyString(50000)."で購入することにした。<br>（以後，焼きそばを調理できます。）$TRE$TBE";
}

sub story2
{
	my $idx=$id2idx{$Q{class}};
	my $shopname="<SPAN>".$DT[$idx]->{shopname}."</SPAN>";
	my $name="<SPAN>".$DT[$idx]->{name}."</SPAN>";
	my $icon=GetTagImgKao($DT[$idx]->{name},$DT[$idx]->{icon});
	my $people=GetTagImgKao("お客","st2");

	$disp.=<<STR;
<TABLE cellpadding="26" width="570">$TR$TD
タコをそのまま販売している$shopnameの店主$nameのもとに，あるときこんなお客がやってきた。<br><br>
$people<SPAN>お客</SPAN>：すいませーん。たこ焼きください。<br>
$icon$name：いらっしゃーい。はい，どうぞ。<br>
$people<SPAN>お客</SPAN>：・・・。<br>
$icon$name：ん？どうしました？<br>
$people<SPAN>お客</SPAN>：あのー，これタコそのまんまなんですけど。<br>
$icon$name：はい，うちは100％タコなんです。<br>
$people<SPAN>お客</SPAN>：・・・。<br>
$icon$name：・・・。<br>
$people<SPAN>お客</SPAN>：・・・せめて焼けよ。<br><br>
やっぱり焼かないとダメだということに気付き，<br>
$nameは<SPAN>たこ焼き器</SPAN>を
STR
	$disp.=GetMoneyString(50000)."で購入することにした。<br>（以後，たこ焼きを調理できます。）$TRE$TBE";
}

sub story3
{
	my $idx=$id2idx{$Q{class}};
	my $shopname="<SPAN>".$DT[$idx]->{shopname}."</SPAN>";
	my $name="<SPAN>".$DT[$idx]->{name}."</SPAN>";
	my $icon=GetTagImgKao($DT[$idx]->{name},$DT[$idx]->{icon});
	my $people=GetTagImgKao("お客","st3");

	$disp.=<<STR;
<TABLE cellpadding="26" width="570">$TR$TD
青海苔をそのまま販売している$shopnameの店主$nameのもとに，あるときこんなお客がやってきた。<br><br>
$people<SPAN>お客</SPAN>：えーとこの店は何を売ってるのかしら？<br>
$icon$name：いらっしゃい。青海苔を売ってますがいかがでしょう。<br>
$people<SPAN>お客</SPAN>：・・・青海苔って焼きそばにかけるやつじゃないの？<br>
$icon$name：いや，うちではそのまま売ってるんです。<br>
$people<SPAN>お客</SPAN>：・・・美容にいいのかしら。じゃあ，それください。<br>
$icon$name：どぞ。<br>
$people<SPAN>お客</SPAN>：もぐもぐ。<br>
$icon$name：・・・あ。<br>
$people<SPAN>お客</SPAN>：ん？何かしら？<br>
$icon$name：・・・歯に青海苔ついてますよ。<br>
$people<SPAN>お客</SPAN>：・・・。<br>
$icon$name：・・・。<br>
$people<SPAN>お客</SPAN>：・・・。<br>
$icon$name：・・・ぷぷっ。<br>
$people<SPAN>お客</SPAN>：・・・笑ったわね！ むきー！<br><br>
青海苔が歯についたままだとカッコ悪いので気をつけよう。<br>
（$shopnameの人気は少し低下したらしい。）
STR
	$disp.="$TRE$TBE";
}

sub story4
{
	my $idx=$id2idx{$Q{class}};
	my $shopname="<SPAN>".$DT[$idx]->{shopname}."</SPAN>";
	my $name="<SPAN>".$DT[$idx]->{name}."</SPAN>";
	my $icon=GetTagImgKao($DT[$idx]->{name},$DT[$idx]->{icon});
	my $people=GetTagImgKao("美術部員","st4");

	$disp.=<<STR;
<TABLE cellpadding="26" width="570">$TR$TD
いまひとつ成績の冴えない$shopnameの店主$nameのもとに，あるときこんなお客がやってきた。<br><br>
$people<SPAN>美術部員</SPAN>：ちょっといいかねそこの君。<br>
$icon$name：は，はい何でしょう。<br>
$people<SPAN>美術部員</SPAN>：君，ぜんぜん試験の成績の方がよくないらしいね。<br>
$icon$name：う・・・た，たしかに。<br>
$people<SPAN>美術部員</SPAN>：しかも，得意科目が１つもないと来てる。こりゃあ重症だ。<br>
$icon$name：ううう・・・よ，余計なお世話です。<br>
$people<SPAN>美術部員</SPAN>：フッ・・・それが余計ではないのだ。<br>
$icon$name：・・・は？<br>
$people<SPAN>美術部員</SPAN>：考えてみたまえ。こんな勉強，意味があると思ってるのかね？<br>
$icon$name：・・・え，いろいろ役に立つのでは。<br>
$people<SPAN>美術部員</SPAN>：役に立つだと？！ そんなことどうだっていい！<br>
$icon$name：ええ？<br>
$people<SPAN>美術部員</SPAN>：君は英語の勉強をしていて，あのすばらしい夕日の織り成す景色に心通わせることができるか？いや，できない。むしろ有害だ。自然を見たまえ！そして心の目で見るのだ！そうすれば，心の中に１つの完成されたビジョンが浮き上がってくるはずだ！そして…<br><br>
（中略。）<br><br>
$people<SPAN>美術部員</SPAN>：…というわけだ。芸術の前にこんな勉強などいらんのだ。わかったか。<br>
$icon$name：は，はいー。<br>
$people<SPAN>美術部員</SPAN>：まあそういうわけだから，君はすぐ美術部に入りなさい。<br><br>
美術部に入れるようになった。<br>
STR
	$disp.="$TRE$TBE";
}

sub story5
{
	my $idx=$id2idx{$Q{class}};
	my $shopname="<SPAN>".$DT[$idx]->{shopname}."</SPAN>";
	my $name="<SPAN>".$DT[$idx]->{name}."</SPAN>";
	my $icon=GetTagImgKao($DT[$idx]->{name},$DT[$idx]->{icon});
	my $people=GetTagImgKao("茶道部員","st5");

	$disp.=<<STR;
<TABLE cellpadding="26" width="570">$TR$TD
ある日，$shopnameの店主$nameのもとに，こんなお客がやってきた。<br><br>
$people<SPAN>茶道部員</SPAN>：すいませーん。アイスください。<br>
$icon$name：いらっしゃいませ。はいどうぞ。<br>
$people<SPAN>茶道部員</SPAN>：・・・ふむ，甘くておいしいわ。でもそれだけじゃだめね。<br>
$icon$name：ええ？（文化祭の出店で評論されても・・・）<br>
$people<SPAN>茶道部員</SPAN>：たしかに，甘さは必要。しかし，もう一方でそれを抑えることも必要。<br>
$icon$name：甘さを，抑える・・・？<br>
$people<SPAN>茶道部員</SPAN>：あなた，国文学とかできる方でしょ。日本にそういう物はない？<br>
$icon$name：えーと，日本で・・・。<br>
$people<SPAN>茶道部員</SPAN>：日本の代表\的な飲み物よ。<br>
$icon$name：・・・ふむふむ。コーラでしょ。<br>
$people<SPAN>茶道部員</SPAN>：それはアメリカです。<br>
$icon$name：うーん・・・あんみつ？<br>
$people<SPAN>茶道部員</SPAN>：それ，よけい甘くなるでしょ！渋みをきかせるのよ，渋みを。<br>
$icon$name：日本独自で渋み・・・うーん・・・。<br>
$people<SPAN>茶道部員</SPAN>：・・・<br>
$icon$name：・・・わかった。青汁でしょ！<br>
$people<SPAN>茶道部員</SPAN>：・・・もういいから茶道部に入りなさい。<br><br>
茶道部に入れるようになった。<br>
STR
	$disp.="$TRE$TBE";
}

sub story6
{
	my $idx=$id2idx{$Q{class}};
	my $shopname="<SPAN>".$DT[$idx]->{shopname}."</SPAN>";
	my $name="<SPAN>".$DT[$idx]->{name}."</SPAN>";
	my $icon=GetTagImgKao($DT[$idx]->{name},$DT[$idx]->{icon});
	my $people=GetTagImgKao("花道部員","st6");

	$disp.=<<STR;
<TABLE cellpadding="26" width="570">$TR$TD
ある日，$shopnameの店主$nameのもとに，こんなお客がやってきた。<br><br>
$people<SPAN>花道部員</SPAN>：ふーむ。<br>
$icon$name：いらっしゃいませ。お求めのものは何でしょう？<br>
$people<SPAN>花道部員</SPAN>：ああ残念でした。物買いに来たわけじゃないから。<br>
$icon$name：それではさようなら。（きっぱり。）<br>
$people<SPAN>花道部員</SPAN>：ちょっと待ちなさいよ。人の話くらいきいたら？<br>
$icon$name：・・・なんでしょう？（めんどくさいなあ。）<br>
$people<SPAN>花道部員</SPAN>：私たちの部活をするには，特定の知識がいるのよ。<br>
$icon$name：ふむふむ。<br>
$people<SPAN>花道部員</SPAN>：たとえばあなた，キャスケードって日本語でどういう意味？<br>
$icon$name：えーと，Cascadeは，・・・滝じゃないですか？<br>
$people<SPAN>花道部員</SPAN>：・・・正解。英語が得意だと便利ね。<br>
$icon$name：いや，たまたまですよ。<br>
$people<SPAN>花道部員</SPAN>：たまたまじゃ困るのよ。花道ってこんなんばっかりよ。<br>
$icon$name：・・・。<br>
$people<SPAN>花道部員</SPAN>：キャスケードっていうのは滝のように花を配置すること。<br>
$icon$name：なるほど，そのまんまですね。<br>
$people<SPAN>花道部員</SPAN>：でも英語を知らないと，意味わかんないでしょ？<br>
$icon$name：たしかに。<br>
$people<SPAN>花道部員</SPAN>：そのことが花道の未来を暗く閉ざしているんだわ！<br>
$icon$name：はあ。<br>
$people<SPAN>花道部員</SPAN>：英語がわかれば簡単なのに，ああもったいない！<br>
$icon$name：・・・はあ。<br>
$people<SPAN>花道部員</SPAN>：英語がわかる人には花道の未来を切り開く責任があるのよ！<br>
$icon$name：・・・はあ。<br>
$people<SPAN>花道部員</SPAN>：じー。<br>
$icon$name：・・・。<br>
$people<SPAN>花道部員</SPAN>：じー。<br>
$icon$name：・・・。<br>
$people<SPAN>花道部員</SPAN>：じー。<br><br>
花道部に入れるようになった。<br>
STR
	$disp.="$TRE$TBE";
}

sub story7
{
	my $idx=$id2idx{$Q{class}};
	my $shopname="<SPAN>".$DT[$idx]->{shopname}."</SPAN>";
	my $name="<SPAN>".$DT[$idx]->{name}."</SPAN>";
	my $icon=GetTagImgKao($DT[$idx]->{name},$DT[$idx]->{icon});
	my $people=GetTagImgKao("化学部員","st7");

	$disp.=<<STR;
<TABLE cellpadding="26" width="570">$TR$TD
ある日，$shopnameの店主$nameのもとに，こんなお客がやってきた。<br><br>
$people<SPAN>化学部員</SPAN>：今度はこれを混ぜてみようかな？<br>
$icon$name：いらっしゃいませ。何をお求めですか？<br>
$people<SPAN>化学部員</SPAN>：ここに売ってある物全部混ぜていい？<br>
$icon$name：お金払ってからにしてください。<br>
$people<SPAN>化学部員</SPAN>：お金ないよ？<br>
$icon$name：・・・さようなら，旅の人。またのお越しをお待ちしてません。<br>
$people<SPAN>化学部員</SPAN>：えー，混ぜてみたいと思わないの？<br>
$icon$name：は？<br>
$people<SPAN>化学部員</SPAN>：世の中で新しいことって混ぜることで起こるんだよ？<br>
$icon$name：いや適当に混ぜてもしょうがないかと・・・。<br>
$people<SPAN>化学部員</SPAN>：うん，そのとおりだよ！<br>
$icon$name：・・・。<br>
$people<SPAN>化学部員</SPAN>：じゃあ，うまく混ぜるにはどうしたらいいと思う？<br>
$icon$name：・・・事前によく考えることでは？<br>
$people<SPAN>化学部員</SPAN>：そうそう！緻密な計算が必要なんだよ。<br>
$icon$name：ふむふむ。<br>
$people<SPAN>化学部員</SPAN>：じゃあ質問。コサインの２乗とサインの２乗を足すといくつ？<br>
$icon$name：・・・。<br>
$people<SPAN>化学部員</SPAN>：緻密な計算で答えるんだ！さあいくつ！<br>
$icon$name：え，えっと・・・１です。<br>
$people<SPAN>化学部員</SPAN>：ＯＫ！じゃあ周期 L の層構\造を成している物質に入射角度θで波長λのＸ線が入射した場合を考えよう！ 最初の層で反射されるＸ線の波が cos(wt) と書けたとすると，第２層目で反射されるＸ線の波は光路差 2Lcosθ を考えるとその計算式は？<br>
$icon$name：・・・えーと，cos(wt-4πLcosθ/λ)です。<br>
$people<SPAN>化学部員</SPAN>：うし！じゃあそのまま計算して３層目までのＸ線の波を重ね合わせてノーマライズすると反射されるＸ線の強度は？<br>
$icon$name：(cos(wt) + cos(wt-4πLcosθ/λ) + cos(wt-8πLcosθ/λ))/3です。<br>
$people<SPAN>化学部員</SPAN>：すごいよ！そうすると当然層の数を増やしていけばブラッグ反射の条件式 cosθ=λ/2L の所にピークが立つはずだよね！層の数を変えて図に表\していったら，きっと１０層ぐらいやれば，きれいなピークが現れるはずだよね！そのピークが・・・<br><br>
・・・化学部に入れるようになった。<br>
STR
	$disp.="$TRE$TBE";
}

sub story8
{
	my $idx=$id2idx{$Q{class}};
	my $shopname="<SPAN>".$DT[$idx]->{shopname}."</SPAN>";
	my $name="<SPAN>".$DT[$idx]->{name}."</SPAN>";
	my $icon=GetTagImgKao($DT[$idx]->{name},$DT[$idx]->{icon});
	my $people=GetTagImgKao("パソ\部員","st8");

	$disp.=<<STR;
<TABLE cellpadding="26" width="570">$TR$TD
ある日，$shopnameの店主$nameのもとに，こんなお客がやってきた。<br><br>
$people<SPAN>パソ\部員</SPAN>：うひょもえー。<br>
$icon$name：いらっしゃいませ。何かお探しですか？<br>
$people<SPAN>パソ\部員</SPAN>：萌えー。<br>
$icon$name：・・・うちでは，萌えーは扱ってません。<br>
$people<SPAN>パソ\部員</SPAN>：たまらないんだ・・・あのネコミミもえー。<br>
$icon$name：だからうちじゃ売ってないって。<br>
$people<SPAN>パソ\部員</SPAN>：二次元の世界もえー。<br>
$icon$name：いや，ですから他の店行ってくださいって。<br>
$people<SPAN>パソ\部員</SPAN>：なに？アニメに興味がないもえ？<br>
$icon$name：誰もそんなこといってません。<br>
$people<SPAN>パソ\部員</SPAN>：じゃあどうして君は自分で萌え文化を創ろうとしないんだもえ？<br>
$icon$name：は？<br>
$people<SPAN>パソ\部員</SPAN>：君は何のために英語や数学を勉強してるんだもえ！<br>
$icon$name：いや，いろいろ役に立つし。<br>
$people<SPAN>パソ\部員</SPAN>：そう！とくに，あきものの関数を読み解くのに役に立つんだもえ！<br>
$icon$name：はあ。<br>
$people<SPAN>パソ\部員</SPAN>：たとえば，DataReadっていうのは何だもえ？<br>
$icon$name：データを読み込むんじゃないですか？<br>
$people<SPAN>パソ\部員</SPAN>：そうもえ！正解だから，10のもえ経験値を獲得だもえ！<br>
$icon$name：・・・。<br>
$people<SPAN>パソ\部員</SPAN>：じゃあ，OutSkinっていうのは何だもえ？<br>
$icon$name：スキンを取り込んで結果を出力するんじゃないかな。<br>
$people<SPAN>パソ\部員</SPAN>：それじゃ，PushLogっていうのはもえ？<br>
$icon$name：ログにデータを送り込むのでは？<br>
$people<SPAN>パソ\部員</SPAN>：正解だもえ！合計50もえ経験値がたまったからレベルアップだもえ！<br>
$icon$name：わ，わーい。<br>
$people<SPAN>パソ\部員</SPAN>：魔法ラブラブフラッシュが使えるようになったもえ！<br>
$icon$name：わーい。<br>
$people<SPAN>パソ\部員</SPAN>：さあ僕と一緒に燃えて萌えて萌えまくるもえ！<br><br>
パソ\部に入れるようになった。<br>
STR
	$disp.="$TRE$TBE";
}

sub story9
{
	my $idx=$id2idx{$Q{class}};
	my $shopname="<SPAN>".$DT[$idx]->{shopname}."</SPAN>";
	my $name="<SPAN>".$DT[$idx]->{name}."</SPAN>";
	my $icon=GetTagImgKao($DT[$idx]->{name},$DT[$idx]->{icon});
	my $people=GetTagImgKao("手品部員","st9");

	$disp.=<<STR;
<TABLE cellpadding="26" width="570">$TR$TD
ある日，$shopnameの店主$nameのもとに，こんなお客がやってきた。<br><br>
$people<SPAN>手品部員</SPAN>：ちょっといいかな。<br>
$icon$name：いらっしゃいませ。何をお求めでしょう？<br>
$people<SPAN>手品部員</SPAN>：１つたこ焼きを作ってみてくれないか。<br>
$icon$name：はい，かしこまりました。<br>
$people<SPAN>手品部員</SPAN>：・・・。<br>
$icon$name：・・・。（じゅー。）<br>
$people<SPAN>手品部員</SPAN>：・・・ほほう，なかなか器用に転がすじゃないか。<br>
$icon$name：転がさないとお好み焼きになってしまいますから。<br>
$people<SPAN>手品部員</SPAN>：こ，これだーーー！！。<br>
$icon$name：え？<br>
$people<SPAN>手品部員</SPAN>：これだよ私の探し求めていたものは！<br>
$icon$name：ん？そんなにたこ焼き食べたかったですか？<br>
$people<SPAN>手品部員</SPAN>：いや，それを食べるつもりはもともとなかった。<br>
$icon$name：がーん。<br>
$people<SPAN>手品部員</SPAN>：重要なのは，そのエレガントな転がし方だ。<br>
$icon$name：はあ。<br>
$people<SPAN>手品部員</SPAN>：それを使えば，ザ・トランプ焼き転がしマジックが完成するはずだ。<br>
$icon$name：あんまおいしくなさそうですね。<br>
$people<SPAN>手品部員</SPAN>：いや，ソ\ースをかければおいしい。<br>
$icon$name：・・・。（ボケをボケで返すなよ。）<br>
$people<SPAN>手品部員</SPAN>：だが，必要なのは，やはりその器用さだな。<br>
$icon$name：ふむふむ。<br>
$people<SPAN>手品部員</SPAN>：あとは，事前に緻密な計算をすることだ。<br>
$icon$name：計算なら得意ですよ。<br>
$people<SPAN>手品部員</SPAN>：よし，そうときまったらすぐ手品部に入りたまえ。<br>
$icon$name：な，なんか今回はあんまり強引な勧誘じゃないですね。<br>
$people<SPAN>手品部員</SPAN>：たまには作者も自然なイベントを作りたいのだろう。<br>
$icon$name：あれ，でも何か忘れてるような・・・？<br>
$people<SPAN>手品部員</SPAN>：ん？何か知らんが，私は帰るぞ。これはもらっておく。<br>
$icon$name：・・・ああっ，たこ焼きの代金！ちょっと待ってー。<br><br>
手品部に入れるようになった。<br>
STR
	$disp.="$TRE$TBE";
}

sub story10
{
	my $idx=$id2idx{$Q{class}};
	my $shopname="<SPAN>".$DT[$idx]->{shopname}."</SPAN>";
	my $name="<SPAN>".$DT[$idx]->{name}."</SPAN>";
	my $icon=GetTagImgKao($DT[$idx]->{name},$DT[$idx]->{icon});
	my $people=GetTagImgKao("演劇部員","st10");

	$disp.=<<STR;
<TABLE cellpadding="26" width="570">$TR$TD
ある日，$shopnameの店主$nameのもとに，こんなお客がやってきた。<br><br>
$people<SPAN>演劇部員</SPAN>：おーっほっほっほっほっ。<br>
$icon$name：いらっしゃいませ・・・。（何か変なの来たー。）<br>
$people<SPAN>演劇部員</SPAN>：おほっほっほっ。<br>
$icon$name：えーと・・・何をお求めですか？<br>
$people<SPAN>演劇部員</SPAN>：買いに来たんじゃないわ。売りに来たのよ。<br>
$icon$name：ええ？<br>
$people<SPAN>演劇部員</SPAN>：今度，私が出る舞台のポスター，買ってくれるわよね？<br>
$icon$name：いりません。（きっぱり。）<br>
$people<SPAN>演劇部員</SPAN>：なんですって！仮にも演劇部の超美人助演女優よ！<br>
$icon$name：主演じゃないじゃん。<br>
$people<SPAN>演劇部員</SPAN>：分かってないわね・・・主演じゃないから売り込みしてるんじゃないの。<br>
$icon$name：な・・・なるほど・・・。<br>
$people<SPAN>演劇部員</SPAN>：地道にポスター売ってれば，人気も上がって主演になる日が来るわ！<br>
$icon$name：はあ・・・。<br>
$people<SPAN>演劇部員</SPAN>：さあ早く買うのよ。次の店にも行かなくちゃいけないから。<br>
$icon$name：いや，演劇に興味ないし。<br>
$people<SPAN>演劇部員</SPAN>：なんですってえええええええ！！<br>
$icon$name：・・・。<br>
$people<SPAN>演劇部員</SPAN>：すぐに演劇部に入りなさい。<br>
$icon$name：結局そうなるのね・・・。<br><br>
演劇部に入れるようになった。<br>
STR
	$disp.="$TRE$TBE";
}

sub story11
{
	my $idx=$id2idx{$Q{class}};
	my $shopname="<SPAN>".$DT[$idx]->{shopname}."</SPAN>";
	my $name="<SPAN>".$DT[$idx]->{name}."</SPAN>";
	my $icon=GetTagImgKao($DT[$idx]->{name},$DT[$idx]->{icon});
	my $people=GetTagImgKao("古典部員","st11");

	$disp.=<<STR;
<TABLE cellpadding="26" width="570">$TR$TD
ある日，$shopnameの店主$nameのもとに，こんなお客がやってきた。<br><br>
$people<SPAN>古典部員</SPAN>：すいませーん。<br>
$icon$name：いらっしゃ・・・うわー！<br>
$people<SPAN>古典部員</SPAN>：あら，びっくりしました？変装ですよこれ。<br>
$icon$name：なんでまたそんなコスプレを・・・。<br>
$people<SPAN>古典部員</SPAN>：お化け屋敷やってるんです。<br>
$icon$name：おお，いいなー。<br>
$people<SPAN>古典部員</SPAN>：何てったってお化け屋敷は文化祭じゃ最高の人気よ。<br>
$icon$name：うんうん確かに。<br>
$people<SPAN>古典部員</SPAN>：でも誰にでもできるものじゃないのよ！<br>
$icon$name：ふむふむ。<br>
$people<SPAN>古典部員</SPAN>：まず，お化けについての古典を読み解くには，国語の知識が必要よ。<br>
$icon$name：国語は得意です。<br>
$people<SPAN>古典部員</SPAN>：それだけじゃない，西洋の書物にあたるには，英語もできないと。<br>
$icon$name：英語もできます。<br>
$people<SPAN>古典部員</SPAN>：さらに，観客を効率よくおどかすためには，綿密な計算がいるの。歩くスピードと心理をきちんと考えないと失敗するわ。<br>
$icon$name：数学もできます。<br>
$people<SPAN>古典部員</SPAN>：・・・。<br>
$icon$name：・・・。<br>
$people<SPAN>古典部員</SPAN>：・・・。<br>
$icon$name：・・・。<br><br>
古典部に入れるようになった。<br>
STR
	$disp.="$TRE$TBE";
}

sub story12
{
	my $idx=$id2idx{$Q{class}};
	my $shopname="<SPAN>".$DT[$idx]->{shopname}."</SPAN>";
	my $name="<SPAN>".$DT[$idx]->{name}."</SPAN>";
	my $icon=GetTagImgKao($DT[$idx]->{name},$DT[$idx]->{icon});
	my $people=GetTagImgKao("実行委員","st12");

	$disp.=<<STR;
<TABLE cellpadding="26" width="570">$TR$TD
ある日，$shopnameの店主$nameのもとに，こんなお客がやってきた。<br><br>
$people<SPAN>実行委員</SPAN>：実行委員会である！一同起立！<br>
$icon$name：・・・はっ！<br>
$people<SPAN>実行委員</SPAN>：礼！<br>
$icon$name：（ぺこり。）<br>
$people<SPAN>実行委員</SPAN>：これから辞令をいいわたす！<br>
$icon$name：へへぇ。<br>
$people<SPAN>実行委員</SPAN>：汝を実行委員会に召し抱える！<br>
$icon$name：まぢ？！<br>
$people<SPAN>実行委員</SPAN>：だが，その前に確認である。<br>
$icon$name：は，はいー。<br>
$people<SPAN>実行委員</SPAN>：我々の文化祭におけるスローガンは！<br>
$icon$name：え，えーと・・・。<br>
$people<SPAN>実行委員</SPAN>：友情，努力，勝利である！<br>
$icon$name：（どっかのマンガかよ。）<br>
$people<SPAN>実行委員</SPAN>：したがって我々が敵とみなすのは！<br>
$icon$name：・・・。<br>
$people<SPAN>実行委員</SPAN>：恋愛，無力，敗北である！<br>
$icon$name：（恋愛だめなのー？！）<br>
$people<SPAN>実行委員</SPAN>：我々が目指すものは！<br>
$icon$name：・・・。<br>
$people<SPAN>実行委員</SPAN>：権力，名誉，オチである！<br>
$icon$name：・・・。<br>
$people<SPAN>実行委員</SPAN>：その調子で何かスローガンを掲げるのだ。<br>
$icon$name：え，えーと・・・。<br>
$people<SPAN>実行委員</SPAN>：・・・。<br>
$icon$name：じゃあ・・・我々が，さん付けで呼ぶものは！<br>
$people<SPAN>実行委員</SPAN>：うむ。<br>
$icon$name：こっくり！花子！貞子！<br>
$people<SPAN>実行委員</SPAN>：・・・。（貞子って，さん付けたか？）<br><br>
実行委員会に入れるようになった。<br>
STR
	$disp.="$TRE$TBE";
}

sub story
{
	OutError('現在の状態ではこのコマンドを実行できません');
}


