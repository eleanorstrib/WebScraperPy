import requests
import bs4
BASE_URL = "http://www.indeed.com/cmp/"

company = "google"

# this gives the response code (eg <Response [200]>)
response = requests.get(BASE_URL + company)

soup = bs4.BeautifulSoup(response.text, 'html.parser')

# add data to a dict of company ratings
company_ratings = {}
company_ratings['overall'] = [float(element.get_text()) for element in soup.select('div span.cmp-average-rating')][0]

rating_categories = [dl.get_text() for dl in soup.select('dl#cmp-reviews-attributes dt')]

print("rating_categories", rating_categories)
print("rate_ct", rate_ct)