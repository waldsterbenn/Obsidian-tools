import os

folder_path = "C:/Users/ls/Documents/Obsidian/Noter/"
#folder_path = "C:/Users/ls/Documents/Obsidian/ObsidianDrinks/"

# DANGER, this will actually delete files

for dir_path, dirs, files in os.walk(folder_path):
    folder_name = os.path.basename(dir_path)
    if folder_name == "":
        folder_name = os.path.basename(os.path.dirname(dir_path))

    index_file_path = os.path.join(dir_path, f"{folder_name}.md")
    if os.path.exists(index_file_path):
        os.remove(os.path.join(dir_path, index_file_path))
