import socket
from imutils.video import VideoStream
import imutils
import time
import cv2
import os
import pickle

HOST = '192.168.1.27'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

HEADERSIZE = 10
"""
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
# vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)
total = 1000

# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream, clone it, (just
	# in case we want to write it to disk), and then resize the frame
	# so we can apply face detection faster
	frame = vs.read()
	orig = frame.copy()
	frame = imutils.resize(frame, width=400)
 
	# detect faces in the grayscale frame

	rects = detector.detectMultiScale(
		cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), scaleFactor=1.1, 
		minNeighbors=5, minSize=(30, 30))
 
	# loop over the face detections and draw them on the frame
	for (x, y, w, h) in rects:
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
	# show the output frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	# so we can later process it and use it for face recognition
	# if the `q` key was pressed, break from the loop
	
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break
# print the total faces saved and do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()		

print(frame)
"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
msg = s.recv(1024)
print(msg.decode("utf-8"))
    ##data = s.recv(1024)

##print('Received', repr(data))

# load OpenCV's Haar cascade for face detection from disk
#detector = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
 
# initialize the video stream, allow the camera sensor to warm up,
# and initialize the total number of example faces written to disk
# thus fa