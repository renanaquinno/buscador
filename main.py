import requests
import requests_cache
from bs4 import BeautifulSoup

url = requests.get(input("Defina a URL: "))
soup = BeautifulSoup(url.text, 'lxml')
keyword = soup.get_text(input("Palavra chave: "))


#depth = input("Defina a profundidade: ")

print(keyword)