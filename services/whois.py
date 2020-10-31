import socket
from abc import ABC
from colorama import Fore
from pprint import pprint
from ipwhois import IPWhois

from services.interface import IService


class Whois(IService, ABC):
    def __init__(self):
        self.address = socket.gethostbyname(input(f'Ip or domain: '))

    def run(self) -> None:
        print(f'{Fore.YELLOW}Scanning...{Fore.RESET}')

        info = IPWhois(self.address).lookup()
        pprint(info)
