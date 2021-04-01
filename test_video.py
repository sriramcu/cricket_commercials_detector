from test_anomaly_detector import run_prediction
import cv2
import sys
import pickle
import shelve
import os
import time

def count_element(arr,ele):
    return len([x for x in arr if x == ele])
    
def test_video(vidfile,modelfolder):
    vidcap = cv2.VideoCapture(vidfile)

    success,image = vidcap.read()
    count = 0
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    desired_fps = 8 #number of frames to process per second
    skip_frames = int(int(fps)/desired_fps)
    
    success = True
    wrs = True
    print("Processing video")

    pred_arr = []
    state = 1 #current state is unmuted
    context_window = 16
    overturn_volume = 0.7 * context_window #12 of 16 must be anomolous to overturn the current unmuted (cricket) state
    overturn_mute = 0.9 * context_window #14 of 16 must be cricket to overturn the current muted(ads) state
    print("Unmute")
    overturn_time = time.time() #time at which previous state was set
    inertia = context_window/desired_fps #number of seconds in which mute or unmute musn't occur- 2 seconds from previous overturn
    while success and wrs:
        success,image = vidcap.read()
        if success and count % skip_frames == 0:   
       
   
            rval = run_prediction(image,modelfolder)
            pred_arr.append(rval)  #0 is anomaly(mute) and 1 is cricket(unmute)
            if count>1000:
                del pred_arr[0] #delete the first frame prediction for every frame processed, once array length crosses 1000 to preserve memory
            
            context = pred_arr[-context_window:]
            if time.time() > overturn_time + inertia and state == 1 and count_element(context,0)>overturn_volume:
                state = 0
                print("Mute")
                overturn_time = time.time()
                #mute()
            elif time.time() > overturn_time + inertia and state == 0 and count_element(context,1)>overturn_mute:
                state = 1
                print("Unmute")
                overturn_time = time.time()
                #unmute()
            
        count += 1



if __name__ == '__main__':
    if len(sys.argv)<3:
        print("py test_video.py model_folder video_file ")
        sys.exit(-1)
    
    # ~ for f in os.listdir('anomalies'):
        # ~ os.remove(os.path.join("anomalies",f))
    test_video(sys.argv[2],sys.argv[1])
    
    
