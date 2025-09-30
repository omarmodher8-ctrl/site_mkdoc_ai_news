import sys
import os

def filter_md_files(md_files_path, memo_files_path):
    with open(md_files_path, 'r') as f:
        md_files = f.read().splitlines()
    with open(memo_files_path, 'r') as f:
        memo_files = f.read().splitlines()

    to_process = []
    for md_file in md_files:
        if not md_file.strip():
            continue
        
        # Skip index.md and my_command.md
        if "index.md" in md_file or "my_command.md" in md_file:
            continue

        memo_file = md_file.replace(".md", ".memo")
        if memo_file not in memo_files:
            to_process.append(md_file)
    return "\n".join(to_process)

if __name__ == "__main__":
    md_files_path = sys.argv[1]
    memo_files_path = sys.argv[2]
    result = filter_md_files(md_files_path, memo_files_path)
    print(result)