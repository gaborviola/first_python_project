from json import load

file = open("characters.json")
content = load(file)

characters = content["characters"]
for c in characters:
    print(c["characterName"])

