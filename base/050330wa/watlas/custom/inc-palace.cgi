# 宮殿設定ファイル 2004/02/28 由來
# ワールドアトラス版

# 王様の依頼内容をカスタマイズできます。
# 「依頼文章」，「依頼するアイテム番号」，「個数」の順に記入します。
# 種類はこの要領で増やすことができます。

($msg[0],$itemno[0],$count[0])=('王室所有の船が台風で破損してしまい，修復のための材料が必要じゃ。',15,100);
($msg[1],$itemno[1],$count[1])=('王室所有の船が台風で破損してしまい，修復のための材料が必要じゃ。',16,100);
($msg[2],$itemno[2],$count[2])=('最近，王室の財宝を狙う盗賊が現れているようじゃ。',87,1);
($msg[3],$itemno[3],$count[3])=('我が国の民には，その日のパンも食べられない子どもがおるのじゃ。',18,1000);
($msg[4],$itemno[4],$count[4])=('我が国の民を元気付けるため，ラム酒を振る舞いたいと思っておる。',19,500);

#記述例 ($msg[5],$itemno[5],$count[5])=('セリフ',10,100);

# 王様と面会するのに必要な点数(低いと面会を拒否)
# 初心者がいきなり使命を達成しようとすると危険。ある程度高く設定すべし。
$deny_point=20000;

1;
