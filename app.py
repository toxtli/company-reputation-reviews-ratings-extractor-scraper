from bs4 import BeautifulSoup
import requests
import random
import pandas
import time

companies = ['upwork.com']
min_time = 0
max_time = 1
start_page = 1
site = 'sitejabber'
ratings = [1,2,3,4,5]
selectors_row = {}
selectors_row['title'] = {'sel':'.review_title'}
selectors_row['content'] = {'sel':'.review_content'}

def get_values(obj, selectors):
	output = {}
	for key in selectors.keys():
		output[key] = obj.select(selectors[key]['sel'])[0].text
		if 'type' in selectors[key]:
			output[key] = selectors[key]['type'](output[key])
	return output

def extract_sitejabber(company,ratings):
	reviews = []
	for rating in ratings:
		page = 1
		while True:
			print('Extracting company: %s Rating: %s Page: %s'%(company,rating,page))
			time.sleep(random.randint(min_time, max_time))
			url = 'https://www.sitejabber.com/reviews/%s?page=%s&rating=%s#reviews' % (company, page, rating)
			r = requests.get(url)
			html_doc = r.text
			soup = BeautifulSoup(html_doc, 'html.parser')
			all_reviews = soup.select('.review_row')
			if len(all_reviews) == 0:
				break
			else:
				page += 1
				for one_review in all_reviews:
					review = get_values(one_review, selectors_row)
					review['rating'] = rating
					reviews.append(review)
	return reviews

def extract_sitejabber(company,ratings):
	reviews = []
	for rating in ratings:
		page = 1
		while True:
			print('Extracting company: %s Rating: %s Page: %s'%(company,rating,page))
			time.sleep(random.randint(min_time, max_time))
			url = 'https://www.sitejabber.com/reviews/%s?page=%s&rating=%s#reviews' % (company, page, rating)
			r = requests.get(url)
			html_doc = r.text
			soup = BeautifulSoup(html_doc, 'html.parser')
			all_reviews = soup.select('.review_row')
			if len(all_reviews) == 0:
				break
			else:
				page += 1
				for one_review in all_reviews:
					review = get_values(one_review, selectors_row)
					review['rating'] = rating
					reviews.append(review)
	return reviews

if site == 'sitejabber':
	for company in companies:
		reviews	= extract_sitejabber(company,ratings)
		df = pandas.DataFrame(reviews)
		df.to_csv('%s_%s.csv'%(company,site))
	
