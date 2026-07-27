from playwright.sync_api import sync_playwright
import time
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("GITHUB_GMAIL_USERNAME")
password = os.getenv("GITHUB_PASSWORD")

def create_browser():
    return p.chromium.launch(headless=False)

def create_page(browser):
    return  browser.new_page()



with sync_playwright() as p:

    browser = create_browser()
    page = create_page(browser)

    page.goto("https://github.com/login")

