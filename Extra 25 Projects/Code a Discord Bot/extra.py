
import discord
import os
from dotenv import load_dotenv
import requests
import json
import random

# Load environment variables from .env.local file
load_dotenv('.env.local')

# Discord intents
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Sad words trigger list
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encouragments = [
    "Cheer up!",
    "Hang in there.",
    "You are a great person / bot"
]

DB_FILE = "db.json"

# Local DB functions
def load_db():
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

def update_encouragments(message):
    db = load_db()
    if "encouragements" in db:
        db["encouragements"].append(message)
    else:
        db["encouragements"] = [message]
    save_db(db)

def delete_encouragment(index):
    db = load_db()
    if "encouragements" in db and len(db["encouragements"]) > index:
        del db["encouragements"][index]
        save_db(db)

# Quote API
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]["a"]
    return quote

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print(f'Message received: {message.content}')

    if message.author == client.user:
        return

    msg = message.content
    db = load_db()

    if msg.startswith("$inspire"):
        quote = get_quote()
        await message.channel.send(quote)

    options = starter_encouragments
    if "encouragements" in db:
        options += db["encouragements"]

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(options))

    if msg.startswith("$new"):
        encouraging_message = msg.split("$new", 1)[1].strip()
        update_encouragments(encouraging_message)
        await message.channel.send("New encouraging message added.")

    if msg.startswith("$del"):
        try:
            index = int(msg.split("$del", 1)[1].strip())
            delete_encouragment(index)
            updated = load_db().get("encouragements", [])
            await message.channel.send(f"Updated list: {updated}")
        except:
            await message.channel.send("Invalid index. Usage: $del 0")

# Run the bot
client.run(os.getenv('TOKEN'))
