import discord
import random
from discord.ext import commands
# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
bot = commands.Bot(command_prefix='',intents=intents)
import os

sayılar=[1,2,3]
@bot.event
async def on_ready():
    print(f'Aktifleştirme ve veri aktarma başarılı! Aktifleştirilen ve veri aktarılan yazılımın ismi: {bot.user}')
@bot.command()
async def Merhaba(ctx):
        await ctx.send("Merhaba!")
@bot.command()
async def taşkağıtmakasoyunuzamanı(ctx):
        await ctx.send("Tamam!")
        await ctx.send("taş mı kağıt mı makas mı?")
@bot.command()
async def tahminoyunuzamanı(ctx):
        await ctx.send("Tamam!")
        await ctx.send("4 ve 6 arasında bir sayı seç! (4 ve 6 da dahil! Ve başına, t yaz! örneğin, t4 gibi!)")
@bot.command
async def t4(ctx):
       sonuc=random.randint(4,6)
       if sonuc==4:
              await ctx.send("kazandın!")
       if sonuc==5:
              await ctx.send('kaybettin!')
       if sonuc==6:
              await ctx.send('kaybettin!')
@bot.command
async def t5(ctx):
       sonuc=random.randint(4,6)
       if sonuc==4:
              await ctx.send("kaybettin!")
       if sonuc==5:
              await ctx.send('kazandın!')
       if sonuc==6:
              await ctx.send('kaybettin!')
@bot.command
async def t6(ctx):
       sonuc=random.randint(4,6)
       if sonuc==4:
              await ctx.send("kaybettin!")
       if sonuc==5:
              await ctx.send('kaybettin!')
       if sonuc==6:
              await ctx.send('kazandın!')
@bot.command()
async def taş(ctx):
        sonuc=random.choice(sayılar)
        if sonuc==1:
               await ctx.send('Berabere! Bir daha deneyebilirsin!')
        if sonuc==2:
               await ctx.send('KAZANDINNNNNN!')
        if sonuc==3:
               await ctx.send('kaybettin! bir daha dene!')
@bot.command()
async def makas(ctx):
        sonuc=random.choice(sayılar)
        if sonuc==1:
               await ctx.send('kaybettin! bir daha dene!')
        if sonuc==2:
               await ctx.send('Berabere! Bir daha deneyebilirsin!')
        if sonuc==3:
               await ctx.send('KAZANDINNNNNN!')
@bot.command()
async def mem(ctx):
       name=random.choice(os.listdir('Resimler'))
       with open(f'Resimler/{name}', 'rb') as f:
              picture = discord.File(f)
       await ctx.send(file = picture)    
@bot.command()
async def kağıt(ctx):
        sonuc=random.choice(sayılar)
        if sonuc==1:
               await ctx.send('KAZANDINNNNNN!')
        if sonuc==2:
               await ctx.send('kaybettin! bir daha dene!')
        if sonuc==3:
               await ctx.send('Berabere! Bir daha deneyebilirsin!')
@bot.command()
async def merhaba(ctx):    
        await ctx.send("Merhaba!")
@bot.command()
async def görüşürüz(ctx):
        await ctx.send('Görüşürüz!!!')
bot.run('botun tokeni')
