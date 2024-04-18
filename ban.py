import discord
from discord.ext import commands

#Replace 'your_bot_token' with your actual bot token
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    try:
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention} from the server.')
    except discord.Forbidden:
        await ctx.send("I don't have permission to ban members.")
    except discord.HTTPException:
        await ctx.send("An error occurred while attempting to ban the member.")

@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    try:
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention} from the server.')
    except discord.Forbidden:
        await ctx.send("I don't have permission to kick members.")
    except discord.HTTPException:
        await ctx.send("An error occurred while attempting to kick the member.")



        

#Replace 'your_bot_token' with your actual bot token
bot.run('MTIwNDQyMTYyMzU4Mzg3NTA3Mw.GS5Heb.V8ZdbUyFwkYcFzdbheAjg7PbpDOWv2V5W28wAA')