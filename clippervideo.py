# Author : Icarus Caesar
# 23/10/22 - 14:24:06

from moviepy.editor import VideoFileClip, TextClip, concatenate_videoclips, CompositeVideoClip
import moviepy.video.fx.all as vfx
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


for clip in clips:
    start = int(clip.duration/2)
    end = start + 2
    subclip = clip.subclip(start, end)
    subclip = subclip.resize(height=720)

    #speed that first 1 sec, slow the second 2 sec
    speed = 1.2
    sped_clip = subclip.subclip(0, 1)
    sped_clip = sped_clip.set_fps(sped_clip.fps * speed)
    sped_clip = sped_clip.fx(vfx.speedx, speed)

    slow = 0.7
    delayed_clip = subclip.subclip(1, 2)
    delayed_clip = delayed_clip.set_fps(delayed_clip.fps * slow)
    delayed_clip = delayed_clip.fx(vfx.speedx, slow)

    done_clip = concatenate_videoclips([sped_clip, delayed_clip])
    clip_arr.append(done_clip)

print("Cropping the upper waterwark")
final_clip = concatenate_videoclips(clip_arr)
# crop the upper water mark
final_clip = final_clip.crop(y1=25)

print("Adding watermark")
# add watermark
txt_clip = TextClip("@farooqahmed", fontsize=25, color='white')
txt_clip = txt_clip.set_pos('center').set_duration(final_clip.duration)
final_clip = CompositeVideoClip([final_clip, txt_clip])

final_clip.write_videofile('cliper.mp4')