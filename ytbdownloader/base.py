from pytube import YouTube 
from pytube import Playlist 
import json
import argparse
import sys

CONFIG_FILE = 'config.json'

def get_arg():
    '''Returns passed arguments'''   
    parser = argparse.ArgumentParser(description='"Ytbdownloader" - A command-line tool to download videos from Youtube. The tool can process playlists and links directly. Also, flexible settings might be set via json configuration file')
    parser.add_argument(
        'input', 
        type=str, 
        help='input name of "*.json" file ', 
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
    tasks = config['tasks']
    for i in range(len(tasks)):
        task = tasks[i]
        is_enable = task['enable']
        # Check if 'enable' tag is true
        if is_enable:
            type = task['type']
            if type == 'youtube':
                # download youtube urls
                process_urls(task)
            elif type == 'playlist':
                # download playlist
                process_playlist(task)
            else:
                raise ValueError('Unknown type:' + type)
    
def process_urls(content):
    # Process YouTube urls
    try:
    # if True:
        path = content['local_path']
        urls = content['urls']
        for q in range(len(urls)):
            url = urls[q]
            video = YouTube(url)
            print('downloading : {} with url : {}'.format(video.title, video.watch_url))
            video.streams.\
            filter(progressive=True, file_extension='mp4').\
            order_by('resolution').\
            desc().\
            first().\
            download(path)
    except Exception: # I can't exclud just "pytube.exceptions.RegexMatchError"
        print(f'Bad url: "{url}" ' )
        exit()

   
        
def process_playlist(content):
#  Process YouTube Playlist 
    try:
        path = content['local_path']
        urls = content['urls']
        for i in range(len(urls)):
            url = urls[i]
            playlist = Playlist(url)
            for video in playlist.videos:
                print('downloading : {} with url : {}'.format(video.title, video.watch_url))
                video.streams.\
                    filter(type='video', progressive=True, file_extension='mp4').\
                    order_by('resolution').\
                    desc().\
                    first().\
                    download(path)
    except KeyError:
        print(f'Bad url: "{url}" ' )
        exit()

def main():
    args = get_arg()
    cfg = load_config(args.input)
    download(cfg)