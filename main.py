import os
import discord

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)


@bot.event
async def on_ready():
    print(f"Bot zalogowany jako {bot.user}")


@bot.event
async def on_message(message):
    # Bot nie odpowiada sam sobie
    if message.author == bot.user:
        return

    # Powtarzanie wiadomości
    if message.content:
        await message.channel.send(message.content)


bot.run(TOKEN)

