/*$(document).ready(function(){
	namespace = '/br00t'; // change to an empty string to use the global namespace

            // the socket.io documentation recommends sending an explicit package upon connection
            // this is specially important when using the global namespace
            var socket = io.connect('http://' + document.domain + ':' + location.port + namespace);
           // var socket = io.connect('http://localhost:5000/test');
            socket.on('connect', function() {
                console.log('Connection established.')
                //socket.emit('my event', {data: 'I\'m connected!'});
            });
            
            // event handler for server sent data
            // the data is displayed in the "Received" section of the page
            socket.on('my response', function(msg) {
                $('#log').append('<br>Received #' + msg.count + ': ' + msg.data);
            });

            // handlers for the different forms in the page
            // these send data to the server in a variety of ways
            
});*/


$(document).ready(function(){



    namespace = '/br00t'; // change to an empty string to use the global namespace

    // the socket.io documentation recommends sending an explicit package upon connection
    // this is specially important when using the global namespace
    var socket = io.connect('http://' + document.domain + ':' + location.port + namespace);
    socket.on('connect', function() {
        socket.emit('my event', {data: '\nCLIENT: connection established'});
    });
            
    // event handler for server sent data
    // the data is displayed in the "Received" section of the page
    socket.on('my response', function(msg) {
        $('#monitoring-panel').append(msg.data);
    });

    // handlers for the different forms in the page
    // these send data to the server in a variety of ways
    $('#emit').submit(function(event) {
        socket.emit('my event', {data: $('#emit_data').val()});
        return false;
    });

    


});

var show = function(){
    $(document).getElementById("monitoring-panel").show();
}

var hide = function() {
    $(document).getElementById("monitoring-panel").hide();
}