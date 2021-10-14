counter = 1
min = 0
list = []
while counter<=5:
    inp = int(input(f"Kerem a {counter}. szamot: "))
    if counter==1 or inp<min:
        min = inp
    list.append(inp)
    counter += 1
print("Kaptam:", list)
print("A legkisebb:", min)

