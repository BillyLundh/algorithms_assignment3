import os

def search_directory(folder_to_search, word_to_find):
    for item in os.listdir(folder_to_search):
        # Search recursively
        if os.path.isdir(os.path.join(folder_to_search, item)):
            search_directory(os.path.join(folder_to_search, item), word_to_find)
        elif os.path.isfile(os.path.join(folder_to_search, item)):
            # Search for word
            look_for_word(os.path.join(folder_to_search, item), word_to_find)

def look_for_word(file, word_to_find):
    with open(file) as f:
        if word_to_find in f.read():
            print(f"Found '{word_to_find}' in file {file}")

while True:
    folder_to_search = input(f"Enter the path to the directory ('q' to quit): ")
    if folder_to_search == 'q':
        break
    word_to_find = input("Enter the word to search for: ")
    search_directory(folder_to_search, word_to_find)
