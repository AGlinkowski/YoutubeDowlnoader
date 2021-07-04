from pytube import Playlist
from moviepy.editor import *
import os

url = input("Podaj ścieżkę do playlisty: ")
p = Playlist(url)
audioName = p.title
playlistCount = len(p.video_urls)
print("Pobieram playlistę " +  audioName + " (" + str(playlistCount) + " utworów)")
it = 0

for video in p.videos:
    it += 1
    print("Pobieram: " + str(it) + " z " + str(playlistCount))
    dir = video.streams.get_audio_only().download(os.path.join(os.path.expanduser('~'), 'downloads\\') + audioName)
    mp3 = AudioFileClip(dir)
    mp3.write_audiofile(dir[:-4] + ".mp3")
    mp3.close()
    os.remove(dir)
    print(dir)
    