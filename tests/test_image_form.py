from uuid import uuid4

from playwright.sync_api import Page, expect


def test_submitting_form_adds_image_to_list(page: Page, base_url: str) -> None:
    title = f"Playwright image {uuid4().hex}"
    page.goto(base_url)

    page.get_by_role("textbox", name="Image Title").fill(title)
    page.get_by_role("textbox", name="Image URL").fill(
        "https://example.com/playwright-image.png"
    )
    page.get_by_role("button", name="Submit Form").click()

    expect(page.get_by_role("heading", name=title)).to_be_visible()


def test_empty_form_shows_validation_messages(page: Page, base_url: str) -> None:
    page.goto(base_url)

    page.get_by_role("button", name="Submit Form").click()

    expect(page.get_by_text("Please type a title for the image.")).to_be_visible()
    expect(page.get_by_text("Please type a valid URL")).to_be_visible()


def test_invalid_url_shows_validation_message(page: Page, base_url: str) -> None:
    title = f"Invalid URL {uuid4().hex}"
    page.goto(base_url)

    page.get_by_role("textbox", name="Image Title").fill(title)
    page.get_by_role("textbox", name="Image URL").fill("not-a-url")
    page.get_by_role("button", name="Submit Form").click()

    expect(page.get_by_text("Please type a valid URL")).to_be_visible()
    expect(page.get_by_role("heading", name=title)).to_have_count(0)
