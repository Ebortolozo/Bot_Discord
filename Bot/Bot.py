import discord
import asyncio
import Cor_elo

from discord.embeds import Embed
import segredo
import elo


COR = 0x690FC3
TOKEN = segredo.seu_token()
client = discord.Client()
 
@client.event
async def on_ready():
    print("Bot iniciado(Barulhos de robo)")
    print(client.user.name)
    print(client.user.id)
    print('Junior-------Gostosão')
 
 
@client.event
async def on_message(msg):

    if msg.content.lower().startswith("!help"):
        embed = discord.Embed(
            title="Comandos Disponiveis:",
            color=COR,
            description="- !elo <nick> - Descobre o elo de qualquer um!\n"
                        "- só tem isso por agora kkk       "
        )
        await msg.channel.send(embed=embed)


    
    if msg.content.lower().startswith("!elo"):
        nick = msg.content[5:]
        posicao = elo.descobrir_elo(nick)
        nome = str(posicao).split()[0]
        print(nome)
        color = Cor_elo.cor(nome)
        embed = discord.Embed(
            title=nick,
            description="Solo/Duo: "+ posicao,
            color = color
        )
        await msg.channel.send(embed=embed)  
              

    if msg.content.startswith("!dinheiro"):
        await msg.channel.send("Mais $1.000 pra conta.")  



client.run(TOKEN)