import requests
from bs4 import BeautifulSoup

# A list of urls to scrape
url = ["https://www.w3schools.com", "https://expo.dev/go", "https://reactnative.dev"]

# Where the data will be stored
items = []

# Loops through each website
for i in url:
    # Loads up the website
    response = requests.get(i)

    soup = BeautifulSoup(response.text, "html.parser")
    
    # Gets all the h1 tags
    titles = soup.find_all("h1")

    # Loops through all the data on the current website
    for title in titles:
        # Adds the item to the list
        items.append(title.text)
        print(title.text)

# Outputs the list of items gathered
print(items)