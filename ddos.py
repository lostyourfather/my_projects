import requests

def ddos(sites):
	for site in sites:
		print(site)
		for i in range(0,10):
			print(requests.get(site))
			

list_of_sites = [ "http://vk.com", "http://google.com", "http://habr.com", "http://yandex.ru", "http://youtube.com"]

ddos(list_of_sites)
