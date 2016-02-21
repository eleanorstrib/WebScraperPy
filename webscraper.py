import requests

response = requests.get('http://pyvideo.org/category/50/pycon-us-2014')

print response.text