from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import math

def getsqr(coordlist):
    baselat = coordlist[0][0]
    baselon = coordlist[0][1]
    degreelen = 111300
    newcoord = []
    for now in coordlist:
        newcoord.append(((now[0] - baselat) * degreelen, (now[1] - baselon) * degreelen * math.sin(baselat)))
    sqr = 0
    for i in range(len(newcoord) - 1):
        sqr += newcoord[i][0] * newcoord[i + 1][1] - newcoord[i + 1][0] * newcoord[i][1]
    sqr += newcoord[-1][0] * newcoord[0][1] - newcoord[0][0] * newcoord[-1][1]
    return abs(sqr)
print()

map = open("squard_of_road_map.osm", 'r', encoding="utf8")
soup = BeautifulSoup(map, "html.parser")
mylist = list()
mysit = list()
mydict = {}
for way in soup.find_all("way"):
    for nd in way.find_all("nd"):
        mylist.append(nd["ref"])
        for node in soup.find_all("node"):
            if node["id"]== nd["ref"]:
                a = float(node['lat'])
                b = float(node["lon"])
                sit = (a, b)
                mysit.append(sit)
    if mylist[0] == mylist[-1]:
        for tag in way.find_all("tag"):
            if tag["k"]=="building":
                #print(way['id'])
                #print(mysit)
                mydict[way["id"]] = getsqr(mysit)
    mylist = list()
    mysit = list()
print(mydict.items())

