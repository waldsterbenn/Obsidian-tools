import os
import glob
import pathlib

# Specify the folder path and the text to add
folder_path = "C:/Users/ls/Documents/Obsidian/Noter/Podcast notes/"

# Loop through all .md files in the folder and its subfolders
for file in glob.glob(os.path.join(folder_path, '**/*.md'), recursive=True):
    filename = os.path.basename(file)
    podname = ''.join(filter(str.isalpha, filename.split('-')
                      [0].strip().replace('  ', ''))).lower()

    with open(file, 'r') as f:
        file_contents = f.read()

    if '# Tags' not in file_contents:
        print(f"Adding tags section to file: {filename}")
        with open(file, 'a', encoding='utf-8') as f:
            f.writelines(["\n\n# Tags",
                          "\n#podcast",
                         f"\n#podcast-{podname}\n"])
