import re
import sys
import requests
from bs4 import BeautifulSoup

HOME_URL = 'http://sekolah.data.kemdikbud.go.id/'

home_page = requests.get(HOME_URL)
soup = BeautifulSoup(home_page.content, 'html.parser')

kota_options = soup.find(id='kode_kabupaten').find_all('option')

count = 0
for option in kota_options:
    text = option.text
    value = option['value']
    print(value + ' ' + text)
    
    count += 1
    if count == 10:
        break