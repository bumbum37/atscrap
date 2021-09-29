import requests
from bs4 import BeautifulSoup
from os import system, path, remove
from time import sleep

def homepage(url):
    req = requests.get(url)

    scrap = BeautifulSoup(req.text, 'html.parser')

    judul = scrap.find('div', class_="rightCol").find('h2').text;print(judul)
    
    data = [] 
    for x in scrap.find('div', class_="rightCol").find_all('a'):
#        sleep(0.2)
        data.append(x.text)
        print(x.text)
        
    direktory = '/sdcard/result.txt'
    if path.exists(direktory):
        remove(direktory)
    with open('/sdcard/result.txt', 'a') as file:
        for x in data:
            file.write(x +'\n')
        print('\nFile berhasil disimpan ke /sdcard/\nDengan nama \'result.txt\'')


def ip(url):
    req = requests.get(url)

    scraping = BeautifulSoup(req.text,'html.parser')

    ip = scraping.find('div').text
    print(ip)



print('''
\n
  .--. .-----. .----..----..---.  .--.  .-.-.  
 / {} \`-' '-'{ {__-`| }`-'} }}_}/ {} \ | } }} 
/  /\  \ } {  .-._} }| },-.| } \/  /\  \| |-'  
`-'  `-' `-'  `----' `----'`-'-'`-'  `-'`-'    
            
            AtsameIP Scraping

1.Info Bug terbaru
2.Check Ip saya
3.Check Bug (Coming Soon)\n''')

pilih = int(input('Masukan Pilihan: '))
if pilih == 1:
    homepage('https://atsameip.intercode.ca/')

if pilih == 2:
    ip('https://atsameip.intercode.ca/whois?myip&igm')

if pilih == 3:
    print('Nanti akan segera datang !')
