from datetime import datetime
from bs4 import BeautifulSoup
from requests import get

response = get("https://index.hu/")
counter = 0
# for line in response.text.splitlines():
#     if line.find("Orbán")!=-1:
#         counter += 1
# print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), counter)
lines = BeautifulSoup(response.text, features="html.parser").get_text().splitlines()
for line in lines:
    if len(line.strip()) != 0:
        print(line)
