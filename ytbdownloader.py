from pytube import YouTube 
from pytube import Playlist 
import json
import argparse
import sys

CONFIG_FILE = 'config.json'

def get_arg():
    parser = argparse.ArgumentParser(description='Download videos from Youtube')
    parser.add_argument(
        '-i', '--input', 
        type=str, 
        help='input name of "*.json" file (default is "/config.json") ', 

        default='config.json' 
        )
    args = parser.parse_args()

    return args

def load_config(filename):
    """Load configuration from a specified file"""
    try:
        fd = open(filename)
        config = json.load(fd)
        return config
    except FileNotFoundError as e:
        print('File not found: ' + filename)
        raise
    except:
        print('Error while processing file ' + filename)
        raise

def download(config):
    """Start download process by processing configuration""" 
    for i in range(len(config['tasks'])):
        # Check if 'enable' tag is true
        if config['tasks'][i]['enable']:
            content = config['tasks'][i]
            type = content['type']
            if type == 'youtube':
                # download youtube urls
                process_urls(content)
            elif type == 'playlist':
                # download playlist
                process_playlist(content)
            else:
                raise ValueError('Unknown type:' + type)
    
def process_urls(content):
    # Process YouTube urls
    path = content['local_path']
    for q in range(len(content['urls'])):
        video = YouTube(content['urls'][q])
        print('downloading : {} with url : {}'.format(video.title, video.watch_url))
        video.streams.\
        filter(progressive=True, file_extension='mp4').\
        order_by('resolution').\
        desc().\
        first().\
        download(path)
        
def process_playlist(content):
#  Process YouTube Playlist 
    path = content['local_path']
    for i in range(len(content['urls'])):
        playlist = Playlist(content['urls'][i])
        for video in playlist.videos:
            print('downloading : {} with url : {}'.format(video.title, video.watch_url))
            video.streams.\
                filter(type='video', progressive=True, file_extension='mp4').\
                order_by('resolution').\
                desc().\
                first().\
                download(path)
    

args = get_arg()
cfg = load_config(args.input)
download(cfg)
