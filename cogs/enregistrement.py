from pydoc import describe
from turtle import color
from discord.ext import commands
import discord

class Register(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.id = 0

    @commands.Cog.listener(name='on_ready')
    async def on_ready(self):
        print("Cog Main ready")

    @commands.command(name="register")
    async def register(self, ctx):
        await ctx.send("test ok")
    
    @commands.command()
    async def status(self, ctx):
        status = discord.Embed(name=f"Status for {ctx.author} is", description=f"{ctx.author.activities}", color=discord.Color.blue())
        await ctx.send(embed=status)

def setup(bot):
    return bot.add_cog(Register(bot))