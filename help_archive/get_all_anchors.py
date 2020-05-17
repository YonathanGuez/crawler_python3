import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
	url = 'https://stackoverflow.com/'
	#url = 'https://web.archive.org/'
	page = requests.get(url)

	soup = BeautifulSoup(page.text, 'html.parser')
	#get all link <a>
	artist_name_list_items = soup.find_all('a')

	for link in artist_name_list_items:
		print(link.prettify())
		#get titel into <a> if we have it
		title = link.get('title')
		print(title)
		# get href into <a>
		href = link.get('href')
		print(href)
