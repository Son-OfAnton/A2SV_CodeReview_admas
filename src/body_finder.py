import requests
from bs4 import BeautifulSoup

def body_finder(link):
    """
    Scrapes the body content of a fana broadcastig corporation web page and saves 
    the text of all paragraphs inside the main article to a file named "news.txt".

    Parameters:
        link (str): The URL of the web page to scrape.

    Raises:
        requests.exceptions.RequestException: If an error occurs during the HTTP request.
        Exception: If any other unexpected error occurs.

    Note:
        The function uses the 'requests' library to perform an HTTP GET request
        to the given 'link' and 'BeautifulSoup' from 'bs4' to parse the HTML content.
        The text of all paragraphs within the main article of the page will be
        saved to the file 'news.txt' in append mode.

    Example:
        link_to_scrape = "https://fanabc.com"  # Replace with the actual link you want to scrape
        body_finder(link_to_scrape)
    """
    try:
        response = requests.get(link)
        
        if response.status_code != 200:
            print(f"Failed to retrieve data from {link}. Status code: {response.status_code}")
            return

        soup = BeautifulSoup(response.content, "html.parser")

        article = soup.find("article")
        
        if article:
            div_entry_content = article.find("div", class_="entry-content clearfix single-post-content")
            
            if div_entry_content:
                p_tags = div_entry_content.find_all("p")
                
                with open("news.txt", "a") as file:
                    for p in p_tags:
                        file.write(p.text + "\n")
        else:
            print("No article found on the page.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the HTTP request: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
