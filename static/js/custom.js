 (function ($) {

  "use strict";

    // COLOR MODE
    $(document).ready(function() {
      var darkModeEnabled = localStorage.getItem('darkModeEnabled');
      if (darkModeEnabled === 'true') {
        $('body').addClass('dark-mode');
        $('.color-mode-icon').addClass('active');
      } else {
        $('body').removeClass('dark-mode');
        $('.color-mode-icon').removeClass('active');
      }
    
      $('.color-mode').click(function() {
        $('.color-mode-icon').toggleClass('active');
        $('body').toggleClass('dark-mode');
        var darkModeEnabled = $('body').hasClass('dark-mode');
        localStorage.setItem('darkModeEnabled', darkModeEnabled);
      });
    });
    
    

    // HEADER
    $(".navbar").headroom();

    // PROJECT CAROUSEL
    $('.owl-carousel').owlCarousel({
    	items: 1,
	    loop:true,
	    margin:10,
	    nav:true
	});

    // SMOOTHSCROLL
    $(function() {
      $('.nav-link, .custom-btn-link').on('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top - 49
        }, 1000);
        event.preventDefault();
      });
    });  

    // TOOLTIP
    $('.social-links a').tooltip();

})(jQuery);


// var swiper = new Swiper('.blog-slider', {
//   spaceBetween: 30,
//   effect: 'fade',
//   loop: false,
//   mousewheel: {
//     invert: false,
//   },
//   // autoHeight: true,
//   pagination: {
//     slidesPerView: 3,
//     el: '.blog-slider__pagination',
//     clickable: true,
//   }
// });


