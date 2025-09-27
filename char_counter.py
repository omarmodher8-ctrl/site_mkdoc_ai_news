import sys

def custom_char_length(text):
    length = 0
    for char in text:
        if ord(char) < 128:  # ASCII characters
            length += 0.5
        else:  # Non-ASCII characters (including full-width Japanese characters)
            length += 1
    return length

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python char_counter.py \"<text_to_count>\"")
    else:
        text = sys.argv[1]
        calculated_length = custom_char_length(text)
        print(calculated_length)
