import scrapy


class ImdbspiderSpider(scrapy.Spider):
    name = "imdbspider"
    allowed_domains = ["imdb.com"]
    start_urls = ["https://lista.mercadolivre.com.br/tenis-corrida-masculino"]

    def parse(self, response):
        products = response.css('div.ui-search-result__wrapper.ui-search-result__wrapper')
        prices = products.css('span.andes-money-amount__fraction::text').getall()
        cents = products.css('span.andes-money-amount__cents::text').getall()
        for products in products:
            yield {
                'brand' : products.css('span.poly-component__brand::text').get(),
                'name' :  products.css('h2.poly-component__title a::text').get(),
                'reviews_rating_number' : products.css('span.poly-reviews__rating::text').get(),
                'review_amount' :products.css('span.poly-reviews__total::text').get().replace('(', '').replace(')', ''),
                'old_price': prices[0] if len(prices) >0 else None,
                'old_price_cents': cents[0] if len(cents) >0 else None,
                'new_price': prices[1] if len(prices) > 1 else None,
                'new_price_cents': cents[1] if len(cents) >1 else None,
            
            }

        pass
