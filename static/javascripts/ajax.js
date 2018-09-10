let csrftoken = Cookies.get('csrftoken');

function loadEditForm(url) {
    document.getElementById('id01').style.display = 'block';
    $.ajax({
        url: url,
        type: 'GET',
        data: {
            csrfmiddlewaretoken: csrftoken,
        },
        timeout:0,
        success: function(data) {
            let id_username = $('#id_username').length;
            let id_email = $('#id_email').length;
            if ((id_username == 0 || id_email == 0)) {
                $('#id02').append(data);
            }
        }
    });
}