import re
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup # to process html text instead of strings on webpage

root = input("root URL: ")
if not root.startswith(("https://", "http://")):
    root = "https://" + root

try:
    website = urllib.request.urlopen(root)
    data = str(website.read()) 

    soup = BeautifulSoup(data, 'html.parser')

    links = [] # list to store urls
    for anchor in soup.find_all('a', href=True):
        href = anchor['href'] # value of href attribute
        fullURL = urljoin(root, href)
        links.append(fullURL)

    file = open("urls.csv", 'w')
    for link in links:
        file.write(link + '\n')
except Exception as e:
    print("Error:", e)

