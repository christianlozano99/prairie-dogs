from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/index.html")
def home():
    return render_template("index.html")

@app.route("/html/services.html")
def services():
    return render_template("/html/services.html")

@app.route("/html/about.html")
def about():
    return render_template("/html/about.html")

if __name__ == "__main__":
    app.run(debug = True,threaded=True)