# Author : Icarus Caeser
# 28/10/22 - 11:14:14

from moviepy.editor import VideoFileClip, TextClip, concatenate_videoclips, CompositeVideoClip
import os

video_file_loc = 'hwd.mp4'
video = VideoFileClip(video_file_loc)

start = 0
stop = 60
subclip = video.subclip(start, stop)
subclip.write_videofile('output.mp4')