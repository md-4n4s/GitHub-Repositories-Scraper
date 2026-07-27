from playwright.sync_api import sync_playwright
import time
from dotenv import load_dotenv
import os
import random

load_dotenv()

username = os.getenv("GITHUB_USERNAME")
password = os.getenv("GITHUB_PASSWORD")


def create_browser():
    return p.chromium.launch(
        headless=False
    )

def create_page(browser):
    return  browser.new_page()

def login(page):

    time.sleep(random.randint(1,3))

    try:
        page.fill("#login_field", username)

        page.fill("#password", password)

        page.locator("input[name=\"commit\"]").click()

        time.sleep(random.randint(1, 3))

        print(page.title())

        time.sleep(10)

    except:
        print("Login failed")

with sync_playwright() as p:

    browser = create_browser()
    page = create_page(browser)

    page.goto("https://github.com/login")

    login(page)