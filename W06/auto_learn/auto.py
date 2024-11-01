from flask import flask

app = flask(name)


@app.route("/")
def home():
    return "Hello world"


if __name__ == "main":
    app.run()
