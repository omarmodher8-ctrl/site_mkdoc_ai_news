
def count_characters(text):
    count = 0
    for char in text:
        if ord(char) < 128:  # ASCII characters
            count += 0.5
        else:  # Non-ASCII characters (including full-width Japanese characters)
            count += 1
    return count

with open(r"G:\repogitory\site_mkdoc_ai_news\docs\temp_memo.txt", "r", encoding="utf-8") as f:
    content = f.read()

length = count_characters(content)
print(length)

