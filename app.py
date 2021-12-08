from flask import Flask, render_template

app = Flask(__name__)

# print(__name__)


@app.route("/")
def index_page():
    return render_template("index.html")

app.run()