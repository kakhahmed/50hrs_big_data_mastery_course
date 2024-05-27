
""" Scrape popular quotes from HTML"""

import requests

url_template = "https://quotes.toscrape.com/page/{}/"

st_txt = '<span class="text" itemprop="text">'
st_author = '<span>by <small class="author" itemprop="author">'

for p in range(11):
    r = requests.get(url_template.format(p))
    if r.status_code != 200:
        raise Exception(
            "Couldn't connect to `quotes.toscrape` "
            f"with error status code {r.status_code}")
    html = r.text
    with open('quotes.csv', 'a') as f:
        for line in html.split('\n'):
            if st_txt in line:
                quote = line.replace(st_txt, '').replace('</span>', '').replace('&#39;', "'")
                quote = quote.strip()
            if st_author in line:
                author = line.replace(st_author, '').replace('</small>', '').replace("  ", "")
                f.write(f"{author},{quote}\n")
