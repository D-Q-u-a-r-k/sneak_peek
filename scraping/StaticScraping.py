import bs4 
import requests
from bs4 import BeautifulSoup as soup

my_url = 'something.com'

# opening up the connection, grabbing the page
r = requests.get(my_url)

#html parsing
page_soup = soup(r.content, 'html5lib')
print(page_soup.prettify()																																																											)

#grab data
containers = page_soup.find("div")
print(containers.prettify())

len(containers)

file_name = "something.csv"
f = open(file_name, "w")

headers = "label1", "label2","label3","label4","label5"

f.close()

 
