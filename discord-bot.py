import time

from discord.ext import commands
import discord
import DungeonMaster as DM

BOT_TOKEN = "MTIwODg5NTU3MzMyMzk0ODAzMg.G91OUQ.97oj7rFXnuj_yQcQTdsoVXhm0r1vqM4Mvqy57E"
CHANNEL_ID = 1208897923710984212

# commands are preceded by '!'
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("testing testing 1 2 3")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("The Weave Shivers")


# adds numbers
@bot.command()
async def Add(ctx, *arr):
    await ctx.send(f"Sum = {DM.add(arr)}")


# roll dice
@bot.command()
async def Roll(ctx, input):
    await ctx.send(DM.roll(input))


@bot.command()
async def Wiki(ctx):
    output = DM.wiki()

    for line in output:
        await ctx.send(line.text)
    await ctx.send("Complete!")


@bot.command()  # issue with spells that have tables (type ul)
async def Spell(ctx, *arr):
    input = ""
    for word in arr:
        input += f"-{word}"
    input = input[1:].lower()
    output = DM.scrapeSpell(input)

    for line in output:
        await ctx.send(line.text)
        time.sleep(0.35)

    await ctx.send("Complete!")


@bot.command()  # issue with spells that have tables (type ul)
async def Feat(ctx, *arr):
    input = ""
    for word in arr:
        input += f"-{word}"
    input = input[1:].lower()
    output = DM.scrapeFeat(input)

    for line in output:
        await ctx.send(line.text)
    await ctx.send("Complete!")


@bot.command()  # issue with spells that have tables (type ul)
async def Race(ctx, *arr):
    input = ""
    for word in arr:
        input += f"-{word}"
    input = input[1:].lower()
    output = DM.scrapeRace(input)
    '''
    for line in output:
        await ctx.send(line.text)
        '''
    await ctx.send("Complete!")

@bot.command()
async def Class(ctx, input):
    input = input.lower()
    output = DM.scrapeClass(input)
    await ctx.send(output[0])
    await ctx.send(output[1])
    await ctx.send(output[2])
    await ctx.send("Complete!")


bot.run(BOT_TOKEN)
