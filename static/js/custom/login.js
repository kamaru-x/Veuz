$(document).ready(function(){
    $('#login-button').on('click' , function(e){
        e.preventDefault();

        var email = $('#email').val()
        var password = $('#password').val()
        
        $.ajax({
            'url' : '/sign-in/',
            'type' : 'POST',
            'data' : {
                'email':email,'password':password
            },

            success : function(response){
                if (response.status === 'error') {
                    $('#error-msg').text(response.message);
                } else {
                    window.location.href = '/';
                }
            },

            error: function(xhr, status, error){
                console.error('AJAX request failed:', status, error);
                $('#error-msg').text('Failed to register. Please try again later.');
            }
        })
    })
})