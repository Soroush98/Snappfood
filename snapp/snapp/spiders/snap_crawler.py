import scrapy
import re
import logging
import json
from scrapy.selector import Selector
from selenium import webdriver
from scrapy.http import HtmlResponse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class CommentSpider(scrapy.Spider):

    name = 'comment2'
    comments_count = 0
    products_count = 0
    start_urls = [
        'https://snappfood.ir/restaurant/city/Tehran?services=CONFECTIONERY'
    ]
    def parse(self, response):
       for href in response.css("a.idn-restaurant-title"):
           yield response.follow(href, self.parse_comment)
    def parse_comment(self,response):

        for href in response.css('#user-reviews div.kk-review'):
            i = []
            print(href.css('::text').extract())
            check = href.css('span.SadIcon')
            if check:
                i.append(-1)
            else:
                i.append(1)
            yield {
                'text': href.css('::text').extract()+i
            }


