#!/usr/bin/env python

import asyncio
import websockets

host = 'localhost'
port = 5000

@asyncio.coroutine
def hello(websocket, path):
    name = yield from websocket.recv()
    print("< {}".format(name))
    greeting = "Hello {}!".format(name)
    yield from websocket.send(greeting)
    print("> {}".format(greeting))

start_server = websockets.serve(hello, host, port)
print 'server running at ' + host + ':' + port
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()