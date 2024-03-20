import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/......"  # Insert the URL of the Wikipedia page you want to scrape
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the main content container and extract the page title
    content_container = soup.find("div", class_="mw-content-container")
    page_title = content_container.find("span", class_="mw-page-title-main").text.strip()
    print("Page Title:", page_title)
    print('-' * 50)

    # Find all <h3> tags and extract relevant information
    h3_tags = soup.find_all("h3")
    for h3_tag in h3_tags:
        # Check if the <h3> tag contains any <span> elements
        span_elements = h3_tag.find_all("span")
        for span in span_elements:
            # Check if the <span> element is not empty and does not contain unwanted text
            span_text = span.text.strip()
            if span_text and span_text not in ['[edit]', 'edit', ']', '[']:
                print(span_text)
                print('-' * 10)

else:
    print("Failed to fetch data from the website.")
