#! /usr/bin/python3


# create a script that counts the number of files in a given directory


#step1: get input from user
#step2:  validate input
#step3: check if directory exists
#step4: count the content
#step5: print output

import os, sys
if len(sys.argv) == 1:
    print("enter an argument")

elif sys.argv[1]==None or sys.argv[1] == "" :
    print("the input is invalid")
else:
    if(os.path.exists(sys.argv[1])):
        count = 0
        for file in os.listdir(os.path.abspath(sys.argv[1])):
            count = count+1
        print("We have:",count,"files in",os.path.abspath(sys.argv[1]))

    else:
        print("Invalid path")
