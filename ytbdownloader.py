from pytube import YouTube 
from pytube import Playlist 

SAVE_PATH = 'C:\\DATA\\RAW'

video = YouTube('https://www.youtube.com/watch?v=8eud2ZQHK1s')
print('downloading : {} with url : {}'.format(video.title, video.watch_url))
video.streams.\
    filter(progressive=True, file_extension='mp4').\
    order_by('resolution').\
    desc().\
    first().\
    download(SAVE_PATH)

'''
playlist = Playlist('https://www.youtube.com/watch?v=fjwF0sCbDtE&list=PL7x1DJTKugPDlSaK0UHPavBovuK8qT38f')
for video in playlist.videos:
    print('downloading : {} with url : {}'.format(video.title, video.watch_url))
    video.streams.\
        filter(type='video', progressive=True, file_extension='mp4').\
        order_by('resolution').\
        desc().\
        first().\
        download(SAVE_PATH)
'''
