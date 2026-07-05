import re

import pytest
from playwright.sync_api import expect

@pytest.mark.SAMPLE_20260701
def test_home_page_should_display_correct_title_and_description(home_page):
    # Open homepage
    home_page.goto()
    
    # Verify site title and site description is correct
    expect(home_page.home_page_locs['title']("E-commerce site testing")).to_be_visible()
    expect(home_page.home_page_locs['description']('Website thực hành – hoctest.com')).to_be_visible()


@pytest.mark.HOME_20260701
def test_search_product_by_keyword_return_matching_products(home_page, product_page, product_detail_page):
    keyword = "ISTQB"
    expected_product_count = 5

    home_page.goto()

    # Step 1: search params appear in the URL and 5 products are found
    home_page.search(keyword)
    expect(product_page.page).to_have_url(re.compile(r"post_type=product&s=ISTQB"))
    expect(product_page.product_page_locs['product_items']).to_have_count(expected_product_count)

    # Step 2: open each product and assert the keyword shows in the title or description
    for i in range(expected_product_count):
        product_page.product_page_locs['product_items'].nth(i).click()

        matches = (
            product_detail_page.product_detail_page_locs['product_title'].or_(
                product_detail_page.product_detail_page_locs['product_description']).filter(has_text=keyword)
        )

        expect(matches.first).to_be_visible()
        product_detail_page.page.go_back()