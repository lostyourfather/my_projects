from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

map = open("map2.osm", 'r', encoding="utf8")
soup = BeautifulSoup(map, "lxml")
cnt = 0
cnt2 = 0

for node in soup.find_all("node"):
    for tag in node("tag"):
        if tag["k"] == "amenity" and tag["v"] == "fuel":
            cnt+=1
for way in soup.find_all("way"):
    for tag in way("tag"):
        if tag["k"] == "amenity" and tag["v"] == "fuel":
            cnt+=1
print(cnt)