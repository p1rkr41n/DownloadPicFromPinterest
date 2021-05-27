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
    linkFromDB = getLinkPin(id)
    count += getPic(linkFromDB, "./Photos/"+str(id)+ linkFromDB[len(linkFromDB)-5:len(linkFromDB)])
#ref.close()
count -= fix("\\Photos\\")
print(count)
