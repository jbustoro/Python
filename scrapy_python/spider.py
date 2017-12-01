#!/usr/bin/env python
# -*- coding: utf-8 -*-
import scrapy

class FilmRatingsSpider(scrapy.Spider):
    name = 'filmRatings'
    allowed_domains = ['filmaffinity.com']

    pelicula = raw_input("\nIntroduce el nombre de una pelicula: ")
    start_urls = ['https://www.filmaffinity.com/es/search.php?stext='+pelicula]

    def parse(self, response):
        self.log('I just visited: ' + response.url)
        yield {
            'rating': response.css('div.avgrat-box::text').extract_first()
        }
