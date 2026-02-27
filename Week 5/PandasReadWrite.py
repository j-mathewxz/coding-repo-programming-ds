# file1 = open("MyFile1.txt", "a")
# file2 = open("/Users/joshmathew/Downloads/MyFile1.txt" , "w+")
#
# file1.close()
#
#
# with open("MyFile1.txt", "r") as f:
#     data = f.read()
#     print(data)
#
#
# file3 = open("myfile.txt", "w")
# L = ["this is delhi \n","This is paris \n", "This is london \n"]
# file3.write("Hello \n")
# file3.writelines(L)
# file3.close()
# file3 = open("myfile.txt","r+")
#
# print("Output of read is")
# print(file3.read())
# print()
#
# file3.seek(0)
# print(file3.read(9))
# file3.seek(0)
# print(file3.readline((9)))
#
# file3.seek(0)
# print(file3.readlines())
# print()
# file1.close()
#
# # Python program to illustrate
# # Append vs write mode
# file1 = open("myfile.txt","w")
# L = ["This is Delhi \n","This is Paris \n","This is London \n"]
# file1.writelines(L)
# file1.close()
# # Append-adds at last
# file1 = open("myfile.txt","a")#append mode
# file1.write("Today \n")
# file1.close()
# file1 = open("myfile.txt","r")
# print("Output of Readlines after appending")
# print(file1.readlines())
# print()
# file1.close()
# # Write-Overwrites
# file1 = open("myfile.txt","w")#write mode
# file1.write("Tomorrow \n")
# file1.close()
# file1 = open("myfile.txt","r")
# print("Output of Readlines after writing")
# print(file1.readlines())
# print()
# file1.close()
# import pandas as pd
# data = pd.read_csv('data.csv')
# # df.to_csv('data.csv')
# # df = pd.read_csv('data.csv', index_col=0)
# # df.to_excel('data.xlsx')
# # df = pd.read_excel('data.xlsx', index_col=0)
# df = pd.DataFrame(data=data).T
# df.to_json('data-columns.json')
#
# df.to_json('data-index.json', orient='index')

# try:
# df = pd.read_csv("missing_file.csv")
# except FileNotFoundError:
# print("File does not exist.")

from pathlib import Path
import pandas as pd
file_path = Path("data") / "data.csv"
df = pd.read_csv(file_path)
print(df)

