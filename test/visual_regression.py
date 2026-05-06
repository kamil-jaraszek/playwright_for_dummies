from PIL.ImageChops import overlay

from pages.dragon_lair import DragonLair
from pages.login import LoginPage
from playwright.sync_api import Page, expect
import pytest
from PIL import ImageChops, Image
import numpy as np
import imagehash

from importlib.metadata import version



def visual_comparison(img_default_path, img_current_path, treshold=0.99):
  img_default = np.array(Image.open(img_default_path).convert("RGB"))
  img_current = np.array(Image.open(img_current_path).convert("RGB"))

  diff = np.abs(img_default - img_current)
  diff_pixels = np.any(diff > 0, axis=1)
  total_pixels = diff_pixels.size
  different_pixels = np.sum(diff_pixels)
  similarity = (total_pixels - different_pixels) / total_pixels
  print(f"Similarity: {similarity:.2%}")

  return similarity >= treshold


@pytest.mark.visual_regression_default
def test_loginpage_visualregression_setdefalutview(page) -> None:
    login_page = LoginPage(page)
    login_page.load()
    print("Visual regression default screenshot")
    page.screenshot(path="screenshots/login_page_default.png", full_page=True)



@pytest.mark.visual_regression
def test_loginpage_visualregression(page) -> None:
    login_page = LoginPage(page)
    login_page.load()
    print("Visual regression test")
    page.screenshot(path="screenshots/login_page_new.png", full_page=True)
    assert visual_comparison("screenshots/login_page_default.png", "screenshots/login_page_new.png",)

    pass
