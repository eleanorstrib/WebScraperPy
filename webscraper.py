import requests
import bs4
import pprint

BASE_URL = "http://pyvideo.org/"
pp = pprint.PrettyPrinter(indent=2)

response = requests.get('http://pyvideo.org/category/50/pycon-us-2014')

# entire dom
soup = bs4.BeautifulSoup(response.text)

# specific section of dom
title_links =  [BASE_URL + a.attrs.get ('href') for a in soup.select('div#video-summary-content a[href^="/video"]')]


pp.pprint(title_links)