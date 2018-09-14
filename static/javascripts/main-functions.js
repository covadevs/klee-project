if(document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', afterLoaded);
} else {
    afterLoaded();
}

function afterLoaded() {
    addItem('button_one', 'Income', null);
    addItem('button_two', 'Button 2', null);
    addItem('button_three', 'Button 3', null);
    addItem('button_four', 'Button 4', null);
    addItem('button_five', 'Button 5', null);
}

function addItem(idItem, text, icon_path){
    let sidebar = document.getElementById('sidebar');
    let link = document.createElement('a');

    let item = document.createElement('div');
    
    let id = document.createAttribute('id');
    id.value = idItem;
    
    let classes = document.createAttribute('class');
    classes.value = 'button-pointer content-sidebar';
    
    // let url = document.createAttribute("href");
    link.href = 'settings';
    

    // link.setAttributeNode(url);
    // link.appendChild(item);
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
    link.appendChild(name);
    item.appendChild(link);
    sidebar.appendChild(item);
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