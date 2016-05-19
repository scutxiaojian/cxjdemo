import urllib.request
from bs4 import BeautifulSoup
import re
import time

def download(url):

	req = urllib.request.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36')
	response = urllib.request.urlopen(req)

	html_cont = response.read()
	soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
		
	view = soup.find('span',class_='link_view').get_text()
	view = re.findall(r"\d+",view)
	print(view[0])


if __name__ == '__main__':
	url = "http://blog.csdn.net/qq_32559763/article/details/51386131"
	while 1:
		download(url)
		time.sleep(3)