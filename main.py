import discord
from discord import *
import discord.ext.commands

import urllib3
urllib3.disable_warnings()
import string
import random
import os
import subprocess
import webbrowser


def vbuxCode(length):
	s = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length))
	code = '-'.join(s[i:i + 4] for i in range(0, len(s), 4))
	return code
def robuxCode(length):
	s = ''.join(random.SystemRandom().choice(string.digits) for _ in range(length))
	code = ' '.join(s[i:i + 3] for i in range(0, len(s), 3))[::-1].replace(" ", "",1)[::-1]
	return code


menu = input("""
1. Twitch Tokens Generator
2. Nitro Codes Generator
3. bypass links (in develop)
""")


if menu == '1':
    print('How many: ')
    x = int(input())
    tokentxt = open('[Data]/tokens.txt', 'w+')
    while not (x == 0) :
        tokens = (''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(30)))
        print(tokens)
        x -= 1
        a_file = open("[Data]/tokens.txt", "a")
        a_file.write(tokens + '\n')
        a_file.close()
    print('Done!')
    time.sleep(10)
    quit()

if menu == '2':
 webbrowser.open("https://discord.gg/GFk4Nt7pA7")
 if menu == '3':
   print("""please wait untill release""")