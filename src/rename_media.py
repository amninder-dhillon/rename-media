import os
import argparse
import PTN

def generate_new_name(parsed, pattern):
    try:
        return pattern.format(**parsed)
    except KeyError as e:
        print(f"Missing key {e} in parsed result: {parsed}")
        return None

def rename_item(original_path, new_name):
    directory = os.path.dirname(original_path)
    new_path = os.path.join(directory, new_name)
    if not os.path.exists(new_path):
        os.rename(original_path, new_path)
        print(f"Renamed:\n  From: {original_path}\n  To:   {new_path}\n")
    else:
        print(f"Skipped (target already exists): {new_path}")

def process_path(path, pattern):
    if os.path.isfile(path) or os.path.isdir(path):
        name = os.path.basename(path)
        parsed = PTN.parse(name)
        if not parsed:
            print(f"Failed to parse: {name}")
            return

        extension = os.path.splitext(name)[1] if os.path.isfile(path) else ""
        new_name = generate_new_name(parsed, pattern)
        if new_name:
            new_name += extension
            rename_item(path, os.path.join(os.path.dirname(path), new_name))
    else:
        print(f"Invalid path: {path}")

def process_folder(folder_path, pattern):
    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path, item)
        process_path(full_path, pattern)

def main():
    parser = argparse.ArgumentParser(description="Rename files/folders using parse-torrent-title")
    parser.add_argument("input_path", help="Path to a file, folder, or directory containing media")
    parser.add_argument("--pattern", required=True, help="Rename pattern using keys like {title}, {season}, {episode}, {year}")

    args = parser.parse_args()
    input_path = os.path.abspath(args.input_path)

    if os.path.isdir(input_path):
        process_folder(input_path, args.pattern)
    else:
        process_path(input_path, args.pattern)

if __name__ == "__main__":
    main()

