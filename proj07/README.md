# proj07

## Sphinxインストールとクイックスタート
```
$ python3 -m venv venv

$ source venv/bin/activate

(venv) $ pip install sphinx

(venv) $ pip freeze
alabaster==0.7.11
Babel==2.6.0
certifi==2018.4.16
chardet==3.0.4
docutils==0.14
idna==2.7
imagesize==1.0.0
Jinja2==2.10
MarkupSafe==1.0
packaging==17.1
pkg-resources==0.0.0
Pygments==2.2.0
pyparsing==2.2.0
pytz==2018.5
requests==2.19.1
six==1.11.0
snowballstemmer==1.2.1
Sphinx==1.7.5
sphinxcontrib-websupport==1.1.0
urllib3==1.23

(venv) $ sphinx-quickstart -q -p SW-Project -a BeProud -v 1.0 sw-project
```

## HTML生成
```
(venv) $ make html
```