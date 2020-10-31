import socket
from colorama import Fore

from services.interface import IService


class Domain(IService):
    def __init__(self) -> None:
        self.address = input(f'Domain: ')

    def run(self) -> None:
        print(f'{Fore.YELLOW}Scanning...')

        try:
            ip = socket.gethostbyname(self.address)
            print(f'{Fore.GREEN}Domain {self.address} ip: {ip}')
        except:
            print(f'{Fore.RED}Domain not found')
