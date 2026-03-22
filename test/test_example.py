import conftest
from playwright.sync_api import Page

# from main import page


def test_clickFamiliars(browser) -> None:
  page = browser.new_page()
  page2 = browser.new_page()


  page.goto("https://www1.flightrising.com/login")
  page.get_by_role("button", name="AGREE").click()
  page.get_by_role("button", name="dismiss cookie message").click()
  page.locator("#uname").fill("Jarasznikos")
  page.locator("#pword").fill("toechodioler")
  page.get_by_role("button", name="Login").click()
  page.get_by_role("link", name="Dragon Lair").click()
  page.locator(".lair-page-dragon-thumbnail").first.click()

  url = page.url

  page2.goto("https://www1.flightrising.com/login")
  page2.get_by_role("button", name="AGREE").click()
  page2.get_by_role("button", name="dismiss cookie message").click()
  page2.locator("#uname").fill("Jarasznikos")
  page2.locator("#pword").fill("toechodioler")
  page2.get_by_role("button", name="Login").click()
  page2.get_by_role("link", name="Dragon Lair").click()
  page2.locator(".lair-page-dragon-thumbnail").first.click()
  page2.get_by_role("link", name="Switch familiars").click()
  page2.get_by_label("Bond Status Any Bonded Today").select_option("not_bonded_today")
  counter = True
  while counter:
    page.locator("#dragon-profile-button-bond").click() #click first familiar
    page2.locator(".itemicon.itemicon-fam-prev").first.click() #select new familiar
    page.locator("#bonding-dialog").get_by_role("button", name="Close").click() # close and refresh



  page.pause()
  page2.pause()
  pass

