from features_extractor.features import load_dataset
from sklearn.ensemble import IsolationForest
import argparse
import pickle
import sys
import shelve
import os


ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help="path to dataset of images")
ap.add_argument("-m", "--model", required=True,
	help="path to output anomaly detection model")
    
ap.add_argument("-c", "--contamination", required=True,
	help="contamination")

    
args = vars(ap.parse_args())

print("[INFO] preparing dataset...")
data = load_dataset(args["dataset"], bins=(3, 3, 3))


print("[INFO] fitting anomaly detection model...")
model = IsolationForest(n_estimators=100, contamination=float(args["contamination"]),
	random_state=42)
model.fit(data)


f = open(args["model"], "wb")
f.write(pickle.dumps(model))
f.close()

print("Anomaly training done")              

