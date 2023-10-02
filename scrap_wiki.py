import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Example'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table you want to scrape
table = soup.find('table', {'class': 'wikitable sortable'})

# Extract the data from the table
data = []
for row in table.find_all('tr'):
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    data.append(cols)

# Print the data
for row in data:
    print(row)
