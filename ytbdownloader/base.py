from pytube import YouTube 
from pytube import Playlist
from pytube import exceptions
import json
import argparse
import sys

def get_arg():
    """Handle command-line arguments"""  
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
        print('File not found: {}'.format(filename))
        exit()
    except:
        print('Error while processing file: {}'.format(filename))
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
                raise ValueError('Unknown type: {}'.format(type))
    
def process_urls(content):
    """Process YouTube urls"""
    path = content['local_path']
    urls = content['urls']
    for q in range(len(urls)):
        url = urls[q]
        try:
            video = YouTube(url)
            print('downloading : {} with url : {}'.format(video.title, video.watch_url))
            video.streams.\
                filter(progressive=True, file_extension='mp4').\
                order_by('resolution').\
                desc().\
                first().\
                download(path)
        except exceptions.RegexMatchError:
            print('The url has wrong format: {}'.format(url))
            # continue
        except exceptions.VideoUnavailable:
            print('The video is unavailable for the url: {}'.format(url))
            # continue
        except exceptions.PytubeError:
            print('Error while processing the url: {}'.format(url))
            # continue
        # if any PytubeError occurs, let log the error and continue processing other urls.

def process_playlist(content):
    """Process YouTube Playlist""" 
    path = content['local_path']
    urls = content['urls']
    for i in range(len(urls)):
        url = urls[i]
        try:
            playlist = Playlist(url)
        except exceptions.RegexMatchError:
            print('The playlist url has wrong format: {}'.format(url))
            # continue
        except exceptions.VideoUnavailable:
            print('The video is unavailable for the playlist url: {}'.format(url))
            # continue
        except exceptions.PytubeError:
            print('Error while processing the playlist url: {}'.format(url))
            # continue
        else:
            if (len(playlist.videos) == 0):
                print('Unable to obtain any video from the playlist url: {}'.format(url))
            else:
                for video in playlist.videos:
                    try:
                        print('downloading : {} with url : {}'.format(video.title, video.watch_url))
                        video.streams.\
                            filter(type='video', progressive=True, file_extension='mp4').\
                            order_by('resolution').\
                            desc().\
                            first().\
                            download(path)
                    except exceptions.VideoUnavailable:
                        print('The following video is unavailable: {}'.format(video))
                        # continue
                    except exceptions.PytubeError:
                        print('Error while processing the video {} from the playlist url: {}'.format(video, url))
                        #continue

def main():
    args = get_arg()
    cfg = load_config(args.input)
    download(cfg)