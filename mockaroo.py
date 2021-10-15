from json import load

file = open("MOCK_DATA.json", encoding="utf-8")
content = load(file)

#for c in content:
#    print(c["ip_address"])

# for c in content:
#     print(c["ip_address"].split(".")[0])

min = 255
for c in content:
    ip_pref = int(c["ip_address"].split(".")[0])
    if int(c["ip_address"].split(".")[0]) < min:
        min = ip_pref
print(min)
