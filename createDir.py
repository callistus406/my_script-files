#! /usr/bin/python3

import os,sys


def action(dir_name):
    full_path = os.getcwd()+"/"+dir_name
#    return full_path
    if(os.path.isdir(full_path)):
        return "Folder already Exist!"
    else:
        os.mkdir(full_path)
        return "Directory created"



if(len(sys.argv)==1):
    print("Pass in an argument")
elif(sys.argv[1]==None  or sys.argv[1].strip()==""):
    print( "Enter a valid name")
else:

    result  = action(sys.argv[1])
    print(result)
