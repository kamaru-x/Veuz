$(document).ready(function(){
    $('.delete-button').on('click', function(e){
        e.preventDefault();

        var id = $(this).data('id');
        var item = $(this);

        if (confirm("Are you sure you want to delete this item?")) {
            $.ajax({
                url: '/field/delete/',
                type: 'POST',
                data: { 'id': id },
                success: function(response){
                    item.closest('tr').remove();
                },
                error: function(xhr, status, error){
                    console.error('AJAX request failed:', status, error);
                }
            });
        }
    });

    $('.edit-button').on('click', function(e){
        e.preventDefault();

        var id = $(this).data('id');
        var itemName = $(this).closest('tr').find('.field-name');
        var itemType = $(this).closest('tr').find('.field-type');

        var nameValue = itemName.text().trim();
        itemName.html(`<input type="text" class="form-control" value="${nameValue}">`);

        var currentType = itemType.text().trim().toLowerCase();

        var selectOptions = `
            <option value="text" ${currentType === 'text' ? 'selected' : ''}>Text</option>
            <option value="number" ${currentType === 'number' ? 'selected' : ''}>Number</option>
            <option value="date" ${currentType === 'date' ? 'selected' : ''}>Date</option>
        `;

        itemType.html(`<select class="form-select">${selectOptions}</select>`);

        var saveButton = $('<button type="button" class="btn btn-primary save-button">Save</button>');
        $(this).closest('td').append(saveButton);

        saveButton.on('click', function() {
            var newName = itemName.find('input').val();
            var newType = itemType.find('select').val();

            $.ajax({
                url : '/field/edit/',
                type : 'POST',
                data : {'id':id,'name':newName,'type':newType},

                success : function(response){
                    itemName.html(newName);
                    itemType.html(newType.charAt(0).toUpperCase() + newType.slice(1));
                },
            });

            $(this).remove();
        });
    });
});