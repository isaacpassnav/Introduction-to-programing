from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/authenticate", methods = ["POST"])
def authenticate():
    user_id = request.form['user_id']
    password = request.form['password']
    return f"Wellcome,{user_id}!"
if __name__ == "__main__":
    app.run(debug = True)