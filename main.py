import requests
from pystyle import Colors, Colorate, Center
import time
import os
import webbrowser
import base64
from tkinter import filedialog as fd

# Colors
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
white = "\033[1;37m"

logo = Colorate.Horizontal(Colors.blue_to_red, Center.XCenter("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠁⠀⠉⠻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠁⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠇⠀⠀⠀⠀⠀⠀⠀⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣀⣤⣤⣤⣤⣤⣤⣄⣸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠞⠋⠉⠀⠀⢀⣀⣀⠀⠀⠈⠉⠙⠳⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣠⡴⢶⣤⣀⣤⣄⠀⠀⠀⠀⠀⠀⣿⣠⡴⠾⠛⠛⠉⠉⠉⠉⠛⠓⠶⣦⣄⣽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⡏⠀⠀⠈⠉⠀⠙⠛⠛⠳⣆⣠⠾⠋⠁⣀⢤⠀⠀⠀⠀⠀⠀⠀⠀⡤⣀⠉⠛⢶⣄⠀⠀⣼⠛⠻⣶⠞⠛⢶⡄⠀⠀
⠀⣠⣼⣷⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⠁⠀⢠⠞⠁⠘⡇⠀⠀⠀⠀⠀⠀⢸⠁⠈⢳⡀⠀⠙⣷⡶⠟⠀⠀⠈⠀⠀⢠⡟⠀⠀
⣸⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⠁⠀⠀⠘⠂⣄⣚⠁⠀⠀⠀⠀⠀⠀⠈⢓⣤⠔⠛⠀⢰⣏⠀⠀⠀⠀⠀⠀⠀⠙⠛⠻⣦
⠹⣦⣀⠀⠀⠀⠀⠀⠀⠀⣤⣤⠟⠀⠀⠀⣰⣿⣿⠉⣱⡄⠀⠀⠀⠀⢠⢾⣿⡏⠙⣆⠀⠀⢹⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽
⠀⣼⠏⠀⠀⠀⠀⠀⠀⠀⠉⣷⠀⢀⠤⢄⣻⡙⠿⠟⣩⠇⢀⣀⣀⠀⠸⣜⠻⠿⢋⣟⡠⠄⡘⢷⣤⡄⠀⠀⠀⠀⠀⣀⣴⠟
⠀⠹⢦⣴⠀⠀⠀⠀⠀⠠⣶⡟⢰⠁⠀⠀⢹⠉⠓⠛⣡⠞⠛⠉⠉⠛⢷⣌⠙⠚⠉⡏⠀⠀⠈⣿⡁⠀⠀⠀⠀⠀⠀⢻⡅⠀
⠀⠀⠀⢿⡀⠀⠀⠀⠀⠀⣸⠇⠈⠢⣀⣠⠜⠀⠀⣸⠏⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠳⡄⠀⠜⠙⢳⡆⠀⠀⣀⣀⣀⣼⠃⠀
⠀⠀⠀⠈⠙⠛⠷⣤⡴⢾⣏⠀⠀⠀⡞⠉⠉⠓⠦⣿⡀⠀⠀⠀⠀⠀⠀⢸⣷⠖⠉⠉⠙⡆⠀⠀⠀⣿⣤⡾⠋⠉⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡀⠀⠀⣇⠀⠰⡀⠀⠈⢷⣄⠀⠀⠀⢀⣠⡟⠁⠀⡰⠃⠀⡎⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⡀⠀⠸⡄⠀⠙⢦⡀⠀⠉⠛⠳⠚⠛⠁⠀⢀⠜⠁⠀⡼⠁⠀⢠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⣄⠀⠘⢦⡀⠀⠙⠲⢤⣀⣀⣀⣀⡤⠖⠁⠀⣠⠞⠁⠀⣴⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣄⡀⠙⠲⢄⣀⠀⠀⠀⠀⠀⠀⣀⡤⠚⠁⢀⣤⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠶⣤⣀⣈⠉⠉⠉⠉⠉⠉⣀⣀⣤⠾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠛⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                       
"""), 1)

credit = Colorate.Horizontal(Colors.red_to_blue, Center.XCenter("""
>> Made by ykknrf
"""), 1)

def show_menu():
    print(Center.XCenter(f"""
{blue}[1]{white} Send Message
{blue}[2]{white} Delete Webhook
{blue}[3]{white} Rename Webhook
{blue}[4]{white} Spam Webhook
{blue}[5]{white} Webhook Info
{blue}[6]{white} Change Avatar
{blue}[7]{white} Exit
"""))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def auto_continue(delay=1):
    time.sleep(delay)
    clear_screen()

def change_avatar(url):
    print(f"\n{blue}[Avatar Change]{white}")
    print(f"{yellow}1.{white} Select image file")
    print(f"{yellow}2.{white} Enter image URL")
    print(f"{yellow}3.{white} Cancel")
    
    choice = input(f"\n{blue}[Select option 1-3]:{white} ")
    
    if choice == "1":
        print(f"\n{yellow}[File Selection]{white} Choose an image...")
        image_path = fd.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    elif choice == "2":
        image_path = input(f"\n{blue}[Image URL]:{white} ")
    else:
        return
    
    if not image_path:
        print(f"{red}[Error] No image selected{white}")
        auto_continue()
        return
    
    try:
        if image_path.startswith(('http://', 'https://')):
            response = requests.get(image_path)
            response.raise_for_status()
            encoded_image = base64.b64encode(response.content).decode('utf-8')
        else:
            with open(image_path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

        requests.patch(url, json={"avatar": f"data:image/jpeg;base64,{encoded_image}"}).raise_for_status()
        print(f"\n{green}[Success] Avatar changed{white}")
    except Exception as e:
        print(f"{red}[Error] {e}{white}")
    auto_continue()

def delete_webhook(url):
    confirm = input(f"\n{red}[WARNING] This cannot be undone. Type 'DELETE' to confirm:{white} ")
    if confirm == 'DELETE':
        try:
            requests.delete(url).raise_for_status()
            print(f"\n{green}[Success] Webhook deleted{white}")
            auto_continue()
            return True
        except Exception as e:
            print(f"{red}[Error] {e}{white}")
    else:
        print(f"\n{yellow}[Cancelled] Webhook not deleted{white}")
    auto_continue()
    return False

def send_message(url):
    message = input(f"\n{blue}[Enter your message]:{white} ")
    try:
        requests.post(url, json={"content": message}).raise_for_status()
        print(f"\n{green}[Sent] Message delivered{white}")
    except Exception as e:
        print(f"{red}[Error] {e}{white}")
    auto_continue(0.5)  # Shorter delay for message sending

def rename_webhook(url):
    new_name = input(f"\n{blue}[New webhook name]:{white} ")
    try:
        requests.patch(url, json={"name": new_name}).raise_for_status()
        print(f"\n{green}[Success] Webhook renamed{white}")
        auto_continue()
        return requests.get(url).json()
    except Exception as e:
        print(f"{red}[Error] {e}{white}")
        auto_continue()
        return None

def spam_webhook(url):
    message = input(f"\n{blue}[Spam message]:{white} ")
    delay = float(input(f"{blue}[Delay between messages (seconds)]:{white} "))
    
    print(f"\n{red}[Spam started] Press Ctrl+C to stop{white}")
    try:
        while True:
            requests.post(url, json={"content": message}).raise_for_status()
            print(f"{yellow}[Sent] {time.strftime('%H:%M:%S')}{white}")
            time.sleep(delay)
    except KeyboardInterrupt:
        print(f"\n{yellow}[Spam stopped]{white}")
    except Exception as e:
        print(f"{red}[Error] {e}{white}")
    auto_continue()

def show_webhook_info(webhook):
    print(f"\n{blue}[Webhook Information]{white}")
    print(f"{yellow}Name:{white} {webhook.get('name', 'Unknown')}")
    print(f"{yellow}ID:{white} {webhook.get('id', 'Unknown')}")
    print(f"{yellow}Channel ID:{white} {webhook.get('channel_id', 'Unknown')}")
    print(f"{yellow}Server ID:{white} {webhook.get('guild_id', 'Unknown')}")
    if 'user' in webhook:
        creator = webhook['user']
        print(f"{yellow}Created by:{white} {creator.get('username', 'Unknown')}#{creator.get('discriminator', '0000')}")
    auto_continue(1.5)  # Longer delay for reading info

def main():
    os.system("title ClownHook")
    current_webhook = None
    current_url = None
    
    while True:
        clear_screen()
        print(logo)
        print(credit)
        
        if not current_webhook:
            print(f"\n{blue}[Webhook Setup]{white}")
            current_url = input(f"{yellow}[Enter webhook URL]:{white} ").strip()
            
            try:
                response = requests.get(current_url)
                if response.status_code == 200:
                    current_webhook = response.json()
                    print(f"\n{green}[Connected] {current_webhook['name']}{white}")
                    time.sleep(1)
                    clear_screen()
                    continue
                else:
                    print(f"{red}[Error] Invalid webhook (Status: {response.status_code}){white}")
                    auto_continue()
                    continue
            except Exception as e:
                print(f"{red}[Error] {e}{white}")
                auto_continue()
                continue
        
        show_menu()
        print(f"\n{yellow}[Active Webhook] {current_webhook['name']}{white}")
        
        try:
            choice = input(f"\n{blue}[Select option 1-7]:{white} ").strip()
            
            if choice == "1":
                send_message(current_url)
            elif choice == "2":
                if delete_webhook(current_url):
                    current_webhook = None
                    current_url = None
            elif choice == "3":
                if new_webhook := rename_webhook(current_url):
                    current_webhook = new_webhook
            elif choice == "4":
                spam_webhook(current_url)
            elif choice == "5":
                show_webhook_info(current_webhook)
            elif choice == "6":
                change_avatar(current_url)
                current_webhook = requests.get(current_url).json()
            elif choice == "7":
                current_webhook = None
                current_url = None
                continue
            else:
                print(f"{red}[Error] Invalid option{white}")
                auto_continue()
        except KeyboardInterrupt:
            print(f"\n{blue}[Exiting...]{white}")
            break

if __name__ == "__main__":
    main()
