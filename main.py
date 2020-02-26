import requests
import requests_cache
import re
from bs4 import BeautifulSoup

url = requests.get(input("Defina a URL: "))
keyword = input("Palavra chave: ")
depth = int(input("Defina a profundidade: "))
soup = BeautifulSoup(url.text, 'lxml')                      #Pega todo o texto da página Web
html = soup.find('html')                                    #Pega todo o texto dentro da tag HTML
conteudo = html.get_text()                                  #Transforma todo o texto em uma unica String


def pesquisa(url, keyword):  
    if re.findall(keyword, conteudo, re.IGNORECASE):        #Verifica se tem a palavra chave no conteúdo
        x  = re.findall(keyword, conteudo, re.IGNORECASE)   #Lista de todas as 
        position = conteudo.index(keyword)                  #Armazena posição index da palavra-chave
        rank = conteudo.count(keyword)                      #conta quantas vezes a palavra-chave aparece na pagina
        print("A pagina tem a Palavra-Chave",keyword)
        print(conteudo[(position-20):(position+20)])        #printa 20 caracteres anteriores e posterioes
    else:
        print("A pagina não tem a Palavra-Chave",keyword)
    
    if depth > 0:
        for link in soup.find_all('a'):                     #Pega todos o links 1/2
            links = (link.get('href'))                      #Pega todos o links 2/2
            
            print(links)


pesquisa (url,keyword)