from playwright.sync_api import Page

from src.pages.base_page import BasePage


class ProductDetailPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def product_detail_page_locs(self):
        return {
            'product_title': self.page.get_by_role("heading",level=1),
            'product_description': self.page.locator('.woocommerce-product-details__short-description')
        }