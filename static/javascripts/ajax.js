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
            console.log(data)
            $("#value_detail").empty().append(fields.value + " "+ fields.value_currency);
            $("#desc_detail").empty().append(fields.description);
            $("#type_detail").empty().append(fields.consumption_opts);
            $("#paid_detail").empty().append(fields.paid ? 'Yes':'No');
            $("#cat_detail").empty().append(fields.category);
            $("#date_detail").empty().append(fields.date);
            document.getElementById("edit").setAttribute("onclick", "loadExchangeEditForm('"+data[1].link+"')")
            document.getElementById("form-edit-consumption").setAttribute("action", ""+data[1].link+"")
            document.getElementById("delete").setAttribute("onclick", "deleteExchange('"+data[2].link+"')")
        },
        error: function(error) {
            console.log(error);
        }
    });
} 

function tableRowClickCategory(url) {
    document.getElementById('modalDetailCategory').style.display = 'block';
    $.ajax({
        url: url,
        type: 'GET',
        data: {
            csrfmiddlewaretoken: csrftoken,
        },
        success: function(data) {
            console.log(data)
            fields = data[0].fields
            $("#name_detail").empty().append(fields.category_name);
            $("#acron_detail").empty().append(fields.category_acron);
            // $("#type_detail").empty().append(fields.consumption_opts);
            // $("#paid_detail").empty().append(fields.paid ? 'Yes':'No');
            // $("#cat_detail").empty().append(fields.category);
            // $("#date_detail").empty().append(fields.date);
            document.getElementById("edit-cat").setAttribute("onclick", "loadCategoryEditForm('"+data[1].link+"')")
            document.getElementById("form-edit-category").setAttribute("action", ""+data[1].link+"")
            document.getElementById("delete-cat").setAttribute("onclick", "deleteCategory('"+data[2].link+"')")

        },
        error: function(error) {
            console.log(error);
        }
    });
} 

function loadExchangeEditForm(url) {
    document.getElementById('modalEditConsumption').style.display = 'block';
    document.getElementById('modalDetailConsumption').style.display = 'none';
    $.ajax({
        url: url,
        type: 'GET',
        data: {
            csrfmiddlewaretoken: csrftoken,
        },
        timeout: 0,
        success: function(data) {
            console.log(data)
            cleanElement('editConsumptionContainer');
            $('#editConsumptionContainer').append(data);
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

function loadCategoryEditForm(url) {
    document.getElementById('modalEditCategory').style.display = 'block';
    document.getElementById('modalDetailCategory').style.display = 'none';
    $.ajax({
        url: url,
        type: 'GET',
        data: {
            csrfmiddlewaretoken: csrftoken,
        },
        timeout: 0,
        success: function(data) {
            console.log(data)
            cleanElement('editCategoryContainer');
            $('#editCategoryContainer').append(data);
            document.getElementById('id_category_name').focus();
        }
    })
}


function deleteExchange(url) {
    var conf = confirm("Deseja realmente deletar?")
    if(conf == true) {
        $.ajax({
            url: url,
            type: 'GET',
            data: {
                csrfmiddlewaretoken: csrftoken,
            },
            timeout: 0,
            success: function(data) {
                window.location.replace("/consumptions")
            }
        })
    }
}

function deleteCategory(url) {
    var conf = confirm("Deseja realmente deletar?")
    if(conf == true) {
        $.ajax({
            url: url,
            type: 'GET',
            data: {
                csrfmiddlewaretoken: csrftoken,
            },
            timeout: 0,
            success: function(data) {
                window.location.replace("/consumptions")
            }
        })
    }
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
    
