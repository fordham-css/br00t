var user = 'devera@storm.cis.fordham.edu'
var pass = 'troisetudes'

$.ajax({
    url: $(this).attr('action'),
    type: 'POST',
    data: $(this).serialize(),
    username: user, 
    password: pass,
    success: function(data){
    //var data = JSON.parse(jsondata);
      console.log(data);
    },
});