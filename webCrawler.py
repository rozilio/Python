'''
create a web crawler
not working completely
'''

import requests
from bs4 import BeautifulSoup


def spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.agora.co.il/toGet.asp?searchType=subCategory&dealType=1&iseek=10030&page=' + str(page)
        sourve_code = requests.get(url)
        plain_text = sourve_code.text
        soup = BeautifulSoup(plain_text, 'lxml')
        for link in soup.findAll('tr', {'class': 'objectsTitleTr'}):
            href = link.click
            print(href)
        page = page + 1

def get_single_item(item_url):
    sourve_code = requests.get(item_url)
    plain_text = sourve_code.text
    soup = BeautifulSoup(plain_text, 'lxml')
    for item_name in soup.findAll():
        print()

spider(1)
