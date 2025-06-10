import cv2
import numpy as np
import face_recognition
import csv
from datetime import datetime

#Extracting faces from Faces folder and making a list
#of expected studets

video_capture = cv2.VideoCapture(0)

face1 = face_recognition.load_image_file("Faces/1.jpg")
encoding1 = face_recognition.face_encodings(face1)[0]

face2 = face_recognition.load_image_file("Faces/2.jpg")
encoding2 = face_recognition.face_encodings(face2)[0]

knownEncodings = [encoding1, encoding2]
knownNames = ["1", "2"]

students = knownNames.copy()

face_locations = []
face_encodings = []

#Making Note of date and time

now = datetime.now()
current_date = now.strftime("%d-%m-%Y")

#Putting data in csv file

f = open(f"{current_date}.csv","w+", newline="")
lnwriter = csv.writer(f)

# Recognize faces

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(knownEncodings, face_encoding)
        face_distance = face_recognition.face_distance(knownEncodings, face_encoding)
        best_match_index = np.argmin(face_distance)

        if matches[best_match_index]:
            name = knownNames[best_match_index]

        #Add Text for present person
        if name in knownNames:
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (10, 100)
            fontScale = 1.5
            fontColor = (255, 0, 0)
            thickness = 3
            lineType = 2
            cv2.putText(frame, name + " Present", bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)

            if name in students:
                students.remove(name)
                current_time = now.strftime("%H-%M-%S")
                lnwriter.writerow([name, current_time])


    cv2.imshow("Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
           

