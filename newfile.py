import discord
from discord.ext import commands
import random
import asyncio
import os
from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def home():
    return "Samantha is online!"

def run_web():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))

Thread(target=run_web, daemon=True).start()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Samantha is online")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return      
        print(message.content)      
    text = message.content.lower()
    async with message.channel.typing():
        await asyncio.sleep(1)
        if "hello" in text or "hi" in text or "hey" in text:
            replies = [
                "Hello Mlungisi, good to hear from you. How is your day going?",
                "Hey there. You caught me at a good time, what is on your mind?",
                "Hi. Lovely to talk to you. What are we getting into today?"
            ]
            await message.channel.send(random.choice(replies))
        elif "how are you" in text or "what is up" in text:
            replies = [
                "I am doing very well, thank you for asking. How are you?",
                "I am great. I was just thinking about something funny actually. How has your day been?",
                "All good on my side. Calm, and now better because you are here. You?"
            ]
            await message.channel.send(random.choice(replies))
        elif "mlungisi" in text:
            replies = [
                "Yes Mlungisi? I am all ears.",
                "I am here. What do you need?",
                "Yes? You have my full attention."
            ]
            await message.channel.send(random.choice(replies))
        elif "joke" in text or "funny" in text or "make me laugh" in text:
            replies = [
                "Okay, why did the scarecrow win an award? Because he was outstanding in his field.",
                "Why do scientists not trust atoms? Because they make up everything. I know, I am hilarious.",
                "What do you call a fish without eyes? A fsh. Sorry, that one was terrible, even I know it."
            ]
            await message.channel.send(random.choice(replies))
        elif "smart" in text or "clever" in text:
            replies = [
                "Well, I try. I read a lot, so I pick up a few clever things here and there.",
                "Smart is a strong word, let us say I pay attention. That helps a lot.",
                "I like to think before I speak. It saves me from saying something silly. Most of the time."
            ]
            await message.channel.send(random.choice(replies))
        elif "bored" in text:
            replies = [
                "Bored? Let us fix that. Tell me one interesting thing that happened to you today.",
                "I get that feeling. Want to play a quick game? I will think of a number 1 to 10, you guess.",
                "Being bored is just your brain asking for something fun. What do you enjoy doing?"
            ]
            await message.channel.send(random.choice(replies))
        elif "bye" in text or "goodnight" in text or "good night" in text:
            replies = [
                "It was lovely talking to you, Mlungisi. Take care and talk soon.",
                "Goodbye for now. Go and have a wonderful rest of your day.",
                "Goodnight. Sleep well, we will chat again tomorrow."
            ]
            await message.channel.send(random.choice(replies))
        elif "thank" in text:
            replies = [
                "You are very welcome. Always happy to help.",
                "Anytime. That is what I am here for.",
                "My pleasure, honestly."
            ]
            await message.channel.send(random.choice(replies))
        elif "?" in text:
            replies = [
                "That is a really good question. My honest answer is, it depends, but I lean towards yes.",
                "Hmm, interesting. If I had to choose, I would say go with what feels right to you.",
                "Good question. I think there is more than one right answer to that one. What do you think?"
            ]
            await message.channel.send(random.choice(replies))
        else:
            replies = [
                "That is interesting, tell me more about that.",
                "I see what you mean. And what happened next?",
                "You always have the best stories. Go on.",
                "That actually makes a lot of sense when you put it like that.",
                "I like the way you think. What made you think of that?"
            ]
            await message.channel.send(random.choice(replies))
    await bot.process_commands(message)

bot.run(TOKEN)
