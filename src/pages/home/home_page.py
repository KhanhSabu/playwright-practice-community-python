from playwright.sync_api import Page
from src.pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.site_description = page.locator('p.site-description')

    @property
    def home_page_locs(self):
        return {
            'title': lambda title: self.page.get_by_role("heading", level=1, name=title),
            'description': lambda description: self.page.get_by_text(description),
            'search_bar': self.page.get_by_placeholder("Search products..."),
            'search_button': self.page.locator(".header-search-button"),
        }

    def goto(self):
        self.navigate('/')

    def search(self, keyword):
        self.home_page_locs['search_bar'].fill(keyword)
        self.home_page_locs['search_button'].click()
