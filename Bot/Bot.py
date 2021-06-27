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
        Solo_duo = posicao[0]
        flex = posicao[1]
        nivel = posicao[2]
        Solo_duo = str(Solo_duo).split()[0]
        print(Solo_duo)
        frase_1 = "Solo/Duo: "+ Solo_duo
        frase_2 = "Flex: " + flex
        frase_3 = "Nivel: " + nivel
        color = Cor_elo.cor(Solo_duo)
        embed = discord.Embed(
            title=nick,
            description = frase_1 + "\n" + frase_2 + "\n" + frase_3,
            
            color = color
        )
        await msg.channel.send(embed=embed)  
              

    if msg.content.startswith("!dinheiro"):
        await msg.channel.send("Mais $1.000 pra conta.")  



client.run(TOKEN)