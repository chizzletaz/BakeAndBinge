$(document).ready(function () {
    $(".dropdown-trigger").dropdown({ 
        hover: true, 
        constrainWidth: false,
        coverTrigger: false,
        });
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('select').formSelect();
});