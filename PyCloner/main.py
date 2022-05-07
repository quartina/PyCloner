mytitle = "PY Cloner - Developed by quartina#7225"
from os import system
system("title "+mytitle)
import psutil
from pypresence import Presence
import time
import sys
client_id = '843570016280772619'
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from serverclone import Clone

client = discord.Client()
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{Fore.RED}

                                    ██╗░░░░░██╗░░░██╗░█████╗░  ░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
                                    ██║░░░░░██║░░░██║██╔══██╗  ██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
                                    ██║░░░░░██║░░░██║███████║  ██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██████╔╝
                                    ██║░░░░░██║░░░██║██╔══██║  ██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██╔══██╗
                                    ███████╗╚██████╔╝██║░░██║  ╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██║░░██║
                                    ╚══════╝░╚═════╝░╚═╝░░╚═╝  ░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
{Style.RESET_ALL}
                                                            {Fore.MAGENTA}Developed by: quartina#7225{Style.RESET_ALL}
        """)
token = input(f'Enter your account token:\n >')
guild_s = input('Enter the discord id you want to copy:\n >')
guild = input('Enter where you want to copy the server you have chosen:\n >')
input_guild_id = guild_s  
output_guild_id = guild  
token = token  


print("  ")
print("  ")

@client.event
async def on_ready():
    extrem_map = {}
    print(f"Loggato in: {client.user}")
    print("Server Cloner")
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    print(f"""{Fore.GREEN}


                                            ░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
                                            ██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
                                            ██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██║░░██║
                                            ██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██║░░██║
                                            ╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██████╔╝
                                            ░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═════╝░

    {Style.RESET_ALL}""")
    await asyncio.sleep(5)
    client.close()


client.run(token, bot=False)
