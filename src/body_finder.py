import requests
from bs4 import BeautifulSoup

def body_finder(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.content, "html.parser")

    article = soup.find("article")
    if article:
        div_entry_content = article.find("div", class_="entry-content clearfix single-post-content")
        
        if div_entry_content:
            p_tags = div_entry_content.find_all("p")
            
            with open("news.txt", "a") as file:
                for p in p_tags:
                    file.write(p.text + "\n")


    
