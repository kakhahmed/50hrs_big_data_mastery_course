import scrapy


class IMDBSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://m.imdb.com/chart/top/']
    # Custom User-Agent to mimic a browser
    custom_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/58.0.3029.110 Safari/537.36'
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url=url, headers=self.custom_headers, callback=self.parse)

    def parse(self, response):
        # Log the URL that is being fetched
        self.log(f"Fetching URL: {response.url}")

        # Check if the request was successful
        if response.status == 200:
            self.log("Successfully fetched the IMDb Top 250 page.")
        else:
            self.log(
                f"Failed to fetch the page. Status code: {response.status}")

        for movie in response.css('li'):
            title = movie.css('h3.ipc-title__text::text').get()
            url = movie.css('a.ipc-title-link-wrapper::attr(href)').get()
            full_url = response.urljoin(url) if url else None
            if full_url:
                title = " ".join(title.split(" ")[1:])
                yield response.follow(
                    full_url, callback=self.movie_info, meta={'title': title})

    def movie_info(self, response):
        movie_title = response.css("span.hero__primary-text::text").get()
        duration = response.css("ul.ipc-inline-list :nth-child(3)::text").get()
        genres = ",".join(response.css("span.ipc-chip__text::text").getall())
        director = ""
        director_url = ""
        for label in response.css(
            'span.ipc-metadata-list-item__label.ipc-metadata-list-item__label--btn'  # noqa
        ):
            if label.xpath('text()').get() in ['Director', 'Directors']:
                director = label.xpath(
                    'following-sibling::*//a[contains(@href, "name")]/text()'
                    ).get()
                director_url = label.xpath(
                    'following-sibling::*//a[contains(@href, "name")]/@href'
                    ).get()
        release_date = response.xpath(
            '//a[contains(text(), "Release date")]/following-sibling::div//li/a/text()'  # noqa
            ).get()
        meta = {
            "Movie name": movie_title,
            "Duration": duration,
            "Genres": genres,
            "Director": director,
            "Release date": release_date,
        }
        yield response.follow(
            director_url,
            callback=self.director_info,
            meta=meta,
            dont_filter=True,
        )

    def director_info(self, response):
        top_four_movies = response.css(
            "a.ipc-primary-image-list-card__title::text").getall()
        meta = response.meta
        yield {
            "Movie name": meta["Movie name"],
            "Duration": meta["Duration"],
            "Genres": meta["Genres"],
            "Director": meta["Director"],
            "Release date": meta["Release date"],
            "Top 4 Movies": ",".join(top_four_movies)
        }
