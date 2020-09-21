# flask_sample_app

# 前提条件

- pyenvとpipenvの環境構築
- pyenvでpython3.7をインストールして利用できる状態にしていること

# 環境構築

- pipenv install Flaskをルートディレクトリ配下で実行するとpipfileに記載している関連モジュールがインストールされる

# 実行方法

- pipenv shell で仮想環境を起動
- 各ディレクトリに移動し、python run.pyあるいはpython hello.pyを実施する
- 右記へアクセス（言わずもがな、Chromeがおすすめです。）　http://127.0.0.1:8888/

# 各フォルダの説明

- basicauth
  - basic認証を求めるモジュール
- hello
  - Hello WorldをResponseするだけ
- hello2
  - Templateエンジンを使ってHTMLをレンダリングして画面表示（helloをちょっとだけ肉付け）
- hello3
  - static ファイルを利用してcssとjqueryを活用して少しリッチな画面表示(hello2をちょっとだけ肉付け)
- json
  - json値をResponse
