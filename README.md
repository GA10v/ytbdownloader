[![Tests Status](./quality/reports/junit/junit-badge.svg?dummy=8484744)](https://htmlpreview.github.io/?https://github.com/digal25/ytbdownloader/blob/master/quality/reports/junit/report.html)
[![Coverage Status](./quality/reports/coverage/coverage-badge.svg?dummy=8484744)](https://htmlpreview.github.io/?https://github.com/digal25/ytbdownloader/blob/master/quality/reports/coverage/html/index.html)

# ytbdownloader

A command-line tool to download videos from Youtube. The tool can process playlists and links directly. Also, flexible settings might be set via json configuration file.
This tool is developed and maintained by volunteers.

## Requirements

- Python 3.6+
- pip

## Install

`pytube` is a Python package that can be installed using `pip`:

``` sh
pip install pytube
```

## Usage

``` plain
usage: ytbdownloader.py [-h] input

A command-line tool to download videos from Youtube. The tool can process playlists and links directly. Also, flexible settings might be set via json configuration file.

positional arguments:
  input       input name of "*.json" file

optional arguments:
  -h, --help  show this help message and exit
```

Example:

``` sh
$ ytbdownloader.py ./config.json
```

## Thanks ❤️
* [GA10v](https://github.com/GA10v)


