import os
import sys
from moviepy.editor import VideoFileClip
import time

def main(argv):
    fname = argv[1]
    
    clip = VideoFileClip(argv[1])
    length = int(clip.duration)+1
    timestamps = []
    ads = []
    for i in range(2,len(argv),2):
        timestamps.append(argv[i])
        ads.append(argv[i+1])
        
    start = 0
    end = 1
    ext = fname.rsplit('.',1)[-1]
    bare_fname = fname.rsplit('.',1)[0]
    segments = []
    for i in range(len(timestamps)):
        segment_name = bare_fname+"_part"+str(i+1)+'.'+ext
        segments.append(segment_name)
        segments.append(ads[i])
        os.system("ffmpeg -i {} -ss {} -to {} {}".format(fname,start,timestamps[i],segment_name))
        start = timestamps[i]
    
    segment_name = bare_fname+"_part"+str(i+2)+'.'+ext
    segments.append(segment_name)
    os.system("ffmpeg -i {} -ss {} -to {} {}".format(fname,start,length,segment_name))
    
    #ffmpeg -f concat -i mylist.txt -c copy output.mp4    
    f = open("mylist.txt",'w')
    for fname in segments:
        f.write("file '{}'\n".format(os.path.abspath(fname)))
    
    f.close()
    os.system("ffmpeg -f concat -safe 0 -i mylist.txt -c copy output{}.mp4".format(int(time.time())))   
    print(segments)
    for fname in segments:
        if 'part' in fname:
            os.remove(fname)
        
        
        
    
    
if __name__ == '__main__':
    if len(sys.argv)<2 or (len(sys.argv)%2)!=0:
        print("Format: py video_mixer.py input.mkv 10 ad1.mkv 20 ad2.mkv 30 ad3.mkv")
        sys.exit(-1)
        
    main(sys.argv)



