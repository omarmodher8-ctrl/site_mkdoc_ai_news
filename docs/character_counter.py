import sys

def calculate_length(text):
    length = 0
    for char in text:
        if ord(char) < 128:  # ASCII characters
            length += 0.5
        else:  # Non-ASCII characters (including full-width Japanese characters)
            length += 1
    return length

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_text = sys.argv[1]
        calculated_len = calculate_length(input_text)
        print(calculated_len)
    else:
        print("Please provide a string as an argument.")
