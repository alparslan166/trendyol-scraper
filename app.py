from flask import Flask, render_template, request
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
    app.run(debug=True)

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