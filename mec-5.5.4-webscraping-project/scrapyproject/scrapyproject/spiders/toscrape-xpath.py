import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes2"

    start_urls = [
            'http://quotes.toscrape.com/page/1/',
        ]

    def parse(self, response):
        for quote in response.xpath("//div[contains(@class, 'quote')]"):
            yield {
                'text': quote.xpath("span[contains(@class, 'text')]/text()").get(),
                'author': quote.xpath("span/small[contains(@class, 'author')]/text()").get(),
                'tags': quote.xpath("div[contains(@class,'tags')]/a[contains(@class, 'tag')]/text()").getall()
                }

        next_page = quote.xpath("//li[@class='next']/a").attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)