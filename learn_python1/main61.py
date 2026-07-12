#  writing files (.txt,.json,.csv) using python.

# txt_data="i like apple"
# file_path = "C:/Users/acer/Desktop/output61.txt"

# try:
#     with open(file_path,"a") as file:   # 'w' to write a file . 'x' we write/create a file if it doesnot already exist . 'a' to appenddata any data  to that file.
#         file.write("\n" +txt_data)
#         print(f"txt file {file_path} was created")
# except FileExistsError:
#     print("that file already exist")


# lets work with collection

# employees=["hero","zero","siko","biko"]
# file_path = "C:/Users/acer/Desktop/output61.txt"

# try:
#     with open(file_path,"a") as file:   # 'w' to write a file . 'x' we write/create a file if it doesnot already exist . 'a' to appenddata any data  to that file.
#         for employee in employees:#  in order for use to write each item within a list we need to iterate over it using loop.
#             file.write(employee + "\n")
#         print(f"txt file {file_path} was created")
# except FileExistsError:
#     print("that file already exist")


# outputing .json file =json file is made of key:value pairs

# import json

# employees={
#     "name":"hero",
#     "age":30,
#     "job":"cook"
# }
# file_path = "C:/Users/acer/Desktop/out61.json"

# try:
#     with open(file_path,"w") as file:   # 'w' to write a file . 'x' we write/create a file if it doesnot already exist . 'a' to appenddata, any data will append to that file.
#       json.dump(employees,file)         # use dump method: will convert our dictionary to json string to output it
#       print(f"json file {file_path} was created")
# except FileExistsError:
#     print("that file already exist")



# working with csv(comma seperated value)

import csv

employees=[["name","age","job"],
           ["hero",20,"cook"],
           ["sandy",23,"unemployee"]
           ]
file_path = "C:/Users/acer/Desktop/outcsv61.csv"

try:
    with open(file_path,"w",newline="") as file:   # 'w' to write a file . 'x' we write/create a file if it doesnot already exist . 'a' to appenddata, any data will append to that file.
      writer=csv.writer(file)           # writer is  an object provide methods for writing data to a csc file.
      for row in employees:
         writer.writerow(row)         # writer method gives use the new line after each row so to prevent use newlint=""
      print(f"csv file  {file_path} is created")
except FileExistsError:
    print("that file already exist")