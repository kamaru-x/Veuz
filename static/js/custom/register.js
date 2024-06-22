$(document).ready(function(){
    $('#register-button').on('click' , function(e){
        e.preventDefault();

        var name = $('#name').val()
        var email = $('#email').val()
        var password = $('#password').val()
        var cpassword = $('#cpassword').val()
        
        $.ajax({
            'url' : '/register/',
            'type' : 'POST',
            'data' : {
                'name':name,'email':email,'password':password,'cpassword':cpassword
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