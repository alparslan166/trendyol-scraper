from flask import Flask, render_template, request
import os  # os modülünü ekleyin
from trendify import scrape_trendyol

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    query = ""
    if request.method == "POST":
        query = request.form.get("query")
        results = scrape_trendyol(query)
    return render_template("index.html", results=results, query=query)

if __name__ == "__main__":
    # Render'dan gelen PORT çevre değişkenine göre portu belirleyin
    port = int(os.environ.get("PORT", 5000))  # Eğer PORT çevre değişkeni yoksa, 5000 portunu kullan
    app.run(debug=True, host="0.0.0.0", port=port)  # Flask'ı dışa açık portta çalıştırın


"""
from flask import Flask, render_template, request
from trendify import scrape_trendyol

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        keyword = request.form.get("keyword")
        if keyword:
            results = scrape_trendyol(keyword)
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
"""