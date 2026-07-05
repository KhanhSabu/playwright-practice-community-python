from playwright.sync_api import Page

from src.pages.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def product_page_locs(self):
        return {
            'product_items': self.page.locator('.type-product'),
        }