""""
Copyright © bastientherond 2022 - https://github.com/bastientherond

Version: 1.0
"""
import discord
from discord.ext import commands, tasks
import os
import json
import platform
import random
import sys

from disnake import Guild

if not os.path.isfile("config/config.json"):
    sys.exit("'config/config.json' not found! Please add it and try again.")
else:
    with open("config/config.json") as file:
        config = json.load(file)



intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or(config["prefix"]), intents=intents, help_command=None)
bot.config = config

def load_commands(command_type: str) -> None:
    for file in os.listdir(f"./cogs/{command_type}"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"cogs.{command_type}.{extension}")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")


if __name__ == "__main__":
    load_commands("basique")
    load_commands("cour")


@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user.name}")
    print(f"Discord API version: {discord.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"En cours d'exec sur: {platform.system()} {platform.release()} ({os.name})")
    print("-------------------")
    status.start()


@tasks.loop(minutes=1.0)
async def status():
    statuses = ["avec toi!", "avec ta mère!", "écraser des beurres !"]
    await bot.change_presence(activity=discord.Game(random.choice(statuses)))



#------------------------------ ajout d'un rôle au moment du join server ----------------------#
@bot.event
async def on_member_join(member):
    print(f"{member.name} a rejoint le serv")
    status = discord.Embed(name=f"Bienvenue !", description=f"Salut {member.name}, soit le bienvenue dans ce serveur !", color=discord.Color.blue())
    channel = bot.get_channel(983442715251458109)
    await member.add_roles(member.guild.get_role(983443250058772561))
    message = await channel.send(embed=status)
    await message.add_reaction("✅")


#------------- change et supprimme un rôle en cliquant sur une emote ---------------------#
@bot.event
async def on_reaction_add(reaction, user):
    if user != bot.user:
        if reaction.emoji == "✅":
            await user.remove_roles(user.guild.get_role(983443250058772561))
            await user.add_roles(user.guild.get_role(983444963469721680))
            newResult = discord.Embed(name="Validation", description=f"Bravo {user.name}, tu peut désormais utiliser le serveur  100% !")
            await reaction.message.edit(embed=newResult)


#------------------- Vérifie les mots dans les msg posté ---------------------------------------#
@bot.event
async def on_message(message):
    if message.author == message.author.bot:
        return
    await bot.process_commands(message)

#---------------------- imprime qui a fait une commande slash ------------------------------------#


bot.run(config["token"])