import socket
from colorama import Fore
from pprint import pprint
from ipwhois import IPWhois

from services.interface import IService


class Whois(IService):
    def __init__(self) -> None:
        self.address = socket.gethostbyname(input(f'Ip or domain: '))

    def run(self) -> None:
        print(f'{Fore.YELLOW}Scanning...{Fore.RESET}')

        try:
            info = IPWhois(self.address).lookup()
            pprint(info)
        except:
            print(f'{Fore.RED}Server not found')
