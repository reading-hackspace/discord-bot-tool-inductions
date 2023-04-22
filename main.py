import logging
import os
from datetime import datetime

import discord
from discord import app_commands, ChannelType, Thread, PrivacyLevel, EntityType
from modules.induction_storage import InductionStore
from modules.tool import Tool

# set up the discord client and app command tree
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# Get the app token and guild ID from environment
bot_token = os.getenv('BOT_TOKEN')
guild_id = os.getenv('GUILD_ID')
if guild_id:
    guild = discord.Object(id=guild_id)
else:
    guild = None

# TODO this needs to be replaced with a DB interaction instead of just being in-memory
# Create persistence mechanism for inductions
induction_store = InductionStore()


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
    induction_store.create(thread.id, tool, interaction.user)

    await interaction.response.send_message(f"Please click into the thread below {username} and have a chat")


@tree.command(name="claim", description="Offer to carry out an induction", guild=guild)
async def claim(interaction: discord.Interaction):
    thread: Thread = interaction.channel
    induction_store.claim(thread.id, interaction.user)
    induction = induction_store.get(thread.id)
    await interaction.response.send_message(f"Induction claimed by {interaction.user.display_name}. You legend!")

    await interaction.guild.create_scheduled_event(name=f"{induction.tool} induction for {induction.requestor.display_name}",
                                                   description=f"This is an automatically generated induction for the {induction.tool}",
                                                   start_time=datetime.fromisoformat('2023-04-23T14:00:00').astimezone(),
                                                   end_time=datetime.fromisoformat('2023-04-23T15:00:00').astimezone(),
                                                   privacy_level=PrivacyLevel.guild_only,
                                                   entity_type=EntityType.external,
                                                   location="rLab – Unit C1, Weldale Street, Reading, RG1 7BX",
                                                   reason="tool induction")

 #  image="https://rlab.org.uk/images/rlab_logo_coloured.png",


@tree.command(name="close", description="Close an induction request", guild=guild)
async def close(interaction):
    await interaction.response.send_message("Induction closed")


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=guild_id))
    print("Ready!")


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    client.run(bot_token)
