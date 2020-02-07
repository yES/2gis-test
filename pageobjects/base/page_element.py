# -*- coding: UTF-8 -*-
from connection import SeleniumChromeWrapper

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePageElement(object):
    """Базовый HTML элемент страницы"""

    def __init__(self, locator):
        self.locator = locator
        self.driver = SeleniumChromeWrapper().get_driver()

    def is_visible(self, timeout=5):
        """Метод для проверки того, отображается ли HTML элемент. Используется для AJAX элементов"""

        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.locator)))
            return True
        except TimeoutException:
            return False
