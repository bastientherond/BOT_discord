from discord.ext import commands

class Cour(commands.Cog):

    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot



def setup(bot):
    bot.add_cog(Cour(bot))