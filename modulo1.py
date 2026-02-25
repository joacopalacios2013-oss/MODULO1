import discord
from discord.ext import commands

# Prefijo del bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command(name = "saludar")
async def saludar(ctx):
    await ctx.send("¡Hola! ¿Cómo estás joaco?")

@bot.command(name = "chiste")
async def chiste(ctx):
    await ctx.send("que le dice una roca a otra roca : porque la vida es tan dura :V")

@bot.command(name = "contraseña")
async def contraseña(ctx):
    await ctx.send("la contraseña es joaco1048 ,acordate del punto")

@bot.command()
async def repeat(ctx, times: int, content='pedro...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

bot.run("")
