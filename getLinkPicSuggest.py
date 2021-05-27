from os import TMP_MAX
import requests
import time
import os
from selenium import webdriver
from ping3 import ping, verbose_ping
from getIDFromHTML import getIDFromHTML
from getLinkPin import getLinkPin
from getPicFromLink import getPic


def getAllIDPinterest(url):
    #download html
    print("Caculating...")
    #waittime=1/st.download()*90000000
    waittime = ping('www.pinterest.com')*10
    print("Wait time for download about: "+str(waittime*800)+"s")
    time.sleep(1)
    driver = webdriver.Edge('./msedgedriver.exe')
    driver.set_window_size(0, 0)
    driver.get(url)

    for i in range(400):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(waittime)
        #print ("\033[A                             \033[A")
        os.system('cls')
        print("Downloading web: "+ str(format(((i/400)*100), ".2f"))+ "%")
    #time.sleep(2)
    print ("\033[A                             \033[A")
    print("Downloading web: 100%")
    html = driver.page_source
    driver.close()
    html = str(html.count('href="/pin/')) + str(html)

    print("COuNTER"+ str(html.count('href="/pin/')))
    #return html

    f = open("./Photos/html.txt", 'w+', encoding='utf-8')
    f.write(html)
    f.close()
    return 0