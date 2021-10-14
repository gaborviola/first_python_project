menuitem = 0
nevek = []
while menuitem != 3:
    menuitem = int(input("1. Uj nev rozitese\n2. Nevek listazasa\n3. Kilepes\n\nValsztasod: "))
    if menuitem == 1:
        nevek.append(input("Kerem a nevet:\n"))
    elif menuitem==2:
        print("Nevek:")
        for n in nevek:
            print(n)
    else:
        print("Bye!")

