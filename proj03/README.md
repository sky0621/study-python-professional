## venv

プロジェクト毎に独立したPython環境を用意

```
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
```

setup.py 作成後
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