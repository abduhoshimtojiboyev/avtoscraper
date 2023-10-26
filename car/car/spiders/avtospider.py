import random

import requests
import scrapy
from urllib.parse import urlencode
from car.items import Car
import http.client

# website shows only 1000 pages and every page contains 20 car so in order to get all cars data i need to divide them into price range
price_ranges = ['https://avtoelon.uz/uz/avto/?price[to]=8500',
                'https://avtoelon.uz/uz/avto/?price-currency=1&price[from]=8%20501&price[to]=13%20000',
                'https://avtoelon.uz/uz/avto/?price-currency=1&price[from]=13%20001&price[to]=50%20000',
                'https://avtoelon.uz/uz/avto/?price-currency=1&price[from]=50%20001']
class AvtospiderSpider(scrapy.Spider):
    name = "avtospider"
    allowed_domains = ["avtoelon.uz"]
    start_urls = ["https://avtoelon.uz/uz/avto/?price[to]=8500"]

    custom_settings = {
        'FEEDS': {
            'carsdata1.csv': {'format': 'csv', 'overwrite': False}
        }
    }


    number_stop = 0
    def parse(self, response):
        catalog_pages = response.css('div.row.list-item')
        for catalog in catalog_pages:
            relative_url = catalog.css('span.a-el-info-title a::attr(href)').get()
            if relative_url is not None:
                car_url = 'https://avtoelon.uz' + relative_url
                yield response.follow(car_url, callback=self.parse_car_page)

        next_page = response.css('span.pag-next-page a ::attr(href)').get()
        if next_page is not None:
            self.number_stop += 1
            print(self.number_stop)
            next_page_url = 'https://avtoelon.uz' + next_page
            yield response.follow(next_page_url, callback=self.parse)

    def parse_car_page(self, response):
        car = Car()
        car['brand'] = response.xpath('//span[@itemprop="brand"]/text()').get()
        car['name'] = response.xpath('//h1/span[@itemprop="name"]/text()').get()
        car['price'] = response.css('span.a-price__text ::text').get()

        dt_list = response.css('dl.description-params dt')
        for dt in dt_list:
            dt_value = dt.css('::text').get()

            # Attempt to get corresponding dd value with an <a> tag
            dd_value = dt.xpath('./following-sibling::dd/a/text()').get()

            # If <a> tag is not found, try to get it without <a> tag
            if dd_value is None:
                dd_value = dt.xpath('./following-sibling::dd/text()').get()

            if dd_value:
                dd_value = dd_value.strip()

            dt_value = dt_value.lower().replace(' ', '')
            if dt_value == 'yili':
                car['year'] = dd_value
            elif dt_value == 'kamibor':
                car['negotiable'] = dd_value
            elif dt_value == 'dvigatelhajmi':
                car['engine_size'] = dd_value
            elif dt_value == "yoqilg'ituri":
                car['fuel_type'] = dd_value
            elif dt_value == 'uzatishqutisi':
                car['transmission_box'] = dd_value
            elif dt_value == 'yurgani':
                car['distance_driven'] = dd_value
            elif dt_value == 'rang':
                car['color'] = dd_value
            elif dt_value == 'kraskaholati':
                car['color_condition'] = dd_value
            elif dt_value == 'uzatma':
                car['gearbox_type'] = dd_value
            elif dt_value == 'optika':
                car['optics'] = dd_value
            elif dt_value == 'salon':
                car['salon'] = dd_value
            elif dt_value == 'media':
                car['media'] = dd_value
            elif dt_value == 'avtomobilopsiyasi':
                car['vehicle_option'] = dd_value
            elif dt_value == 'viloyat':
                car['region'] = dd_value
            elif dt_value == 'shahar':
                car['city'] = dd_value
            else:
                pass

        yield car
