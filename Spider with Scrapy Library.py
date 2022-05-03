# Building Spider with Scrapy Library

import scrapy

class EagleSpider(scrapy.Spider):
    name='eagle'
    start_urls=[
        'https://quotes.toscrape.com/'
    ]

# the all data will store in the response object
# and with the help of response we could extract the Data
# we have two kind of selector in this library :CSS and XPATH
def parse(self,response):
    print('#'*20)
    for data in response.css('div.quote'):
        yield{
            'title':data.css('spaan.text::text').get(),
            'aouthor':data.css('small:author::text').get(),
            'tags':data.css('div.tages a::text').get(),
        }
    
# inorder to extract all data from alll pages we need to pave all pages
# the following source codes pave all the pages

    next_page=response.css('li.next a::attr(href)').get()
    if next_page:
        next_page=response.urljoin(next_page)
        yield scrapy.Request(url=next_page,callback=self.parse)



