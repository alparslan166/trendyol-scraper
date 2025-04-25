from flask import Flask, render_template, request
import os  # os modülünü ekleyin
from trendify import scrape_trendyol
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form["query"]
        results = scrape_trendyol(query)
        return render_template("results.html", results=results)
    return render_template("index.html")


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