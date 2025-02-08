# pip install face_recognition
# pip install cmake
# pip install dlib
# pip install opencv-python 
# pip install numpy

import face_recognition
import cv2 # it is opencv-python
import numpy as np # for handling large array & mathmatical operation
import csv   # for to stor date in structure from
from datetime import datetime 

video_capture= cv2.VideoCapture(0)

#load konw Faces

atharva_image= face_recognition.load_image_file("faces/atharva.jpeg")
atharva_encoding=face_recognition.face_encodings(atharva_image)[0]

sarthak_image= face_recognition.load_image_file("faces/sarthak.jpeg")
sarthak_encoding=face_recognition.face_encodings(sarthak_image)[0]

#khushi_image= face_recognition.load_image_file("faces/khushi.jpeg")
#khushi_encoding=face_recognition.face_encodings(khushi_image)[0]

kown_face_encoding=[atharva_encoding,sarthak_encoding]
kown_face_name=["atharva","sarthak"]

#list of accepeted students
students=kown_face_name.copy()

face_location=[]
face_encoding=[]

#get the current date and time

now=datetime.now()
current_date=now.strftime("%Y-%m-%d")

f=open(f"{current_date}.csv","w+",newline="")
lnwriter=csv.writer(f)

while True:
    _,frame=video_capture.read()
    small_frame=cv2.resize(frame,(0,0), fx=0.25, fy=0.25)
    rgb_small_frame= cv2.cvtColor(small_frame,cv2.COLOR_BGR2RGB)

    # recognize faces

    face_location=face_recognition.face_locations(rgb_small_frame)
    face_encoding=face_recognition.face_encodings(rgb_small_frame,face_location)

    for face_encoding in face_encoding:
        matches=face_recognition.compare_faces(kown_face_encoding,face_encoding)
        face_distance=face_recognition.face_distance(kown_face_encoding,face_encoding)
        best_match_index=np.argmin(face_distance)

        if(matches[best_match_index]):
            name=kown_face_name[best_match_index]
        
        #add text if person is present

        if name in kown_face_name:
            font= cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText=(10,100)
            fontScale=1.5
            fontColor=(255,0,0)
            thickness=3
            lineType=2
            cv2.putText(frame,name+" Present",bottomLeftCornerOfText,font,fontScale,fontColor,thickness,lineType)

            if name in students:
                students.remove(name)
                current_time=now.strftime("%H-%M-%S")
                lnwriter.writerow([name,current_time])

    cv2.imshow("Attendance",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()