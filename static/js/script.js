// For displaying bootstrap toasts
$('.toast').toast('show');

// Toggle collapse for bootstrap accordion
$('.accordion-card').each(function(i) {
    $(this).click( function() {
        // $(this).collapse('toggle');
    });
});