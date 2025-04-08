from discord.ext import commands
import discord

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="button")
    async def button(self, ctx):
        view = discord.ui.View()
        button = discord.ui.Button(label="Click Me!", style=discord.ButtonStyle.green)

        async def button_callback(interaction):
            await interaction.response.send_message("You clicked the button!", ephemeral=True)

        button.callback = button_callback
        view.add_item(button)
        await ctx.send("Click the button below!", view=view)

async def setup(bot):
    await bot.add_cog(Fun(bot))
