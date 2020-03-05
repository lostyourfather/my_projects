import xmltodict

fin = open('map (4).xml', 'r', encoding='utf8')
xmltext = fin.read()
fin.close()
cnt = 0
xml = xmltodict.parse(xmltext)
for node in xml["osm"]["node"]:
    for tag in node:
        if tag == "tag":
            if isinstance(node['tag'], list):
                for i in node["tag"]:
                    if (i["@k"]) == "shop":
                       print("L.marker([" + node['@lat'] +", "+ node['@lon']+ "]).addTo(mymap);")
            elif isinstance(node['tag'], dict):
                if node['tag']["@k"]=="shop":
                    print("L.marker([" + node['@lat'] +", "+ node['@lon']+ "]).addTo(mymap);")
