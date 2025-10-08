def count_memo_characters(text):
    count = 0
    for char in text:
        if ord(char) < 128:  # ASCII characters
            count += 0.5
        else:  # Non-ASCII characters (including full-width Japanese characters)
            count += 1
    return count

summary = "Google Veo3がGeminiアプリで利用可能に。テキストから高品質動画を生成し、ASMR、短編映画、広告等で活用。Sora 2と比較され、GitHubで再現プロジェクトも。"
print(count_memo_characters(summary))
