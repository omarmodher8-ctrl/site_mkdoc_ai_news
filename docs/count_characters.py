import sys

def count_characters(text):
    count = 0
    for char in text:
        if ord(char) < 128:  # ASCII characters
            count += 0.5
        else:  # Non-ASCII characters
            count += 1
    return count

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_text = sys.argv[1]
        length = count_characters(input_text)
        print(length)
    else:
        print("Usage: python count_characters.py \"your text\"")
