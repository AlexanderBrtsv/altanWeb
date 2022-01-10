from flask import Flask, render_template, request
from pwdgenerator import hashing

app = Flask(__name__)

# print(__name__)


@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/product", methods=["GET", "POST"])
def product_page():
    msg = None
    # name = ""
    # pwd = ""
    if request.method == "POST":
        salt = request.form.get("salt")
        pwd = request.form.get("pwd")
        num_char = request.form.get("num_char")

        # msg = f"{name}, {pwd}"
        if (salt != None) and (pwd != None):
            msg = hashing(pwd, salt, num_char)

    return render_template(
        "product.html", 
        msg = msg,
        # name = name,
        # password = pwd
    )

# http://127.0.0.1:5000/test?v1=Hello&v2=Hi
@app.route("/test")
def test_page():
    var_1 = request.args.get("v1")
    var_2 = request.args.get("v2")
    return f"""
    <h1>Test</h1>
    <p> Var 1: {var_1} </p>
    <p> Var 2: {var_2} </p>
    """

if __name__== "__main__":
    app.run(debug=True)