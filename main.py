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

    print("Loging in...")
    time.sleep(random.randint(1,3))

    try:
        page.fill("#login_field", username)

        page.fill("#password", password)

        page.locator("input[name=\"commit\"]").click()

    except:
        print("Login failed")

    else:
        print("Login successful")

with sync_playwright() as p:

    browser = create_browser()
    page = create_page(browser)

    page.goto("https://github.com/login")

    login(page)

    search = input("Enter search term: ")

    page.locator("button[aria-label=\"Search or jump to…\"]").click()

    page.locator("#query-builder-test").wait_for()
    page.fill("#query-builder-test", search)
    page.locator("#query-builder-test").press("Enter")

    time.sleep(10)