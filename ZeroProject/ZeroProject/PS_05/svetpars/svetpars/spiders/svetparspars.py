import scrapy


class SvetparsparsSpider(scrapy.Spider):
    name = "svetparspars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/sankt-peterburg/category/svet"]

    def parse(self, response):
        fixtures = response.css('div.WdR1o')
        for fixture in fixtures:
            yield {
                'name': fixture.css('div.lsooF span::text').get(),
                'price': fixture.css('div.pY3d2 span::text').get(),
                'url': fixture.css('link').attrib['href']
            }
