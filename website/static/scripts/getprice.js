$(document).ready(function() {
    $('#service-select').change(function() {
        var selectedService = $(this).val();
        $.ajax({
            url: '/price-estimate',  // Flask route to handle the request
            type: 'POST',
            data: {service: selectedService},
            success: function(response) {
                $('#price').text(response);  // Update the text of h1#price
            },
            error: function(xhr, status, error) {
                console.error('Error:', status, error);
            }
        });
    });
});