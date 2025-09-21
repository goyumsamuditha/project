"""RSS feed parser to collect structured items."""
import logging
import requests
import xml.etree.ElementTree as ET
from typing import List, Optional


class RSSItem:  # This is the class representing a single RSS feed item.
    """Class representing a single RSS feed item."""

    def __init__(self):  # Initialize the RSSItem class.
        self.data: List[Dict] = []

    def scraper(self, url: str) -> None:  # Method to scrape RSS feed from a given URL.
        """Fetch RSS feed content from a URL."""
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            root = ET.fromstring(response.content)
            for item in root.findall('.//item'):  # Parse each item in the RSS feed.
                title = item.findtext('title')
                link = item.findtext('link')
                pub_date = item.findtext('pubDate')
                description = item.findtext('description')
                self.data.append({
                    'title': title,
                    'link': link,
                    'pub_date': pub_date,
                    'description': description
                })
        except requests.RequestException as e:  # Handle request exceptions.
            logging.error(f"Error fetching RSS feed: {e}")
