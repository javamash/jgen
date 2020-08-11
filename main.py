from time import sleep
from os import system
import random
import string
import json

jgen = f"""   _                  
  (_)                 
   _  __ _  ___ _ __  
  | |/ _` |/ _ \ '_ \ 
  | | (_| |  __/ | | |
  | |\__, |\___|_| |_|
 _/ | __/ |           
|__/ |___/             \n"""

# load config
with open('config.json') as config:
    cfg = json.load(config)

while True:
    failed = False
    while not failed:
        print(jgen)
        try:
            length = int(input('[ + ] Length Of Password: '))
        except ValueError:
            print('[ - ] Please enter a number.')
            sleep(2)
            system('cls')
            continue
        failed = True
            
        usage = str(input('[ + ] Password Usage:'))
        pwd = ''.join(random.SystemRandom().choice(string.punctuation + string.ascii_letters + string.digits) for _ in range(length))

        print('[ + ] Generated Password: ' + pwd)

        # logging
        directory = cfg['dir']
        f = open(directory, 'a')
        f.write(pwd + "       :       " + usage + "\n")
        f.close()
        
        secret = cfg['secret']
        if secret:
            print('\nAdd my discord: Nexus#9567 :DDD')
        
    break
