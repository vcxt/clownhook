import aiohttp
import asyncio
import os
import sys
from colorama import Fore, init

# Initialize colorama
init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_centered_ascii():
    ascii_art = r"""    
                                                  
                                                  
      1111111        999999999             66666666   
     1::::::1      99:::::::::99          6::::::6    
    1:::::::1    99:::::::::::::99       6::::::6     
    111:::::1   9::::::99999::::::9     6::::::6      
       1::::1   9:::::9     9:::::9    6::::::6       
       1::::1   9:::::9     9:::::9   6::::::6        
       1::::1    9:::::99999::::::9  6::::::6         
       1::::l     99::::::::::::::9 6::::::::66666    
       1::::l       99999::::::::9 6::::::::::::::66  
       1::::l            9::::::9  6::::::66666:::::6 
       1::::l           9::::::9   6:::::6     6:::::6
       1::::l          9::::::9    6:::::6     6:::::6
    111::::::111      9::::::9     6::::::66666::::::6
    1::::::::::1     9::::::9       66:::::::::::::66 
    1::::::::::1    9::::::9          66:::::::::66   
    111111111111   99999999             666666666     
                                                
                                                """
    terminal_width = os.get_terminal_size().columns
    for line in ascii_art.split('\n'):
        print(Fore.RED + line.center(terminal_width))
    print(Fore.WHITE + "made by ykknrf on discord".center(terminal_width) + "\n")

async def spam_webhooks(webhooks, message, count):
    print("\nSpamming messages...")
    for _ in range(count):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for webhook in webhooks:
                tasks.append(session.post(webhook, json={"content": message}))
            await asyncio.gather(*tasks)
            await asyncio.sleep(0.1)
    print(f"\nSent {count} messages to {len(webhooks)} webhook(s)")

async def delete_webhooks(webhooks):
    print("\nnuke deployed")
    async with aiohttp.ClientSession() as session:
        tasks = []
        for webhook in webhooks:
            tasks.append(session.delete(webhook))
        await asyncio.gather(*tasks)
    print(f"nuked {len(webhooks)} webhook(s)")

async def main():
    while True:
        clear_screen()
        print_centered_ascii()
        
        webhooks = []
        while not webhooks:
            urls = input("webhook(s) URL: ").strip()
            webhooks = [url.strip() for url in urls.split(',') if url.strip()]
            if not webhooks:
                print("failed to find webhook url")
        
        message = input("message: ").strip()
        
        count = 0
        while count < 1 or count > 99:
            try:
                count = int(input("how many times: "))
            except ValueError:
                print("enter a number between 1 - 99.")
        
        await spam_webhooks(webhooks, message, count)
        
        while True:
            choice = input("\ndelete the webhook? (y / n): ").strip().lower()
            if choice in ['y', 'n']:
                break
            print("enter either yes (y), or no (n)")
        
        if choice == 'y':
            await delete_webhooks(webhooks)
        else:
            print("webhooks were not deleted")
        
        print("\n#vaporised")
        await asyncio.sleep(2)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)