$(document).ready(function(){
    $('#search').on('click change keyup paste', function(e) {
        e.preventDefault();
        
        var query = $('#search').val()

        $.ajax({
            url : '/search/employee/',
            type : 'POST',
            data : {'query':query},

            success: function(response) {
                var result = ''

                if (response.result.length !== 0){
                    for (let i = 0; i < response.result.length; i++) {
                        result += `<tr>
                                        <td>${i+1}</td>
                                        <td>${response.result[i].First_Name}</td>
                                        <td>${response.result[i].Last_Name}</td>
                                        <td>${response.result[i].Email}</td>
                                        <td>${response.result[i].Mobile}</td>
                                        <td>
                                            <a href="/settings/${response.result[i].id}/">
                                                <i class="bx bx-cog bx-sm me-2 text-warning" data-bs-toggle="tooltip" data-bs-offset="0,4" data-bs-placement="bottom" data-bs-html="true" title="Settings"></i>
                                            </a>
                                            <a href="/employee/delete/${response.result[i].id}/">
                                                <i class="bx bx-trash bx-sm ms-2 text-danger" data-bs-toggle="tooltip" data-bs-offset="0,4" data-bs-placement="bottom" data-bs-html="true" title="Delete"></i>
                                            </a>
                                        </td>
                                    </tr>`;
                        $('#emp-table').html(result)
                    }
                }else{
                    result = 'No data found'
                }
            },

            error: function(xhr, status, error) {
                console.error('AJAX error:', error);
                alert('Failed to get response');
            },
        })
    })
})