# Author : Icarus Caeser
# 23/10/22 - 18:39:06

from moviepy.editor import ImageClip, TextClip, concatenate_videoclips, CompositeVideoClip
import os

directory = 'photos'
photo_files = os.listdir(directory)
photos = []
for file in photo_files:
    print(f'Loading photo {file}')
    img = ImageClip(f'{directory}/{file}').set_duration(0.7)
    img = img.resize(height=1200)
    photos.append(img)

concat_clip = concatenate_videoclips(photos, method="compose")
concat_clip.write_videofile("ptest1.mp4", fps=24)