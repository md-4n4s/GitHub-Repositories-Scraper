from playwright.sync_api import sync_playwright
import time
from dotenv import load_dotenv
import os
import random
import csv
from urllib.parse import urljoin

url = "https://github.com"

load_dotenv()

# Get username and password from env file
username = os.getenv("GITHUB_USERNAME")
password = os.getenv("GITHUB_PASSWORD")

# Function launches Chromium broswer 
def create_browser():
    return p.chromium.launch(
        headless=True # browser runs without opening a visible window
    )

# Creates a new browser tab
def create_page(browser):
    return  browser.new_page()

def login(page):

    print("Logging in...")
    time.sleep(random.randint(1,3))

    try:
        page.fill("#login_field", username)
        page.fill("#password", password)

        # Clicks input where name = commit
        page.locator("input[name=\"commit\"]").click()

    except:
        print("Login failed")

    else:
        print("Login successful")

with sync_playwright() as p:

    browser = create_browser()
    page = create_page(browser)

    page.goto("https://github.com/login")

    try:
        login(page)

        # Get the search from user from console
        search = input("Enter search term: ")

        page.locator("button[aria-label=\"Search or jump to…\"]").click()

        # Wait for it to load
        page.locator("#query-builder-test").wait_for()
        page.fill("#query-builder-test", search)

        # Press Enter (not on page)
        page.locator("#query-builder-test").press("Enter")

        repositories = []

        # Scrapes 2 pages
        for _ in range(2):

            time.sleep(random.randint(1, 3))
            results = page.locator("div.Repositories-module__resultContent__X93zw")

            for i in range(results.count()):
                repository = results.nth(i) # Get repository element at the current index

                repo = {"name": repository.locator("div.Header-module__title__EpJLU").inner_text().strip(),
                        "url": urljoin(url, repository.locator("h3 a").get_attribute("href")),
                        "stars": repository.locator("ul.Footer-module__footer__rWx13 a").inner_text().strip()}
                print(repo)
                repositories.append(repo)

            # Move to next page
            page.locator("a[aria-label=\"Next Page\"]").click()

        # Craete or open repositories.csv in write mode
        with open("repositories.csv", "w", newline="") as csvfile:
            # Create a writer to write in csv file
            writer = csv.writer(csvfile)

            writer.writerow(["Name", "URL", "Stars"])

            for repo in repositories:
                writer.writerow([repo["name"], repo["url"], repo["stars"]])

    except:
        print("Error occured")

# Close the browser
browser.close()
