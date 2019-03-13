#Semple clection of user Face
import cv2 # impoort openCV library
import numpy as np #import nympy for nomerical method

face_classifier = cv2.CascadeClassifier('C:/Users/dush4/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')#location for CascadeClassifire pre defind face data

#Defind a Function for extractor
def face_extractor(img):
    #convert RBG image in gray scale image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)
    if faces is():
        return None
    for(x,y,w,h) in faces:
        # give the dimention for cropped face
        cropped_face = img[y:y+h, x:x+w]
        return cropped_face

#on camera
cap = cv2.VideoCapture(0) 
#initialization of count variable
count = 0     
while True:
    ret, frame = cap.read()
    #If face is Detect Then execute the program
    if face_extractor(frame) is not None: 
        count +=1
        face = cv2.resize(face_extractor(frame),(200,200))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        file_name_path = 'C:/Users/dush4/Pictures/sample pic/user' + str(count)+'.jpg'
        cv2.imwrite(file_name_path, face)
        cv2.putText(face, str(count),(50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
        cv2.imshow('face crope',face)
    else:
        print('NO FACE DITECTION')
        pass
    if count == 100:
        break
cap.release()
