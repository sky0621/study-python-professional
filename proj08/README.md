# モジュール分割設計と単体テスト

## ★セットアップ

- 同プロジェクト専用のPython環境を用意
```
$ python3 -m venv venv
```

- 用意したPython環境を適用
```
$ source venv/bin/activate
```

## ★アーキテクチャ参考例
<pre>
ユーザ -> [View] -> [ApplicationModel] -> [ServiceGateway] -> 外部サービス
                                          -> [DomainModel] -> データベース
                    -> [DomainModel] -> データベース
</pre>

#### ■View

リクエストを受け取り、レスポンスを返す。 

Controller(※Webフレームワークが担う？)からリクエストパラメータを取得する。

パラメータチェックを行う。

ApplicationModelを呼び出す。

呼び出し結果をユーザに表示可能なHTML形式に変換してレスポンスボディを作成する。

#### ■DomainModel

永続化オブジェクト。RDBMSとやりとり。

※SQLAlchemy等のO/Rマッパーを用いる。

#### ■ApplicationModel

アプリの一時的な状態を保持（※１リクエスト間か複数画面またぎ）する。

ロジックをあまり持たず、処理のフローを担当するため、依存モジュールが多くなる。

#### ■ServiceGateway

外部システムのラッパー。外部システムへの依存コードを閉じ込める。

## ★パッケージ参考例
<pre>
project/
  +-- __init__.py ... WSGIアプリのエントリーポイント等、起動に必要な処理を書く。その他、modelの初期化等。
  +-- views.py
  +-- models.py
  +-- services/
        +-- __init__.py
        +-- twitter.py
        +-- twitpic.py
  +-- utils.py
  +-- templates/ ... HTMLテンプレート
  +-- tests/
        +-- __init__.py
        +-- test_models.py
        +-- test_views.py
        +-- test_services.py
        +-- test_utils.py
</pre>
