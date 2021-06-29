import scrapy


class BrickSetSpider(scrapy.Spider):
    name = "myspyder"
    
    
    def start_requests(self):
        return [
            scrapy.Request('http://esmarketingdigital.com')
        ]

    def parse(self, response):
        anchors = response.css('a::text').extract()
        for a in anchors:
        	yield {'text': a}
