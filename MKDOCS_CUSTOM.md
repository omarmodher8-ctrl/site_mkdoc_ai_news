# MKDocs カスタマイズ一覧

このドキュメントでは、標準の MkDocs から追加・変更しているポイントをまとめています。新しい変更を加えた際はここに追記してください。

## 設定ファイル (`mkdocs.yml`)
- テーマ: `material`、`overrides/main.html` を指定してヘッダーメタタグや構造化データをカスタマイズ。
- プラグイン:
  - `search`（日本語/英語両対応）
  - `macros`（独自マクロを読み込む。`include_dir: macros`、`modules: [macros.home]`）
  - `description_from_memo`（自作プラグイン。`.memo` の内容をページ description に適用）
  - `awesome-pages`（`.pages` による並び順制御）
- `site_url` や `extra` に SNS 情報 / デフォルト OGP 画像を設定。

## テンプレート (`overrides/main.html`)
- `<meta>` や構造化データ（JSON-LD）をページ情報と `extra` の設定から生成。
- 日付（`page.meta.date`）があれば見出し直下に表示するスタイルとスクリプトを組み込み。

## 独自マクロ (`macros/home.py`)
- `latest_pages(limit)` : 最新記事の簡易一覧を生成。
- `home_sections(per_category, max_categories)` : カテゴリ別に最新記事を整形し、トップページの本文で使用。
- `.memo`・`date`・YAML 前書きなどを解析してタイトルや概要を補完。

## 自作プラグイン (`plugins/description_from_memo.py`)
- 各 `.md` に隣接する `.memo` ファイルを読み込み、`page.meta['description']` を自動設定。
- 拡張パッケージとして `setup.py` でインストール可能な形に整備。

## ドキュメント構造
- 各記事は `.md` と `.memo` のペアで管理し、`.pages` でディレクトリごとの並びを制御。
- Markdown の先頭で `date`（必須）や `image`、`author` などのフロントマターを定義。
- `.memo` はトップページや OGP 用の要約として使用。

## 補助スクリプト
- `mkdocs_serve.ps1` : 仮想環境を有効化しつつ `mkdocs serve --dev-addr 127.0.0.1:8000` を実行。
- `mkdocs_restart.ps1` : 既存の `mkdocs serve` プロセスを停止し、指定ポートで再起動。

## 依存パッケージ (`requirements.txt`)
- `mkdocs`
- `mkdocs-material`
- `mkdocs-awesome-pages-plugin`
- `mkdocs-macros-plugin`

## その他
- `.gitignore` で `site/`（ビルド成果物）を除外。
- `CLOUDFLARE_PAGES_DEPLOY.md` にデプロイ手順、`MANUAL.md` に運用ルールを整備。

これらの内容を参考に、新しいカスタマイズを行った際は本書を更新してください。
