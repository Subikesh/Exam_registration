// For displaying bootstrap toasts
$('.toast').toast('show');

// Toggle collapse for bootstrap accordion
$('.accordion-card').each(function(i) {
    $(this).click( function() {
        // $(this).collapse('toggle');
    });
});

// Checkbox toggle 
$('.subject-row').each(function(i) {
    $(this).on('click', function() {
        let checkBox = $(this).children('td:first').children('input');
        checkBox.attr("checked", !checkBox.attr("checked"));
    });
});