import os 
import time           
import random        
import pystyle       
import requests      

from pystyle import *              
from console.utils import set_title

def cls():                                          
    os.system("cls" if os.name == "nt" else "clear")
                                                    
def pause():                                        
    os.system("pause >nul")                         

banner = """                                                                                        
██████╗ ██╗      ██████╗  ██████╗ ██████╗ ██╗   ██╗    ██╗██████╗     
██╔══██╗██║     ██╔═══██╗██╔═══██╗██╔══██╗╚██╗ ██╔╝    ██║██╔══██╗    
██████╔╝██║     ██║   ██║██║   ██║██║  ██║ ╚████╔╝     ██║██████╔╝    
██╔══██╗██║     ██║   ██║██║   ██║██║  ██║  ╚██╔╝      ██║██╔═══╝     
██████╔╝███████╗╚██████╔╝╚██████╔╝██████╔╝   ██║       ██║██║         
╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝    ╚═╝       ╚═╝╚═╝         
                                                                      
██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗                    
██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗                   
██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝                   
██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝                    
███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║                        
╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝                        
Simple IP Lookup By Bloody                                                                      
"""

cls()                                                                    
h_h2 = ["Halal", "Haram"]                                                
print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(banner)))

Write.Print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", Colors.rainbow, interval=0)
Write.Print(f"This program is:", Colors.purple_to_blue, interval=0)
choice = Write.Print(f" {random.choice(h_h2)}\n", Colors.green_to_white, interval=0)

set_title("Bloody IP Lookup | Made By: Bloody | Enter IP")                                                #
Write.Print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", Colors.rainbow, interval=0)#       
ip_input = Write.Input("Enter IP address: ", Colors.rainbow, interval=0.008)                              #
Write.Print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", Colors.rainbow, interval=0)#


def lookup():
    set_title(f"Bloody IP Lookup | Made By: Bloody | Looking Up: {ip_input}")
    time.sleep(0.65)
    headers = {
        'authority': 'ipinfo.io',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'referer': 'https://ipinfo.io/',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        }
    # Sending request to https://ipinfo.io to get results
    r = requests.get(f'https://ipinfo.io/widget/demo/{ip_input}', headers=headers)
    ip = r.json()['data']['ip']
    city = r.json()['data']['city']
    region = r.json()['data']['region']
    country = r.json()['data']['country']
    timezone = r.json()['data']['timezone']
    address = r.json()['data']['abuse']['address']
    country = r.json()['data']['abuse']['country']

# Printing Output
    set_title("Bloody IP Lookup | Made By: Bloody | IP Information Successfully Found!")
    Write.Print('IP: ', Colors.purple_to_blue, interval=0.008)
    Write.Print(f'{ip}\n', Colors.green_to_white, interval=0.008)
    Write.Print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", Colors.rainbow, interval=0)
    Write.Print('City: ', Colors.red_to_yellow, interval=0.008)
    Write.Print(f'{city}\n', Colors.blue_to_purple, interval=0.008)
    Write.Print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", Colors.rainbow, interval=0)
    Write.Print('Region: ', Colors.purple_to_red, interval=0.008)
    Write.Print(f'{region}\n', Colors.blue_to_purple, interval=0.008)
    Write.Print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", Colors.rainbow, interval=0)
    Write.Print('Country: ', Colors.green_to_cyan, interval=0.008)
    Write.Print(f'{country}\n', Colors.white_to_blue, interval=0.008)
    Write.Print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", Colors.rainbow, interval=0)
    Write.Print('Timezone: ', Colors.white_to_blue, interval=0.008)
    Write.Print(f'{timezone}\n', Colors.white_to_green, interval=0.008)
    Write.Print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", Colors.rainbow, interval=0)
    Write.Print('Address: ', Colors.rainbow, interval=0.008)
    Write.Print(f'{address}\n', Colors.rainbow, interval=0.008)
    Write.Print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", Colors.rainbow, interval=0)
    set_title("Bloody IP Lookup | Made By: Bloody | Finished!")
    Write.Print("Press any key to continue . . .", Colors.rainbow, interval=0.008)
    pause()

if __name__ == "__main__":
    lookup()