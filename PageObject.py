# -*- coding: utf-8 -*-
import urlparse


class Page(object):
    BASE_URL = 'https://rabota.mail.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()
