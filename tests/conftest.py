import os
import pytest
from dotenv import load_dotenv

from src.pages.product.product_detail_page import ProductDetailPage
from src.pages.product.product_page import ProductPage
from src.pages.home.home_page import HomePage

# Load environment variables
load_dotenv()

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """
    Override browser_context_args to set the base_url from environment.
    """
    base_url = os.getenv("BASE_URL", "https://e-commerce-dev.betterbytesvn.com/")
    return {
        **browser_context_args,
        "base_url": base_url,
    }

@pytest.fixture
def home_page(page):
    """
    Fixture to provide an initialized HomePage instance.
    """
    return HomePage(page)

@pytest.fixture
def product_page(page):
    return ProductPage(page)

@pytest.fixture
def product_detail_page(page):
    return ProductDetailPage(page)
