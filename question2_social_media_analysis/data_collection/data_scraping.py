"""Book Scraper Module
This script scrapes book data from books.toscrape.com, handles pagination,
implements basic error handling, and saves results in CSV/JSON format.
"""
import time
import logging
import requests
import re

from urllib.parse import urljoin
from typing import List, Dict, Optional
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class BookScraper:
    base_url = "http://books.toscrape.com/" # Example website for scraping

    def __init__(self, delay: float = 1.0, max_retries: int = 3): # delay between requests, max retries on failure
        self.delay = delay
        self.max_retries = max_retries
        self.session = requests.Session()
        self.books: List[Dict[str, any]] = []

    def fetch_page(self, url: str) -> Optional[BeautifulSoup]: # Fetch and parse a page
        for attempt in range(self.max_retries):
            try:
                response = self.session.get(url)
                response.raise_for_status()
                response.encoding = "utf-8"
                return BeautifulSoup(response.text, "html.parser")
            except requests.RequestException as e: # Handle request exceptions
                logging.error(f"Error fetching {url}: {e}. Attempt {attempt + 1} of {self.max_retries}.")
                time.sleep(self.delay)
        return None

    def scrape(self, pages: int = 3) -> None: # Scrape a given number of pages
        for page in range(1, pages + 1):
            url = f"{self.base_url}catalogue/page-{page}.html"
            html = self.fetch_page(url)
            if not html:
                continue

            books = html.find_all("article", class_="product_pod")
            for book in books:
                title = book.h3.a["title"]

                # Clean price text
                price_text = book.find("p", class_="price_color").text
                price_clean = re.sub(r"[^\d.]", "", price_text)
                price = float(price_clean)

                rating = book.p["class"][1]

                # Build absolute book URL safely
                relative_url = book.h3.a["href"]
                book_url = urljoin(self.base_url + "catalogue/", relative_url)

                # Fetch category from detail page
                category, availability = "Unknown", "Unknown"
                book_html = self.fetch_page(book_url)
                if book_html:
                    breadcrumb = book_html.select("ul.breadcrumb li a")
                    if len(breadcrumb) >= 3:
                        category = breadcrumb[2].text.strip()

                    availability = book_html.select_one("p.availability")
                    if availability:
                        availability = availability.text.strip()

                    description = book_html.select_one("#product_description ~ p")
                    if description:
                        description = description.text.strip()

                        # Append book data to the list
                        self.books.append({
                            "title": title,
                            "price": price,
                            "rating": rating,
                            "category": category,
                            "availability": availability,
                            "description": description
                        })
                time.sleep(self.delay)  # Respectful delay between requests