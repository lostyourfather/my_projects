from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

def countLinks(res):
    uniqLinks = set()
    resp = urlopen(res)  # скачиваем файл
    html = resp.read().decode('utf8')  # считываем содержимое
    soup = BeautifulSoup(html, 'html.parser')  # делаем суп
    k = 0
    for link in soup.find_all("a"):
        if link.has_attr('href'):
            s = link.get('href')
            if s.startswith('/w') and (':' not in s) and (not s.startswith('#')):
                uniqLinks.add(s)


    return uniqLinks
a = 'https://stepik.org/media/attachments/lesson/258943/Moscow.html'
b = 'https://stepik.org/media/attachments/lesson/258944/New-York.html'
ourLinks = (countLinks(a) & countLinks(b))
ourLinks = sorted(ourLinks)
for i in range(0, len(ourLinks)):
    print(ourLinks[i])