import requests
url = requests.get("https://www.flipkart.com/watches/pr?sid=r18")
from bs4 import BeautifulSoup
soup = BeautifulSoup(url.content, "html.parser")
names = soup.find_all("div", class_="_2WkVRV")
prices = soup.find_all("div", class_="_30jeq3")
for name, price in zip(names, prices):
    print(name.text, price.text)
import pandas as pd
data = []
for name, price in zip(names, prices):
    data.append({"name": name.text, "price": price.text})
df = pd.DataFrame(data)
df.to_csv("flipkart_watches.csv", index=False)
