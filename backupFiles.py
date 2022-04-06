import os
import shutil

source = input("Enter source folder name")
destiantion = input("Enter destiantion folder name")

source = source+"/"
destiantion = destiantion+"/"

list_of_files = os.listdir(source)

for file in list_of_files:
    shutil.copy((source+file), destiantion)


