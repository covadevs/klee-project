let csrftoken = Cookies.get('csrftoken');

function loadEditForm(url) {
    document.getElementById('modalProfile').style.display = 'block';
    $.ajax({
        url: url,
        type: 'GET',
        data: {
            csrfmiddlewaretoken: csrftoken,
        },
        timeout:0,
        success: function(data) {
            cleanElement('modalProfileContainer');
            $('#modalProfileContainer').append(data);
        }
    });
}

function loadChangePasswordForm(url) {
    document.getElementById('modalChangePassword').style.display = 'block';
    $.ajax({
        url: url,
        type: 'GET',
        data: {
            csrfmiddlewaretoken: csrftoken,
        },
        timeout: 0,
        success: function(data) {
            cleanElement('changePasswordContainer');
            $('#changePasswordContainer').append(data);
        }
    });
}

function loadIncomeForm(url) {
    document.getElementById('modalCreateIncome').style.display = 'block';
    $.ajax({
        url: url,
        type: 'GET',
        data: {
            csrfmiddlewaretoken: csrftoken,
        },
        timeout: 0,
        success: function(data) {
            cleanElement('createIncomeContainer');
            $('#createIncomeContainer').append(data);
        }
    })
}

function cleanElement(id) {
    let id_element = document.getElementById(id);
    while(id_element.firstChild) {
        id_element.removeChild(id_element.firstChild);
    }
}
