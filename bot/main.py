import os
import discord

TOKEN = os.getenv("DISCORD_TOKEN")

print("=== TEST TOKENA ===")
print("Czy token istnieje:", TOKEN is not None)
print("Długość tokena:", len(TOKEN) if TOKEN else 0)

if not TOKEN:
    print("BLĄD: DISCORD_TOKEN nie istnieje!")
    exit()

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)


@bot.event
async def on_ready():
    print(f"Bot zalogowany jako {bot.user}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content:
        await message.channel.send(message.content)


bot.run(TOKEN)