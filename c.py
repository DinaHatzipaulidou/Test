# --------------------------------
# NOTE: exp1
# --------------------------------
from flask import flask

app = flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"
    pass
