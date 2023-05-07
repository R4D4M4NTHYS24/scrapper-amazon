from flask import Flask, jsonify
import scrapper

app = Flask(__name__)

@app.route('/amazon',methods=["GET"])
def amazon():
    scrapper

    if scrapper.response.status_code == 200:
        soup = scrapper.soup
        urls = scrapper.urls        
        urls = [ "https://www.amazon.com"+i.get('href') for i in urls[:5] ]
        print(urls)
        return jsonify({"data":urls})

    return jsonify ({"response:failed!"})

if __name__ == "__main__":
    app.run(debug=True,port=5000,host="0.0.0.0")

