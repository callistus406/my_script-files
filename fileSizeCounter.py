#! /usr/bin/python3
import os,sys
path = os.path.abspath(sys.argv[1])
dirs = os.listdir(path)
if len(sys.argv)==1:
    print("Invalid Input: Enter directory path")
else:
    print("Directory  =>"+"Directory Size")
    print("=============================")
    for dir in dirs:
        print( dir+" => "+ str(os.path.getsize(path+"/" + dir)))
