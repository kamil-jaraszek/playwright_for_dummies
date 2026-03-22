from playwright.sync_api import Page
from pages.login import LoginPage


class DragonLair(LoginPage):
  # URL = "https://www1.flightrising.com/lair/"

  def __init__(self, page: Page) -> None:
    super().__init__(page)
    self.page = page
    page.set_default_navigation_timeout(60_000)
    self.lair_link = page.get_by_role("link", name="Dragon Lair")
    self.first_dragon_thumbnail = page.locator(".lair-page-dragon-thumbnail").first
    self.switch_familiars_button = page.get_by_role("link", name="Switch familiars")
    self.familiar_filter_list = page.get_by_label("Bond Status Any Bonded Today")
    self.bond_familiar_button =  page.locator("#dragon-profile-button-bond")
    self.new_first_familiar = page.locator(".itemicon.itemicon-fam-prev").first
    self.close_bonding_dialog =  page.locator("#bonding-dialog").get_by_role("button", name="Close")


  def open_lair(self) -> None:
    self.lair_link.click()

  def open_lair_by_link(self) -> None:
    self.page.goto(self.URL)

  def open_first_dragon(self) -> None:
    self.first_dragon_thumbnail.click()

  def select_first_familiar(self) -> None:
   self.new_first_familiar.click()

  def switch_familiar(self) -> None:
    self.switch_familiars_button.click()

  def familiar_filter(self, option: str) -> None:
    self.familiar_filter_list.select_option(option)

  def close_bonding(self) -> None:
    self.close_bonding_dialog.click()

  def bond_familiar(self) -> None:
    self.bond_familiar_button.click()
