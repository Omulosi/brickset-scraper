
import scrapy

class BricksetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['http://brickset.com/assets/year-2016']

