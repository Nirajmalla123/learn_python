# Read files (.txt,.json,.csv) using python

# file_path = "C:/Users/acer/Desktop/output61.txt"
# try:
#     with open(file_path,"r") as file:
#         content = file.read()
#         print(content)

# except FileNotFoundError:
#       print("that file doesnot found")
# except PermissionError:
#      print("you don't have permission to read that file")


# to read json file

# import json

# file_path = "C:/Users/acer/Desktop/out61.json"
# try:
#     with open(file_path,"r") as file:
#         content = json.load(file)
#         print(content["name"])

# except FileNotFoundError:
#       print("that file doesnot found")
# except PermissionError:
#      print("you don't have permission to read that file")

# to read csv file

import csv

file_path = "C:/Users/acer/Desktop/outcsv61.csv"
try:
    with open(file_path,"r") as file:    # with is a statement -> it wrap the block of code within a context manager and it will close a file if we open it to prevent from unexpected behaviour  
        content = csv.reader(file)
        for line in content:
             print(line[0])
except FileNotFoundError:
      print("that file doesnot found")
except PermissionError:
     print("you don't have permission to read that file")

