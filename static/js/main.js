/*  ---------------------------------------------------
    Template Name: Dreams
    Description: Dreams wedding template
    Author: Colorib
    Author URI: https://colorlib.com/
    Version: 1.0
    Created: Colorib
---------------------------------------------------------  */

'use strict';

(function ($) {

    /*------------------
        Preloader
    --------------------*/
    $(window).on('load', function () {
        $(".loader").fadeOut();
        $("#preloader").delay(200).fadeOut("slow");

        /*------------------
            Portfolio filter
        --------------------*/
        $('.portfolio__filter li').on('click', function () {
            $('.portfolio__filter li').removeClass('active');
            $(this).addClass('active');
        });
        if ($('.portfolio__gallery').length > 0) {
            var containerEl = document.querySelector('.portfolio__gallery');
            var mixer = mixitup(containerEl);
        }
    });

    /*------------------
        Background Set
    --------------------*/
    $('.set-bg').each(function () {
        var bg = $(this).data('setbg');
        $(this).css('background-image', 'url(' + bg + ')');
    });

    //Masonary
    $('.work__gallery').masonry({
        itemSelector: '.work__item',
        columnWidth: '.grid-sizer',
        gutter: 10
    });

    /*------------------
		Navigation
	--------------------*/
    $(".mobile-menu").slicknav({
        prependTo: '#mobile-menu-wrap',
        allowParentLinks: true
    });

    /*------------------
		Hero Slider
	--------------------*/
    $('.hero__slider').owlCarousel({
        loop: true,
        dots: true,
        mouseDrag: false,
        animateOut: 'fadeOut',
        animateIn: 'fadeIn',
        items: 1,
        margin: 0,
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: true,
    });

    var dot = $('.hero__slider .owl-dot');
    dot.each(function () {
        var index = $(this).index() + 1;
        if (index < 10) {
            $(this).html('0').append(index);
        } else {
            $(this).html(index);
        }
    });

    /*------------------
        Testimonial Slider
    --------------------*/
    $(".testimonial__slider").owlCarousel({
        loop: true,
        margin: 0,
        items: 3,
        dots: true,
        dotsEach: 2,
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: true,
        responsive: {
            992: {
                items: 3
            },
            768: {
                items: 2
            },
            320: {
                items: 1
            }
        }
    });

    /*------------------
        Latest Slider
    --------------------*/
    $(".latest__slider").owlCarousel({
        loop: true,
        margin: 0,
        items: 3,
        dots: true,
        dotsEach: 2,
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: true,
        responsive: {
            992: {
                items: 3
            },
            768: {
                items: 2
            },
            320: {
                items: 1
            }
        }
    });

    /*------------------
        Logo Slider
    --------------------*/
    $(".logo__carousel").owlCarousel({
        loop: true,
        margin: 100,
        items: 6,
        dots: false,
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: true,
        responsive: {
            992: {
                items: 5
            },
            768: {
                items: 4
            },
            480: {
                items: 3
            },
            320: {
                items: 2
            }
        }
    });

    /*------------------
        Video Popup
    --------------------*/
    $('.video-popup').magnificPopup({
        type: 'iframe'
    });

    /*------------------
        Counter
    --------------------*/
    $('.counter_num').each(function () {
        $(this).prop('Counter', 0).animate({
            Counter: $(this).text()
        }, {
            duration: 4000,
            easing: 'swing',
            step: function (now) {
                $(this).text(Math.ceil(now));
            }
        });
    });


    /*---------------
    Animated Header & Background
    -----------------*/
//     new FinisherHeader({
//   "count": 4,
//   "size": {
//     "min": 1200,
//     "max": 1500,
//     "pulse": 0.1
//   },
//   "speed": {
//     "x": {
//       "min": 0,
//       "max": 0.2
//     },
//     "y": {
//       "min": 0,
//       "max": 0.2
//     }
//   },
//   "colors": {
//     "background": "#040c1c",
//     "particles": [
//       "#d1002c",
//       "#04102c",
//       "#00bfe7",
//       "#d1002c",
//       "#00bfe7"
//     ]
//   },
//   "blending": "overlay",
//   "opacity": {
//     "center": 0.8,
//     "edge": 0.2
//   },
//   "skew": 0,
//   "shapes": [
//     "c",
//     "t"
//   ]
// });
// new FinisherHeader2({
//   "count": 12,
//   "size": {
//     "min": 1300,
//     "max": 1500,
//     "pulse": 0
//   },
//   "speed": {
//     "x": {
//       "min": 0.6,
//       "max": 3
//     },
//     "y": {
//       "min": 0.6,
//       "max": 3
//     }
//   },
//   "colors": {
//     "background": "#060607",
//     "particles": [
//       "#040c1c",
//       "#040d22",
//       "#051d4d",
//       "#051641"
//     ]
//   },
//   "blending": "none",
//   "opacity": {
//     "center": 0.6,
//     "edge": 0
//   },
//   "skew": 0,
//   "shapes": [
//     "c"
//   ]
// });

// new FinisherHeader({
//   "count": 10,
//   "size": {
//     "min": 1300,
//     "max": 1500,
//     "pulse": 0.3
//   },
//   "speed": {
//     "x": {
//       "min": 0.1,
//       "max": 0.6
//     },
//     "y": {
//       "min": 0.1,
//       "max": 0.6
//     }
//   },
//   "colors": {
//     "background": "#040c1c",
//     "particles": [
//       "#d1002c",
//       "#04102c",
//       "#00bfe7",
//       "#d1002c",
//       "#00bfe7"
//     ]
//   },
//   "blending": "overlay",
//   "opacity": {
//     "center": 0.5,
//     "edge": 0.05
//   },
//   "skew": 0,
//   "shapes": [
//     "c"
//   ]
// });


})(jQuery);