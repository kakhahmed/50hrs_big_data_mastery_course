import re

import requests
from BS4 import BeautifulSoup

# Setting `User-Agent` that mimics a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/58.0.3029.110 Safari/537.36'
}
url = "https://m.imdb.com/"
req = requests.get(f"{url}chart/top/", headers=headers)
req.raise_for_status()  # Ensure we notice HTTP errors

soup = BeautifulSoup(req.text, 'html.parser')

# Find the movie containers
movie_containers = soup.find_all(
    'li',
    class_='ipc-metadata-list-summary-item sc-10233bc-0 iherUv cli-parent',
    limit=25
)


def decide_type_of_child(texts):
    duration = None
    aud_rate = None
    for text in texts:
        if re.match(r'\d{4}$', text):
            pass  # year
        elif re.match(r'\d+h \d+m', text):
            duration = text
        else:
            aud_rate = text
    return aud_rate, duration


with open("imbd_movies_name_rating.csv", 'w') as f:
    f.write("Title; Year; Rating; Audience rating; Genres")
    f.write('\n')
    # Get Title, movie year, and rating
    for movie in movie_containers:
        # Remove first number before title name.
        title = " ".join(
            movie.find(
                'h3', class_='ipc-title__text').string.split(" ")[1:])
        year = movie.find('span', class_='cli-title-metadata-item').string
        # Get only rating and discard other rating metadata.
        rating = movie.find(
            'div',
            class_="sc-e2dbc1a3-0 ajrIH sc-b189961a-2 fkPBP cli-ratings-container"
        ).get_text("|", strip=True).split("|")[0]

        movie_url = url + movie.a['href']
        # Access movie url.
        req = requests.get(movie_url, headers=headers)
        req.raise_for_status()  # Ensure we notice HTTP errors

        soup = BeautifulSoup(req.text, 'html.parser')
        movie_details = soup.find("ul", class_='ipc-inline-list ipc-inline-list--show-dividers sc-d8941411-2 cdJsTz baseAlt')
        rate_and_duration = movie_details.get_text('|').split('|')
        if len(rate_and_duration) == 3:
            _, aud_rate, duration = rate_and_duration
        else:
            aud_rate, duration = decide_type_of_child(rate_and_duration)
            
        genres = ','.join([g.string for g in soup.findAll('span', class_='ipc-chip__text')[:-1]])

        f.write(f"{title}; {year}; {rating}; {aud_rate}; {genres}")
        f.write('\n')
