import requests
from bs4 import BeautifulSoup
from body_finder import body_finder

def headline():
    """
    Extracts headlines from a web page and calls the 'body_finder' function
    to scrape the content of each headline link.

    Raises:
        requests.exceptions.RequestException: If an error occurs during the HTTP request.
        Exception: If any other unexpected error occurs.

    Note:
        The function sends an HTTP GET request to "https://www.fanabc.com" and
        uses 'BeautifulSoup' from 'bs4' to parse the HTML content.
        It finds all <h2> and <h3> tags and then extracts the URLs of the <a> tags within.
        If the URL starts with "https", it calls the 'body_finder' function to
        scrape the content of that link.

    Example:
        headline()
    """
    try:
        response = requests.get("https://www.fanabc.com")
        
        if response.status_code != 200:
            print(f"Failed to retrieve data from https://www.fanabc.com. Status code: {response.status_code}")
            return

        soup = BeautifulSoup(response.content, "html.parser")
        h_tags = soup.find_all(["h2", "h3"])
        
        for h in h_tags:
            a_tags = h.find_all("a")

            for a_tag in a_tags:
                link = a_tag.get("href")
                if link.startswith("https"):
                    body_finder(link)
                    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the HTTP request: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

headline()
