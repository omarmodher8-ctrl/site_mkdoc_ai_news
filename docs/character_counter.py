import sys

def count_characters(text):
    length = 0
    for char in text:
        if ord(char) < 128:  # ASCII characters
            length += 0.5
        else:  # Non-ASCII characters (including full-width)
            length += 1
    return length

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_text = sys.argv[1]
        calculated_length = count_characters(input_text)
        print(calculated_length)
    else:
        print("Usage: python character_counter.py <text>")