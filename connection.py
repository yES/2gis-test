# -*- coding: UTF-8 -*-
from selenium import webdriver


class SeleniumChromeWrapper(object):
    """Враппер для web драйвера. Реализован как singleton"""

    _instance = None
    driver = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SeleniumChromeWrapper, cls).__new__(cls, *args, **kwargs)
        if not cls.driver:
            cls.driver = webdriver.Chrome()
        return cls._instance

    def get_driver(self):
        return self.driver
