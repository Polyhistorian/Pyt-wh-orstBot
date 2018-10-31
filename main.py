import discord
import command_preprocessor
import json

try:
    with open('config.json') as json_data_file:
        data = json.load(json_data_file)
except FileNotFoundError:
    print('You have to copy the example_config.json to a file named config.json and place in the required details.')
    exit(1)

try:
    token = str(data["token"])
    # OwnerID = data["OwnerID"] #Unused for the moment.
except KeyError:
    print("config.json is malformed please fix the file structure.")
    exit(1)


client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    test_game = discord.Game(name="my creators ramblings", type=2)
    await client.change_presence(game=test_game)


@client.event
async def on_message(message):
    await command_preprocessor.process(message, client)


client.run(token)
