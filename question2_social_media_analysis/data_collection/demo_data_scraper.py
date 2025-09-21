"""Scraper for demo e-commerce site (webscraper.io test site)."""
import requests
import time
import logging
from typing import List, Dict, Optional
from bs4 import BeautifulSoup


class DemoScraper:
    """Scraper for demo e-commerce site (webscraper.io test site)."""

    BASE_URL = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops?page={}"

    def __init__(self, delay: float = 1.0, max_retries: int = 3):  # Added type hint for max_retries
        self.delay = delay
        self.max_retries = max_retries
        self.data: List[Dict] = []

    def _fetch_page(self, url: str) -> Optional[str]:  # Added return type hint
        """Fetch a page with retries."""
        for attempt in range(self.max_retries):  # Use max_retries attribute
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                return response.text
            except requests.RequestException as e:  # Catch all request-related exceptions
                logging.warning(f"Attempt {attempt + 1} failed: {e}")
                time.sleep(self.delay)
        logging.error(f"Failed to fetch {url} after {self.max_retries} attempts.")  # Use max_retries attribute
        return None

    def scrape(self, pages: int = 2) -> None:  # Added type hint for pages
        for page in range(1, pages + 1):  # Changed to 1-based indexing
            html = self._fetch_page(self.BASE_URL.format(page))
            if not html:
                continue
            soup = BeautifulSoup(html, 'html.parser')
            products = soup.select_one('.col-sm-4.col-lg-4.col-md-4')
            for product in products:  # Extract product details
                title = product.select_one('.title').get('title', '').strip()
                price = product.select_one('.price').text.replace('$', '').strip()
                description = product.select_one('.description').text.strip()
                self.data.append({
                    'title': title,
                    'price': float(price),
                    'description': description
                })
            time.sleep(self.delay)  # Respectful scraping
