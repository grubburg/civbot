import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random
import civmeta

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix='!')


@bot.command(name="draft")
async def draft(ctx, numcivs):
    channel = bot.get_channel(480628202956390410)

    n = len(channel.members)
    numcivs = int(numcivs)
    civs = random.sample(civmeta.civs, len(civmeta.civs))

    for i, m in enumerate(channel.members):
        
        playername = ("**" + str(m).split("#")[0] + "**")
        
        pcivs = [civs.pop(0) for _ in range(int(numcivs))]
        
        civstring = ''
        for i in range(numcivs):
            

            emoji = str(discord.utils.get(ctx.guild.emojis, name=pcivs[i][0]))

            newciv = ("\t\t"+ emoji + random.choice(pcivs[i][1]) + emoji)
            
            civstring = civstring + newciv

        response = "{}: {}".format(playername, civstring)


        await ctx.send(response+ "\n" + "="*64)



@bot.command(name="mapvote")
async def mapvote(ctx):
    channel = bot.get_channel(480628202956390410)
    n = len(channel.members)

    worldagereacts = [""]


    await ctf.send("WorldAge (New/Standard/Old)")




"""
Polling function:

- World Age
    - New
    - Standard
    - Old
    - Random

- Map Type
    - Pangea
    - Continents
    - Fractal
    - Continents/Islands
    - Small Continents
    
- Temperature
    - Cold
    - Standard
    - Hot
- Rainfall
    - Arid
    - Standard
    - Wet
- Sealevel
    - Low
    - Standard
    - High

"""




bot.run(TOKEN)

