from time import time
from getLinkPicSuggest import getAllIDPinterest
from getIDFromHTML import getIDFromHTML
from getLinkPin import getLinkPin
from getPicFromLink import getPic
from fixDownloadedPic import fix
import os
import shutil

try:
    os.mkdir("./Photos/")
except:
    #os.rmdir("./Photos/")
    shutil.rmtree("./Photos/")
    os.mkdir("./Photos/")
getAllIDPinterest("https://www.pinterest.com/pin/91268329930642744/")

#time.sleep(1)
#ref = open("html.txt", 'r', encoding='utf-8')
#content = ref.read()
listID=getIDFromHTML("./Photos/html.txt")
count=0
for id in listID:
    count += getPic(getLinkPin(id), "./Photos/"+str(id)+ ".jpg")
#ref.close()
count -= fix("\\Photos\\")
print(count)
