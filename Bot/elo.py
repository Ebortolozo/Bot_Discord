import requests 
from bs4 import BeautifulSoup 

def descobrir_elo(nome_usuario):
    site = "https://br.op.gg/summoner/userName="
    url = site+nome_usuario
    print(url)
    res = requests.get(url)
    res.encoding = "utf-8"
    #elo Solo_duo
    soup = BeautifulSoup(res.text, "html.parser")
    elo = soup.find(class_="TierRank")
    Solo_duo = elo.text
    #elo Flex
    elo_2 = soup.find(class_="sub-tier__rank-tier")
    Flex = elo_2.text
    Flex = Flex.strip()
    #nivel
    elo_3 = soup.find(class_="Level tip")
    nivel = elo_3.text
    #print(title)
    print(Solo_duo)
    print(Flex)
    print(nivel)
    #print(res.text)