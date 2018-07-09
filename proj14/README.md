# Django

## setup
<pre>
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install django==1.11.7
$ pip install factory-boy==2.9.2
$ pip install django-debug-toolbar
$ pip freeze
Django==1.11.7
django-debug-toolbar==1.9.1
factory-boy==2.9.2
</pre>

## architecture
<pre>
[user] - request -> [[URLディスパッチャー]] -> [[View]] -> [[Model]] -> [RDB]
      <- response -                            |    -> [[Templateシステム]]
                                               |
                                           [[Cacheシステム]] -> [cache(memchache等)]
                    [[管理インタフェース]]
                    [[プロジェクト設定ファイル]]

[[プロジェクト管理用スクリプト]]
[[Django管理用スクリプト]]
</pre>

## create project

### create site
<pre>
$ django-admin startproject fssite
$ la -R fssite/
fssite/:
合計 16K
drwxr-xr-x 2 koge koge 4.0K  7月  9 15:02 fssite
-rwxr-xr-x 1 koge koge  804  7月  9 15:02 manage.py

fssite/fssite:
合計 20K
-rw-r--r-- 1 koge koge    0  7月  9 15:02 __init__.py
-rw-r--r-- 1 koge koge 3.1K  7月  9 15:02 settings.py
-rw-r--r-- 1 koge koge  763  7月  9 15:02 urls.py
-rw-r--r-- 1 koge koge  390  7月  9 15:02 wsgi.py
</pre>

### create app
<pre>
$ cd fssite/
$ python manage.py startapp refrigerator
$ la refrigerator/
合計 32K
-rw-r--r-- 1 koge koge    0  7月  9 15:05 __init__.py
-rw-r--r-- 1 koge koge   63  7月  9 15:05 admin.py
-rw-r--r-- 1 koge koge   99  7月  9 15:05 apps.py
drwxr-xr-x 2 koge koge 4.0K  7月  9 15:05 migrations
-rw-r--r-- 1 koge koge   57  7月  9 15:05 models.py
-rw-r--r-- 1 koge koge   60  7月  9 15:05 tests.py
-rw-r--r-- 1 koge koge   63  7月  9 15:05 views.py
</pre>
<pre>
$ python manage.py startapp account
$ la account/
合計 32K
-rw-r--r-- 1 koge koge    0  7月  9 17:19 __init__.py
-rw-r--r-- 1 koge koge   63  7月  9 17:19 admin.py
-rw-r--r-- 1 koge koge   89  7月  9 17:19 apps.py
drwxr-xr-x 2 koge koge 4.0K  7月  9 17:19 migrations
-rw-r--r-- 1 koge koge   57  7月  9 17:19 models.py
-rw-r--r-- 1 koge koge   60  7月  9 17:19 tests.py
-rw-r--r-- 1 koge koge   63  7月  9 17:19 views.py
</pre>

## run server
<pre>
$ python manage.py runserver
</pre>
