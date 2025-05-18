import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Contraseñas guardadas en memoria
contraseñas_guardadas = []

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')
    channel = bot.get_channel(1349550281829908554)
    if channel:
        await channel.send("Bot iniciado. Usa !comandos para ver lo que puedo hacer.")

@bot.command()
async def repetir(ctx, veces: int, *, mensaje: str):
    for _ in range(veces):
        await ctx.send(mensaje)

@bot.command()
async def comandos(ctx):
    await ctx.send(
        "Comandos disponibles:\n"
        "!repetir <veces> <mensaje> - Repite un mensaje.\n"
        "!generar <longitud> - Genera una contraseña.\n"
        "!ver - Muestra las contraseñas guardadas."
    )

@bot.command()
async def generar(ctx, longitud: int = 12):
    if longitud < 4 or longitud > 64:
        await ctx.send("Por favor, elige una longitud entre 4 y 64.")
        return
    contraseña = "".join(random.choice(caracteres) for _ in range(longitud))
    contraseñas_guardadas.append(contraseña)
    await ctx.send(f"Contraseña generada: `{contraseña}`")

@bot.command()
async def ver(ctx):
    if contraseñas_guardadas:
        lista = "\n".join(f"{i+1}: {c}" for i, c in enumerate(contraseñas_guardadas))
        await ctx.send(f"Contraseñas guardadas:\n{lista}")
    else:
        await ctx.send("No hay contraseñas guardadas aún.")



bot.run("TOKEN")
