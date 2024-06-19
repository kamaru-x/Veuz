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

    $('#adb').on('click', function(e) {
        e.preventDefault();

        $('#add-div').append(
            `<div class="row">
                <div class="col-md-5 mb-3">
                    <input class="form-control field-title" type="text" placeholder="Enter Field Title" required/>
                </div>
                <div class="col-md-5 mb-3">
                    <input class="form-control field-data" type="text" placeholder="Enter Field Data" required/>
                </div>
                <div class="col-md-2 mb-3">
                    <button class="btn btn-success ecb" type="button"> Confirm Entry</button>
                </div>
            </div>`
        );
    });

    $('#add-div').on('click', '.ecb', function() {
        var row = $(this).closest('.row');
        var titleValue = row.find('.field-title').val();
        var dataValue = row.find('.field-data').val();

        if (titleValue !== '' && dataValue !== '') {
            $.ajax({
                url: '/employee/data/add/',
                type: 'POST',
                data: {
                    'eid': employee_id,
                    'title': titleValue,
                    'data': dataValue
                },

                success: function(response) {
                    $('#data-div').append(
                        `<div class="mb-3 col-md-6">
                            <label for="" class="form-label">${titleValue}</label>
                            <div class="input-group">
                                <input class="form-control" type="text" value="${dataValue}" />
                                <span id="${response.data_id}" class="input-group-text cursor-pointer data-delete">
                                    <a href="/employee/data/delete/${response.data_id}/">
                                        <i class="bx bx-trash text-danger"></i>
                                    </a>
                                </span>
                            </div>
                        </div>`
                    );
        
                    row.remove();
                },

                error: function(xhr, status, error) {
                    console.error('AJAX error:', error);
                    alert('Failed to add data');
                }
            });
        } else {
            alert('Please enter both title and data');
        }
    });

    $('.ad-data').on('click change keyup paste' , function(){
        var data_id = $(this).data('id')
        var data = $(this).val()
        
        $.ajax({
            url : '/employee/data/edit/',
            type : 'POST',
            data : {
                'data_id':data_id,'data':data
            },

            success : function(response){
                
            },

            error: function(xhr, status, error) {
                console.error('AJAX error:', error);
                alert('Failed to add data');
            }
        })
    })

})