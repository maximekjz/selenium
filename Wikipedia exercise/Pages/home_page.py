from selenium.webdriver.common.by import By
from .search_result_page import SearchResult
from Introduction.Config.config import TestData
from BasePage import BasePage

class HomePage(BasePage):

    #Log in variables
    USERNAME = (By.ID, 'wpName1')
    PASSWORD = (By.ID, 'wpPassword1')
    LOGIN_BUTTON = (By.ID, 'wpLoginButton')
    SIGNIN_TITLE = (By.ID, 'wpSigninTitle')
    KEEP_LOGGED_IN = (By.ID, 'wpKeepLoggedIn')
    FEATURED_ARTICLE_TITLE = (By.ID, "From_today's_featured_article")
    FEATURED_ARTICLE_CONTENT = (By.ID, "From_today.27s_featured_article")
    DID_U_KNOW_TITLE = (By.ID, "Did_you_know_...")
    DID_U_KNOW_CONTENT = (By.ID, "mp-dyk")
    SISTER_PROJECTS = (By.ID, "Wikipedia's_sister_projects")
    WELCOME = (By.ID, 'mp-welcomecount')
    LANGUAGE_DROPDOWN = (By.ID, "searchLanguage")
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'cdx-button cdx-button--action-default cdx-button--weight-normal cdx-button--size-medium cdx-button--framed cdx-search-input__end-button')
    SEARCH_FIELD = (By.CSS_SELECTOR, 'cdx-text-input cdx-text-input--has-start-icon cdx-text-input--status-default cdx-search-input__text-input')
    SEARCH_SUGGESTIONS = (By.CSS_SELECTOR, '.cdx-menu-item__text')


    def __init__(self, driver):
        super().__init__(driver)

    def get_logged_in_page_title(self, title):
        return self.get_title(title)

    def is_login_title_exists(self):
        return self.is_visible(self.LOGIN_BUTTON)

    def is_signin_link_exists(self):
        return self.is_visible(self.SIGNIN_TITLE)

    def do_login(self, username, password):
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.KEEP_LOGGED_IN)
        self.do_click(self.LOGIN_BUTTON)
        return HomePage(self.driver)

    def new_url(self):
        self.is_url_new(TestData.LOG_URL)

    def check_visibility_of_elements(self):
        elements = [
            self.FEATURED_ARTICLE_TITLE,
            self.FEATURED_ARTICLE_CONTENT,
            self.DID_U_KNOW_TITLE,
            self.DID_U_KNOW_CONTENT,
            self.SISTER_PROJECTS
        ]
        return all(self.is_visible(element) for element in elements)

    def change_language(self, language_code):
        dropdown = self.get_element(self.LANGUAGE_DROPDOWN)
        dropdown.send_keys(language_code)

    def do_search(self, search_content):
        self.do_send_keys(self.SEARCH_FIELD, search_content)
        self.do_click(self.SEARCH_BUTTON)
        return SearchResult(self.driver)

    def is_search_button_visible(self):
        return self.is_visible(self.SEARCH_BUTTON)

    def is_search_field_visible(self):
        return self.is_visible(self.SEARCH_FIELD)

    def enter_search_term(self, partial_term):
        self.do_send_keys(self.SEARCH_FIELD, partial_term)

    def search_suggestions_visible(self):
        return self.is_visible(self.SEARCH_SUGGESTIONS)