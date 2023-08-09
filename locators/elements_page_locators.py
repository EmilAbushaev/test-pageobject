from selenium.webdriver.common.by import By


class TextSearchFieldLocators:
    SEARCH_FIELD = (By.XPATH, '//input[@class="search3__input mini-suggest__input"]')
    SUGGEST_BOX = (By.XPATH, '//li[@data-index="0"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[@class="search3__button mini-suggest__button"]')
    FIRST_LINK_LINE = (By.XPATH, '//a[@data-log-node="1_f09mw01-03"]/b')


class ImageBoxTestLocators:
    SEARCH_FIELD = (By.XPATH, '//input[@class="search3__input mini-suggest__input"]')
    MENU_BOX = (By.XPATH, '//div[@class="services-suggest__icons-more"]')
    IMAGE_BUTTON = (By.XPATH, '//a[@aria-label="Картинки"]')
    FIRST_CATEGORY = (By.XPATH, '//div[@class="PopularRequestList-Item PopularRequestList-Item_pos_0"]')
    NAME_OF_FIRST_CATEGORY = (By.XPATH, '//div[@class="PopularRequestList-SearchText"]')
    INPUT_FIELD = (By.XPATH, '//span[@class="input__box"]')
    FIRST_IMAGE = (By.XPATH, '//div[@class="serp-item serp-item_type_search '
                             'serp-item_group_search serp-item_pos_0 justifier__item i'
                             '-bem serp-item_js_inited justifier__item_first"]')
    IMAGE_IS_OPEN = (By.XPATH, '//img[@class="MMImage-Origin"]')
    BUTTON_NEXT = (By.XPATH, '//div[contains(@class, "ButtonNext")]')
    BUTTON_PREV = (By.XPATH, '//div[contains(@class, "ButtonPrev")]')
