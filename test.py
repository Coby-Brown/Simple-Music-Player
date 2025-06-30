import MusicList
from pathlib import Path
from playsound import playsound
musicList = MusicList.music
question = 'Minecraft'
playlist = []
for row in musicList:
    if question in row:
        playlist.append((row[0]))
playlist.append(-1)
print(playlist)
n=0
if n == 1000000:
    exit
else:
    currentSong = int(playlist[n])
    n+1
    print(n)
    print(currentSong)
    for row in musicList:
        if currentSong in row:
            play = str(row[1])
    print(play)
    playsound(play)