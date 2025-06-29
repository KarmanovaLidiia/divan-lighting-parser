import scrapy

class DivanSpider(scrapy.Spider):
    name = "divan"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/divany"]

    def parse(self, response):
        items = response.css('div[data-testid="product-card"]')
        for item in items:
            yield {
                'name': item.css('span[itemprop="name"]::text').get(),
                'price': item.css('meta[itemprop="price"]::attr(content)').get(),
                'url': response.urljoin(item.css('a::attr(href)').get())
            }
