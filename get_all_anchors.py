import requests
from bs4 import BeautifulSoup
url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm'
#url = 'https://web.archive.org/'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
#get all link <a>
artist_name_list_items = soup.find_all('a')

for link in artist_name_list_items:
    print(link.prettify())
    #get titel into <a> if we have it
    tet = link.get('title')
    print(tet)
    # get href into <a>
    tet_2 = link.get('href')
    print(tet_2)
