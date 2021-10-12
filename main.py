from os import write
from googlesearch import search
from colorama import Fore
print(Fore.LIGHTBLUE_EX + '''
███╗   ██╗███████╗ ██████╗ ███╗   ██╗
████╗  ██║██╔════╝██╔═══██╗████╗  ██║
██╔██╗ ██║█████╗  ██║   ██║██╔██╗ ██║
██║╚██╗██║██╔══╝  ██║   ██║██║╚██╗██║
██║ ╚████║███████╗╚██████╔╝██║ ╚████║
╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝
Made by End/2y4''')
dork = input(f'[{Fore.BLUE}INPUT{Fore.WHITE}]>> ')
print(f'[{Fore.GREEN}LOADING{Fore.WHITE}] Grabbing results using google api!')
for results in search(dork, tld="com", num=50, stop=50, pause=2):
    print(f'[{Fore.RED }RESULT{Fore.WHITE}] ' + results)
