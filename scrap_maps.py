import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/maps/place/Seattle,+WA'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the data you want to scrape
name = soup.find('h1', {'class': 'section-hero-header-title-title'}).text.strip()
rating = soup.find('span', {'class': 'section-star-display'}).text.strip()
address = soup.find('div', {'class': 'ugiz4pqJLAG__primary-text gm2-body-2'}).text.strip()

# Print the data
print(f'Name: {name}')
print(f'Rating: {rating}')
print(f'Address: {address}')
