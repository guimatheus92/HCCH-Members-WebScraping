from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime

# Base URL to be used for the links
base_url = "https://www.hcch.net"

# URLs to scrape
urls = ["https://www.hcch.net/pt/states/hcch-members/", "https://www.hcch.net/en/states/hcch-members/"]

def get_countries_data(url):
    # Get the HTML content of the page
    html = requests.get(url).content
    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(html, 'html.parser')
    # Find the div containing the countries list
    filter_soup = soup.find("div", class_="row states-listing")
    # Find all the anchor tags within the div
    children = filter_soup.findChildren("a" , recursive=True)
    # Create an empty list to store the scraped data
    records = []
    # Loop through each anchor tag
    for child in children:
        # Append a dictionary containing the scraped data to the list
        records.append({'date': datetime.today().strftime('%Y-%m-%d'),'country': child.text.strip(), 'link': base_url + child['href'], 'language': url.split("/")[-3]})
    # Create a dataframe from the list of dictionaries
    df = pd.DataFrame.from_records(records)
    # Reorder the columns
    df = df[['date','country','link','language']]
    # Return the dataframe
    return df

# Concatenate the dataframes returned by the function for each url
df = pd.concat([get_countries_data(url) for url in urls])

print(df)