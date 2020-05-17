from selenium import webdriver
from bs4 import BeautifulSoup

if __name__ == '__main__':
	# Chrome run in back : headless
	options = webdriver.ChromeOptions()
	options.add_argument('headless')

	# Start chrome browser and run JS
	browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe', options=options)
	browser.get('https://www.lemonde.fr/')

	# Switch format: Scraping
	s = BeautifulSoup(browser.page_source, 'html.parser')
	print(s.prettify())
	print(browser.current_url)
	browser.quit()