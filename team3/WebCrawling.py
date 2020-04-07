# from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

# html = urlopen("https://aws.amazon.com/new/?nc1=h_ls&whats-new-content-all.sort-by=item.additionalFields.postDateTime&whats-new-content-all.sort-order=desc&wn-featured-announcements.sort-by=item.additionalFields.numericSort&wn-featured-announcements.sort-order=asc")
# bsObject = BeautifulSoup(html, "html.parser")

req = requests.get("https://aws.amazon.com/new/?nc1=h_ls&whats-new-content-all.sort-by=item.additionalFields.postDateTime&whats-new-content-all.sort-order=desc&wn-featured-announcements.sort-by=item.additionalFields.numericSort&wn-featured-announcements.sort-order=asc")
html = req.text
soup = BeautifulSoup(html, 'html.parser')

##CSS Selector html factor find

# select1 = soup.select_one('#aws-page-content ul.aws-directories-container')
# print (select1)

find = soup.find(id='aws-page-content')
print ("find", find)

