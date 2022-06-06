from discord.ext import commands
import discord

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            description="Voicis la listes de toutes les commandes actuellement dispo pour toi chakal ;)",
            color=0x9C84EF
        )
        embed.set_author(
            name="Liste des commandes"
        )
        embed.add_field(
            name="!ping",
            value="Répond pong",
            inline=False
        )
        embed.add_field(
            name="!botinfo",
            value="Donne toute les informations à propos du bot.",
            inline=False
        )
        embed.add_field(
            name="!clear {nombre de msg a supp}",
            value="Supprime un nombre donnée de messages.",
            inline=False
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))