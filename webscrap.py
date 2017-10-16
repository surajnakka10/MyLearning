from urllib.request import urlopen
from bs4 import BeautifulSoup

link = input('Enter URL: ')
count = input('Enter Count: ')
position = input('Enter position: ')
for each in range(int(count) + 1):
	print ('Retrieving: ', link)	
	handle = urlopen(link).read()
	soup = BeautifulSoup(handle, 'html.parser')
	span = soup('a')
	links = ([(tag.get('href'), tag.contents[0]) for tag in span])
	link = links[int(position) - 1][0]