import sys

def count_characters(text):
    count = 0
    for char in text:
        if ord(char) < 128:  # ASCII characters
            count += 0.5
        else:  # Non-ASCII characters (including full-width Japanese characters)
            count += 1
    return count

if __name__ == "__main__":
    if len(sys.argv) > 1:
        text_to_count = sys.argv[1]
        length = count_characters(text_to_count)
        print(length)
    else:
        print("Please provide a string to count.")
