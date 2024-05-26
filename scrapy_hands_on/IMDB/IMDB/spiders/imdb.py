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
            yield scrapy.Request(url=url, headers=self.custom_headers, callback=self.parse)

    def parse(self, response):
        # Log the URL that is being fetched
        self.log(f"Fetching URL: {response.url}")

        # Check if the request was successful
        if response.status == 200:
            self.log("Successfully fetched the IMDb Top 250 page.")
        else:
            self.log(f"Failed to fetch the page. Status code: {response.status}")

        for movie in response.css('li'):
            title = movie.css('h3.ipc-title__text::text').get()
            url = movie.css('a.ipc-title-link-wrapper::attr(href)').get()
            full_url = response.urljoin(url) if url else None
            if full_url:
                title = " ".join(title.split(" ")[1:])
                yield response.follow(full_url, callback=self.movie_info, meta={'title': title})
        
                #yield {
                #    'title': title,
                #    'url': response.urljoin(url) if url else None,                
                #}

    def movie_info(self, response):
        title = response.meta.get("title")
        movie_title = response.css("span.hero__primary-text::text").get()
        print("Title", title, "Movie title", movie_title)