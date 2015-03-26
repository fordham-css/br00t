$(document).ready(function(){

	//var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
	var socket = io.connect('http://localhost:5000');
	socket.on('my response', function(msg) {
		$('#log').append('<p>Received: ' + msg.data + '</p>');
	});
	$('form#emit').submit(function(event) {
		socket.emit('my event', {data: $('#emit_data').val()});
		return false;
	});
	$('form#broadcast').submit(function(event) {
		socket.emit('my broadcast event', {data: $('#broadcast_data').val()});
		return false;
	});
});