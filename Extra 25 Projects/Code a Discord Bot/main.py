# import discord
# import os
# from dotenv import load_dotenv
# import requests
# import json
# import random
# from replit import db

# # Load environment variables from .env.local file
# load_dotenv('.env.local')

# # Create an instance of Intents and enable message_content
# intents = discord.Intents.default()
# intents.message_content = True  # Important for reading message content

# # Initialize the client with intents
# client = discord.Client(intents=intents)

# sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

# starter_encouragments = [
#     "Cheer up!",
#     "Hang in there.",
#     "You are a great person / bot"
# ]


# # Updated

# def get_quote():
#     response = requests.get("https://zenquotes.io/api/random")
#     json_data = json.loads(response.text)
#     quote = json_data[0]['q'] + " -" + json_data[0]["a"]
#     return quote

# def update_encouragments(encouraging_message):
#     if "encouragements" in db.keys():
#         encouragements = db["encouragements"]
#         encouragements.append(encouraging_message)
#         db["encouragements"] = encouragements
#     else:
#         db["encouragements"] = [encouraging_message] 

# def delete_encouragment(index):
#     encouragements = db["encouragements"]
#     if len(encouragements) > index:
#         del encouragements[index]
#         db["encouragements"] = encouragements  

# @client.event
# async def on_ready():
#     print(f'We have logged in as {client.user}')

# @client.event
# async def on_message(message):
#     print(f'Message received: {message.content}')  # Debug: print incoming messages

#     # Ignore messages from the bot itself
#     if message.author == client.user:
#         return
    
#     msg = message.content

#     # Respond to $hello
#     # if message.content.startswith('$hello'):
#     if msg.startswith('$inspire'):
#         quote = get_quote()
#         # await message.channel.send('Hello!')
#         await message.channel.send(quote)

#     options = starter_encouragments
#     if "encouragements" in db.keys():
#         options = options + db["encouragements"]

    
#     if any(word in msg for word in sad_words):
#         await message.channel.send(random.choice(options))

#     if msg.startswith("$new"):
#         encouraging_message = msg.split("$new",1)[1]
#         update_encouragments(encouraging_message)
#         await message.channel.send("New encouraging message added.")

#     if msg.startswith("$del"):
#         encouragements = []
#         if "encouragements" in db.keys():
#             index = int(msg.split("$del", 1)[1])
#             delete_encouragment(index)
#             encouragements = db["encouragements"]
#         await message.channel.send(encouragements)    



# # Run the bot using the token from the environment variable
# client.run(os.getenv('TOKEN'))

import discord
import os
from dotenv import load_dotenv
import requests
import json
import random
import sqlite3
from keep_alive import keep_alive

# Load environment variables from .env.local file
load_dotenv('.env.local')

# Create an instance of Intents and enable message_content
intents = discord.Intents.default()
intents.message_content = True  # Important for reading message content

# Initialize the client with intents
client = discord.Client(intents=intents)

# Setup SQLite database connection
conn = sqlite3.connect('encouragements.db')  # Connect to the SQLite database (or create it if it doesn't exist)
cursor = conn.cursor()

# Create the encouragements table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS encouragements (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    message TEXT)''')

# Create the responding table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS responding (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    value BOOLEAN)''')
conn.commit()

# Predefined words and messages
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]
starter_encouragments = [
    "Cheer up!",
    "Hang in there.",
    "You are a great person / bot"
]

# Ensure 'responding' table has an entry for the bot's responding status
cursor.execute("INSERT OR IGNORE INTO responding (id, value) VALUES (1, 1)")
conn.commit()

# Function to get a random quote
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]["a"]
    return quote

# Function to add an encouraging message to the database
def update_encouragments(encouraging_message):
    cursor.execute("INSERT INTO encouragements (message) VALUES (?)", (encouraging_message,))
    conn.commit()

# Function to delete an encouraging message by ID
def delete_encouragment(index):
    cursor.execute("DELETE FROM encouragements WHERE id = ?", (index,))
    conn.commit()

# Fetch all encouragement messages from the database
def get_encouragements():
    cursor.execute("SELECT message FROM encouragements")
    return [row[0] for row in cursor.fetchall()]

# Fetch the responding status
def get_responding_status():
    cursor.execute("SELECT value FROM responding WHERE id = 1")
    result = cursor.fetchone()
    return result[0] if result else True  # Default to True if no result

# Set the responding status
def set_responding_status(value):
    cursor.execute("UPDATE responding SET value = ? WHERE id = 1", (value,))
    conn.commit()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print(f'Message received: {message.content}')  # Debug: print incoming messages

    # Ignore messages from the bot itself
    if message.author == client.user:
        return
    
    msg = message.content

    # Respond to $inspire
    if msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    # Check if bot is allowed to respond
    if get_responding_status():

        # Get encouragements from both the starter list and the database
        options = starter_encouragments + get_encouragements()

        if any(word in msg for word in sad_words):
            await message.channel.send(random.choice(options))

        if msg.startswith("$new"):
            encouraging_message = msg.split("$new", 1)[1]
            update_encouragments(encouraging_message)
            await message.channel.send("New encouraging message added.")

        if msg.startswith("$del"):
            try:
                index = int(msg.split("$del", 1)[1])
                delete_encouragment(index)
                await message.channel.send(f"Deleted encouragement at index {index}.")
            except ValueError:
                await message.channel.send("Please provide a valid index to delete.")

        if msg.startswith("$list"):
            encouragements = get_encouragements()
            await message.channel.send(encouragements)

        if msg.startswith("$responding"):
            value = msg.split("$responding", 1)[1].strip().lower()

            if value == "true":
                set_responding_status(True)
                await message.channel.send("Responding is on.")
            elif value == "false":
                set_responding_status(False)
                await message.channel.send("Responding is off.")

keep_alive()
# Run the bot using the token from the environment variable
client.run(os.getenv('TOKEN'))
