#! /usr/bin/python3

import os,sys

def count_content(path):
    count=0
    for item in path:
        count = count+1

    return count


if len(os.sys.argv) ==1:
    print("Invalid input: Enter a directory path")
elif os.sys.argv[1].strip()==None or os.sys.argv[1].strip()=="":
    print( "Enter a valid directory")
else:
    result = count_content(os.listdir(sys.argv[1]))
    print("We have ",result,"files in",os.path.basename(os.path.abspath(sys.argv[1])), "directory")
