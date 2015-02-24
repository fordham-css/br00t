import os
from flask import Flask, render_template, flash

from flask import session, url_for, request, redirect, flash


app = Flask(__name__)
app.config["DEBUG"] = True
app.secret_key = "dev key"


# Controllers
@app.errorhandler(404)
def page_not_found(error):
    return "Page not found", 404

@app.route("/")
def hello():
    return render_template("index.html")



#launch info
if __name__ == "__main__":
    app.run(host="0.0.0.0")
