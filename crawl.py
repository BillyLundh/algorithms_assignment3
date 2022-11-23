import os

home = os.path.expanduser("~")
print(home)

path = "/Users/billy/Desktop/hh"


# This give the head of the path
print(f"The dirname path is: {os.path.dirname(path)}")
# This gives the tail of the path
print(f"The basename path is: {os.path.basename(path)}")


search = input("Enter search: ")


for root, dir_names, file_names in os.walk(path):
    for f in file_names:
        fname = os.path.join(root, f)
        if fname.endswith('.py'):
            with open(fname) as myfile:
                line = myfile.read()
                c = line.count(search)
                if c:
                    print(f"The file name is: {fname}")
 #                   print(f"The count is: {c}")
                else:
                	print("No matches found")
