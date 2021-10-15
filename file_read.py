data=[]
with open("MOCK_CSV.csv", encoding="utf-8") as f:
    linecount = 0
    for line in f:
        if linecount != 0:
            fields = line.split(",")
            item = {"name": fields[0] + " " + fields[1], "ip": fields[3].strip()}
            data.append(item)
        linecount += 1
print(data)
    