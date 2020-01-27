import requests
import re
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}

URL = "https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR11.TRC1.A0.H0.Xcambridge+audio+a5.TRS0&_nkw=cambridge+audio+a5&_sacat=0"

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

arr = list(range(11))[1:11]

url_array = []

for val in arr:
    item = soup.find(id="srp-river-results-listing"+str(val))
    x = item.a
    url_array.append(x.get('href'))

for x, url in enumerate(url_array):
    print(x+1)
    print(url)

# for link in soup.find_all('a'):
#     if "https://www.ebay.co.uk/itm/" in link.get('href'):
#         url_array.append(link.get('href'))

# # tags = soup.find(id='srp-river-results-listing2',
# #  href=re.compile(r'[/]([a-z]|[A-Z])\w+')).attrs['href']
# for i, x in enumerate(url_array):
#     print(i+1)
