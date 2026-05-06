from playwright.sync_api import Page


class LoginPage:
  URL = "https://www1.flightrising.com/login"

  def __init__(self, page: Page) -> None:
    self.page = page
    self.username_input = page.locator("#uname")
    self.password_input = page.locator("#pword")
    self.login_button =  page.get_by_role("button", name="Login")

    self.agree_button = page.get_by_role("button", name="AGREE")
    self.dismiss_coockie_button = page.get_by_role("button", name="dismiss cookie message")

  def load(self, url = URL) -> None:
    self.page.goto(url)
    try :
      self.agree_button.click()
      self.dismiss_coockie_button.click()
    except Exception:
      print("Element not found, probably already accepted cookies")

  def login(self, login = "Jarasznikos", password = "toechodioler" ) -> None:
    self.username_input.fill(login)
    self.password_input.fill(password)
    self.login_button.click()

  def pause(self) -> None:
    self.page.pause()
