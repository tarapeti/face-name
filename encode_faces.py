# python3 encode_faces.py --dataset dataset --encodings encodings.pickle --detection-method hog

from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--dataset", required=True,
	help="path to faces + images")
ap.add_argument("-e", "--encodings", required=True,
	help="path to facial encodings")
ap.add_argument("-d", "--detection-method", type=str, default="cnn",
	help="`hog` or `cnn`")
args = vars(ap.parse_args())

imagePaths = list(paths.list_images(args["dataset"]))

knownEncodings = []
knownNames = []

for (i, imagePath) in enumerate(imagePaths):

	print("processing image {}/{}".format(i + 1,
		len(imagePaths)))
	name = imagePath.split(os.path.sep)[-2]

	image = cv2.imread(imagePath)
	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	boxes = face_recognition.face_locations(rgb,
		model=args["detection_method"])


