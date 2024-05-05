import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime
import os

def load_known_faces(directory):
    known_face_encodings = []
    known_face_names = []
    
    for filename in os.listdir(directory):
        name, ext = os.path.splitext(filename)
        if ext.lower() in ('.jpg', '.jpeg', '.png', '.bmp'):
            img_path = os.path.join(directory, filename)
            img = cv2.imread(img_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)  # Convert BGR to RGBA
            img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)  # Convert RGBA to RGB
            encoding = face_recognition.face_encodings(img)[0]
            known_face_encodings.append(encoding)
            known_face_names.append(name)
    
    return known_face_names, known_face_encodings


video_capture = cv2.VideoCapture(0)

known_faces_dir = "Data/"
known_face_names, known_face_encodings = load_known_faces(known_faces_dir)

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(current_date + '.csv', 'w+', newline="")
lnwriter = csv.writer(f)

attendance_recorded = set()

tolerance = 0.4

while True:
    ret, frame = video_capture.read()

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=tolerance)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            if name not in attendance_recorded:
                current_time = datetime.now().strftime("%H-%M-%S")
                lnwriter.writerow([name, current_time])
                attendance_recorded.add(name)

        face_names.append(name)

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()
