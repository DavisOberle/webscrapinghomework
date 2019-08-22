import os
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

response = requests.get(url)

soup = bs(response.text, 'html.parser')

results = soup.find_all('a')

url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

response2 = requests.get(url2)

soup2 = bs(response2.text, 'html.parser')

results2 = soup2.find_all('img')

url3 = 'https://space-facts.com/mars/'

marstable = pd.read_html(url3)

df = marstable[0]

htmltable = df.to_html()

htmltable = htmltable.replace('\n', '')

url4 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

response4 = requests.get(url4)

soup4 = bs(response4.text, 'html.parser')

results4 = soup.find_all('img')
