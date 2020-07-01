import os
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
        
        playername = str(m).split("#")[0]
        
        pcivs = [civs.pop(0) for _ in range(int(numcivs))]
        
        civstring = ''
        for i in range(numcivs):
            civstring = civstring + pcivs[i] + " "

        response = "{}: {}".format(playername, civstring)


        await ctx.send(response)



bot.run(TOKEN)

