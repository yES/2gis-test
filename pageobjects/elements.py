# -*- coding: UTF-8 -*-
from base.page_element import BasePageElement
from selenium.webdriver.common.keys import Keys


css_locators = {
    'search_input': 'input.suggest__input',
    'search_submit_button': 'button.searchBar__submit._directory',
    'search_no_results_area': 'div.noResults._error_catalogNotFound',
    'search_results_area': 'div.searchResults__list',
    'search_suggest_list': 'ul.suggest__suggests',
}


class SearchFiledElement(BasePageElement):
    """Поле ввода строки поиска"""

    def __init__(self):
        self.locator = css_locators['search_input']
        super(SearchFiledElement, self).__init__(self.locator)

    def __set__(self, obj, val):
        self.driver.find_element_by_css_selector(self.locator).send_keys(val)

    def submit_by_enter(self):
        """Отправка поискового запроса по нажатию клавиши Enter"""

        self.driver.find_element_by_css_selector(self.locator).send_keys(Keys.RETURN)


class SearchSubmitButton(BasePageElement):
    """Кнопка поиска"""

    def __init__(self):
        self.locator = css_locators['search_submit_button']
        super(SearchSubmitButton, self).__init__(self.locator)

    def press(self):
        self.driver.find_element_by_css_selector(self.locator).click()


class SearchResultsArea(BasePageElement):
    """Блок для вывода резудьтатов поиска"""

    def __init__(self):
        self.locator = css_locators['search_results_area']
        super(SearchResultsArea, self).__init__(self.locator)


class SearchNoResultsArea(BasePageElement):
    """Блок для вывода информации о том, что ничего не найдено"""

    def __init__(self):
        self.locator = css_locators['search_no_results_area']
        super(SearchNoResultsArea, self).__init__(self.locator)


class SearchSuggestList(BasePageElement):
    """Список подсказок при поиске"""

    def __init__(self):
        self.locator = css_locators['search_suggest_list']
        super(SearchSuggestList, self).__init__(self.locator)

    def click_first_element(self):
        return self.driver.find_element_by_css_selector('{} > li:first-child'.format(self.locator)).click()
