import asyncio
from parser import bdecode
import pprint

def get_peers():
    with open("one-piece.torrent", "rb") as f:
        torrent_data = f.read()
    decoded_data = bdecode(torrent_data)
    pprint.pprint(decoded_data[b'info'])

get_peers()