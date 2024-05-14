const content = document.getElementById("content");

$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        if ($('#sidebar').hasClass('active')) {
            content.style.width = "100%";
            content.style.marginLeft = "0";
            content.style.paddingLeft = "5%";
            content.style.paddingRight = "5%";
        } else {
            content.style.width = "";
            content.style.marginLeft = "";
        }
    });
});






  
