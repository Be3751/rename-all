# rename-all
## 概要
指定のフォルダ内にあるファイル名を一括で置換し、置換後のファイル名に識別番号を付けるためのスクリプト（現在はbashとpythonのみ対応）  
研究室内で撮影した画像ファイルの名前をいちいち手動で変えるのが面倒すぎるので、開発をして自分が使うだけじゃなく後輩や同期にも配る予定。  
面倒なことはプログラムにやらせよう！💻

## ディレクトリ構成
main.py：メイン処理   
target：変更対象ディレクトリ，特定の人物の画像のみを含める    
origin：元画像，変換に失敗した場合の元画像バックアップ

## 使い方
### Pythonを用いる場合
`python3 main.py 対象ディレクトリ名`

## 動作例
実行：  
`python3 main.py fhoge`

結果：  
`renamed './fhoge/gjaege.png' into './fhoge/fhoge_01.png'.`  
`renamed './fhoge/ba81b.png' into './fhoge/fhoge_02.png'.`  
`renamed './fhoge/pg1jr2.png' into './fhoge/fhoge_03.png'.`  
`renamed './fhoge/2jhnge.png' into './fhoge/fhoge_04.png'.`  
`renamed './fhoge/ge42dbr.png' into './fhoge/fhoge_05.png'.`
