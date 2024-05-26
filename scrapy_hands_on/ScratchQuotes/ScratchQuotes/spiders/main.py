import scrapy

class ScratchQuotes(scrapy.Spider):
    name = 'quotes'
    start_urls =  ['https://quotes.toscrape.com']

    def parse(self, response):
        for quote in response.css('.quote'):
            yield {
                'quotes': quote.css('.text::text').get(),
                'author': quote.css('.author::text').get(),
                'tags': quote.css('.tag::text').getall(),
            }

        next_page_url = response.css('li.next a::attr(href)').get()

        # check for last page
        if next_page_url:
            yield response.follow(next_page_url, callback=self.parse)
        else:
            print("\n\n\n\n Last Page!")
