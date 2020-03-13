import requests
import re
from bs4 import BeautifulSoup

url = input("Defina a URL: ")
keyword = input("Palavra chave: ")
depth = int(input("Defina a profundidade: "))

lista_links = []                                                                    #Cria lista vazia para armazenas os links
lista_rank = []                                                                     #Cria lista vazia para armazenas os ranks

def pesquisa(url, keyword, depth):  
    urlGet = requests.get(url)                                                      #Recebe a requisição get
    keyword = keyword                                                               #Recebe palavra-chave
    depth = depth                                                                   #Recebe profundidade

    soup = BeautifulSoup(urlGet.text, 'lxml')                                       #Pega todo o texto da página Web
    html = soup.find('body')                                                        #Pega todo o texto dentro da tag Body
    conteudo = html.get_text()                                                      #Transforma todo o texto em uma unica String

    if re.findall(keyword, conteudo, re.IGNORECASE):                                #Verifica se tem a palavra chave no conteúdo
        position = conteudo.upper().index(keyword.upper())                          #Armazena posição index da palavra-chave
        rank = conteudo.upper().count(keyword.upper())                              #Conta quantas vezes a palavra-chave aparece na pagina
        lista_rank.append(rank)
        lista_links.append(url)

        frase = (conteudo[(position-20):(position+20)]).split('\n')                 #Forma as frase com 20 caracteres anteriores e posterioes e da um split quando tem quebra de linha
        frase = " ".join(frase)                                                     #Junta a frase separda anteriomente
        print("FRASE:",frase)                                                       #Print a frase
    else:
        print("A pagina não tem a Palavra-Chave:",keyword)
    try:
        if depth > 0:                                                               #Condicional de se profundidade for maior que 0
            depth = 0                                                               #Coloca profundidade em 0
            c = 1                                                                   #Inicia o contador em 1
            for link in soup.find_all('a'):                                         #Pega todos o links 1/2
                links = (link.get('href'))                                          #Pega todos o links 2/2
                if links is not None and links[:4] == 'http':                       #Pega somente os links que começam com http    
                    c += 1                                                          #Contador de link verdadeiro
                    print('\n')
                    print(c,"º Link")                                               #Print o numero do link                    
                    print("LINK:",links)                                            #Print o link
                    pesquisa(links, keyword, depth)                                 #Chama novamente função pesquisa
            print("-------------------------------- RANK -------------------------------- ")
            print("POS | Keywords |                 LINK ")
            for i in range(len(lista_links)):                                       #For com o tamanho da lista de links
                i += 1                                                              #Contador += 1
                maior = max(lista_rank)                                             #Recebe o maior valor da lista de rank
                indice = lista_rank.index(max(lista_rank))                          #Identifica o indice do maior valor
                print("{}        {}       {}".format(i,maior,lista_links[indice]))  #Print contador, maior valor, e link correspondente ao maior valor
                lista_rank.pop(indice)                                              #Remove o maior valor
                lista_links.pop(indice)                                             #Remove o link correpondente ao maior valor
    except:
            print("-------------------------------- RANK -------------------------------- ")
            print("POS | Keywords |                 LINK ")
            for i in range(len(lista_links)):                                       #For com o tamanho da lista de links
                i += 1                                                              #Contador += 1
                maior = max(lista_rank)                                             #Recebe o maior valor da lista de rank
                indice = lista_rank.index(max(lista_rank))                          #Identifica o indice do maior valor
                print("{}        {}       {}".format(i,maior,lista_links[indice]))  #Print contador, maior valor, e link correspondente ao maior valor
                lista_rank.pop(indice)                                              #Remove o maior valor
                lista_links.pop(indice)                                             #Remove o link correpondente ao maior valor
pesquisa (url, keyword, depth)