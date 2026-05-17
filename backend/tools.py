import requests
from bs4 import BeautifulSoup

SERPER_API_KEY = "YOUR_KEY"

def web_search(query):
    url = "https://google.serper.dev/search"
    payload = {"q": query}
    headers = {"X-API-KEY": SERPER_API_KEY}
    res = requests.post(url, json=payload, headers=headers)
    return res.json()

def scrape_page(url):
    r = requests.get(url, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup.get_text()

def arxiv_search(query):
    url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results=5"
    return requests.get(url).text