import time
import socket
import threading
from abc import ABC
from colorama import Fore

from services.interface import IService


class Scanner(IService, ABC):
    def __init__(self):
        self.address = input(f'Ip or domain: ')
        self.timeout = float(input(f'Timeout (0.5 by default): ') or 0.5)

    def run(self) -> None:
        # Launching threads
        print(f'{Fore.YELLOW}Scanning...')
        for i in range(1, 65536):
            threading.Thread(target=self.scan_port, kwargs={'port': i}).start()

    def scan_port(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(self.timeout)

        try:
            # Check port
            con = s.connect((self.address, port))

            current_time = time.ctime(time.time())
            print(f'{Fore.GREEN}{current_time} Port: {port} is open.')

            con.close()
        except:
            pass
