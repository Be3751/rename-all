#!/bin/bash

# 操作対象とするファイルのリストを取得
dir_path="${1}*"
target_files=`find $dir_path -type f`

# 変更後のファイル名
# 直近のディレクトリまでのパスのみを切り出し、2つ名の変数で指定されたファイル名を連結する
# target/hogehoge.png -> target/
changed_name="${1%/*.}"
echo $changed_name

# 各ファイル名を置換
for file in $target_files;
do
	echo $file
	# mv $file 
done
