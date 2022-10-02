import scrapy
## creates html file that iwll later be used by scrape code

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://safe.density.io/#/displays/dsp_956223069054042646?token=shr_o69HxjQ0BYrY2FPD9HxdirhJYcFDCeRolEd744Uj88e',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'RSF_datas-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)