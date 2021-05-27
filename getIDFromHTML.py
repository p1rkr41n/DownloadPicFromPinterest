from ast import Num
import os

def getIDFromHTML(htmlFile):
    f = open(htmlFile, 'r+', encoding='utf-8')
    #f.write(getAllIDPinterest("https://www.pinterest.com:443/pin/730357264559116463/"))
    html= f.read()
    content = str(html)
    contentSplited = content.split()
    #print(contentSplited)
    NumLink = int(content[0:3])
    listID=[]
    for string in contentSplited:
        #print(string)
        if string.find('href="/pin/') != -1:
            #print(string)
            sub=0
            try:
                int((string[len(string)-20:len(string)-19]))
                sub=0
            except: 
                try:
                    int((string[len(string)-19:len(string)-18]))
                    sub=1
                except:
                    try:
                        int((string[len(string)-18:len(string)-17]))
                        sub=2
                    except:
                        try:
                            int((string[len(string)-17:len(string)-16]))
                            sub=3
                        except:
                            pass
            #print((string[len(string)-20+sub:len(string)-2]))
            listID+=[(string[len(string)-20+sub:len(string)-2])]
        #else:
            #print(string.find('href="/pin/'))
    #print(listID)
    return listID
            #int((string[len(string)-20:len(string)-2]))
    #f.close()
#listID=getIDFromHTML("html.txt")