from playwright.sync_api import Page

from src.pages.base_page import BasePage


class ProductDetailPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.product_title = self.page.get_by_role("heading", level=1)
        self.product_description = self.page.locator('.woocommerce-product-details__short-description')