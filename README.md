# flask_sample_app

English 1st,Japanese 2nd.

# Prerequisites

--Construction of environment for pyenv and pipenv
--Pyenv has python3.7 installed and ready to use

# Environment

--When pipenv install Flask is executed under the root directory, the related modules described in pipfile are installed.

# Execution method

--Start virtual environment with pipenv shell
--Go to each directory and run python run.py or python hello.py
--Access to the right (Needless to say, Chrome is recommended.) Http://127.0.0.1:8888/

# Description of each folder

--basicauth
   --A module that requires basic authentication
--hello
   --Response Hello World
--hello2
   --Render HTML using Template engine and display on screen (extend hello)
--hello3
   --Slightly rich screen display using css and jquery using static files (extending hello2)
--json
   --Response the json value

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
