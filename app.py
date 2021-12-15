from flask import Flask, render_template

app = Flask(__name__)

# print(__name__)


@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/product")
def product_page():
    return render_template("product.html")

if __name__== "__main__":
    app.run(debug=True)