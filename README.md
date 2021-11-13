[![Tests Status](./quality/reports/junit/junit-badge.svg?dummy=8484744)](./quality/reports/junit/report.html)
[![Coverage Status](./quality/reports/coverage/coverage-badge.svg?dummy=8484744)](./quality/reports/coverage/index.html)

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
Usage: ytbdownloader.py <options>

  Download all Youtube videos to a local directory

Options:
  input <config>    Path to a configuration file in JSON format (Required)
  -h, --help        Show this message and exit.
```

Example:

``` sh
$ ytbdownloader.py input ./config.json
```

## Thanks ❤️
* [GA10v](https://github.com/GA10v)


