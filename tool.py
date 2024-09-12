import requests
from bs4 import BeautifulSoup
import webbrowser
import os

try:
    try:
        os.system("cls")
    except:
        os.system("clear")
except:
    pass

def open_link(url):
    webbrowser.open(url)

def Find_Data(num):
    url = 'https://simdata.net/search.php?type=mobile&search='
    r = requests.get(url+num)
    html_response = r.content
    html_response = html_response.decode('utf-8')
    
    soup = BeautifulSoup(html_response, 'html.parser')
    
    # Find the table
    table = soup.find('table')
    
    # Try to find the header row (thead)
    try:
        headers = [th.text.strip() for th in table.find('thead').find_all('th')]
    except AttributeError:
        # If thead is not found, assume headers are in the first row of tbody
        headers = [th.text.strip() for th in table.find('tbody').find_all('tr')[0].find_all('th')]
    
    # Extract data from rows
    data = []
    for row in table.find('tbody').find_all('tr'):
        row_data = [td.text.strip() for td in row.find_all('td')]
        data.append(row_data)
    
    # Print the data in a tabular format
    print("Name | Number | CNIC | Address")
    print("-----|--------|------|---------")
    for row in data:
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")

while True:
    print("""
    Lisenced to @ZeemiBhai

    ▄███████▄     ▄████████    ▄████████   ▄▄▄▄███▄▄▄▄    ▄█  ▀█████████▄     ▄█    █▄       ▄████████  ▄█  
    ██▀     ▄██   ███    ███   ███    ███ ▄██▀▀▀███▀▀▀██▄ ███    ███    ███   ███    ███     ███    ███ ███  
        ▄███▀   ███    █▀    ███    █▀  ███   ███   ███ ███▌   ███    ███   ███    ███     ███    ███ ███▌ 
    ▀█▀▄███▀▄▄  ▄███▄▄▄      ▄███▄▄▄     ███   ███   ███ ███▌  ▄███▄▄▄██▀   ▄███▄▄▄▄███▄▄   ███    ███ ███▌ 
    ▄███▀   ▀ ▀▀███▀▀▀     ▀▀███▀▀▀     ███   ███   ███ ███▌ ▀▀███▀▀▀██▄  ▀▀███▀▀▀▀███▀  ▀███████████ ███▌ 
    ▄███▀         ███    █▄    ███    █▄  ███   ███   ███ ███    ███    ██▄   ███    ███     ███    ███ ███  
    ███▄     ▄█   ███    ███   ███    ███ ███   ███   ███ ███    ███    ███   ███    ███     ███    ███ ███  
    ▀████████▀   ██████████   ██████████  ▀█   ███   █▀  █▀   ▄█████████▀    ███    █▀      ███    █▀  █▀   
    
                                                                                    t.me/AnonCyberWarrior

    <==========================   S I M   D A T A   S E A R C H E R   ==========================================>
    <===================== D E V E L O P E D   B Y   Z E E M I B H A I ==========================================> 

    1. Join AnonCyberWarrior Whatsapp Groups
    2. Get Fb,Insta,Tiktok,Yt,Telegram Services.
    3. Search Mobile number / CNIC data.
    4. Visit Youtube.
    5. Online Earning Course.
    6. Exit.

    """)

    choose = int(input("Choose any one from above menu : "))
    if choose == 1:
        print("Join all whatsapp groups from below : \n https://whatsapp.com/channel/0029VaCCUQoJ93wLxSIftN0H")
        open_link("https://whatsapp.com/channel/0029VaCCUQoJ93wLxSIftN0H")
        try:
            try:
                os.system("cls")
            except:
                os.system("clear")
        except:
            pass
    elif choose == 2:
        print("Visit Below Website for Followers,Likes,Views & Subscribers of Following website: \nFacebook\nInstagram\nYoutube\nTelegram\nTiktok\n\thttps://www.mastpanel.online")
        open_link("https://mastpanel.online")
        try:
            try:
                os.system("cls")
            except:
                os.system("clear")
        except:
            pass
    elif choose == 3:
        keep_run = True
        while keep_run:
            num = input("Enter number/CNIC (Like this 3******** / 37*********1 ): ")
            if "3465277602" in num:
                print("Name : ZeemiBhai\nOwner of AnonCyberWarrior & MastPanel")
            elif "3435041018" in num:
                print("Name : ZeemiBhai\nOwner of AnonCyberWarrior & MastPanel")
            elif "3205715909" in num:
                print("Name : ZeemiBhai\nOwner of AnonCyberWarrior & MastPanel")
            elif "34350" in num or "345598" in num:
                print("=========================================================================")
                print("Number not allowed- Search Another")
                print("\n \t In case of issue contact : @zeemibhai_bot on telegram")
                print("==========================================================================")
            else:
                Find_Data(num)
            inp = input("Do you want to search another number (press q to cancel) : ")
            if "q" in inp:
                keep_run = False
        try:
            try:
                os.system("cls")
            except:
                os.system("clear")
        except:
            pass
    elif choose == 4:
        print("Subscribe Youtube for Content Related to Hacking,Programming,Online Earning and etc \n\t https://youtube.com/@AnonCyberWarrior ")
        open_link("https://youtube.com/@AnonCyberWarrior")
        try:
            try:
                os.system("cls")
            except:
                os.system("clear")
        except:
            pass
    elif choose == 5:
        print("Join telegram for Online Earning,Hacking and other Tech Courses.\n\t https://t.me/AnonCyberWarrior")
        open_link("https://t.me/AnonCyberWarrior")
        try:
            try:
                os.system("cls")
            except:
                os.system("clear")
        except:
            pass
    elif choose == 6:
        exit()
    else:
        print("Invalid input.")
