import os

folder_path = "C:/Users/ls/Documents/Obsidian/Noter/"
#folder_path = "C:/Users/ls/Documents/Obsidian/ObsidianDrinks/"

excluded_folders = ['.obsidian','plugins','.stfolder']

for dir_path, dirs, files in os.walk(folder_path):
    folder_name = os.path.basename(dir_path)
    if folder_name == "":
        folder_name = os.path.basename(os.path.dirname(dir_path))
    
    if any(word in dir_path for word in excluded_folders):
        continue  # Skip iteration if the folder name contains one of the excluded words
    
    index_file_path = os.path.join(dir_path, f"{folder_name}.md")
    if index_file_path == "C:/Users/ls/Documents/Obsidian/Noter/Noter.md" or index_file_path == 'C:/Users/ls/Documents/Obsidian/ObsidianDrinks/ObsidianDrinks.md':
        continue
    with open(index_file_path, 'w', encoding='utf-8') as f:
        for dir in dirs:
            f.write(f"[[{dir}]]\n")
        for file in files:
            if file.startswith('Index -'):
                os.remove(os.path.join(dir_path, file))
            else:
                if file.endswith('.md'):
                    f.write(f"[[{file}]]\n")
        f.write("\n\n#index")
