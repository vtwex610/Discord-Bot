from discord.ext import commands
import discord

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx):
        await ctx.send(f"Pong! Latency: {round(self.bot.latency * 1000)}ms")

    @commands.command(name="say")
    async def say(self, ctx, *, message):
        await ctx.send(message)

async def setup(bot):
    await bot.add_cog(General(bot))
