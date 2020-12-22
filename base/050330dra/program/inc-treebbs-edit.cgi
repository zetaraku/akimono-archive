# 掲示板書き込み処理 2003/09/25 由來

if ($Q{message} eq "" || $Q{message} =~ /^(\x81\x40|\s|<br>)+$/)
	{ OutError("メッセージが入力されていません。"); }
if ($Q{sub} eq "" || $Q{sub} =~ /^(\x81\x40|\s)+$/)
	{ OutError("タイトルが入力されていません。"); }

# 管理者認識
$Q{name}=$adminname,$Q{town}="" 	if ($MASTER_USER);

# ログファイル読み込み
open(IN,$datafile);
@lines = <IN>;
close(IN);

# 記事no.
$top = shift(@lines);
($count,$ip,$tim) = split(/<>/, $top);
if ($count % 9999) { $count++; } else { $count=1; }

	# 親記事
	if ($Q{no} eq 'new') {
		unshift (@lines,"$count<>no<>0<>$Q{sub}<>$Q{town}<>$Q{name}<>$Q{message}<>$NOW_TIME<>$host<>$count<>$Q{smail}<>0<>\n");
		@new = @lines;
	}
	# レス記事
	else {
		# レスのついたツリーとそうでないツリーを分割
		@new=();	# 上げられるツリー
		@tmp=();	# 残るツリー
		$flag=0;
		foreach (@lines) {
			chop;
			($no,$reno,$lx,$t,$e,$n,$m,$tm,$h,$OYA,$smail,$res) = split(/<>/);
			if ($flag == 1 && $lx2 > $lx && $OYA == $Q{oya}) {
				$flag=2;	#そのままくっつく
				push(@new,"$count<>$Q{no}<>$lx2<>$Q{sub}<>$Q{town}<>$Q{name}<>$Q{message}<>$NOW_TIME<>$host<>$Q{oya}<>$Q{smail}<>0<>\n");
			}
			if ($no == $Q{no}) {
				$res++;
			push(@new,"$no<>$reno<>$lx<>$t<>$e<>$n<>$m<>$tm<>$h<>$OYA<>$smail<>$res<>\n");
				}
			elsif ($Q{oya} == $OYA) { push(@new,"$_\n"); }
			else { push(@tmp,"$_\n"); }
				if ($no == $Q{no}) {
				$flag=1;
				$lx2 = $lx + 1;
			}
		}
		if ($flag != 2) {
			#最後にくっつく
			push(@new,"$count<>$Q{no}<>$lx2<>$Q{sub}<>$Q{town}<>$Q{name}<>$Q{message}<>$NOW_TIME<>$host<>$Q{oya}<>$Q{smail}<>0<>\n");
		}
		push(@new,@tmp);
	}
	# 最大記事数処理
	if (@new > $max) {
		foreach (0 .. $#new) {
			my($p_file) = pop(@new);
			local($no,$reno,$lx) = split(/<>/, $p_file);
			if ($#new+1 <= $max && $reno eq 'no') {
				last;
				}
		}
	}

	unshift(@new,"$count<>$addr<>$NOW_TIME<>\n");
	OpenAndCheck(GetPath($COTEMP_DIR,'treelog'));
	print OUT @new;
	close(OUT);
	CoDataCA();
	CoUnLock();

	$disp.="書き込みを完了しました。 --".GetMenuTag('treebbs','[記事一覧に戻る]');
1;