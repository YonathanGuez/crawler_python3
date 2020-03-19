from selenium import webdriver
from bs4 import BeautifulSoup

if __name__ == '__main__':
	# prepare the option for the chrome driver
	options = webdriver.ChromeOptions()
	options.add_argument('headless')

	# start chrome browser
	#browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
	browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe', options=options)
	browser.get('https://www.lemonde.fr/')
	s = BeautifulSoup(browser.page_source, 'html.parser')
	print(s.prettify())
	print(browser.current_url)
	browser.quit()