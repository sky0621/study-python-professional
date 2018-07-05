# proj07

## Sphinxインストールとクイックスタート
```
$ python3 -m venv venv

$ source venv/bin/activate

(venv) $ pip install sphinx

(venv) $ pip freeze
alabaster==0.7.11
Babel==2.6.0
　・
　・
　・
Sphinx==1.7.5
sphinxcontrib-websupport==1.1.0
urllib3==1.23

(venv) $ sphinx-quickstart -q -p SW-Project -a BeProud -v 1.0 sw-project
```

## HTML生成
```
(venv) $ make html
```