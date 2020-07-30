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
