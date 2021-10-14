from discordTogether import DiscordTogether    #in import lines

togetherControl =  DiscordTogether(client)   #above on_ready message

@client.command()
async def start(ctx):
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
    await ctx.send(f"Click the blue link!\n{link}"
