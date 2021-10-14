from discord.ext import commands
from discordTogether import DiscordTogether    

togetherControl =  DiscordTogether(client)   

@client.event
async def on_ready():
    print(f"Bot logged into {client.user}.")
    
    
@client.command()
async def start(ctx):
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
    await ctx.send(f"Click the blue link!\n{link}"
                   
             
client.run("BOT_TOKEN_HERE")
