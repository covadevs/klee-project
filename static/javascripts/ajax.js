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
            document.getElementById('id_username').focus();
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
            document.getElementById('id_password').focus();
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
            document.getElementById('id_value_0').focus();
        }
    })
}

function loadConsumptionForm(url) {
    document.getElementById('modalCreateConsumption').style.display = 'block';
    $.ajax({
        url: url,
        type: 'GET',
        data: {
            csrfmiddlewaretoken: csrftoken,
        },
        timeout: 0,
        success: function(data) {
            console.log(data)
            cleanElement('createConsumptionContainer');
            $('#createConsumptionContainer').append(data);
            document.getElementById('id_value_0').focus();
            $(function() {
                $("#id_date").datepicker({
                    changeMonth: true,
                    changeYear: true,
                    dateFormat: 'yy-mm-dd',
                });
            });
        }
    })
}

$(function() {
    $("#id_date").datepicker();
})

function cleanElement(id) {
    let id_element = document.getElementById(id);
    while(id_element.firstChild) {
        id_element.removeChild(id_element.firstChild);
    }
}

function cleanFilter(id) {
    let form = document.forms[id];
    form['id_value'].value = "";
    form['id_consumption_opts'].value = "";
    form['id_paid'].value = 1;
    form['id_date_0'].value = "";
    form['id_date_1'].value = "";
    form['id_category_opts'].value = "";
    form['id_description'].value = "";
    form.submit();
}

function tableRowClick(url) {
    document.getElementById('modalDetailConsumption').style.display = 'block';
    $.ajax({
        url: url,
        type: 'GET',
        data: {
            csrfmiddlewaretoken: csrftoken,
        },
        success: function(data) {
            fields = data[0].fields
            $("#value_detail").empty().append(fields.value + " "+ fields.value_currency);
            $("#desc_detail").empty().append(fields.description);
            $("#type_detail").empty().append(fields.consumption_opts);
            $("#paid_detail").empty().append(fields.paid ? 'Yes':'No');
            $("#cat_detail").empty().append(fields.category);
            $("#date_detail").empty().append(fields.date);
        },
        error: function(error) {
            console.log(error);
        }
    });
} 

function loadCategoryForm(url) {
    document.getElementById('modalCreateCategory').style.display = 'block';
    $.ajax({
        url: url,
        type: 'GET',
        data: {
            csrfmiddlewaretoken: csrftoken,
        },
        success: function(data) {
            cleanElement('createCategoryContainer');
            $('#createCategoryContainer').append(data);
            document.getElementById('id_category_name').focus();
        },
        error: function(error) {
            console.log(error);
        }
    });
}
    
