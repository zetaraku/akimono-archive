# 特殊デコード 2003/09/25 由來

OutError("送信サイズが大きすぎます") if ($ENV{'CONTENT_LENGTH'} > 10240);
require $JCODE_FILE;

binmode(STDIN);
my $Boundary = <STDIN>;
$Boundary =~ s/\x0D\x0A//;
while (<STDIN>) {
	if (/^\s*Content-Disposition:/i) {
		my $Name;
		# フォームの項目名を得る
		if (/\bname="([^"]+)"/i or /\bname=([^\s:;]+)/i) {
			$Name = $1;
		}
		# ファイル名を取得
		if (/\bfilename="([^"]*)"/i or /\bfilename=([^\s:;]*)/i) {
			$FILENAME{$Name} = $1 || 'unknown';
		}
		# ヘッダ内容を読み取る
		# ヘッダの終了を示す空行を検出したらループを抜ける
		while (<STDIN>) {
			last if (not /\w/);
			if (
				/^\s*Content-Type:\s*"([^"]+)"/i
				or /^\s*Content-Type:\s*([^\s:;]+)/i
			) {
			$MIMETYPE{$Name} = $1;
			}
		}
		# データ本体を読み取る
		# データの終了を示すBoundaryを検出したらループを抜ける
		while (<STDIN>) {
			last if (/^\Q$Boundary\E/);
			$Q{$Name} .= $_;
		}
		$Q{$Name} =~s /\x0D\x0A$//; # 末尾の\r\nを取り除く
		if ($Q{$Name}) {
			# ファイルの場合
			if ($FILENAME{$Name} or $MIMETYPE{$Name}) {
				# MacBinaryを検出して削除
				if (
					$MIMETYPE{$Name}
					=~ /^application\/(x-)?macbinary$/i
				) {
				# Headerと末尾のリソースを削除
					$Q{$Name} = substr(
						$Q{$Name},
						128,
						unpack("N", substr($Q{$Name}, 83, 4))
					);
				}
			}
			# ファイル以外の場合
			else {
				&jcode::convert(\$Q{$Name}, 'sjis');
				$Q{$Name} =~ s/&/&amp;/g;
				$Q{$Name} =~ s/"/&quot;/g;
				$Q{$Name} =~ s/</&lt;/g;
				$Q{$Name} =~ s/>/&gt;/g;
				$Q{$Name} =~ s/\x0D\x0A/<br>/g;
				$Q{$Name} =~ s/\x0D/<br>/g;
				$Q{$Name} =~ s/\x0A/<br>/g;
			}
		}
	}
	# Boundaryを検出したらループを抜ける
	last if (/^\Q$Boundary--\E/);
}
	@Q{qw(nm pw ss)}=split(/!/,$Q{u},3) if exists $Q{u};
1;
