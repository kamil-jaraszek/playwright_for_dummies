from pages.dragon_lair import DragonLair
from pages.login import LoginPage
from playwright.sync_api import Page
import pytest
from playwright.sync_api import Browser

from test.conftest import credentials


def test_flightrising_login(page) -> None:
    login_page = LoginPage(page)
    login_page.load()
    login_page.login()
    pass

@pytest.mark.klikacz_general
def test_flightrising_bond_all_familiars(page: Page,credentials) -> None:
    username = credentials["username"]
    password = credentials["password"]
    dragon_lair_first_tab = DragonLair(page)
    dragon_lair_second_tab = DragonLair(page.context.new_page())
    dragon_lair_first_tab.load()
    dragon_lair_first_tab.login(username, password)
    dragon_lair_first_tab.open_lair()
    dragon_lair_first_tab.open_first_dragon()

    dragon_lair_second_tab.load("https://www1.flightrising.com/lair/")
    dragon_lair_second_tab.open_lair()
    dragon_lair_second_tab.open_first_dragon()
    # dragon_lair_first_tab.pause()
    # dragon_lair_second_tab.pause()
    dragon_lair_second_tab.switch_familiar()
    dragon_lair_second_tab.familiar_filter("not_bonded_today")

    while True:
        counter = 0
        dragon_lair_first_tab.bond_familiar() #click first familiar
        dragon_lair_second_tab.select_first_familiar() #select new familiar
        dragon_lair_first_tab.close_bonding() # close and refresh
        counter = counter + 1
        print(f"Bonded {counter} familiars")
    dragon_lair_first_tab.pause()
    dragon_lair_second_tab.pause()


