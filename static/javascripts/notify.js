let notifyDuration = 4500;

$(document).ready(function() {
    $('body').fadeIn('slow');

    $('#notification-container').fadeIn('slow', function() {
        setTimeout(function() {
            $('.success').fadeOut('slow');
        }, notifyDuration);

        setTimeout(function() {
            $('.warning').fadeOut('slow');
        }, notifyDuration);

        setTimeout(function() {
            $('.error').fadeOut('slow');
        }, notifyDuration);

        setTimeout(function() {
            $('.info').fadeOut('slow');
        }, notifyDuration);

        setTimeout(function() {
            $('.debug').fadeOut('slow');
        }, notifyDuration);
    });
});

function closeNotification() {
    $('.notification-box').fadeOut('fast');
}