from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)

@app.route('/amazon', methods=["GET", "POST"])
def amazon():
    if request.method == "POST":
        # Aquí puedes manejar la lógica para procesar los datos enviados en la solicitud POST
        # ...
        return jsonify({"response": "Datos procesados correctamente"}), 200

    # Si la solicitud es GET, obtienes los datos de la URL
    word = "play5"
    url = "https://www.amazon.com/s?k={}".format(word)
    headers = {"FUser": "An", "user-agent": "an"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        try:
            urls = soup.find('div', attrs={"class": "s-main-slot s-result-list s-search-results sg-row"}).find_all('a', attrs={"class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})
            urls = [f"https://www.amazon.com{i.get('href')}" for i in urls[:5]]
        except:
            urls = []

        response_data = {"data": urls}
        return jsonify(response_data), 200

    return jsonify({"response": "failed!"}), 500

# Configura las cabeceras CORS
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
