import sys, threading, requests,ctypes 
from googlesearch import search
from colorama import Fore


# updated 3am 10/13/21
# rewriten version by psaux org created by End

class Banner():
    _banner = f"""
                  \033[38;2;123;232;212m╔════════════════════╗
                  \033[38;2;123;232;212m║    ╔╗╔╔═╗╔═╗╔╗╔    ║
                  \033[38;2;123;232;212m║    ║║║║╣ ║ ║║║║    ║
                  \033[38;2;123;232;212m║    ╝╚╝╚═╝╚═╝╝╚╝    ║
                  \033[38;2;123;232;212m║   Made by End/2y4  ║
                  \033[38;2;123;232;212m╚════════════════════╝
   \033[38;2;123;232;212m╔══════════════════════════════════════════════════╗
   \033[38;2;123;232;212m║                                                  ║
   \033[38;2;123;232;212m║  ► python3 main.py [dork] [amount of results]    ║
   \033[38;2;123;232;212m║                                                  ║
   \033[38;2;123;232;212m╚══════════════════════════════════════════════════╝
"""
    _req = f"""
    
    
    
    """



print(Banner._banner)
try:
    _dork = sys.argv[1]
    _count = int(sys.argv[2])
except:
    print(Banner._req)
    sys.exit()

print(f'{Fore.RESET}[{Fore.GREEN}LOADING{Fore.WHITE}] Grabbing results using google api!')
print(f'[{Fore.LIGHTBLACK_EX}INFO{Fore.WHITE}] Using dork ({_dork}) and scraping {_count} times\n')

def _getstats(results):
    try:
        _stat = requests.get(results, timeout=2).status_code
    except:
        pass 
    return {
        "status": _stat
    }

def google(_dork, _count):
    count = 0
    try:
        for results in search(str(_dork), tld="com", num=_count, stop=_count):
            count += 1
            try:
                stat = _getstats(results)
                print(f'{Fore.RESET}[{Fore.RED }RESULT{Fore.WHITE}]({stat["status"]})[{count}] ' + results)
                if count > _count:
                    break
                    

                if stat["status"] == 200:
                    with open("dorked.txt", 'a+') as fil: 
                        fil.write(results+'\n')
            except:
                pass
    except Exception as e:
        print(e)
        print(f"[{Fore.RED }ERROR{Fore.WHITE}] Google error try again later!")
        sys.exit()

for _ in range(1):
    thread = threading.Thread(target=google, args=((_dork,_count)), name="Google Scrape")
    thread.start()
    thread.join()
    


