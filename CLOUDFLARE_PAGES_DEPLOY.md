# Cloudflare Pages での MkDocs サイト公開手順

## 1. リポジトリ準備
- プロジェクトルートにある `requirements.txt` を Cloudflare のビルド環境で利用するため、以下のパッケージを記載しています。
  - mkdocs
  - mkdocs-material（Material テーマを利用するため）
  - mkdocs-awesome-pages-plugin（ページ並び制御に使用）
  - mkdocs-macros-plugin（トップページのカスタムマクロで使用）
- 独自プラグイン `plugins/description_from_memo.py` を Cloudflare でも使えるようにするため、`setup.py` でパッケージ化し `pip install -e .` で登録できる構成にしています。
- `.gitignore` に `site/` を追加し、ローカルビルド成果物をコミットしないようにしています。

## 2. GitHub へ push
- すべての変更をコミットし、Cloudflare Pages と連携している GitHub リポジトリへ push します。

## 3. Cloudflare Pages で新規プロジェクト作成
- Cloudflare Pages の管理画面で「新しいプロジェクト」を作成し、対象の GitHub リポジトリを選択します。
- ビルドコマンド: `mkdocs build`（`python -m mkdocs build` でも可）
- 出力ディレクトリ: `site`

## 4. カスタムドメイン設定（任意）
- Cloudflare Pages の「カスタムドメイン」から独自ドメイン / サブドメインを追加します。
- value-domain など DNS プロバイダ側で CNAME もしくは A レコードを Cloudflare 指定値に向けるよう変更します。

## 5. デプロイ / 公開
- push された内容に応じて自動ビルド・デプロイが実行されます。
- ビルドエラーが発生した場合は Cloudflare Pages のビルドログを確認します。

## 6. トラブルシューティング
- `requirements.txt` に必要なパッケージが揃っているか確認する。
- `mkdocs.yml` に記載したプラグイン・テーマのパスが正しいか確認する。
- ローカルで `mkdocs build` を実行し、同じエラーが再現しないか確認する。
- `.memo` や YAML フロントマターの `date` が欠けているとトップページの一覧に表示されないため、必要に応じて追記する。

## 7. ローカル開発の補助スクリプト
- `mkdocs_serve.ps1`: 仮想環境 `.venv` を有効化した上で `mkdocs serve --dev-addr 127.0.0.1:8000` を実行する PowerShell スクリプト。
- `mkdocs_restart.ps1`: 指定ポートで稼働中の `python.exe` を停止し、`mkdocs serve` を再起動する PowerShell スクリプト（デフォルトは 6283 番ポート）。
- Cloudflare へのデプロイ前に、ローカルでこれらスクリプトを実行して表示確認を行うと安全です。
