import re
import sys
import requests
import csv
from bs4 import BeautifulSoup

HOME_URL = 'http://sekolah.data.kemdikbud.go.id/'
SEARCH_URL = HOME_URL + 'chome/pencarian/'

STATUS_LIST = ['N', 'S']
STATUS_STR = {'N': 'Negeri', 'S': 'Swasta'}
BENTUK_LIST = ['TK','KB','TPA','SPS','SD','SMP','SDLB','SMPLB','MI','MTs','Paket A','Paket B',
    'SMA','SMLB','SMK','MA','MAK','Paket C','Akademik','Politeknik','Sekolah Tinggi','Institut',
    'Universitas','SLB','Kursus','Keaksaraan','TBM','PKBM','Life Skill','Satap TK SD','Satap SD SMP',
    'Satap TK SD SMP','Satap SD SMP SMA','RA','SMP Terbuka','SMPTK','SMTK','SDTK','SPK PG','SPK TK',
    'SPK SD','SPK SMP','SPK SMA','Pondok Pesantren','SMAg.K','SKB','Taman Seminari','TKLB',
    'Pratama W P','Adi W P','Madyama W P','Utama W P']


outputfile = open("daftar_sekolah.csv", "w+")
ouput_field = ['kode_kabupaten', 'kode_kec', 'kode_sekolah', 'nama_sekolah', 'jenjang', 'status', 'link_page_sekolah']
writer = csv.DictWriter(outputfile, fieldnames=ouput_field)
writer.writeheader()

inputfile = open("daftar_daerah.csv")
reader = csv.DictReader(inputfile)
for row in reader:
    kode_kabupaten = row['kode_kabupaten']
    nama_kabupaten = row['nama_kabupaten']
    kode_kec = row['kode_kec']
    nama_kecamatan = row['nama_kec']
    
    for bentuk in BENTUK_LIST:
        for status in STATUS_LIST:
            page = 1
            while True:
                search_query = {
                    'page': page,
                    'kode_kabupaten': kode_kabupaten,
                    'kode_kec': kode_kec,
                    'bentuk': bentuk,
                    'status': status,
                }

                search_page = requests.post(SEARCH_URL, data=search_query)
                search_soup = BeautifulSoup(search_page.content, 'html.parser')
                page_load = list(search_soup.find(id='pageload').children)[0]

                sekolah_list = page_load.find_all('a', {'class': 'text-info'})
                num_sekolah = len(sekolah_list)

                if num_sekolah < 1:
                    page = 1
                    break

                for sekolah in sekolah_list:
                    nama_sekolah = sekolah.text
                    kode_sekolah = nama_sekolah[nama_sekolah.find("(")+1:nama_sekolah.find(")")]
                    link_page_sekolah = sekolah['href']
                    print(kode_sekolah + ' ' + nama_sekolah)

                    output_row = {
                        'kode_kabupaten': kode_kabupaten,
                        'kode_kec': kode_kec,
                        'kode_sekolah': kode_sekolah,
                        'nama_sekolah': nama_sekolah,
                        'jenjang': bentuk,
                        'status': STATUS_STR[status],
                        'link_page_sekolah': link_page_sekolah
                    }
                    writer.writerow(output_row)

                page += 1
