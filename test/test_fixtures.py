from pages.dragon_lair import DragonLair
from pages.login import LoginPage
from playwright.sync_api import Page
import pytest

@pytest.mark.parametrize("username", ["dupa1", "dupa2", "dupa3"])
def test_fixtures_flightrisghn_login(login_page: LoginPage, username) -> None:

  login_page.load()
  login_page.login()
  print(username)
  login_page.pause()



