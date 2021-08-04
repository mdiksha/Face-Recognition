import urllib.request
import cv2
import numpy as np
import imutils
import os

url = 'http://192.168.0.103:8080/shot.jpg'

dataset = "dataset"
name = "diksha"

path = os.path.join(dataset,name)
if not os.path.isdir(path):
    os.mkdir(path)

(width,height) = (130,100)

alg = "haarcascade_frontalface_default.xml"
haar_cascade = cv2.CascadeClassifier(alg)
count = 1

while True:
    while count < 51:
        print(count)
        imgPath = urllib.request.urlopen(url)
        imgNP = np.array(bytearray(imgPath.read()),dtype=np.uint8)
        img = cv2.imdecode(imgNP,-1)
        img = imutils.resize(img,width=450)
        grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        face = haar_cascade.detectMultiScale(grayImg,1.3,4)
        for (x,y,w,h) in face:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            faceOnly = grayImg[y:y+h,x:x+w]
            resizeImg = cv2.resize(faceOnly,(width,height))
            cv2.imwrite("%s/%s.jpg" %(path,count), faceOnly)
            count+=1
        cv2.imshow("CameraFeed",img)
        key = cv2.waitKey(1) & 0xFF
        if key == ord ('q'):
            break          
print("Image Captured Successfully")
cv2.destroyAllWindows()

