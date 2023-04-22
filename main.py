import os
import discord
from discord import app_commands

bot_token = os.getenv('BOT_TOKEN')
guild_id = os.getenv('GUILD_ID')

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


# TODO This guild id can be removed in production but the commands will take about an hour to register. Probably worth
# doing this as an environment variable so that it is None if not set
@tree.command(name="test_command", description="The best bot command ever!", guild=discord.Object(id=guild_id))
async def test_command(interaction):
    await interaction.response.send_message("Hello!")
    print("Ready!")

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=guild_id))
    print("Ready!")


client.run(bot_token)