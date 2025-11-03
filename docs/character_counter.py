import sys

def count_characters(text):
    count = 0
    for char in text:
        # Check if the character is ASCII (0-127)
        if ord(char) < 128:
            count += 0.5
        else:
            count += 1
    return count

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                memo_content = f.read()
            length = count_characters(memo_content)
            print(length)
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Usage: python character_counter.py <file_path>")