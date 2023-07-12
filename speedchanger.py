from moviepy.editor import VideoFileClip, TextClip, concatenate_videoclips, CompositeVideoClip
import moviepy.video.fx.all as vfx
import os

video_file_name = 'all4.mp4'
clip = VideoFileClip(video_file_name)
clip = clip.without_audio()
clip_arr = []

cutsec = 1
tim = 0
flipper = True

try:
    while tim < clip.duration:
        if flipper:
            # speed up
            # speed that first 1 sec, slow the second 2 sec
            speed = 1
            sped_clip = clip.subclip(tim, tim+2)
            sped_clip = sped_clip.set_fps(sped_clip.fps * speed)
            sped_clip = sped_clip.fx(vfx.speedx, speed)
            clip_arr.append(sped_clip)
            tim += 2
        else:
            slow = 0.6
            delayed_clip = clip.subclip(tim, tim+1)
            delayed_clip = delayed_clip.set_fps(delayed_clip.fps * slow)
            delayed_clip = delayed_clip.fx(vfx.speedx, slow)
            clip_arr.append(delayed_clip)
            tim += 1

        print(f'{tim } {flipper}')
        flipper = not flipper
except:
    print("some exception")

print("Cropping the upper waterwark")
final_clip = concatenate_videoclips(clip_arr)
# crop the upper water mark
#final_clip = final_clip.crop(y1=25)

# print("Adding watermark")
# # add watermark
# txt_clip = TextClip("@farooqahmed", fontsize=25, color='white')
# txt_clip = txt_clip.set_pos('center').set_duration(final_clip.duration)
# final_clip = CompositeVideoClip([final_clip, txt_clip])

final_clip.write_videofile('some1.mp4', )
