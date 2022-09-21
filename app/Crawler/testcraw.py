from bs4 import BeautifulSoup
import urllib.request

url =  'https://www.traveloka.com/vi-vn/hotel/vietnam/city/pleiku-city-10011467'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

new_feeds = soup.find( class_='css-1dbjc4n r-1ifxtd0').find_all('a,h3')

for feed in new_feeds:
	title = feed.get('h3')
	link = feed.get('href')
	print('Title: {} - Link: {}'.format(title, link))