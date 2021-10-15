from requests import get

response = get("https://raw.githubusercontent.com/jeffreylancaster/game-of-thrones/master/data/characters.json")
content = response.json()

characters = content["characters"]
for c in characters:
    print(c["characterName"])
