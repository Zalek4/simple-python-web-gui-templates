function sendData() { 
    var value = document.getElementById('input').value; 
    $.ajax({ 
        url: '/process', 
        type: 'POST', 
        contentType: 'application/json', 
        data: JSON.stringify({ 'value': value }), 
        success: function(response) { 
            document.getElementById('output_a').innerHTML = response.result_a;
            document.getElementById('output_b').innerHTML = response.result_b;
            document.getElementById('output_c').innerHTML = response.returned;
        }, 
        error: function(error) { 
            console.log(error); 
        } 
    }); 
};