import sys
import os
from tabulate import tabulate
import csv

def main():
    user = sys.argv
    info = []
    if checkFileName(user) in getFileList():
        with open("Task33_Pizza/"+checkFileName(user),"r") as file:
            data = csv.reader(file)
            for i in data:
                info.append(i)
        header = info[0]
        print(tabulate(info[1:],headers=header,tablefmt="grid"))
    elif checkFileName(user) == 1:
        sys.exit("Too many commands")
    elif checkFileName(user) == 2:
        sys.exit("Too small commands")
    elif checkFileName(user) not in getFileList():
        sys.exit("File not Found")

def getFileList():
    return os.listdir("Task33_Pizza")

def checkFileName(txt):
    if len(txt) > 2:
        return 1
    elif len(txt) < 2:
        return 2
    else:
        return txt[1]

if __name__ == "__main__":
    main()
