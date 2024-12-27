import bencodepy

def main():
    print("BitTorrent client running...")

    with open('./download.torrent', 'rb') as f:
        meta_info = f.read()
        torrent = bencodepy.decode(meta_info)
        print(torrent)


if __name__ == "__main__":
    main()
