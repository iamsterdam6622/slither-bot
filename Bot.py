import os
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

Thread(target=run).start()
import discord
from discord.ext import commands

# Vervang de tekst tussen de haakjes door jouw eigen token
TOKEN = 'MTUzOTI2NzM4ODIzMzQ5MDUzMg.GkRVC2.Wv3X8lp1Tb-1Ip5SjaenKLXfqVTcxwrksTXT4E'

# Instellingen voor de bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Melding wanneer de bot online komt
@bot.event
async def on_ready():
    print(f'Ingelogd als {bot.user.name}')

# Een simpel testcommando: typ !hallo in Discord
@bot.command()
async def hallo(ctx):
    await ctx.send('Ik ben online en klaar voor actie!')

# Bot starten
bot.run(TOKEN)
