from os import name
import requests
from requests.api import get
import os

def getPic(pic_url, namePic):
    print("Downloading: "+ pic_url)
    with open( namePic, 'wb') as handle:
        try:
            response = requests.get(pic_url, stream=True)
        except:
            return 0
        if not response.ok:
            print(response)
        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)
    #print(os.stat(namePic).st_size)
    if (os.stat(namePic).st_size < 500):
        os.remove(namePic)
        print("deleted: "+ namePic)
        return 0
    else:
        return 1