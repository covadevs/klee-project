if(document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', afterLoaded);
} else {
    afterLoaded();
}

function afterLoaded() {
    addItem('button_one', 'Income', null, 'incomes');
    addItem('button_two', 'Expense', null, 'consumptions');
    addItem('button_three', 'Charts', null, 'charts');
    addItem('button_four', 'Category', null, 'categories');
}

function addItem(idItem, text, icon_path, href) {
    let sidebar = document.getElementById('sidebar');
    let link = document.createElement('a');

    let item = document.createElement('div');

    let id = document.createAttribute('id');
    id.value = idItem;
    
    let classes = document.createAttribute('class');
    classes.value = 'button-pointer content-sidebar';
    
    link.href = href;

    link.setAttributeNode(id);
    link.setAttributeNode(classes);
    
    if(icon_path !== null) {
        let img = document.createElement('img');
        let src = document.createAttribute('src');
        let img_class = document.createAttribute('class');

        src.value = icon_path;
        img_class.value = 'button-icon';
        img.setAttributeNode(src);
        img.setAttributeNode(img_class);

        item.appendChild(img);
    }

    let name = document.createTextNode(text);
    link.appendChild(name);
    link.appendChild(item);
    sidebar.appendChild(link);
}

$(document).ready(function() {
    let pic_options_container = document.getElementById('pic-options-container');
        $('#pic-profile').on('click', function() {
            if ($('#pic-options-container').css('display') === 'none') {
                console.log('entrou');
                $('#pic-options-container').fadeIn('fast');
                pic_options_container.style.display = 'grid';
            } else if ($('#pic-options-container').css('display') === 'grid') {
                $('#pic-options-container').fadeOut('fast');
            }
        });
});