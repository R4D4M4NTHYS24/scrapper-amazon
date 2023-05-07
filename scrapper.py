import requests
from bs4 import BeautifulSoup

def get_data():
    word = "play5"
    url = "https://www.amazon.com/s?k={}".format(word)
    headers = {"FUser": "An","user-agent": "an"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    urls = soup.find('div', attrs={"class": "s-main-slot s-result-list s-search-results sg-row"}).find_all('a', attrs={"class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})

    return {"status_code": response.status_code, "urls": urls}
