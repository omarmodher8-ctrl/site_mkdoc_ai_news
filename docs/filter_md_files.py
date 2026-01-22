
import os
import sys

def filter_md_files():
    """
    Finds all .md files in the current working directory and its subdirectories that do not have a corresponding .memo file.
    Returns a list of absolute paths to these .md files.
    """
    base_dir = os.getcwd()
    target_md_files = []
    for root, _, files in os.walk(base_dir):
        # Exclude .venv directory
        if '.venv' in root:
            continue
        for file in files:
            if file.endswith(".md"):
                md_path = os.path.join(root, file)
                memo_path = os.path.join(root, file.replace(".md", ".memo"))
                if not os.path.exists(memo_path):
                    target_md_files.append(md_path)
    return target_md_files

if __name__ == "__main__":
    output_file = os.path.join(os.getcwd(), "filtered_md_files.txt")
    files_to_process = filter_md_files()
    with open(output_file, "w", encoding="utf-8") as f:
        for md_file in files_to_process:
            f.write(md_file + "\n")
    print(f"Filtered MD files written to: {output_file}")
