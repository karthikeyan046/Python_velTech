import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

visited = set()

def crawl(url, depth=2):
    if url in visited or depth == 0:
        return

    try:
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        visited.add(url)

        soup = BeautifulSoup(page.text, 'html.parser')
        title = soup.title.string.strip() if soup.title else "No Title"
        print(f"[{len(visited)}] {url} → {title}")

        for tag in soup.find_all('a', href=True):
            link = urljoin(url, tag['href'])
            if urlparse(link).netloc == urlparse(url).netloc:
                crawl(link, depth - 1)

        time.sleep(1)

    except:
        pass

# Start crawling
crawl('https://quotes.toscrape.com', depth=2)


#package to be installed:
#pip install requests
#pip install beautifulsoup4
