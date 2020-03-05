from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
import csv

url = urlopen("https://stepik.org/media/attachments/lesson/258944/New-York.html")
selector = "wikitable collapsible collapsed"
tag = "table"
doc = open("result.csv", 'w', encoding="utf-8")
html = url.read().decode("utf-8")
soup = BeautifulSoup(html, 'html.parser')
table = soup.findAll(tag, { "class" : selector }, limit=3)

for n in table:
    rows = n.findAll("tr")
    for i in rows:
        for j in i.findAll("th"):
            print(j.text.strip(), end=",")
        for k in i.findAll("td"):
            print(k.text.strip(), end=",")
        print()
    print()
    print()