import cv2
import face_recognition

imgHuz=face_recognition.load_image_file('data/huz.jpg')
imgHuz=cv2.cvtColor(imgHuz,cv2.COLOR_BGR2RGB)
imgTest=face_recognition.load_image_file('data/TestHuz.jpg')
imgTest=cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

faceLoc=face_recognition.face_locations(imgHuz)[0]
encodeHuz=face_recognition.face_encodings(imgHuz)[0]
cv2.rectangle(imgHuz,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)

faceLocTest=face_recognition.face_locations(imgTest)[0]
encodeHuzTest=face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)

result=face_recognition.face_distance([encodeHuz],encodeHuzTest)
print(result)
cv2.imshow('huz',imgTest)
cv2.waitKey(0)




# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# cap = cv2.VideoCapture(0)
# # for external Ip camera
# # cap = cv2.VideoCapture('192.168.1.100:8080/video')
# # model=prdf.LoadModel()
# while True:
#     _, img = cap.read()
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#     for (x, y, w, h) in faces:
#         cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)


#         # cv2.putText(img,prdf.runModel(model,img),(x,y),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,0),3)
#     cv2.imshow('img', img)
#     k = cv2.waitKey(30) & 0xff
#     if k==27:
#         break
# cap.release()