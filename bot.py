import discord
from discord.ext import commands
import json

# Cargar configuración
with open('config.json', 'r') as f:
    config = json.load(f)

# Configuración del bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=config["prefix"], intents=intents)

# Evento: Bot listo
@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

# Comando: ping
@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

# Comando: help personalizado
@bot.command(name='help')
async def custom_help(ctx):
    embed = discord.Embed(
        title="📚 Lista de comandos",
        description="Aquí están los comandos disponibles:",
        color=discord.Color.blue()
    )
    embed.add_field(name="`!ping`", value="Responde con Pong!", inline=False)
    embed.add_field(name="`!help`", value="Muestra este mensaje de ayuda.", inline=False)
    
    await ctx.send(embed=embed)

# Ejecutar bot
bot.run(config["token"])
