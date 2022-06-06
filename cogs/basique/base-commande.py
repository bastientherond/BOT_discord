from discord.ext import commands
import discord
import platform

class Base(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong :)')

    @commands.command()
    async def botinfo(self, context):
        embed = discord.Embed(
            description="Mon premier BOT (https://github.com/bastientherond/BOT_discord)",
            color=0x9C84EF
        )
        embed.set_author(
            name="Bot information"
        )
        embed.add_field(
            name="proprio:",
            value="ɳααɾσ_O#1575",
            inline=True
        )
        embed.add_field(
            name="Version de python:",
            value=f"{platform.python_version()}",
            inline=True
        )
        embed.add_field(
            name="Prefix:",
            value=f"/ (Commande de base) ou {self.bot.config['prefix']} pour les commandes propres à ce bot.",
            inline=False
        )
        embed.set_footer(
            text=f"Demandé par {context.author}"
        )
        await context.send(embed=embed)

    @commands.command()
    async def clear(self, ctx, amount):
        await ctx.channel.purge(limit=int(amount))

def setup(bot):
    bot.add_cog(Base(bot))