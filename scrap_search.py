import re
import sys
import requests
import csv
from bs4 import BeautifulSoup

HOME_URL = 'http://sekolah.data.kemdikbud.go.id/'
SEARCH_URL = HOME_URL + 'chome/pencarian/'

STATUS_LIST = ['N', 'S']
BENTUK_LIST = ['TK','KB','TPA','SPS','SD','SMP','SDLB','SMPLB','MI','MTs','Paket A','Paket B',
    'SMA','SMLB','SMK','MA','MAK','Paket C','Akademik','Politeknik','Sekolah Tinggi','Institut',
    'Universitas','SLB','Kursus','Keaksaraan','TBM','PKBM','Life Skill','Satap TK SD','Satap SD SMP',
    'Satap TK SD SMP','Satap SD SMP SMA','RA','SMP Terbuka','SMPTK','SMTK','SDTK','SPK PG','SPK TK',
    'SPK SD','SPK SMP','SPK SMA','Pondok Pesantren','SMAg.K','SKB','Taman Seminari','TKLB',
    'Pratama W P','Adi W P','Madyama W P','Utama W P']

search_query = {
    'page': 5,
    'kode_kabupaten': '026600',
    'kode_kec': '026602',
    'bentuk': 'SMA',
    'status': 'S',
}
search_page = requests.post(SEARCH_URL, data=search_query)
search_soup = BeautifulSoup(search_page.content, 'html.parser')
page_load = list(search_soup.find(id='pageload').children)[0]

sekolah_list = page_load.find_all('a', {'class': 'text-info'})
print(len(sekolah_list))
for row in sekolah_list:
    nama_sekolah = row.text
    link_sekolah = row['href']
    print(nama_sekolah)
    print(link_sekolah)