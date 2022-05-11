import discord
import requests
import json
import random

client=discord.Client()

def get_quote():
    response=requests.get("https://zenquotes.io/api/random")
    json_data=json.loads(response.text)
    quote=json_data[0]['q']
    return(quote)


nice_words=["good","better","excellent","great","nice"]
nice_replies=["Ho hoo!","way to go my bro","Ohh yeah","Ohh yes",":-)"]

@client.event
async def on_ready():
    print('You have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author==client.user:
        return
    
    if message.content.startswith('$Hello'):
        await message.channel.send('Hello! I am Phoe , nice to meet you')
    
    if message.content.startswith('$inspire'):
        quote=get_quote()
        await message.channel.send(quote)
    for word in nice_words:
        if word in message.content:
              await message.channel.send(nice_replies[nice_words.index(word)])
token_d=''
client.run(token_d)
