
// $('.nav li a').click(function(e) {
//   var $this = $(this);
//   if (!$this.hasClass('active')) {
//     $this.addClass('active');
//   }
//   //e.preventDefault();
// });


$(function () {
    setNavigation();
});

function setNavigation() {
    var path = window.location.pathname;
    path = path.replace(/\//g,"");
    path = decodeURIComponent(path);
    if (path == "")
      path = "home";

    $(".nav a").each(function () {
        var href = $(this).attr('href').replace(/\//g,"");
        if (href == "")
          href = "home";
        //alert(path.substring(0, href.length) + "  " + href);          
        if (path.substring(0, href.length) === href) {
            $(this).closest('li').addClass('active');
        }
        else{
          $(this).closest('li').removeClass('active');
        }
    });
}