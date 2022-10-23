import os
import random




def GenerateRandomPhoto():
    photoList = os.listdir('static/photo/')
    a = 0
    b = 15
    c = []
        
    while True:


        if(a == b):
            break
            
        n = random.randint(1,len(photoList))
        randomPhoto = photoList[n-1]
            
        if randomPhoto in c:
            continue
            
        c.append(randomPhoto)
        a = a+1


    return c


