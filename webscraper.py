import requests
from bs4 import BeautifulSoup as soup

response = requests.get('http://pyvideo.org/category/50/pycon-us-2014')

print response.text