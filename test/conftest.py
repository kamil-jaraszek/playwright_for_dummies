import pytest

from pages.login import LoginPage
from pages.dragon_lair import DragonLair

@pytest.fixture
def dragon_page(page) -> DragonLair:
    return DragonLair(page)

@pytest.fixture
def login_page(page) -> LoginPage:
    return LoginPage(page)

