from registro_ig import app
from flask import Flask , render_template

@app.route("/")
def index():
    return "Server running"

        