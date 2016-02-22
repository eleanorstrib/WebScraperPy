import requests
import bs4
BASE_URL = "http://www.indeed.com/cmp/"

company = "google"

# this gives the response code (eg <Response [200]>)
response = requests.get(BASE_URL + company)

soup = bs4.BeautifulSoup(response.text, 'html.parser')

# add data to a dict of company ratings
company_ratings = {}
company_ratings['overall'] = soup.select('div span.cmp-average-rating')


print(company_ratings)