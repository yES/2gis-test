# -*- coding: utf-8 -*-
from connection import SeleniumChromeWrapper
from pageobjects.pages import MainPage

import unittest


class DoubleGisSearchTestCase(unittest.TestCase):
    """Поиск информации по нажатию кнопки поиска"""

    @classmethod
    def setUpClass(cls):
        cls.verificationErrors = []
        cls.driver = SeleniumChromeWrapper().get_driver()
        super(DoubleGisSearchTestCase, cls).setUpClass()

    def test_not_found(self):
        """Поиск по нажатию кнопки поиска, который не выдает результатов"""

        page = MainPage()
        page.search_field = 'sdfsdf'
        page.search_button.press()
        self.assertTrue(page.search_no_results_area.is_visible())

    def test_not_found_by_enter(self):
        """Поиск по нажатию клавиши Enter, который не выдает результатов"""

        page = MainPage()
        page.search_field = 'sdfsdf'
        page.search_field.submit_by_enter()
        self.assertTrue(page.search_no_results_area.is_visible())

    def test_success(self):
        """Поиск по нажатию кнопки поиска, который выдает список результатов"""

        page = MainPage()
        page.search_field = 'adidas'
        page.search_button.press()
        self.assertTrue(page.search_results_area.is_visible())

    def test_success_by_enter(self):
        """Поиск по нажатию клавиши Enter, который выдает список результатов"""

        page = MainPage()
        page.search_field = 'adidas'
        page.search_field.submit_by_enter()
        self.assertTrue(page.search_results_area.is_visible())

    def test_success_by_suggest(self):
        """Успешный поиск с помошью выбора подсказки из саджеста"""

        page = MainPage()
        page.search_field = u'пицц'
        self.assertTrue(page.search_suggest_list.is_visible())
        page.search_suggest_list.click_first_element()
        self.assertTrue(page.search_results_area.is_visible())

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super(DoubleGisSearchTestCase, cls).tearDownClass()

if __name__ == "__main__":
    unittest.main()
