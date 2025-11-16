import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import csv

# RSS feed URL
rss_url = "https://www.europarl.europa.eu/rss/doc/top-stories/en.xml"

def get_top_stories_to_csv(rss_url, output_file="european_parliament_top_stories.csv"):
    # Fetch RSS feed
    response = requests.get(rss_url)
    response.raise_for_status()

    # Parse XML
    root = ET.fromstring(response.content)
    channel = root.find("channel")

    stories = []

    for item in channel.findall("item"):
        title = item.findtext("title")
        link = item.findtext("link")
        pub_date = item.findtext("pubDate")
        description_html = item.findtext("description")

        # Clean HTML using BeautifulSoup
        soup = BeautifulSoup(description_html, "html.parser")
        description_text = soup.get_text(" ", strip=True)

        stories.append({
            "Title": title,
            "Link": link,
            "Publication Date": pub_date,
            "Description": description_text
        })

    # Save to CSV
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Title", "Link", "Publication Date", "Description"])
        writer.writeheader()
        writer.writerows(stories)

    print(f"Successfully saved {len(stories)} top stories to '{output_file}'")

if __name__ == "__main__":
    get_top_stories_to_csv(rss_url)
