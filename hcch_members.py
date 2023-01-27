from bs4 import BeautifulSoup
import requests

url = "https://www.hcch.net/pt/states/hcch-members/"

html = requests.get(url).content

soup = BeautifulSoup(html, 'html.parser')
filter_soup = soup.find("div", class_="row states-listing")


children = filter_soup.findChildren("a" , recursive=True)
for child in children:
    for country in child:
        print(country.text.strip())
    print(child['href'])
    