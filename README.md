
# Face Recognition attendance System using Python
This Python program uses face recognition to automatically mark attendance. 
The program detects faces in real-time using a webcam, compares them to a database of known faces, and records the attendance of recognized faces in a CSV file.
## Features
-Real-time face detection and recognition.

-Records attendance with timestamps.

-Supports multiple faces in the frame.
## Installation
```bash
Python 3.x
OpenCV
NumPy
face_recognition
CSV
```
## Roadmap
Start
1. Initialize video capture from webcam
2. Load known faces and their encodings from the "Data" directory
3. Open a CSV file for recording attendance
4. Initialize an empty set to keep track of recorded attendance
5. Set tolerance for face recognition (default: 0.4)
6. Start an infinite loop:
a. Read a frame from the video capture

b. Resize the frame to 1/4 size for faster processing

c. Convert the frame from BGR to RGB

d. Find face locations and encodings in the frame

e. Initialize an empty list to store recognized face names

f. For each face encoding in the frame:

     i. Compare the face encoding with known face encodings
     ii. If a match is found:
         - Get the name of the recognized face
         - Check if attendance for this face has been recorded
         - If not, record the attendance with the current time
     iii. Add the recognized face name to the list of face names

g. For each recognized face in the frame:

    i. Draw a rectangle around the face
    ii. Display the recognized face name near the face
h. Show the video frame

    i. Check for 'q' key press:
       - If pressed, break the loop
7. Release video capture and close all OpenCV windows
8. Close the CSV file
End

