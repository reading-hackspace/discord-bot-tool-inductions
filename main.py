import os
from enum import Enum
from sqlite3 import Date

import discord
from discord import app_commands, ChannelType

# from discord.types.channel import ChannelType

bot_token = os.getenv('BOT_TOKEN')
guild_id = os.getenv('GUILD_ID')
if guild_id:
    guild = discord.Object(id=guild_id)
else:
    guild = None

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

class Tool(Enum):
    Laser_Cutter = 1
    PLA_Printer = 2
    Vinyl_Cutter = 3


@tree.command(name="request_induction", description="Create a new request for an induction", guild=guild)
async def request_induction(interaction: discord.Interaction, tool: Tool):

    channel = client.get_channel(int(interaction.channel_id))
    username = interaction.user.display_name
    user_mention = interaction.user.mention

    thread = await channel.create_thread(
        name=f"{tool.name} for {username}",
        type=ChannelType.public_thread
    )
    await thread.send(f"Please drop some suggested dates and times in this thread {user_mention}. The more flexibility "
                      f"you have, the easier it will be for someone to provide an induction. Someone will come and "
                      f"discuss as soon as we can")

    await interaction.response.send_message("")

    # await interaction.response.send_message(f"Induction requested for {tool} on {date}")


@tree.command(name="claim", description="Offer to carry out an induction", guild=guild)
async def claim_induction(interaction):
    await interaction.response.send_message("Induction claimed")



@tree.command(name="close", description="Close an induction request", guild=guild)
async def close_induction(interaction):
    await interaction.response.send_message("Induction closed")


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=guild_id))
    print("Ready!")


client.run(bot_token)
