with open("numbers.txt", encoding="utf-8", mode="w") as f:
    for i in range(10):
        f.write(f"Szam: {i}\n")
