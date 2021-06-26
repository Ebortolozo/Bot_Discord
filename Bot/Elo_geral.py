import requests 
from bs4 import BeautifulSoup 

nick_do_pessoal = ["Jogador l", "Aniac", "mich4el j4ckson"]

for n in nick_do_pessoal:
    nome_usuario = n
    site = "https://br.op.gg/summoner/userName="
    url = site+nome_usuario
    #print(url)
    res = requests.get(url)
    res.encoding = "utf-8"
    soup = BeautifulSoup(res.text, "html.parser")
    elo = soup.find(class_="TierRank")
    james = elo.text
    print(james)

