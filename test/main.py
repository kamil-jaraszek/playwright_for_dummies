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
  context2 = browser.new_context()
  page2 = context2.new_page()
  page = context.new_page()
  page.goto("https://www1.flightrising.com/login")
  page2.goto("https://www1.flightrising.com")
  page.pause()
  page2.pause()
  print("Test")
