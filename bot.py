import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from services.captionService import caption
from services.videoService import get_random_video, mark_as_sent

load_dotenv()

VIDEO_FOLDER = "YOUR VIDEOS FOLDER"
SENT_FOLDER = "YOUR SENT FOLDER"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def post(ctx):
    video = get_random_video(VIDEO_FOLDER)
    if video is None:
        await ctx.send("No videos found.")
        return

    text = caption(video)
    await ctx.send(text, file=discord.File(video))
    mark_as_sent(video, SENT_FOLDER)


bot.run(os.getenv("YOUR DISCORD TOKEN"))