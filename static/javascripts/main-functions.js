if(document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', afterLoaded);
} else {
    afterLoaded();
}

function afterLoaded() {
    addItem('button_one', 'Settings', '/static/images/settings.svg');
    addItem('button_two', 'Button 2', null);
    addItem('button_three', 'Button 3', null);
    addItem('button_four', 'Button 4', null);
}

function addItem(idItem, text, icon_path){
    let sidebar = document.getElementById('sidebar');
    let item = document.createElement('div');
    
    let id = document.createAttribute('id');
    id.value = idItem;
    
    let classes = document.createAttribute('class');
    classes.value = 'button-pointer content-sidebar';
    
    item.setAttributeNode(id);
    item.setAttributeNode(classes);
    
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
    item.appendChild(name);

    sidebar.appendChild(item);
}

$(document).ready(function() {
    let pic_options = document.getElementById('pic-options');

    $('#pic-profile').on('mouseover', function() {
        $('#pic-options').fadeIn('fast');
        pic_options.style.display = 'grid';
    });

    $('#pic-profile').on('mouseleave',function() {
        $('#pic-options').fadeOut('fast');
    });

    $('#pic-options').on('mouseover', function() {
        $(this).stop(true, true).fadeOut();
    });
});