# 宮殿設定ファイル 2003/07/19 由來

# 王様の依頼内容をカスタマイズできます。
# 「依頼文章」，「依頼するアイテム番号」，「個数」の順に記入します。
# 種類はこの要領で増やすことができます。

($msg[0],$itemno[0],$count[0])=('我が国の庭園には，もっと植物を植えたいと思っておる。',9,200);
($msg[1],$itemno[1],$count[1])=('我が国の民には，薬を買う金もない病人がおるのだ。',23,400);
($msg[2],$itemno[2],$count[2])=('我が国の民には，もっとおしゃれに気を使って欲しいと思っておる。',31,120);
($msg[3],$itemno[3],$count[3])=('隣国の魔法技術は，我が国をも上回ると聞いておる。',40,40);
($msg[4],$itemno[4],$count[4])=('我が国の民には，パンを買う金もない者もおるのだ。',57,250);
($msg[5],$itemno[5],$count[5])=('我が国の観光客によると，土産物が不足していると聞いておる。',67,60);

#記述例 ($msg[6],$itemno[6],$count[6])=('セリフ',10,100);

# 王様と面会するのに必要な点数(低いと面会を拒否)
# 初心者がいきなり使命を達成しようとすると危険。ある程度高く設定すべし。
$deny_point=20000;

1;
