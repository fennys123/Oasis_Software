$(".hamburger").click(function() {
    var $wrapper = $(".wrapper");
    if ($wrapper.hasClass("collapsar")) {
      $wrapper.removeClass("collapsar");
    } else {
      $wrapper.addClass("collapsar");
    }
  });