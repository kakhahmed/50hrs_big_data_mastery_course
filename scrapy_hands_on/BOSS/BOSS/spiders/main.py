from scrapy import Request, Spider


class BOSSSpider(Spider):
    name = 'boss'
    start_urls = ['https://www.hugoboss.com/de/herren/']
    # Custom User-Agent to mimic a browser
    custom_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/58.0.3029.110 Safari/537.36'
    }

    def start_requests(self):
        for url in self.start_urls:
            yield Request(
                url=url, headers=self.custom_headers, callback=self.parse)

    def parse(self, response):
        # Log the URL that is being fetched
        self.log(f"Fetching URL: {response.url}")

        # Check if the request was successful
        if response.status == 200:
            self.log("Successfully fetched the BOSS Herren home page.")
        else:
            self.log(
                f"Failed to fetch the page. Status code: {response.status}")

        category_urls = response.css(
            'a[data-navid="21888"] + div .col-xl-offset-1 a::attr(href)').getall()
        for url in category_urls:
            yield Request(
                url, callback=self.category_products_info, meta={"boss_url": response.url})

    def category_products_info(self, response):
        products_urls = response.css(
            'a.js-product-tile__product-image::attr(data-url)').getall()
        for url in products_urls:
            yield response.follow(url, callback=self.product_info)

        # check if reached page with last product.
        prdct_counter = response.css(
            'div.simplepagingbar__products--counter p::text').get().split(" ")
        next_page_url = response.css(
            'a.js-simplepagingbar-link[aria-label="Weiter"]::attr(href)').get()
        # e.g. `375 Produkte von 375` for last page
        if prdct_counter[0] != prdct_counter[-1]:
            yield Request(next_page_url, callback=self.category_products_info)

    def product_info(self, response):
        product_name = response.css(
            'h1.pdp-stage__header-title::text').get().replace("\n", "")
        available_colors = ",".join(
            response.css('a.slides__slide::attr(title)').getall())
        image_urls = response.css(
            'img.pdp-images__adaptive-picture-image::attr(src)').getall()
        image_urls = [
            url.split("?")[0]+"wid=768&qlt=80" for url in image_urls]
        image_urls = ','.join(image_urls)
        care_info = ','.join(
            response.css('div.care-info title::text').getall())
        yield {
            "Product Name": product_name,
            "Available Colors": available_colors,
            "Image URL": image_urls,
            "Care Instructions": care_info,
        }
