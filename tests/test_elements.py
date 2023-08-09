import time

from pages.elements_page import TextSearchField, ImageSearchService


class TestElements:
    class TestWebSearch:

        def test_search_field(self, driver):
            web_search_field = TextSearchField(driver, 'https://ya.ru')
            web_search_field.open()
            time.sleep(8)
            checked_search_field = web_search_field.check_search_field()

            assert checked_search_field is not None, 'search field does not found'

            web_search_field.fill_search_field()
            checked_suggest_box = web_search_field.check_suggest()

            assert checked_suggest_box is not None, 'suggest box does not found'

            web_search_field.push_enter()

            assert driver.current_url == \
                   "https://ya.ru/search/?text=%D0%A2%D0%B5%D0%BD%D0%B7%D0%BE%D1%80&lr=" \
                   "43&search_source=yaru_desktop_common&search_domain=yaru", \
                'url does not correct'

            checked_link = web_search_field.check_link_first_line()

            assert checked_link == 'https://tensor.ru/', 'url does not correct'


    class TestImageBox:

        def test_ya_images(self, driver):
            check_ya_images = ImageSearchService(driver, 'https://ya.ru')
            check_ya_images.open()
            time.sleep(10)
            check_ya_images.check_image_button()
            time.sleep(3)

            driver.switch_to.window(driver.window_handles[1])
            assert driver.current_url == 'https://ya.ru/images/', 'url does not correct'

            check_ya_images.open_first_category()
            time.sleep(3)

            check_ya_images.open_first_image()
            time.sleep(3)
