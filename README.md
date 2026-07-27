# GitHub Repository Search Scraper

A Python script that logs into GitHub, searches for repositories matching a
search term, and exports the results (name, URL, star count) to a CSV file.

It uses [Playwright](https://playwright.dev/python/) to drive a headless
Chromium browser.

## How it works

1. Loads GitHub credentials from a `.env` file.
2. Launches a headless Chromium browser via Playwright.
3. Logs into GitHub using the provided username/password.
4. Prompts you for a search term and submits it via GitHub's search bar.
5. Scrapes the results across 2 pages of the search results, collecting each
   repository's name, URL, and star count.
6. Writes all collected repositories to `repositories.csv`.

## Requirements

- Python 3.8+
- [playwright](https://pypi.org/project/playwright/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

Install dependencies:

```bash
pip install playwright python-dotenv
playwright install chromium
```

## Setup

Create a `.env` file in the same directory as the script with your GitHub
credentials:

```
GITHUB_USERNAME=your-username
GITHUB_PASSWORD=your-password
```

## Usage

Run the script:

```bash
python scraper.py
```

You'll be prompted to enter a search term:

```
Enter search term: machine learning
```

The script will log in, perform the search, page through the first two
result pages, and print each repository as it's found.

## Output

A `repositories.csv` file is created (or overwritten) in the current
directory with the following columns:

| Column | Description                     |
|--------|----------------------------------|
| Name   | Repository name                 |
| URL    | Full URL to the repository      |
| Stars  | Star count as displayed on GitHub |

## Notes 

- **Selectors are fragile.** The script relies on specific CSS class names
  (e.g. `Repositories-module__resultContent__X93zw`) that GitHub generates
  dynamically and may change without notice, breaking the scraper.
- **Only 2 pages** of search results are collected (adjust the `range(2)`
  loop in the script to change this).
