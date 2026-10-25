import pytest
from playwright.sync_api import Page


@pytest.fixture(autouse=True)
def set_playwright_timeouts(page: Page) -> None:
    page.set_default_timeout(5000)
    page.set_default_navigation_timeout(5000)
