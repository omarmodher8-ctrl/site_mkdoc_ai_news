import sys

def count_chars(text):
    count = 0
    for char in text:
        if ord(char) < 128:  # ASCII
            count += 0.5
        else:
            count += 1
    return count

text = "Google Veo3を活用した動画生成が活発化し、広告自動化やXでの作品共有が相次ぐ。プロンプトの工夫や品質に関する議論もなされ、ツール連携が進んでいる。"
print(f"Text: {text}")
print(f"Length: {count_chars(text)}")