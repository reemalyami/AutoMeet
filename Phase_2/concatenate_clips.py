#SCRIPT FOR EXTRACTING THE DEFINED EVENTS FROM THE MATCH RECORDING & MERGING THEM IN 1 VIDEO
#OUTPUT VIDEO AND SUBCLIPS ARE SAVED IN THE SERVER AND THEIR PATHS ARE SENT IN VIDEO.JSON
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip 
import subprocess
import glob
import os

def sec(time):
  a= sum(x * int(t) for x, t in zip([60, 1], time.split(":")))
  return a

required_video_file = "Path"
events= [] #A list of times; Format example: ('37:42', '39:12')
times=[]

for i in events:
  entry= str(sec(i[0])) + '-' + str(sec((i[1])))
  times.append(entry)

times = [x.strip() for x in times]
for time in times:
    starttime = int(time.split("-")[0])
    endtime = int(time.split("-")[1])
    ffmpeg_extract_subclip(required_video_file, starttime, endtime, targetname=str(times.index(time) + 1) + "_clip.mp4")

file_paths = sorted(glob.glob('/Users/PATH/*.mp4'), key=os.path.getmtime)
# create a text file with paths to all videos
print(file_paths)
with open('PATH/list.txt', 'w') as f:
    for fp in file_paths:
        f.write(f'file {fp}\n')

# run ffmpeg to concat videos
command = "ffmpeg -f concat -safe 0 -i PATH/list.txt -c:v copy output.mp4"
subprocess.call(command,shell=True)
