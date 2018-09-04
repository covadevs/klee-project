$(document).ready(function() {
    $('body').fadeIn('slow');

    $('.notification-container').fadeIn('slow', function() {
        setTimeout(function() {
            $('.success').fadeOut('slow');
        }, 1000);

        setTimeout(function() {
            $('.warning').fadeOut('slow');
        }, 1000);

        setTimeout(function() {
            $('.error').fadeOut('slow');
        }, 1000);

        setTimeout(function() {
            $('.info').fadeOut('slow');
        }, 1000);

        setTimeout(function() {
            $('.debug').fadeOut('slow');
        }, 1000);
    });

    $('.success').on('click',function(){
        $('.success').parent().attr('style', 'display:none;');
    });

    $('.warning').on('click',function(){
        $('.waning').parent().attr('style', 'display:none;');
    });

    $('.error').on('click',function(){
        $('.error').parent().attr('style', 'display:none;');
    });

    $('.info').on('click',function(){
        $('.info').parent().attr('style', 'display:none;');
    });

    $('.debug').on('click',function(){
        $('.debug').parent().attr('style', 'display:none;');
    });
});