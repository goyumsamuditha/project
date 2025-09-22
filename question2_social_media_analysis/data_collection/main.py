"""Main script to run all scrapers and save data to CSV."""
import json
import csv
import logging


from data_scraping import BookScraper
from demo_data_scraper import DemoScraper
from rss_scraper import RSSItem

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') # Configure logging

def save_to_csv(filename,data) -> None: # Save data to a CSV file.
    """Save data to a CSV file."""
    if not data:
        logging.warning("No data to save to CSV.")
        return
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    logging.info(f"Data saved to {filename}")

def main():
    """Main function to run scrapers and save data."""
    # Books Scraper
    books_scraper = BookScraper()
    books_scraper.scrape(pages=50)
    save_to_csv('books_data.csv', books_scraper.books)

    # Demo Scraper
    demo_scraper = DemoScraper()
    demo_scraper.scrape()
    save_to_csv('demo_data.csv', demo_scraper.data)

    # RSS Scraper
    rss_scraper = RSSItem()
    rss_scraper.scraper("https://www.theguardian.com/world/rss")
    save_to_csv("rss_items.csv", rss_scraper.data)

    logging.info("All scrapers have finished running.")

if __name__ == "__main__":
    main()