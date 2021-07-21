import discord
import os
from markov_Sharon import open_and_read_file, make_chains, make_text

"""
def open_and_read_file(file_path): return string
def make_chains(text_string, n_gram): return dictionary
def make_text(chains): return string
"""

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        # Get a Markov chain
        file_as_string = open_and_read_file('green-eggs.txt')
        chains = make_chains(file_as_string, 2)
        text = make_text(chains)
        await message.channel.send(text)



TOKEN = os.environ['DISCORD_TOKEN']
client.run(TOKEN)
