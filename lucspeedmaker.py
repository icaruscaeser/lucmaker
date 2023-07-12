# Author : Icarus Caesar
# 23/10/22 - 14:24:06

from moviepy.editor import VideoFileClip, TextClip, concatenate_videoclips, CompositeVideoClip
import os

video_files = os.listdir('videos')
video_files.sort()
clips = []
for file in video_files:
    print(f'Loading file {file}')
    clips.append(VideoFileClip(f'videos/{file}'))


cutsec = 1

final_clip = None
clip_arr = []

clipper = 0
while len(clips) > 0:
    for clip in clips:
        if clip.duration < clipper + cutsec:
            clips.remove(clip)
            continue
        subclip = clip.subclip(clipper, clipper+cutsec)
        '''if final_clip is None:
            #final_clip = subclip
        else:
            #final_clip = concatenate_videoclips([final_clip, subclip])'''
        clip_arr.append(subclip)
    clipper += cutsec
    print(clipper)

print("Cropping the upper waterwark")
final_clip = concatenate_videoclips(clip_arr)
# crop the upper water mark
final_clip = final_clip.crop(y1=25)

print("Adding watermark")
# add watermark
txt_clip = TextClip("@farooqahmed", fontsize=25, color='white')
txt_clip = txt_clip.set_pos('center').set_duration(final_clip.duration)
final_clip = CompositeVideoClip([final_clip, txt_clip])

final_clip.write_videofile('all3.mp4')