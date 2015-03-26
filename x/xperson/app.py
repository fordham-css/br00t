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

# Session
"""
The MIT License (MIT)

Copyright (c) 2013 Dave P.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import signal, sys, ssl, logging
from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer, SimpleSSLWebSocketServer
from optparse import OptionParser

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)

class SimpleChat(WebSocket):

	def handleMessage(self):
		if self.data is None:
			self.data = ''
		
		for client in self.server.connections.itervalues():
			if client != self:
				try:
					client.sendMessage(str(self.address[0]) + ' - ' + str(self.data))
				except Exception as n:
					print n


	def handleConnected(self):
		print self.address, 'connected'
		for client in self.server.connections.itervalues():
			if client != self:
				try:
					client.sendMessage(str(self.address[0]) + ' - connected')
				except Exception as n:
					print n

	def handleClose(self):
		print self.address, 'closed'
		for client in self.server.connections.itervalues():
			if client != self:
				try:
					client.sendMessage(str(self.address[0]) + ' - disconnected')
				except Exception as n:
					print n


	
host='localhost'
port=5000 
server = SimpleSSLWebSocketServer(host, port, SimpleChat)

def close_sig_handler(signal, frame):
	server.close()
	sys.exit()

signal.signal(signal.SIGINT, close_sig_handler)

#server.serveforever()


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
