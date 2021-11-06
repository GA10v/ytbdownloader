from pytube import YouTube 
from pytube import Playlist 
import json

def open_json():
# пытается найти и открыть файл config.json 
    try:
        config = json.load(open('config.json'))
        return config
    except:
        config = None
        print('не нашел config.json')
        return config

def download_choicer(config):
# проверяет ключь "enable" и выбирает как скачивать видео, через YouTube или Playlist
    for i in range(len(config)):
        if config[i]["enable"]:
            if config[i]['tasks'][0]['type'] == 'single':
                date = config[i]
                YouTube_downloader(date)
            elif config[i]['tasks'][0]['type'] == 'playlist':
                date = config[i]
                Playlist_downloader(date)
    
def YouTube_downloader(date):
# скачивает видео через YouTube
    SAVE_PATH = date['tasks'][0]['local_path']
    for q in range(len(date['tasks'][0]['urls'])):
        video = YouTube(date['tasks'][0]['urls'][q])
        print('downloading : {} with url : {}'.format(video.title, video.watch_url))
        video.streams.\
        filter(progressive=True, file_extension='mp4').\
        order_by('resolution').\
        desc().\
        first().\
        download(SAVE_PATH)
        
def Playlist_downloader(date):
#  скачивает видео через Playlist 
    SAVE_PATH = date['tasks'][0]['local_path']
    for i in range(len(date['tasks'][0]['urls'])):
        playlist = Playlist(date['tasks'][0]['urls'][i])
        for video in playlist.videos:
            print('downloading : {} with url : {}'.format(video.title, video.watch_url))
            video.streams.\
                filter(type='video', progressive=True, file_extension='mp4').\
                order_by('resolution').\
                desc().\
                first().\
                download(SAVE_PATH)
    


config = open_json()
download_choicer(config)

# SAVE_PATH = config[0]['tasks'][0]['local_path']
# print()

# video = YouTube('https://www.youtube.com/watch?v=8eud2ZQHK1s')
# print('downloading : {} with url : {}'.format(video.title, video.watch_url))
# video.streams.\
#     filter(progressive=True, file_extension='mp4').\
#     order_by('resolution').\
#     desc().\
#     first().\
#     download(SAVE_PATH)

# '''
# SAVE_PATH = "/Users/galo/Downloads/video/незнайка"
# playlist = Playlist('https://www.youtube.com/watch?v=fjwF0sCbDtE&list=PL7x1DJTKugPDlSaK0UHPavBovuK8qT38f')
# for video in playlist.videos:
#     print('downloading : {} with url : {}'.format(video.title, video.watch_url))
#     video.streams.\
#         filter(type='video', progressive=True, file_extension='mp4').\
#         order_by('resolution').\
#         desc().\
#         first().\
#         download(SAVE_PATH)
