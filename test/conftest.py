import pytest

from pages.login import LoginPage
from pages.dragon_lair import DragonLair

@pytest.fixture
def dragon_page(page) -> DragonLair:
    return DragonLair(page)

@pytest.fixture
def login_page(page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture()
def on_start():
  print("on_start")


def pytest_addoption(parser):
  parser.addoption("--username", action="store", default=None)
  parser.addoption("--password", action="store", default=None)

#hasła są w keepasie
#python3 -m pytest .\test\test_flightrising.py --headed --slowmo 1500 -m klikacz_general --username=Jarasznikos --password=toechodioler
@pytest.fixture
def credentials(request):
  username = request.config.getoption("--username")
  password = request.config.getoption("--password")
  if username and password:
    return {"username": username, "password": password}
  else:
    raise ValueError("Please provide --username and --password when running the tests.")


