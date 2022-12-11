import os

# Path to the directory you want to search
dir_path = "/path/to/directory"
# The word you want to search for
search_word = input("Search for a word: ")

# Recursively search for the given word in the files of the given directory
for root, dirs, files in os.walk(dir_path):
    for f in files:
        file_path = os.path.join(root, f)
        with open(file_path) as file:
            # Check if the search word is in the current file
            if search_word in file.read():
                print(f"Found '{search_word}' in file {file_path}")
