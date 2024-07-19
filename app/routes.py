import sys
from app import app

sys.path.append('C:\\Users\\montz\\OneDrive\\Codes\\lyricfyIT-project\\lyricfyIT-server\\app\\scripts')

import os
from flask import request
from enums import SongCodec
from legacy_download import DownloaderSongLegacy
from song import Song

token = os.getenv("MEDIA_USER_TOKEN")

@app.route("/")
def hello_world():
  return 'Hello World!'

@app.route("/get")
def getAll():
  url = request.headers.get('url')
  return retAll(url);

def retAll(url):
  try:
    codec = SongCodec.AAC_LEGACY
    legacy = DownloaderSongLegacy(codec, token)
    print("Legacy ✅")

    song_info = legacy.downloader.app.getSongInfo(url)
    webPlayback = legacy.downloader.app.getWebPlayback(song_info['id'])[0]

    stream_info = legacy.getStreamInfo(webPlayback)
    decryption_key = legacy.getDecryptionKey(stream_info.pssh, song_info['id'])

    encrypted_path = legacy.getEncryptedPath(song_info['id'])
    remuxed_path = legacy.getRemuxedPath(song_info['id'])

    legacy.downloader.download(encrypted_path, stream_info.stream_url)
    legacy.remux(encrypted_path, remuxed_path, decryption_key)

    tags = legacy.downloader.getTags(webPlayback)
    cover_url = legacy.downloader.getCoverUrl(song_info['attributes']['artwork']['url'])
    cover_file = legacy.downloader.downloadCoverFile(cover_url)
    legacy.downloader.applyTags(remuxed_path, tags, cover_url)

    final_path = legacy.getFinalPath()
    legacy.downloader.moveToFinalPath(remuxed_path, final_path)

    song = Song(song_info, cover_file)
    song_json = song.getDataFix()

  except Exception as e:
    print('Error: ' + str(e))
    
  return song_json