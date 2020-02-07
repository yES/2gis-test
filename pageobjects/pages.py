# -*- coding: UTF-8 -*-
from connection import SeleniumChromeWrapper
from pageobjects.base.page_object import BasePageObject
from pageobjects.elements import SearchFiledElement, SearchSubmitButton, SearchResultsArea,\
    SearchNoResultsArea, SearchSuggestList


class MainPage(BasePageObject):
    """Главная страница сайта 2Гис"""

    url = 'http://2gis.ru/'
    search_field = SearchFiledElement()
    search_button = SearchSubmitButton()
    search_results_area = SearchResultsArea()
    search_no_results_area = SearchNoResultsArea()
    search_suggest_list = SearchSuggestList()

    def __init__(self):
        self.driver = SeleniumChromeWrapper().get_driver()
        self.driver.get(self.url)
