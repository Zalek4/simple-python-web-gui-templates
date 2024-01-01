function getData() { 
    //var value = document.getElementById('div1').value; 
    $.ajax({
        url: '/request', 
        type: 'GET', 
        contentType: 'application/json', 
        //data: JSON.stringify({ 'value': value }), 
        success: function(response) {
            document.getElementById('div1').innerHTML = response['a'];
            console.log(JSON.stringify(response))
        }, 
        error: function(error) { 
            console.log(error); 
        }
    });
};