# rename-all
## 概要
指定のフォルダ内にあるファイル名を一括で置換し、置換後のファイル名に識別番号を付けるためのシェルスクリプト  
研究室内で撮影した画像ファイルの名前をいちいち手動で変えるのが面倒すぎるので、開発をして自分が使うだけじゃなく後輩や同期にも配る予定。  
面倒なことはプログラムにやらせよう！💻

## ディレクトリ構成
main.*：メイン処理   
target：変更対象ディレクトリ，特定の人物の画像のみを含める    
origin：元画像，変換に失敗した場合の元画像バックアップ

## 使い方
### Pythonを用いる場合
`python3 main.py 対象ディレクトリ 変換ファイル名`

## 動作例
実行：  
`python3 main.py temp msonobe`

結果：  
`renamed './target/piyo_05.png' into './target/hoge_01.png'.`  
`renamed './target/piyo_04.png' into './target/hoge_02.png'.`  
`renamed './target/piyo_03.png' into './target/hoge_03.png'.`  
`renamed './target/piyo_02.png' into './target/hoge_04.png'.`  
`renamed './target/piyo_01.png' into './target/hoge_05.png'.`
