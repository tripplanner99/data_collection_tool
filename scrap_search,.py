import requests
url = "https://google.com/search?q=python+web+scraping"
response = requests.get(url)
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")
results = soup.find_all("div", class_="g")
for result in results:
    title = result.find("h3").text
    snippet = result.find("div", class_="IsZvec").text
    print(title)
    print(snippet)
    print("------")
import pandas as pd
data = []
for result in results:
    title = result.find("h3").text
    snippet = result.find("div", class_="IsZvec").text
    data.append({"title": title, "snippet": snippet})
df = pd.DataFrame(data)
df.to_csv("google_search_results.csv", index=False)
