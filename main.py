import logging
import os
from enum import Enum

import discord
from discord import app_commands, ChannelType, Thread

from modules.induction_storage import InductionStore
from modules.tool import Tool

# from discord.types.channel import ChannelType
logging.getLogger().setLevel(logging.INFO)
bot_token = os.getenv('BOT_TOKEN')
guild_id = os.getenv('GUILD_ID')
if guild_id:
    guild = discord.Object(id=guild_id)
else:
    guild = None

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

induction_store = InductionStore()
# test

@tree.command(name="request_induction", description="Create a new request for an induction", guild=guild)
async def request_induction(interaction: discord.Interaction, tool: Tool):
    channel = client.get_channel(int(interaction.channel_id))
    username = interaction.user.display_name
    user_mention = interaction.user.mention

    thread = await channel.create_thread(
        name=f"{tool.name} for {username}",
        type=ChannelType.public_thread
    )
    thread_message = await thread.send(
        f"Please drop some suggested dates and times in this thread {user_mention}. The more flexibility "
        f"you have, the easier it will be for someone to provide an induction. Someone will come and "
        f"discuss as soon as we can")
    thread: Thread = thread_message.channel
    induction_store.create_induction(thread.id, tool, interaction.user)

    await interaction.response.send_message(f"Please click into the thread below {username} and have a chat")


@tree.command(name="claim", description="Offer to carry out an induction", guild=guild)
async def claim(interaction: discord.Interaction):
    thread: Thread = interaction.channel
    induction_store.claim_induction(thread.id, interaction.user)
    await interaction.response.send_message(f"Induction claimed by {interaction.user.display_name}. You legend!")


@tree.command(name="close", description="Close an induction request", guild=guild)
async def close(interaction):
    await interaction.response.send_message("Induction closed")


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=guild_id))
    print("Ready!")


client.run(bot_token)
