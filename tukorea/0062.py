from typing import List, Dict

class Music:
    def __init__(self, id: int, play: int):
        self.id = id
        self.play: int = play

class Album:
    def __init__(self):
        self.accumulated_play = 0
        self.music: List[Music] = []

    def add(self, music: Music):
        self.music.append(music)
        self.accumulated_play += music.play


N = int(input())

album: Dict[str, Album] = {}
for num in range(N):
    genre, play = input().split()

    if genre not in album.keys():
        album[genre] = Album()
    album[genre].add(Music(num, int(play)))

for i in range(2):
    genre = max(album, key=lambda k: album[k].accumulated_play)
    for music in sorted(album[genre].music, key=lambda x: x.play, reverse=True)[:2]:
        print(music.id)
    del album[genre]