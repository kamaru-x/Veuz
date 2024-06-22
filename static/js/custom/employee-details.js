$(document).ready(function(){
    var employee_id = $('#employee-id').val()

    $('#firstName, #lastName, #email, #mobile').on('click change keyup paste', function(e) {
        e.preventDefault();

        var fname = $('#firstName').val()
        var lname = $('#lastName').val()
        var email = $('#email').val()
        var mobile = $('#mobile').val()

        $.ajax({
            url : '/employee/edit/',
            type : 'POST',
            data : {
                'eid':employee_id,'fname':fname,'lname':lname,'email':email,'mobile':mobile
            },

            success : function(response){
                
            }
        })
    });

    $('.employee-data').on('click change keyup paste', function(e) {
        e.preventDefault();

        var id = $(this).data('id')
        var data = $(this).val()

        $.ajax({
            url : '/employee/data/edit/',
            type : 'POST',
            data : {
                'id':id,'data':data
            },

            success : function(response){
                
            }
        })
    });

})