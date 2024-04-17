N = eval(input())

albums = {}
for i in range(N):
    genre, play = input().split()
    play = int(play)
    if genre not in albums:
        albums[genre] = [play, (i, play), (-1, 0)]
    else:
        albums[genre][0] += play
        if play > albums[genre][1][1]:
            albums[genre][2] = albums[genre][1]
            albums[genre][1] = (i, play)
        elif play > albums[genre][2][1]:
            albums[genre][2] = (i, play)

result = []
for key, value in albums.items():
    result.append((key, albums[key][0]))

result.sort(key=lambda x: x[1], reverse=True)

for genre, play in result:
    print(albums[genre][1][0])
    if albums[genre][2][0] != -1:
        print(albums[genre][2][0])
