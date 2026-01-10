# https://ai-news.komiyamma.net

[![GitHub release](https://img.shields.io/github/v/release/komiyamma/site_mkdoc_ai_news)](https://github.com/komiyamma/site_mkdoc_ai_news/releases)

AIが生成したニュース記事を公開するための技術検証用ウェブサイトです。

このリポジトリは、[MkDocs](https://www.mkdocs.org/) をベースに、Cloudflare Pagesでの運用に特化したカスタム機能を実験的に開発・導入する場として利用しています。

## 主な技術的特徴

- **動的なページ管理**: `mkdocs-awesome-pages-plugin` と連携し、Pythonスクリプト (`hooks.py`, `update_root_pages.py`) を使ってビルド時にナビゲーション (`.pages`) を自動生成します。
- **カスタムプラグイン**: `plugins/` ディレクトリに独自のMkDocsプラグインを配置し、サイトの機能を拡張しています。
- **Cloudflare Pages連携**: Cloudflare Pagesの自動デプロイを前提とした設定やスクリプトが含まれています。詳細は `CLOUDFLARE_PAGES_DEPLOY.md` を参照してください。

## セットアップ

ローカル環境でサイトを立ち上げるには、以下の手順を実行します。

```bash
# 依存パッケージのインストール
pip install -r requirements.txt

# ローカルプラグインのインストール
pip install -e .
```

セットアップ後、次のコマンドで開発サーバーを起動できます。

```bash
mkdocs serve
```

PowerShell環境向けに、仮想環境の有効化とサーバー起動をまとめたスクリプトも用意しています (`mkdocs_serve.ps1`)。

## 記事の追加・運用方法

記事の作成やサイトの運用に関する詳細な手順は、以下のマニュアルを参照してください。

- **[運用マニュアル (MANUAL.md)](MANUAL.md)**