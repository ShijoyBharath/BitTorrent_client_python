import bencodepy
from rich import print
import hashlib
import random
import requests
import socket


def parse_torrent_file(file_path):
    with open(file_path, "rb") as f:
        meta_info = f.read()
        torrent_data = bencodepy.decode(meta_info)
        torrent_info = torrent_data[b"info"]

        torrent_files = []
        for item in torrent_info[b"files"]:
            torrent_files.append({"length": item[b"length"], "path": item[b"path"]})

        return {
            "announce": torrent_data[b"announce"],
            "info_hash": hashlib.sha1(bencodepy.encode(torrent_info)),
            "piece_length": torrent_info[b"piece length"],
            "pieces": torrent_info[b"pieces"],
            "files": torrent_files,
        }

def get_peers(tracker_url, info_hash):
    peer_id = '-PY0001-' + ''.join([str(random.randint(0, 9)) for _ in range(12)])
    port = random.randint(6881,6889)

    params = {
        'info_hash' : info_hash,
        'peer_id' : peer_id.encode(),
        'port' : port,
        'uploaded' : 0,
        'downloaded' : 0,
        'left' : 0,
        'compace' : 1
    }

    response = requests.get(tracker_url, params = params)
    print(response)
    tracker_response = bencodepy.decoded(response.content)

    peers_binary = tracker_response[b'peers']
    peers = [(socket.inet_ntoa(peers_binary[i : i + 4]), int.from_bytes(peers_binary[i + 4 : i + 6], 'big')) for i in range(0, len(peers_binary), 6)]
    return peers

def request_piece():
    return

def validate_piece():
    return True

def save_to_file(data, file_path):
    return

if __name__ == "__main__":
    PATH = "./download.torrent"
    torrent = parse_torrent_file(PATH)

    print(get_peers(torrent['announce'], torrent['info_hash']))


