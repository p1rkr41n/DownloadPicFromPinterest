from os import walk
from typing import ContextManager, Counter
import PIL
from PIL import Image
from getLinkPinFromName import getlink
from getPicFromLink import getPic
import os
#This code can download all Photos with name file in Pinterest
# This code return num of deleted file
def fix(folder):
    directory= os.getcwd()+ folder
    _, _, filenames = next(walk(str(directory)))
    len(filenames)
    count =0
    fixName =[]
    for name in filenames:
        pathfile= directory + name
        #pathfile=str(pathfile)
# loading the image
        try:
            global img
            with PIL.Image.open(pathfile) as img:
# fetching the dimensions
                wid, hgt = img.size
# displaying the dimensions
    #print(str(wid) + "x" + str(hgt))
            if 1.66 < float(hgt/wid) and float(hgt/wid) < 2.0 :
                print(name + ": PASS")
            else:
                #print(pathfile)
                path = os.path.join(directory,name)
                os.remove(path)
                print(name+" : REMOVED")
                count += 1
        except:
            os.remove(os.path.join(directory,name))
            print(name+" : REMOVED")
#print(len(fixName))
    return count
#fix("\\Photos\\")
