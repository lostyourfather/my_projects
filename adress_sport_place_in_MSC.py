import urllib.request

import json

from urllib.request import urlopen, urlretrieve

response = urlopen( 'https://apidata.mos.ru/v1/datasets/1251/rows?api_key=71d9fefa7fccf3d4216f2963a36a8353&versionNumber=7&releaseNumber=60')

respData = response.read().decode('utf-8')

lst = json.loads(respData)

d1 = {}

d2 = {}
d3 = {}
mylist = list()

for now in lst:

    cells = now['Cells']

    AdmArea = cells['AdmArea']

    District = cells['District']

    Address = cells['Address']
    mylist.append(Address)
    if d2.get(District, 0) != 0:
        d2.get(District).append(mylist[0])
        d3 = d2.get(District)
        d1[AdmArea][District] = d3
    else:
        if d1.get(AdmArea,0) != 0:
            d2[District] = mylist
            d3[District] = mylist
            d1[AdmArea][District] = mylist
        else:
            d2[District] = mylist
            d3[District] = mylist
            d1[AdmArea] = d3

#    d1[AdmArea] = d3
    d3 ={}
    print(d1)
    mylist = list()
fout = open('outage.json', 'w', encoding='utf-8')

json.dump(d1, fout, ensure_ascii=False)

fout.close()