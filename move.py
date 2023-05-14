import os
import shutil

fromdir = "C:/Users/ASUS/Downloads/Pic"
todir = "C:/Users/ASUS/Desktop/Images"
listoffiles = os.listdir(fromdir)
print(listoffiles)

for file in listoffiles:
    name,ext = os.path.splitext(file)
   # print(name)
   # print(ext)
    if ext== "":
        continue
    if ext in [".gif",".png",".jpg",".jpeg",".jfif"]:
        path1=fromdir + "/" + file
        path2=todir + "/" + "imagefiles"
        path3=todir + "/" + "imagefiles" + "/" + file
        if os.path.exists(path2):
            print("moving"+file+"..")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving"+file+"..")
            shutil.move(path1,path3)
