import re
import sys
import requests
from bs4 import BeautifulSoup

f = open("daftar_kab_kec.csv","w+")
f.write('kode_kab,kabupaten,kode_kec,kecamatan\n')

HOME_URL = 'http://sekolah.data.kemdikbud.go.id/'
KEC_URL = HOME_URL + 'chome/kecamatan/'

home_page = requests.get(HOME_URL)
soup = BeautifulSoup(home_page.content, 'html.parser')
kota_options = soup.find(id='kode_kabupaten').find_all('option')

count = 0
for option in kota_options:
    text = option.text
    value = option['value']
    if not value:
        continue

    print(value + ' ' + text)
    kec_page = requests.post(KEC_URL,
        data={'kode_kabupaten': str(value)})
    kec_soup = BeautifulSoup(kec_page.content, 'html.parser')
    kec_options = kec_soup.find(id='kode_kec').find_all('option')
    if len(kec_options) <= 3:
        f.write('{},"{}",,\n'.format(value, text))

    kec_count = 0
    for kec_option in kec_options:
        kec_text = kec_option.text
        kec_value = kec_option['value']
        if not kec_value:
            continue

        print('    ' + kec_value + ' ' + kec_text)
        f.write('{},"{}",{},"{}"\n'.format(value, text, kec_value, kec_text))
