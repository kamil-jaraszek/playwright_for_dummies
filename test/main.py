# from playwright.sync_api import sync_playwright
#
# with sync_playwright() as playwright:
#   browser = playwright.chromium.launch(headless=False)
#   context = browser.new_context()
#   page = context.new_page()
import playwright


def test_run():
  browser = playwright.sync_api.sync_playwright().start().chromium.launch(headless=False)
  context = browser.new_context()
  page = context.new_page()
  page.goto("https://www1.flightrising.com/login")
  page.get_by_role("button", name="AGREE").click()
  page.get_by_role("button", name="dismiss cookie message").click()
  page.locator("#uname").fill("Jarasznikos")
  page.locator("#pword").fill("toechodioler")
  page.get_by_role("button", name="Login").click()
  storage = context.storage_state(path="jarasznikos_storage.json")
  # page.pause()

def test_logged():
  browser = playwright.sync_api.sync_playwright().start().chromium.launch(headless=False)
  context = browser.new_context(storage_state="jarasznikos_storage.json")
  page = context.new_page()
  page.goto("https://www1.flightrising.com/lair")
  page.pause()
