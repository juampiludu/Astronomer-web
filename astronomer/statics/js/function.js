$(document).ready(function () {

    $('.sidenav').sidenav();
    $('input#input_text').characterCounter();
    M.updateTextFields();

    $('#weight_button').click(function () {
        $('#text_mercury').html('it works!');
    });

});

$(document).on('click', 'ul li', function () {
    $(this).addClass('active').siblings().removeClass('active');
});