from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)

@app.route('/amazon', methods=["GET"])
def amazon():
    word = "play5"
    url = "https://www.amazon.com/s?k={}".format(word)
    headers = {"FUser": "An","user-agent": "an"}
    response = requests.get(url, headers=headers)
   
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        try:
            urls = soup.find('div', attrs={"class": "s-main-slot s-result-list s-search-results sg-row"}).find_all('a', attrs={"class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})
            urls = [f"https://www.amazon.com{i.get('href')}" for i in urls[:5]]
        except:
            urls = []    
      
        return jsonify({"data": urls})

    return jsonify({"response": "failed!"})

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
