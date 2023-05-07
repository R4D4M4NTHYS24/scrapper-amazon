import requests
from bs4 import BeautifulSoup

word = "play5"
url = "https://www.amazon.com/s?k={}".format(word)
headers = {"FUser": "An","user-agent": "an"} #Importante pues las webs a las que se les practica web scrapping suelen validar si la peticion es realizada por un usuario o un software retornandole a este ultimo una respuesta de 503
response = requests.get(url,headers=headers)
#print(response.status_code)
soup = BeautifulSoup(response.content, 'html.parser')

#a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal
urls = soup.find('div', attrs={"class":"s-main-slot s-result-list s-search-results sg-row"}).find_all('a',attrs={"class":"a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})
#print("https://www.amazon.com"+urls[0].get('href'))
