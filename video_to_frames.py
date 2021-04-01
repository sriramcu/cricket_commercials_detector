import cv2
import sys
import time
import os

def video_to_frames(vidfile,imgdir='.',desired_fps=3):
    
    if not os.path.isfile(vidfile):
        print("No such file: {}".format(vidfile))
        sys.exit(-1)
        
    if not os.path.isdir(imgdir):
        print("No such directory: {}".format(vidfile))
        sys.exit(-1)
        
    vidcap = cv2.VideoCapture(vidfile)
    #print(vidcap.read())
    success,image = vidcap.read()
    count = 0
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    #desired_fps = 3
    skip_frames = int(int(fps)/desired_fps)
    
    success = True
    wrs = True
    print("Saving frames from video")
    while success and wrs:
      success,image = vidcap.read()
      if success and count % skip_frames == 0:   
        wrs = cv2.imwrite(os.path.join(imgdir,"frame{}{}.jpg".format(int(time.time()),count)), image)     # save frame as JPEG file
      
      count += 1


if __name__ == '__main__':
	if len(sys.argv)<2:
		print("py vtf.py video imgdir(optional) desired fps(optional)")
    if len(sys.argv)>3:
        imgdir = sys.argv[2]
        desired_fps = int(sys.argv[3])
    else:
        desired_fps = 3
        imgdir = '.'
    video_to_frames(sys.argv[1],imgdir,desired_fps)
