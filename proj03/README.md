## venv

プロジェクト毎に独立したPython環境を用意

- 同プロジェクト専用のPython環境を用意
```
$ python3 -m venv venv
```

- 用意したPython環境を適用
```
$ source venv/bin/activate
```

- bottle をインストール
```
(venv) ~~~~ $ pip install requests bottle

(venv) ~~~~ $ pip freeze
bottle==0.12.13
certifi==2018.4.16
chardet==3.0.4
idna==2.7
pkg-resources==0.0.0
requests==2.19.1
urllib3==1.23
```

- 用意したPython環境の適用解除
```
(venv) ~~~~ $ deactivate
```

- setup.py に従ってインストール
```
(venv) ~~~~ $ pip install -e .
Obtaining file:///work/src/python/github.com/sky0621/study-python-professional/proj03
Collecting Flask (from norilog==1.0.0)
  Using cached https://files.pythonhosted.org/packages/7f/e7/08578774ed4536d3242b14dacb4696386634607af824ea997202cd0edb4b/Flask-1.0.2-py2.py3-none-any.whl
Collecting itsdangerous>=0.24 (from Flask->norilog==1.0.0)
  Using cached https://files.pythonhosted.org/packages/dc/b4/a60bcdba945c00f6d608d8975131ab3f25b22f2bcfe1dab221165194b2d4/itsdangerous-0.24.tar.gz
　　　・
　　　・
　　　・
Successfully installed Flask-1.0.2 Jinja2-2.10 MarkupSafe-1.0 Werkzeug-0.14.1 click-6.7 itsdangerous-0.24 norilog
```

- ソース配布パッケージを作る
```
(venv) ~~~~ $ python setup.py sdist
running sdist
running egg_info
　　　・
　　　・
　　　・
Creating tar archive
removing 'norilog-1.0.0' (and everything under it)
```

- wheel パッケージを作る
```
(venv) ~~~~ $ python setup.py bdist_wheel
running bdist_wheel
running build
　　　・
　　　・
　　　・
adding 'norilog-1.0.0.dist-info/RECORD'
removing build/bdist.linux-x86_64/wheel
```
