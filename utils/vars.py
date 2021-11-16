import os
from qbittorrentapi import Client

from utils.db import config


class Dirs:
    download_dir = "/home/data/downloads"
    tv_dir = "/home/data/tv"
    movie_dir = "/home/data/movies"
    music_dir = "/home/data/music"
    books_dir = "/home/data/books"


class QbitVars:
    public_qbit = Client(host='qbit.shitbox.media',
                         username=config["public_qbit"]["username"], password=config["public_qbit"]["password"])

    private_qbit = Client(host='secure-qbit.shitbox.media',
                          username=config["private_qbit"]["username"], password=config["private_qbit"]["password"])
