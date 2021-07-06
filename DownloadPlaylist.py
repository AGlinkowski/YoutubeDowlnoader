from genericpath import exists
from pytube import Playlist, cli
from moviepy.editor import *
import os
import sys

def DownloadVideos(vid, _elementTitle, savePath):
    """Funkcja pobierająca video z elementu playlisty"""
    vid.register_on_progress_callback(cli.on_progress) #Rejestracja callback wyświetlającego progress bar
    vid.streams.get_highest_resolution().download(savePath) #Pobranie video
    sys.stdout.write("\n") #Przejście do nowej linii nie kasujące progress bar
    sys.stdout.flush()
    print("Pobrano: " + _elementTitle) #Wypisanie pobranego elementu
    
def DownloadAudios(aud, _elementTitle, savePath):
    """Funkcja pobierająca video z elementu playlisty"""
    aud.register_on_progress_callback(cli.on_progress) #Rejestracja callback wyświetlającego progress bar
    dir = aud.streams.get_audio_only().download(savePath) #Pobieranie audio i przechwycenie ścieżki z nazwą pliku
    sys.stdout.write("\n") #Przejście do nowej linii nie kasujące progress bar
    sys.stdout.flush()
    
    mp3 = AudioFileClip(dir) #Wczytanie pliku audio
    mp3.write_audiofile(dir[:-4] + ".mp3") #Konwersja audio do mp3
    mp3.close()
    os.remove(dir) #Usunięcie pierwotnego pliku audio
    print("Pobrano: " + _elementTitle) #Wypisanie pobranego elementu

#==========Początek programu============

url = input("Podaj ścieżkę do playlisty: ")
type = input("Co chcesz pobrać? v - video; a - audio: ")
if (not type in {"a", "v"}):
    sys.exit("wybrano zły typ")
    

playListElements = Playlist(url)
playListName = playListElements.title
playListCount = len(playListElements.video_urls)

print("Pobieram playlistę " +  playListName + " (" + str(playListCount) + " utworów)")

#Pobranie listy elementów w docelowej ścieżce
path = os.path.join(os.path.expanduser('~'), 'downloads\\' + playListName)
if os.path.exists(path):
    actualElements = os.listdir(path)
else:
    actualElements = []

#Pętla pobierania elementów playlisty
it = 0
for video in playListElements.videos:
    it += 1
    elementTitle = video.title
    print("Pobieram: " + str(it) + " z " + str(playListCount) + ": \"" + elementTitle + "\"")
    
    #Sprawdzenie czy dany element jest już pobrany
    elementExist = 0
    for s in actualElements:
        if (s[:-4] == elementTitle):
            if (type == "a" and s[-3:] == "mp3"): #Interesują nas tylko pliki audio w formacie mp3
                elementExist = 1
                break
            else:
                elementExist = 1
                break
    
    if (elementExist == 1):
        print("Element istnieje")
    elif (type == "v"):
        DownloadVideos(video, elementTitle, path)
    else:
        DownloadAudios(video, elementTitle, path)

    
