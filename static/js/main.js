'use strict';
console.log("Script Loaded");

(function ($) {

    /*------------------
        Preloader
    --------------------*/
    $(window).on('load', function () {
        $(".loader").fadeOut();
        $("#preloader").delay(200).fadeOut("slow");
    });

    /*------------------
        Portfolio filter
    --------------------*/
    $('.portfolio__filter li').on('click', function () {
        console.log("Portfolio Filter Clicked");
        $('.portfolio__filter li').removeClass('active');
        $(this).addClass('active');
    if ($('.portfolio__gallery').length > 0) {
        var containerEl = document.querySelector('.portfolio__gallery');
        console.log("Container Element:", containerEl);
        var mixer = mixitup(containerEl);
    }
    });

    /*------------------
        Background Set
    --------------------*/
    $('.set-bg').each(function () {
        var bg = $(this).data('setbg');
        console.log("Background Set: ", bg);
        $(this).css('background-image', 'url(' + bg + ')');
    });

    //Masonary
    // $('.work__gallery').masonry({
    //     itemSelector: '.work__item',
    //     columnWidth: '.grid-sizer',
    //     gutter: 10
    // });

    /*------------------
		Navigation
	--------------------*/
    $(".mobile-menu").slicknav({
        prependTo: '#mobile-menu-wrap',
        allowParentLinks: true
    });

    /*------------------
        Finisher-Header
    --------------------*/
    document.addEventListener("DOMContentLoaded", function() {
        const config1 = {
            className: "finisher-header",
            "count": 4,
            "size": {
                "min": 1200,
                "max": 1500,
                "pulse": 0.1
            },
            "speed": {
                "x": {
                    "min": 0,
                    "max": 0.2
                },
                "y": {
                    "min": 0,
                    "max": 0.2
                }
            },
            "colors": {
                "background": "#040c1c",
                "particles": [
                    "#d1002c",
                    "#04102c",
                    "#00bfe7",
                    "#d1002c",
                    "#00bfe7"
                ]
            },
            "blending": "overlay",
            "opacity": {
                "center": 0.8,
                "edge": 0.2
            },
            "skew": 0,
            "shapes": [
                "c",
                "t"
            ]
        };
        
        new FinisherHeader(config1);
    });
   

    /*------------------
        Project Slider
    --------------------*/
    $(".work__slider").owlCarousel({
        loop: true,
        margin: 0,
        items: 1,
        dots: true,
        dotsEach: 1,
        smartSpeed: 1500,
        autoHeight: true,
        autoplay: true,
        responsive: {
            992: {
                items: 1
            },
            768: {
                items: 1
            },
            320: {
                items: 1
            }
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
        Latest Blog Slider
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
    // $('.video-popup').magnificPopup({
    //     type: 'iframe'
    // });

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



})(jQuery);