import requests
import bs4
BASE_URL = "http://www.indeed.com/cmp/"
RATING_DENOMINATOR = 85.225
AVAILABLE_STARS = 5

company = "pinterest"

# this gives the response code (eg <Response [200]>)
response = requests.get(BASE_URL + company)

soup = bs4.BeautifulSoup(response.text, 'html.parser')

# add data to a dict of company ratings
company_ratings = {}

if len(soup.select('dl#cmp-reviews-attributes dt')) != 0:
	rating_categories = [dl.get_text() for dl in soup.select('dl#cmp-reviews-attributes dt')]

	# need to grab pixel values from dom, splice, and turn into integers
	rating_stars_raw = [span.attrs.get('style') for span in soup.select('span.cmp-star-on')]
	rating_stars_clean = [float(item[7:-2]) for item in rating_stars_raw]

	for item in rating_categories:
		company_ratings[item] = round(((rating_stars_clean[rating_categories.index(item)]/RATING_DENOMINATOR) * AVAILABLE_STARS), 1)

	company_ratings['Overall'] = [float(element.get_text()) for element in soup.select('div span.cmp-average-rating')][0]
	print("company_ratings", company_ratings)
else:
	print("There are no ratings available for %s." % company.title())

