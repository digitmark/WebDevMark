document.getElementById('ctheme').onclick = function (){

    var theme = document.getElementById('theme_css');
    // alert(theme);
    
    if (theme.href.match('css/style.css')){
        document.getElementById('theme_css').href='css/style2.css';
    } else{
        document.getElementById('theme_css').href='css/style.css';
}
    // = 'css/style2.css'

};