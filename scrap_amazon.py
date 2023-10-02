import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com/dp/B08J5F3GJW'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the product title
title = soup.find('span', {'id': 'productTitle'}).text.strip()

# Find the product price
price = soup.find('span', {'class': 'a-price-whole'}).text.strip()

# Find the product rating
rating = soup.find('span', {'class': 'a-icon-alt'}).text.strip()

# Find the product reviews
reviews = []
for review in soup.find_all('div', {'class': 'a-section review aok-relative'}):
    review_title = review.find('a', {'class': 'a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold'}).text.strip()
    review_text = review.find('span', {'class': 'a-size-base review-text review-text-content'}).text.strip()
    reviews.append({'title': review_title, 'text': review_text})

# Print the product details and reviews
print(f'Title: {title}')
print(f'Price: {price}')
print(f'Rating: {rating}')
print('Reviews:')
for i, review in enumerate(reviews):
    print(f'Review {i+1}: {review["title"]}\n{review["text"]}\n')
