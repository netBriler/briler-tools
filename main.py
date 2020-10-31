from services import Ddos, Scanner, Whois
from colorama import Fore, init, ansi, Style

init()
ansi.clear_screen()

print(
    f"""{Fore.CYAN}
██████╗░██████╗░██╗██╗░░░░░███████╗██████╗░
██╔══██╗██╔══██╗██║██║░░░░░██╔════╝██╔══██╗
██████╦╝██████╔╝██║██║░░░░░█████╗░░██████╔╝
██╔══██╗██╔══██╗██║██║░░░░░██╔══╝░░██╔══██╗
██████╦╝██║░░██║██║███████╗███████╗██║░░██║
╚═════╝░╚═╝░░╚═╝╚═╝╚══════╝╚══════╝╚═╝░░╚═╝
-------------------------------------------
████████╗░█████╗░░█████╗░██╗░░░░░░██████╗
╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝
░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░
░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗
░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝
░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░
    {Fore.YELLOW}NOTE: CTRL + C If you want to Quit.{Fore.RESET}


[1] DDOS attack
[2] Open ports scanner
[3] Whois ip
"""
)

select = input('[+] : ')

if select == '1':
    Ddos().run()
elif select == '2':
    Scanner().run()
elif select == '3':
    Whois().run()
else:
    print(f'{Fore.RED}{Style.BRIGHT}No such action: "{select}"')
    exit()
