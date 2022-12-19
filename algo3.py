import os

dir_path = input("Enter the path to the directory: ")
search_word = input("Search for a word: ")
found = False

for root, dirs, files in os.walk(dir_path):
    for f in files:
        file_path = os.path.join(root, f)
        with open(file_path) as file:
            if search_word in file.read():
                print(f"Found '{search_word}' in file {file_path}")
                found = True
                break
    if found:
        break

if not found:
    print(f"Could't find '{search_word}' in any files")
