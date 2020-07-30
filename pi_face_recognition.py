# python3 pi_face_recognition.py --cascade haarcascade_frontalface_default.xml --encodings encodings.pickle

import argparse
import pickle


ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cascade", required=True,
	help = "path to where the face cascade resides")
ap.add_argument("-e", "--encodings", required=True,
	help="path to serialized db of facial encodings")
args = vars(ap.parse_args())

data = pickle.loads(open(args["encodings"], "rb").read())
