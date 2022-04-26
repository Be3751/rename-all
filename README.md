# rename-all
## 概要 - Overview
指定のフォルダ内にあるファイル名を一括で置換し、置換後のファイル名に識別番号を付けるためのスクリプト（現在はbashとpython3のみ対応）  
研究室内で撮影した画像ファイルの名前をいちいち手動で変えるのが面倒すぎるので、開発をして自分が使うだけじゃなく後輩や同期にも配る予定📖  
面倒なことはプログラムにやらせよう！💻

## 各ファイル・フォルダの説明 - Description
main.py：メイン処理   
target：変更対象ディレクトリ，特定の人物の画像のみを含める    
origin：元画像，変換に失敗した場合の元画像バックアップ

## 使い方 - Usage
### Python3を用いる場合 - In case of using Python3
`python3 main.py 対象ディレクトリ名 識別番号の開始位置`  
⚠️識別番号の開始を省略した場合，デフォルトで1になる

準備：
- まずは一括変更したいファイル名を付けたディレクトリを新規作成
- 次に作成したディレクトリに一括変換の対象としたいファイルを詰め込む

実行：  
`python3 main.py fhoge 4`

結果：  
`renamed './fhoge/gjaege.png' into './fhoge/fhoge_04.png'.`  
`renamed './fhoge/ba81b.png' into './fhoge/fhoge_05.png'.`  
`renamed './fhoge/pg1jr2.png' into './fhoge/fhoge_06.png'.`  
`renamed './fhoge/2jhnge.png' into './fhoge/fhoge_07.png'.`  
`renamed './fhoge/ge42dbr.png' into './fhoge/fhoge_08.png'.`
