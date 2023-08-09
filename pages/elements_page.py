import time

from selenium.webdriver import Keys
from pages.base_page import BasePage
from locators.elements_page_locators import TextSearchFieldLocators, ImageBoxTestLocators


class TextSearchField(BasePage):
    locators = TextSearchFieldLocators()

    def check_search_field(self):
        search_field = self.element_is_visible(self.locators.SEARCH_FIELD)
        time.sleep(3)
        return search_field

    def fill_search_field(self):
        self.element_is_visible(self.locators.SEARCH_FIELD).send_keys('Тензор')
        time.sleep(3)

    def check_suggest(self):
        suggest_box = self.element_is_visible(self.locators.SUGGEST_BOX)
        time.sleep(3)
        return suggest_box

    def push_enter(self):
        self.element_is_visible(self.locators.SEARCH_FIELD).send_keys(Keys.ENTER)
        time.sleep(3)

    def check_link_first_line(self):
        simple_link = self.element_is_visible(self.locators.FIRST_LINK_LINE)
        time.sleep(3)
        link_href = simple_link.get_attribute('href')
        time.sleep(3)
        simple_link.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        url = self.driver.current_url
        return link_href, url


class ImageSearchService(BasePage):
    locators = ImageBoxTestLocators()

    def check_image_button(self):
        self.element_is_visible(self.locators.SEARCH_FIELD).click()
        time.sleep(3)
        self.element_is_visible(self.locators.MENU_BOX).click()
        time.sleep(3)
        self.element_is_visible(self.locators.IMAGE_BUTTON).click()
        time.sleep(3)

    def open_first_category(self):
        category_name = self.element_is_visible(self.locators.FIRST_CATEGORY)
        time.sleep(3)
        category_name.click()
        time.sleep(3)

    def open_first_image(self):
        first_image = self.element_is_visible(self.locators.FIRST_IMAGE)
        time.sleep(3)
        self.action_move_to_element(first_image)
        time.sleep(3)
        first_image.click()
