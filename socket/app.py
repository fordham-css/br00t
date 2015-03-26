import os
from flask import Flask, render_template, flash
from flask import session, url_for, request, redirect
from flask.ext.socketio import SocketIO, emit

app = Flask(__name__)
app.config['DEBUG'] = True
socketio = SocketIO(app)

# Controllers
@app.errorhandler(404)
def page_not_found(error):
	 return 'Page not found', 404

@app.route('/')
def index():
	return render_template('index.html')
	return result

@socketio.on('my event')
def test_message(message):
    emit('my response', {'data': 'got it!'})




#launch info
if __name__ == '__main__':
    socketio.run(app)

'''
if __name__ == '__main__':
	 app.run(host='0.0.0.0')
'''