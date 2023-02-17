# access logをRedashで視覚化

## 環境構築
1. 下記コマンドを実行
    ```bash
    git clone https://github.com/ken-sayama/setup-redash-locally.git
    cd setup-redash-locally
    docker compose run --rm server create_db
    docker compose up
    ```
1. http://localhost:8080 を開く

## CSVの取り込み
1. Connect a Data Sourceリンクをクリック
1. CSVを選択
1. 任意の名前を入力

## データの視覚化
1. Create / New Queryをクリック
1. プルダウンからData Sourceを選択
1. [ドロップボックス](https://www.dropbox.com/)にcsvをアップロード
1. 入力欄にhttps://dl.dropboxusercontent.com/s/識別子/ファイル名.csv?dl=0を入力
1. Executeボタンをクリック
1. Add Visualizationをクリック

## Data Sourceで取り込んだCSVを読み込む方法
1. Connect a Data Sourceリンクをクリック
1. Query Resultsを選択
1. 任意の名前を入力

## 参考サイト

## アクセスログをCSVに変換
- [Convert Apache/Nginx Unified Log Format to CSV](https://gist.github.com/joswr1ght/c2e08f520933bb36c0b19aa0dcb6a173)
- [apache/nginxのアクセスログをtsv形式に変換する | akamist blog](https://akamist.com/blog/archives/3486)
- [Python でcsv出力したら一行空く件 - Qiita](https://qiita.com/ryokurta256/items/defc553f5165c88eac95)

## Redash構築
- [Redashを手軽にローカルに構築する](https://zenn.dev/kenny/articles/c6d7504f4837a3)
- [RedashでCSVファイルを読み込ませる(インポートする) - Qiita](https://qiita.com/D_eng/items/cedb8e6d3bccc2207b61)
- [CSV data source error - Support / Self Hosted Redash Support - Redash Discourse](https://discuss.redash.io/t/csv-data-source-error/9409)

## Markdown
- [Markdownで番号付きリスト内にコードを入れる | cloud.config Tech Blog](https://tech-blog.cloud-config.jp/2019-07-18-useing-code-for-numberedlist-with-markdown)

## グラフを順番に並べる
- [How to order by in a chart? - Redash Discourse](https://discuss.redash.io/t/how-to-order-by-in-a-chart/1668)
