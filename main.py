import requests
import requests_cache
import re
from bs4 import BeautifulSoup


url = input("Defina a URL: ")
keyword = input("Palavra chave: ")
depth = int(input("Defina a profundidade: "))


def pesquisa(url, keyword, depth):  
    url = requests.get(url)
    keyword = keyword
    depth = depth

    soup = BeautifulSoup(url.text, 'lxml')                      #Pega todo o texto da página Web
    html = soup.find('html')                                    #Pega todo o texto dentro da tag HTML
    conteudo = html.get_text()                                  #Transforma todo o texto em uma unica String
    

    if re.findall(keyword, conteudo, re.IGNORECASE):            #Verifica se tem a palavra chave no conteúdo
        x  = re.findall(keyword, conteudo, re.IGNORECASE)       #Armazena de todas as ocorrencias
        position = conteudo.upper().index(keyword.upper())      #Armazena posição index da palavra-chave
        #rank = conteudo.count(keyword)                         #Conta quantas vezes a palavra-chave aparece na pagina
        print("A pagina tem a Palavra-Chave:",keyword)
        print(conteudo[(position-20):(position+20)])            #Print 20 caracteres anteriores e posterioes
    else:
        print("A pagina não tem a Palavra-Chave:",keyword)
    
    if depth > 0:
        depth = 0
        c = 1
        for link in soup.find_all('a'):                         #Pega todos o links 1/2
            links = (link.get('href'))                          #Pega todos o links 2/2
           # if links[0:4] == 'http':                           #Pega somente os links que começam com http
            if links is not None and links[:4] == 'http':       #Pega somente os links que começam com http
                c += 1
                print('\n')
                print(c,"º Link")
                print(links)
                pesquisa(links, keyword, depth)
            
pesquisa (url, keyword, depth)