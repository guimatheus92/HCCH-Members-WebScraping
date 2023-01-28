from datetime import datetime
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Define the base URL and the list of URLs to be scraped
base_url = "https://www.hcch.net"
urls = ["https://www.hcch.net/pt/states/hcch-members/", "https://www.hcch.net/en/states/hcch-members/"]

# Define a function to get the data from the URLs
def get_countries_data():
    # Initialize an empty list to store the records
    records = []
    # Get the current date and time and format it as a string
    DT_RUN = datetime.now().strftime("%Y-%m-%d")
    # Loop through each URL in the list
    for url in urls:
        # Get the HTML content from the URL
        html = requests.get(url).content
        # Create a BeautifulSoup object to parse the HTML
        soup = BeautifulSoup(html, 'html.parser')
        # Find the div element with class "row states-listing"
        filter_soup = soup.find("div", class_="row states-listing")
        # Find all child elements within the div element
        children = filter_soup.findChildren("a" , recursive=True)        
        # Loop through each child element
        for child in children:
            # Get the country name
            NM_COUNTRY = child.text.strip()            
            # Get the link to the country's page
            DS_COUNTRYLINK = base_url + child['href']
            # Get the ISO alpha-2 code for the country
            CD_ISOALPHA2 = DS_COUNTRYLINK[-2:]
            # Get the language of the website
            NM_WEBSITELANGUAGE = url.split("/")[-4]
            # Get the source link of the data
            DS_SOURCELINK = url            
            # Append the data to the records list
            records.append([DT_RUN, NM_COUNTRY, CD_ISOALPHA2, DS_COUNTRYLINK, NM_WEBSITELANGUAGE, DS_SOURCELINK])

    # Create a dataframe from the records list
    df = pd.DataFrame(records, columns=["DT_RUN", "NM_COUNTRY", "DS_COUNTRYLINK", "NM_WEBSITELANGUAGE", "DS_SOURCELINK"])
    return df

# Call the function to get the data
df = get_countries_data()

# Export the dataframe to a CSV file
#df.to_csv('countries_data.csv', index=False)

# Print the dataframe
print(df)