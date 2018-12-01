import re
import sys
import requests
from bs4 import BeautifulSoup

HOME_URL = 'http://sekolah.data.kemdikbud.go.id/'

home_page = requests.get(HOME_URL)
soup = BeautifulSoup(home_page.content, 'html.parser')

kota_options = soup.find(id='kode_kabupaten')

for option in kota_options:
    text = option.text
    value = option['value']
    print(value + ' ' + text)
