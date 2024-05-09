from bs4 import BeautifulSoup
import requests

url_template = "https://quotes.toscrape.com/page/{}/"

for p in range(11):
    r = requests.get(url_template.format(p))
    if r.status_code != 200:
        raise Exception(
            "Couldn't connect to `quotes.toscrape` "
            f"with error status code {r.status_code}")
    soup = BeautifulSoup(r.text, 'html.parser')
    with open('quotes.csv', 'a') as f:
        for quote in soup.find_all("span", class_="text"):
            f.write(quote.string)
            f.write("\n")
    with open('authors.csv', 'a') as f:
        for author in soup.find_all("small", class_="author"):
            f.write(author.string)
            f.write("\n")