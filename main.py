import bencodepy
from rich import print
import hashlib


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
    return peers

def request_piece():
    return response

def validate_piece():
    return True

def save_to_file(data, file_path):
    return

if __name__ == "__main__":
    PATH = "./download.torrent"
    torrent = parse_torrent_file(PATH)


