from pytube import Playlist
import os

url = input("Podaj ścieżkę do playlisty: ")
p = Playlist(url)
playlistName = p.title
playlistCount = len(p.video_urls)
print("Pobieram playlistę " +  playlistName + " (" + str(playlistCount) + " utworów)")
it = 0

for video in p.videos:
    it += 1
    print("Pobieram: " + str(it) + " z " + str(playlistCount))
    dir = video.streams.get_audio_only().download(os.path.join(os.path.expanduser('~'), 'downloads\\') + playlistName)
    print(dir)
    