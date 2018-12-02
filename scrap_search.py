import re
import sys
import requests
from bs4 import BeautifulSoup

HOME_URL = 'http://sekolah.data.kemdikbud.go.id/'
status_list = ['N', 'S']
bentuk_list = ['TK','KB','TPA','SPS','SD','SMP','SDLB','SMPLB','MI','MTs','Paket A','Paket B',
    'SMA','SMLB','SMK','MA','MAK','Paket C','Akademik','Politeknik','Sekolah Tinggi','Institut',
    'Universitas','SLB','Kursus','Keaksaraan','TBM','PKBM','Life Skill','Satap TK SD','Satap SD SMP',
    'Satap TK SD SMP','Satap SD SMP SMA','RA','SMP Terbuka','SMPTK','SMTK','SDTK','SPK PG','SPK TK',
    'SPK SD','SPK SMP','SPK SMA','Pondok Pesantren','SMAg.K','SKB','Taman Seminari','TKLB',
    'Pratama W P','Adi W P','Madyama W P','Utama W P']

home_page = requests.get(HOME_URL)
soup = BeautifulSoup(home_page.content, 'html.parser')
kota_options = soup.find(id='bentuk').find_all('option')

for option in kota_options:
    value = option['value']
    if not value:
        continue

    print("'" + value + "'", end=",")