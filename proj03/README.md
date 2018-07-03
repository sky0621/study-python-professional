## venv

プロジェクト毎に独立したPython環境を用意

$ python3 -m venv venv

$ source venv/bin/activate

(venv) ~~~~ $ pip install requests bottle

(venv) ~~~~ $ pip freeze
bottle==0.12.13
certifi==2018.4.16
chardet==3.0.4
idna==2.7
pkg-resources==0.0.0
requests==2.19.1
urllib3==1.23

(venv) ~~~~ $ deactivate
