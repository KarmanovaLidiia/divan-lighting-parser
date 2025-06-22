import scrapy

class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/divany-i-kresla"]

    def parse(self, response):
        # Получаем все карточки диванов
        divans = response.css('div[data-testid="product-card"]')

        for divan in divans:
            yield {
                'name': divan.css('a::text').get(),  # название
                'price': divan.css('meta[itemprop="price"]::attr(content)').get(),  # цена
                'url': divan.css('a::attr(href)').get()  # ссылка
            }
