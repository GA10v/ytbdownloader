from pytube import YouTube 
from pytube import Playlist 
import json
import argparse

def get_arg():
    parser = argparse.ArgumentParser(description='Download videos from Youtube')
    parser.add_argument(
        '-i', '--input', 
        type=str, 
        help='input name of "*.json" file (default is "/config.json") ', # default не по ТЗ, но я хотел попробывать.. сработает или нет

        default='config.json' #не по ТЗ, но я хотел попробывать.. сработает или нет 
        )
    args = parser.parse_args()

    return args

def open_json(args):
# пытается найти и открыть файл config.json 

    if args.input[-5::] != '.json': #теперь можно не писать расширение *.json (не по ТЗ, но я хотел попробывать.. сработает или нет)
        args.input += '.json'

    try:
        config = json.load(open(args.input))
        return config
    except:
        config = None
        print('не нашел *.json файл')
        return config

def download_choicer(config):
# проверяет ключь "enable" и выбирает как скачивать видео, через YouTube или Playlist
    for i in range(len(config)):
        if config[i]["enable"]:
            if config[i]['tasks'][0]['type'] == 'youtube':
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
    

args = get_arg()
config = open_json(args)
download_choicer(config)
