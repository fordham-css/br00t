import os, threading, time
from flask import Flask, render_template, flash
from flask import session, url_for, request, redirect


app = Flask(__name__)
app.config["DEBUG"] = True
app.secret_key = "dev key"

# Threading
"""
def worker():
	 print threading.currentThread().getName(), 'Starting'
	 time.sleep(2)
	 print threading.currentThread().getName(), 'Exiting'

def my_service():
	 print threading.currentThread().getName(), 'Starting'
	 time.sleep(3)
	 print threading.currentThread().getName(), 'Exiting'

t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker) # use default name

w.start()
w2.start()
t.start()
"""

# Controllers
@app.errorhandler(404)
def page_not_found(error):
	 return "Page not found", 404

@app.route("/")
def index():
	return render_template("index.html")
	return result



#launch info
if __name__ == "__main__":
	 app.run(host="0.0.0.0")
