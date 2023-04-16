import discord
from discord.ext import commands
import datetime
import time

bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())
bot.work_start_time = datetime.datetime.now()

token = "MTA4Njg3NzQ5MjIzMDUwNDU0OA.Gomk-z.XZU-cc7RDUnI8-0dGPpelexEWQ9DbHGjLF6zvY"

def is_user(user_id):
    def predicate(ctx):
        return ctx.author.id == user_id
    return commands.check(predicate)

@bot.event
async def on_ready():
    print('봇이 실행됨 ㅋ'.format(bot))

@bot.command()
@is_user(898195502443675681)
async def 출근(ctx):
    now = datetime.datetime.now()
    work_time_delta = now - ctx.bot.work_start_time
    work_time_minutes = work_time_delta.total_seconds() // 60

    embed = discord.Embed(title="", description=f"{ctx.author.mention}님이 출근하셨습니다.", color=0x65D35D)
    embed.set_author(name=f"{ctx.author.display_name}#{ctx.author.discriminator}", icon_url="https://media.discordapp.net/attachments/1082276379397201974/1097023955610640457/Jett_rev_v2.jpg?width=787&height=443")
    embed.set_footer(text=f'\n출근시간: {now.strftime("%m-%d")} {now.hour}:{now.minute}')

    await ctx.send(embed=embed)

@bot.command()
@is_user(898195502443675681)
async def 퇴근(ctx):
    now = datetime.datetime.now()
    work_time_delta = now - ctx.bot.work_start_time
    work_time_minutes = work_time_delta.total_seconds() // 60

    embed = discord.Embed(title="", description=f"{ctx.author.mention}님이 퇴근하셨습니다.", color=0xFF3636)
    embed.set_author(name=f"{ctx.author.display_name}#{ctx.author.discriminator}", icon_url="https://media.discordapp.net/attachments/1082276379397201974/1097023955610640457/Jett_rev_v2.jpg?width=787&height=443")
    embed.set_footer(text=f'\n퇴근시간: {now.strftime("%m-%d")} {now.hour}:{now.minute}\n근무시간: {int(work_time_minutes)}분')

    await ctx.send(embed=embed)


bot.run(token)