"""Book Scraper Module
This script scrapes book data from books.toscrape.com, handles pagination,
implements basic error handling, and saves results in CSV/JSON format.
"""
import time
import logging
import requests
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

            books = html.find_all("article", class_="product_pod") # Find all book entries
            for book in books: # Extract book details
                title = book.h3.a["title"]
                price = float(book.find("p", class_="price_color").text.replace("£", "").strip())
                rating = book.p["class"][1]
                self.books.append({"title": title, "price": price, "rating": rating})

            time.sleep(self.delay) # Respectful delay between page requests