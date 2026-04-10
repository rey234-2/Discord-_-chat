import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def nasilsin(ctx):
    await ctx.send('Ben bir yapay zeka chat botuyum. Nasıl yardımcı labilirim?')
@bot.command()
async def yazı_tura(ctx):
    sonuc = random.choice(["Yazı", "Tura"])
    await ctx.send("Para havada dönüyor... Ve sonuç: **(sonuc)**! 🪙")
@bot.command()
async def zar_at(ctx):
    zar = random.randint(1, 6)
    await ctx.send("Zar atıldı: 🎲 **(zar)** geldi!")
@bot.command()
async def selamla(ctx):
    await ctx.send("Ooo hoş geldin ! Bugün seni çok enerjik gördüm. 😎")    
@bot.command()
async def tavsiye(ctx):
    tavsiyeler = [
        "Bugün kendine bir iyilik yap ve bol su iç! 💧",
        "Kod yazarken hata alırsan derin bir nefes al, sorun mutlaka çözülür. 💻",
        "Biraz ekran başından uzaklaşıp gözlerini dinlendirmeye ne dersin? ✨"
    await ctx.send(random.choice(tavsiyeler))
@bot.command()
async def temizle(ctx, miktar=5):
    await ctx.channel.purge(limit=miktar + 1)
    await ctx.send(f"🧹 {miktar} adet mesaj süpürüldü!", delete_after=3) 
 @bot.command(name="soru")
async def sekiz_ball(ctx, *, soru):
    cevaplar = [
        "Kesinlikle evet! ✅",
        "Pek sanmıyorum... ❌",
        "Şu an buna cevap veremem, işlemcim ısınıyor. 🔥",
        "Belki de başka bir zaman sormalısın. ✨",
        "Geleceği pek parlak görmüyorum dostum. 💀",
        "Evet, ama dikkatli olmalısın! ⚠️"
    ]
    await ctx.send("Soru: Cevap: {random.choice(cevaplar)}")    
@bot.event
async def on_member_join(member):
    if channel:
        await channel.send(f"Hoş geldin {member.mention}! Aramıza katıldığın için çok mutluyuz. 🎉")
bot.run("token")
