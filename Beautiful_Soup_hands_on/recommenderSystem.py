import requests
from bs4 import BeautifulSoup


def main():
    # Setting `User-Agent` that mimics a browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/58.0.3029.110 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'
    }
    url = "https://m.imdb.com/"

    user_movie_name = input("Enter movie name: ")

    req = requests.get(f"{url}chart/top/", headers=headers)
    req.raise_for_status()

    soup = BeautifulSoup(req.text, 'html.parser')

    # Find the movie containers
    movie_containers = soup.find_all(
        'li',
        class_='ipc-metadata-list-summary-item sc-10233bc-0 iherUv cli-parent',
        limit=250
    )
    movie_url = ""
    for m in movie_containers:
        title = " ".join(
            m.find('h3', class_='ipc-title__text').string.split(" ")[1:])
        if user_movie_name.lower() == title.lower():
            movie_url = url + m.a['href']
            break

    if not movie_url:
        print(f"No movie found with the name {user_movie_name}")
        return

    print(f"Found movie: {title}")
    print("Movie URL:", movie_url)
    req = requests.get(movie_url, headers=headers)
    req.raise_for_status()
    soup = BeautifulSoup(req.text, 'html.parser')
    # Find first director name
    director_cotainer = soup.find(
        "div",
        class_="ipc-metadata-list-item__content-container")
    director_url = url + director_cotainer.a["href"]
    print("Director URL:", director_url)

    req = requests.get(director_url, headers=headers)
    req.raise_for_status()
    director_soup = BeautifulSoup(req.text, 'html.parser')
    # Get top work
    top_containers = director_soup.find_all("div", class_="ipc-list-card--span")
    top_work = []
    for top in top_containers:
        top_work.append(top.find("a", class_="ipc-primary-image-list-card__title").string)    
    print(f"Top work: {top_work}")

if __name__ == "__main__":
    main()