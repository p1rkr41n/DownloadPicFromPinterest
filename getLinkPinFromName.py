#this function can return link photos if you have its name
def getlink(name):
    nameFile = name
    linkImg = "https://i.pinimg.com/originals/"+ nameFile[0:2] +"/" + nameFile[2:4]+"/"+ nameFile[4:6]+"/" + nameFile
    return linkImg