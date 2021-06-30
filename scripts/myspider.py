# My Spider
# ==============================================================================
# Web Scraping with Scrappy
# ==============================================================================
import scrapy


class MySpider(scrapy.Spider):
    name = "spider"

    def start_requests(self):
        urls = [
            'http://esmarketingdigital.es/',
            'http://esmarketingdigital.es/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Scrap Web Page and Save  Code in File
    # ==============================================================================        

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'esmarketingdigital_copy.html'
        #filename = f'spyder-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
 
