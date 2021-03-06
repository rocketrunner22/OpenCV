import cv2 as cv
import numpy as np
import imutils
import time
from imutils.video import VideoStream
from imutils.video import FPS


faceCascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
video_feed = VideoStream(src=0).start()
print("[INFO] starting video stream...")
time.sleep(2.0)
fps = FPS().start()

while ((cv.waitKey(1) & 0xFF) != ord("q")):
	frame = video_feed.read() #get webcam feed
	frame = imutils.resize(frame, width=500)
	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #grayscale image
	found = faceCascade.detectMultiScale (gray, scaleFactor=1.1, minNeighbors=10, minSize = (30, 30)) #detect faces
	for (x, y, w, h) in found: cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2) #draw a rectangle around faces
	cv.imshow("Video Feed", frame)
	fps.update()

fps.stop()
print ("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
print ("[INFO] FPS: {:.2f}".format(fps.fps()))
cv.destroyAllWindows()
