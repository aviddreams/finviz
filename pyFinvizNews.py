import requests
from bs4 import BeautifulSoup
import csv
import pdb
import datetime
#pdb.set_trace() - python step by step debugger command
print datetime.datetime.now()
print "Finviz Performance Start"
url = "http://www.finviz.com/quote.ashx?t=intc"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)
titleslist = soup.find_all('a',{"class" : "tab-link-news"})
