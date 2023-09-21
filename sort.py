import os, sys, shutil


if len(sys.argv) == 1:
    print("Enter an argument")
else:
    if  os.path.exists( sys.argv[1]):
        #step1
        src = sys.argv[1]
        #step2
        for res in os.listdir(src):

            if os.path.isfile(res):
                fileName= res.split(".")
                #step3
                ext=fileName[-1]
                os.mkdir(os.path.join(os.getcwd(),ext))

               # print(ext)
                shutil.move(os.path.join(os.getcwd(),res),os.path.join(os.getcwd(),ext))
                print("===========Files successfully sorted")
            else:
                print("is a directory")
    else:
        print("File does not exist")