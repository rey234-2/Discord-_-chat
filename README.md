@bot.command()
async def cat(ctx):
    with open('images/cat.jpg', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
