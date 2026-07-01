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
        }

    def goto(self):
        self.navigate('/')
