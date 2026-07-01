from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, path: str = '/'):
        """
        Navigates to a specific path relative to the baseURL or an absolute URL.
        """
        self.page.goto(path)
