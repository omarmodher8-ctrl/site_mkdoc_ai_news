# Cloudflare Pages でのMkDocsサイト公開手順

## 1. リポジトリ準備
- プロジェクトルートに `requirements.txt` を作成し、以下を記載：
  - mkdocs
  - mkdocs-material（テーマを使う場合）
  - mkdocs-awesome-pages-plugin（プラグインを使う場合）
  - その他必要なプラグイン
- 独自プラグイン（例: plugins/description_from_memo.py）がある場合は、setup.pyを用意し、パッケージとしてインストールできるようにする
- `.gitignore` に `site/` や仮想環境、ビルド生成物を追加

## 2. GitHubへpush
- すべてのファイルをコミットし、GitHubリポジトリへpush

## 3. Cloudflare Pagesで新規プロジェクト作成
- Cloudflare Pagesの管理画面で「新しいプロジェクト」を作成
- GitHubリポジトリを選択
- ビルドコマンド：`mkdocs build` または `python -m mkdocs build`
- 出力ディレクトリ：`site`

## 4. カスタムドメイン設定（任意）
- Cloudflare Pagesの「カスタムドメイン」から独自ドメインやサブドメインを追加
- value-domain等でDNS設定を行い、CNAMEまたはAレコードをCloudflare指定値に変更

## 5. デプロイ・公開
- pushや設定変更のたびに自動ビルド・公開
- ビルドエラー時はCloudflare Pagesのビルドログを確認

## 6. トラブルシューティング
- requirements.txtに必要なパッケージが全て記載されているか確認
- mkdocs.ymlやプラグインのパス・記法ミスがないか確認
- ローカルで `mkdocs build` を実行し、同じエラーが出るか確認

---
何か問題があればビルドログの詳細を確認し、必要に応じてパッケージや設定を修正してください。
