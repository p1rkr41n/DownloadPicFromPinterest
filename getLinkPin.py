#This file can export link from pinterest ID  
import requests

session = requests.session()

def getLinkPin(id):
    pin_url = "https://www.pinterest.com:443/pin/"+str(id)+"/"
    pin_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0 Waterfox/78.6.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Upgrade-Insecure-Requests": "1", "Te": "trailers", "Connection": "close"}
    r= session.get(pin_url, headers=pin_headers)
    r=r.text
    linkPic = r[r.find('href="https://i.pinimg.com/originals')+6:(r.find('href="https://i.pinimg.com/originals')+82)]
    return linkPic
#getLinkPin(587649451368063087)