import requests
from bs4 import BeautifulSoup
from body_finder import body_finder

def headline():
    response = requests.get("https://www.fanabc.com")
    soup = BeautifulSoup(response.content, "html.parser")

    h_tags = soup.find_all(["h2", "h3"])
    for h in h_tags:
        a_tags = h.find_all("a")

        for a_tag in a_tags:
            link = a_tag.get("href")
            if link.startswith("https"):
                body_finder(link)

headline()
