# !/usr/bin/env python3
##########SecurityLeader#################
#############Thank You  ##########
###########port scanner ######

# importing the necessary packages
import time
import sys
import os


# clear
def clear_sc():
    # for windows OS
    if os.name == "nt":
        os.system("cls")

        # for linux / Mac OS
    else:
        os.system("clear")


clear_sc()


#####end loding######

# colored text and background
def prRed(skk): print("\033[91m {}\033[00m".format(skk))


def prGreen(skk): print("\033[92m {}\033[00m".format(skk))


def prYellow(skk): print("\033[93m {}\033[00m".format(skk))


def prLightPurple(skk): print("\033[94m {}\033[00m".format(skk))


def prPurple(skk): print("\033[95m {}\033[00m".format(skk))


def prCyan(skk): print("\033[96m {}\033[00m".format(skk))


def prLightGray(skk): print("\033[97m {}\033[00m".format(skk))


def prBlack(skk): print("\033[98m {}\033[00m".format(skk))


import socket
import time
import concurrent.futures
import sys

if len(sys.argv) == 1:
    print(f'\nUsage: "python3 port_scan.py <IP>"\n(Use "-h" option for more info)')
    sys.exit()
if '-h' in sys.argv or '--help' in sys.argv:
    print('''
Example usage: python3 port_scan.py 192.168.234.234 -p 1-1000 
-h                     To show this message
-p(optional)           The range of ports to scan. (default: 1-65535)''')
    sys.exit()
min_range, max_range = 1, 65535

ip = sys.argv[1]
if '-p' in sys.argv:
    min_range, max_range = sys.argv[sys.argv.index('-p') + 1].split('-')

banner = '''
          +-------------------------------------------------+
          |               _                                 |
          |              /  \                               |
          |             /|oo \      | P O R T  | I P |   |
          |            (_|  /_)                             |
          |             _`@/_ \    _   | S C A N N E R |    |
          |            |     | \   \\                       |
          |            | (*) |  \   ))    Secret, XX,  LK   |
          |   ______   |__U__| /  \//                       |
          |  / FIDO \   _//|| _\   /   FidoNet 1:617/1337   |
          | (________) (_/(_|(____/                         |
          |                  (SL)                           |
          +-------------------------------------------------+
         =[ PORT SCANNER V 1.0     ]
+ -- --  =[ A Multi-Threaded Port-Scanner in python3        ]

Port ip: Example : python3 port_scan.py www.example.com -p 1-1000
'''
prCyan(banner)


def scanner(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        s.connect((ip, port))
        print(f"Port {str(port).ljust(4)}     OPEN         {socket.getservbyport(port, 'tcp')}")
    except socket.timeout:
        s.close()


def main():
    prGreen("─" * 40)
    print(f"Scanning {str(int(max_range) + 1 - int(min_range))} ports in {ip}")
    prGreen("─" * 40)
    print("PORT          STATE        SERVICE")
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        results = [executor.submit(scanner, i) for i in range(int(min_range), int(max_range) + 1)]
        for f in concurrent.futures.as_completed(results):
            f.result()
    end = time.perf_counter()

    prGreen("─" * 40)
    print(f"Scanning Took {round(end - start, 2)}s")


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()
