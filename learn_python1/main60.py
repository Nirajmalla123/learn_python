# python file detection
  # for file detection we can either use relative file path ( folder/filename) or absolute file path (c:/users/brcode/desktop/test.txt)

import os


file_path="test60.txt"         #  relative file path

if os.path.exists(file_path):
    print(f"the location '{file_path}' exists")
else:
    print("doesnot exist")


file_path1="C:/Users/acer/Desktop/test.txt"         #  absolute file path

if os.path.exists(file_path1):
    print(f"the location '{file_path1}' exists")
    if os.path.isfile(file_path1):
        print("that is a file")
    elif os.path.isdir(file_path1):
        print("that is a directory")
else:
    print("doesnot exist")
