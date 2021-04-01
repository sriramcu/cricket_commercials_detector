from features_extractor.features import quantify_image
import argparse
import pickle
import cv2
import os
import numpy as np
import time

def run_prediction(image,modelfolder,display=True):



    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    features = quantify_image(hsv, bins=(3, 3, 3))
   
    
    
    for f in os.listdir(modelfolder):
        
        modelfile = os.path.join(modelfolder,f)
        model = pickle.loads(open(modelfile, "rb").read())
        preds = model.predict([features])
    
        preds = preds[0]
        label = "anomaly" if preds == -1 else "normal{}".format(f)
        color = (0, 0, 255) if preds == -1 else (0, 255, 0)
        if preds!=-1:
            break
    
    
    if display:
        cv2.putText(image, label, (10,  25), cv2.FONT_HERSHEY_SIMPLEX,
            0.7, color, 2)
        
        cv2.imshow("Output", image)
        cv2.waitKey(1)
            
    if label == 'anomaly':
        return 0
    else:
        return 1
    
if __name__ == '__main__':
    

    ap = argparse.ArgumentParser()
    ap.add_argument("-m", "--model", required=True,
        help="path to trained anomaly detection model")
    ap.add_argument("-i", "--image", required=True,
        help="path to input images directory")
    args = vars(ap.parse_args())

    model = pickle.loads(open(args["model"], "rb").read())
    print("[INFO] loading anomaly detection model...")


    for f in os.listdir(args["image"]):
        
        image_path = os.path.join(args["image"],f)
        image = cv2.imread(image_path)
        run_prediction(image,model)
    
    

    
    
