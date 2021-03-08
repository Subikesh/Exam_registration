// For displaying bootstrap toasts
$('.toast').toast('show');

// Checkbox toggle 
$('.subject-row').each(function(i) {
    $(this).on('click', function() {
        let checkBox = $(this).children('td:first').children('input');
        checkBox.attr("checked", !checkBox.attr("checked"));
    });
});