from __future__ import unicode_literals
from yt_dlp import YoutubeDL
import urllib
import shutil
ydl_opts = {}
import os


# check for file 'todownload.txt'
urls_file = 'todownload.txt'
if os.path.isfile(urls_file):

    with open(urls_file) as urlsf:
        for url in urlsf.readlines():
            print(f'getting video from {url}')
            with YoutubeDL() as ydl:
            	ydl.download(url)
else:
    print(f'{urls_file} does not exist')

#yt = YouTube(url)
#yt = yt.get('mp4', '720p')
#yt.download(name)
