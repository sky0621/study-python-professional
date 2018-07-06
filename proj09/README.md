# Pythonパッケージの利用と開発への適用

## バージョン指定方法

### ■最新取得
<pre>
$ pip install -U colander
$ pip freeze
colander==1.4
</pre>

### ■バージョン指定して取得
<pre>
$ pip install -U colander==1.0
$ pip freeze
colander==1.0
</pre>

### ■特定バージョン未満（の最新安定版）を取得
<pre>
$ pip install -U "colander<1.0"
$ pip freeze
colander==0.9.9
</pre>

### ■特定バージョン未満（の最新版）を取得
<pre>
$ pip install -U "colander<1.0" --pre
$ pip freeze
colander==0.9.9
</pre>

### ■指定バージョンの範囲で取得
<pre>
$ pip install -U "colander>=0.9,<0.9.9"
$ pip freeze
colander==0.9.8
</pre>

## パッケージ配布形式

### ■sdist

パッケージのソース、メタデータ、ビルド方法などをアーカイブしたソース配布形式

`setup`スクリプトを読み込み、C拡張があればビルドし、必要なPythonパッケージを確認して、 `site-packages`へコピーする。

### ■wheel

ビルド済みのC拡張やPythonパッケージのみを含み、ファイルを展開するだけでインストールが完了するバイナリパッケージ。

Pythonの公式パッケージで、PEP491で定義されている。

#### wheelhouseの作成
<pre>
$ pip wheel markupsafe -w wheelhouse
$ la wheelhouse/
合計 40K
-rw-r--r-- 1 koge koge  29K  7月  6 16:17 MarkupSafe-1.0-cp36-cp36m-linux_x86_64.whl
</pre>

#### wheelhouse作成物のインストール
<pre>
$ pip install --no-index -f wheelhouse markupsafe
$ pip freeze
MarkupSafe==1.0
</pre>

## manylinux

### manylinux wheel作成

#### （１）まず、環境依存wheelを作成（※環境の準備されたDockerコンテナ使用）
<pre>
$ sudo docker pull quay.io/pypa/manylinux1_x86_64
$ sudo docker images
REPOSITORY                         TAG                 IMAGE ID            CREATED             SIZE
quay.io/pypa/manylinux1_x86_64     latest              fd11e6f53575        2 days ago          881MB
$ 
$ sudo docker run quay.io/pypa/manylinux1_x86_64 /opt/python/cp36-cp36m/bin/pip -V
pip 10.0.1 from /opt/_internal/cpython-3.6.5/lib/python3.6/site-packages/pip (python 3.6)
$ 
$ sudo docker run --rm -v $PWD/wheelhouse:/io/wheelhouse quay.io/pypa/manylinux1_x86_64 /opt/python/cp36-cp36m/bin/pip wheel -w /io/wheelhouse SQLAlchemy
Collecting SQLAlchemy
Building wheels for collected packages: SQLAlchemy
Successfully built SQLAlchemy
$ 
$ la wheelhouse/
-rw-r--r-- 1 root root 1.1M  7月  6 16:39 SQLAlchemy-1.2.9-cp36-cp36m-linux_x86_64.whl
</pre>
※ `--rm` ・・・実行後にコンテナを削除する。

※ `-v $PWD/wheelhouse:/io/wheelhouse` ・・・ホストの `wheelhouse` をコンテナ内の `/io/wheelhouse` にマウントする。

#### （２）次に、（１）で作成したwheelをmanylinux wheelに変換
<pre>
$ sudo docker run --rm -v $PWD/wheelhouse:/io/wheelhouse quay.io/pypa/manylinux1_x86_64 auditwheel repair /io/wheelhouse/SQLAlchemy-1.2.9-cp36-cp36m-linux_x86_64.whl -w /io/wheelhouse
Repairing SQLAlchemy-1.2.9-cp36-cp36m-linux_x86_64.whl
Previous filename tags: linux_x86_64
New filename tags: manylinux1_x86_64
Previous WHEEL info tags: cp36-cp36m-linux_x86_64
New WHEEL info tags: cp36-cp36m-manylinux1_x86_64

Fixed-up wheel written to /io/wheelhouse/SQLAlchemy-1.2.9-cp36-cp36m-manylinux1_x86_64.whl
$ 
$ la wheelhouse/
-rw-r--r-- 1 root root 1.1M  7月  6 16:49 SQLAlchemy-1.2.9-cp36-cp36m-manylinux1_x86_64.whl
</pre>
※ `auditwheel repair` ・・・ `wheel`を`manylinux wheel`に変換するコマンド。

## プライベートリリース

PyPI管理外（例：GitHub）のパッケージをインストール
<pre>
$ pip install https://github.com/shimizukawa/logfilter/archive/logfilter-0.9.3.zip
$ pip freeze
logfilter==0.9.3
</pre>

## 依存ライブラリのファイル化と取り込み
<pre>
$ pip freeze > requirements.txt
$ pip install -r requirements.txt
</pre>

## 本番デプロイ用に依存ライブラリファイルを修正

### ■requirements.txt
<pre>
--no-index
-f wheelhouse
-r run-requires.txt
</pre>
※ `--no-index` ・・・本番環境を想定した場合、PyPIに問い合わせる必要はないため、Indexサーバーを使わない。

※ `-f wheelhouse` ・・・ライブラリの取得元を`wheelhouse`に限定する。
