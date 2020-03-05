from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
mylist = list(input().split())
mylist = list(map(float, mylist))
minLat = mylist[0]
minLon = mylist[1]
maxLat = mylist[2]
maxLon = mylist[3]
cnt = int(input())
deltaLat = (maxLat-minLat)/cnt
deltaLon = (maxLon-minLon)/cnt
for i in range(cnt):
    for j in range(cnt):
        nminLat = minLat+deltaLat*i
        nmaxLat = minLat+deltaLat*(i+1)
        nminLon = minLon+deltaLon*j
        nmaxLon = minLon + deltaLon * (j + 1)
        print(nminLat, nminLon, nmaxLat, nmaxLon)
