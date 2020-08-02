import argparse
import cv2
from imutils.video import VideoStream

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cascade", required=True,
	help="path to cascade.xml")
ap.add_argument("-o", "--output", required=True,
	help="path to output dir")

args = vars(ap.parse_args())

detector = cv2.CascadeClassifier(args["cascade"])

vs = VideoStream(usePiCamera=True).start()

tatal = 0

while True:
	frame = vs.read()
	old = frame.copy()
	frame = imutils.resize(frame, width = 400)

	rects = detectore.detecMultiScale(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))


