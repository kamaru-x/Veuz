$(document).ready(function(){
    $('#search').on('click change keyup paste', function(e) {
        e.preventDefault();
        
        var query = $('#search').val();

        $.ajax({
            url: '/search/employee/',
            type: 'POST',
            data: {'query': query},
            success: function(response) {
                var result = '';

                if (response.result.length !== 0) {
                    for (let i = 0; i < response.result.length; i++) {
                        result += `<tr>
                                        <td>${i+1}</td>
                                        <td>${response.result[i].First_Name}</td>
                                        <td>${response.result[i].Last_Name}</td>
                                        <td>${response.result[i].Email}</td>
                                        <td>${response.result[i].Mobile}</td>
                                        <td>
                                            <a href="/employee/details/${response.result[i].id}/">
                                                <i class="bx bx-cog bx-sm me-2 text-warning" data-bs-toggle="tooltip" data-bs-offset="0,4" data-bs-placement="bottom" data-bs-html="true" title="Settings"></i>
                                            </a>
                                            <i data-id="${response.result[i].id}" class="bx bx-trash bx-sm ms-2 text-danger delete-button" style="cursor: pointer;" data-id="${response.result[i].id}" data-bs-toggle="tooltip" data-bs-offset="0,4" data-bs-placement="bottom" data-bs-html="true" title="Delete"></i>
                                        </td>
                                    </tr>`;
                    }
                    $('#emp-table').html(result);
                } else {
                    $('#emp-table').html('<tr><td colspan="6">No data found</td></tr>');
                }
            },
            error: function(xhr, status, error) {
                console.error('AJAX error:', error);
                alert('Failed to get response');
            },
        });
    });

    $('#emp-table').on('click', '.delete-button', function(e) {
        e.preventDefault();

        var id = $(this).data('id');
        var item = $(this);

        if (confirm("Are you sure you want to delete this item?")) {

            item.closest('tr').remove();

            $.ajax({
                url: '/employee/delete/',
                type: 'POST',
                data: { 'id': id },
                success: function(response){
                    console.log(response.status)
                },
                error: function(xhr, status, error){
                    console.error('AJAX request failed:', status, error);
                }
            });
        }
    });
});