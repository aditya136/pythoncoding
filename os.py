# import os 

# foldername = input("What is your python's folder name:")

# x = foldername

# os.remove(x)


# Simple Maleware

import os

files = []

for file in os.listdir():
    if file == "loop.py":
            continue
    files.append(file)

print(files)
