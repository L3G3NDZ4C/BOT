import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)



@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')
    # Mensaje de comandos disponibles
    commands_list = (
        "Comandos disponibles:\n"
        "!repeat <veces> <mensaje> — Repite el mensaje el número de veces indicado."
    )
    channel = bot.get_channel(1349550281829908554)
    await channel.send(commands_list)


@bot.command()
async def repeat(ctx, times: int, *, content='repeating...'):
    for i in range(times):
        await ctx.send(content)


bot.run("TOKEN")
