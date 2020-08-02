import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cascade", required=True,
	help="path to cascade.xml")
ap.add_argument("-o", "--output", required=True,
	help="path to output dir")

args = vars(ap.parse_args())
