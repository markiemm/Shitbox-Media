from qbittorrentapi import Client, client
from qbittorrentapi import TorrentStates
from main import config

download_dir = "/home/data/downloads"
tv_dir = "/home/data/tv"
movie_dir = "/home/data/movies"
music_dir = "/home/data/music"


public_qbit = Client(host='qbit.shitbox.media', username=config["public_qbit"]["username"], password=config["public_qbit"]["password"])

private_qbit = Client(host='secure-qbit.shitbox.media', username=config["private_qbit"]["username"], password=config["private_qbit"]["password"])
