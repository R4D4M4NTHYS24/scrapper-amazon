from flask import Flask, jsonify
import scrapper

app = Flask(__name__)

@app.route('/amazon', methods=["GET"])
def amazon():
    scrapper_data = scrapper.get_data()

    if scrapper_data["status_code"] == 200:
        urls = scrapper_data["urls"]
        urls = [f"https://www.amazon.com{i.get('href')}" for i in urls[:5]]
        print(urls)
        return jsonify({"data": urls})

    return jsonify({"response": "failed!"})

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
