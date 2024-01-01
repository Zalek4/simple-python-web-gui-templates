// Sends a 'GET' request to the specified URL
function getData() { 
    $.ajax({
        url: '/get', 
        type: 'GET', 
        contentType: 'application/json', 
        success: function(response) {
            document.getElementById('div1').innerHTML = response['a'];
            console.log(response)
        }, 
        error: function(error) { 
            console.log(error); 
        }
    });
};

// Sends a 'POST' request to the specified URL
function postData() {
    let value = 10
    $.ajax({
        url: '/post', 
        type: 'POST', 
        contentType: 'application/json', 
        data: JSON.stringify({ 'value' : value }), 
        success: function(response) {
            document.getElementById('div2').innerHTML = response['value'];
            console.log(response)
        }, 
        error: function(error) { 
            console.log(error); 
        }
    });
};