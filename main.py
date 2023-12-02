import discord
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f"Hai fatto l\\'accesso come {bot.user}")

@bot.command()
async def ciao(ctx):
    await ctx.send(f"Ciao! Sono un bot {bot.user}!")

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("MTE3MjkyODU0MDU2MDM0MzEyMQ.GW5_-V.oNEPsvEe7Dli7kjbB9-vWNjdzlTrzM_bTD4Okc")