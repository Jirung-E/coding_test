string = input()
bomb = input()
length = len(string)

while True:
    string = string.replace(bomb, "")
    if length == len(string):
        break
    length = len(string)

print(string)