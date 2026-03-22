from pages.dragon_lair import DragonLair
from pages.login import LoginPage
from playwright.sync_api import Page


def test_fixtures_flightrisghn_login(login_page: LoginPage) -> None:

  login_page.load()
  login_page.login()
  login_page.pause()
