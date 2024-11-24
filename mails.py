import urllib.request
import re
from urllib.parse import urljoin  # To handle relative URLs

regex_mail = re.compile(r"[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z]+")

file = open("urls.csv", 'r')
urls = file.readlines()
file.close()  # Manually close the file

file2 = open("emails.csv", 'a')

for url in urls:
    url = url.strip()  # Remove trailing whitespace or newlines

    if url.startswith("#"):
        continue

    if not url.startswith(("https://", "http://")):
        root_url = input("root URL: ")
        url = urljoin(root_url, url)

    try:
        requested_url = urllib.request.urlopen(url)
        data = str(requested_url.read())

        emails = regex_mail.findall(data)

        for item in emails:
            file2.write(item + "\n")
    except Exception as e:
        print(f"Error processing {url}: {e}")

file2.close()  

