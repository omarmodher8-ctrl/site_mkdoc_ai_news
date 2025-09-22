import sys

def count_characters(text):
    count = 0
    for char in text:
        if '!' <= char <= '~' or ' ' == char:  # ASCII characters (printable + space)
            count += 0.5
        else:  # Non-ASCII characters (including full-width, Japanese, etc.)
            count += 1
    return count

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_text = sys.argv[1]
        length = count_characters(input_text)
        print(length)
    else:
        print("Please provide a string to count.")