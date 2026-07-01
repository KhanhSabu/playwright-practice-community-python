import pytest
from playwright.sync_api import expect

@pytest.mark.SAMPLE_20260701
def test_home_page_should_display_correct_title_and_description(home_page):
    # Open homepage
    home_page.goto()
    
    # Verify site title and site description is correct
    expect(home_page.home_page_locs['title']("E-commerce site testing")).to_be_visible()
    expect(home_page.home_page_locs['description']('Website thực hành – hoctest.com')).to_be_visible()
