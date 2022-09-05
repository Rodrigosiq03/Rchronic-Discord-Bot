import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        self.help_message = '''
```
Comandos gerais:
!help - mostra todos os comandos disponiveis
!p <pesquisa> - procura a musica no youtube e começa a tocar no canal onde vc estiver. Retoma a musica se ela estiver pausada
!q - mostra a lista de musicas
!skip - pula a musica que esta sendo tocada
!clear - Para a musica que esta sendo tocada e limpa a lista de musicas
!leave - Desconecta o bot do canal de voz
!pause - pausa a musica que esta sendo tocada ou retoma caso esteja pausada
!resume - retoma a musica que esta sendo tocada
```        
        
'''
        self.text_channel_text = []

    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_text.append(channel)
        
        await self.send_to_all(self.help_message)

    async def send_to_all(self, msg):
        for text_channel in self.text_channel_text:
            await text_channel.send(msg)

    @commands.command(name='help', help='Mostra todos os comandos disponiveis')
    async def help(self, ctx):
        await ctx.send(self.help_message)

