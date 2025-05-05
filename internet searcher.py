import requests
from bs4 import BeautifulSoup

search = input("enter anything to search: ")
url = f"https://en.wikipedia.org/wiki/{search}"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
title = soup.find("h1").text
print(f"Title: {title}")
paragraphs = soup.find_all("p")
for i, paragraph in enumerate(paragraphs):
    print(f"Paragraph {i+1}: {paragraph.text}")
