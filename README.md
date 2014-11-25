make_crapmp3
============

概要
------------
python3専用  
適当なビット列のノイズmp3を作成します。  
フレームの出力がかなり適当なので、再生プレーヤーによっては正常に再生されない可能性があります。  
(winamp5.666にて再生確認)

コマンドライン引数
------------
* -o   : 出力先を指定。省略可(省略時はカレントへ出力)
* -dic : 単語を列挙したtxtファイル。この中から無作為抽出してファイル名を決める。省略可(省略した場合はcrap.mp3)
* -c   : ファイル数を指定。省略可。
指定した場合、ファイル名でディレクトリを作成し、連番.ファイル名.mp3を作成する(01.crap.mp3等)

使用例
------------
python make_crapmp3.py -dic testdic.txt -c 10

