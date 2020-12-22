# 個別ユーザー管理 2005/03/30 由來

require $JCODE_FILE;
Lock();
DataRead();
CheckUserPass();
OutError('') if !$MASTER_USER || $USER ne 'soldoutadmin';

OutError('ユーザが見つかりません') if !defined($name2idx{$Q{user}});
my $DT=$DT[$name2idx{$Q{user}}];

$Q{comment}="【".jcode::sjis($Q{comment})."】" if $Q{comment} ne '';

#重複登録自動アクセス制限の個別対応
if($Q{nocheckip})
{
	$disp.='重複登録チェック対象外としました',$DT->{nocheckip}=1 if $Q{nocheckip} eq 'nocheck';
	$disp.='重複登録チェック対象としました',$DT->{nocheckip}='' if $Q{nocheckip} eq 'check';
}

#アクセス制限制御
if($Q{blocklogin})
{
	$Q{blocklogin}=jcode::sjis($Q{blocklogin});
	if($Q{blocklogin} eq 'off')
	{
		$disp.='アクセス制限を解除しました';
		$DT->{blocklogin}='';
		$DT->{lastlogin}=$NOW_TIME;
	}
	elsif($Q{blocklogin} eq 'stop')
	{
		$disp.='経営休止に設定しました['.$Q{blocklogin}.']';
		$DT->{blocklogin}=$Q{blocklogin};
	}
	elsif($Q{blocklogin} ne '')
	{
		$disp.='アクセス制限をしました['.$Q{blocklogin}.']';
		$DT->{blocklogin}=$Q{blocklogin};
	}
}

#追放
if($Q{closeshop} eq 'closeshop')
{
	CloseShop($DT->{id},'追放');
	PushLog(1,0,"$Q{comment}$DT->{shopname}は追放されました。") if (!$Q{log});

	$disp.="追放完了";
	$DTblockip=$DT->{remoteaddr};
}

#賞品授与(デバッグにも使用できます)
if($Q{senditem})
{
	my $itemno=$Q{senditem};
	my $ITEM=$ITEM[$itemno];
	my $itemcount=$Q{count};
	$itemcount+=$DT->{item}->[$itemno-1];
	$itemcount=$ITEM->{limit} if $itemcount>$ITEM[$itemno]->{limit};
	$DT->{item}->[$itemno-1]=$itemcount;
	
	PushLog(2,0,"$Q{comment}$DT->{shopname}に$ITEM->{name}が贈られました。") if $Q{comment};
	$disp.="$ITEM->{name} $Q{count}$ITEM->{scale} 賞品授与完了";
}

#賞金授与(デバッグにも使用できます)
if($Q{sendmoney})
{
	$DT->{money}+=$Q{sendmoney};
	#$DT->{saletoday}+=$Q{sendmoney};
	
	PushLog(2,0,"$Q{comment}$DT->{shopname}に賞金が贈られました。") if $Q{comment};
	$disp.=GetMoneyString($Q{sendmoney})." 賞金授与完了";
}

#持ち時間授与(デバッグにも使用できます)
if($Q{sendtime})
{
	$disp.=$Q{sendtime}."時間 持ち時間授与完了";
	$Q{sendtime}=$Q{sendtime} * 3600;
	$DT->{time}-=$Q{sendtime};
	
	PushLog(2,0,"$Q{comment}$DT->{shopname}に「".GetTime2HMS($Q{sendtime})."」が贈られました。") if $Q{comment};
}

#爵位授与(デバッグにも使用できます)
if($Q{senddig})
{
	$disp.=$Q{senddig}."ポイント 爵位経験値授与完了";
	$DT->{dignity}+=$Q{senddig};
	
	PushLog(2,0,"$Q{comment}$DT->{shopname}に爵位経験値".($Q{senddig}+0)."ポイントが贈られました。") if $Q{comment};
}

RenewLog();
DataWrite();
DataCommitOrAbort();
UnLock();

$disp="行いたい処理とそのパラメータを正しく選択/記述してください" if $disp eq '';
$disp.=" <-- $DT->{shopname} [$DT->{name}] $Q{comment}";

$NOMENU=1;
$Q{bk}="none";
OutSkin();
1;
