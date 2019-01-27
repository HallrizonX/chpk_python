jQuery(document).ready(function ($) {
    $('.clients-slider-js').slick({
        infinite: true,
        slidesToShow: 5,
        slidesToScroll: 1,
        arrows: true,
        adaptiveHeight: true,
        autoplay: true,
        autoplaySpeed: 2000,
        responsive: [{
            breakpoint: 1030,
            settings: {
                slidesToShow: 2,
                adaptiveHeight: true,
                arrows: false,
                slidesToScroll: 1,
                autoplay: true,
                autoplaySpeed: 2000,
            }
        },{
           breakpoint: 750,
           settings: {
               slidesToShow: 2,
               adaptiveHeight: true,
               arrows: true,
               slidesToScroll: 1,
               autoplay: true,
               autoplaySpeed: 2000,
               mobileFirst: true
           } 
        }]
    });
    $('.feedback-slider-js').slick({
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        adaptiveHeight: true,
        dots: true,
        autoplay: true,
        autoplaySpeed: 6000
    });

    $('#phone, #top-phone').inputmask("+9-(999)-999-99-99");

    $('.top-button-js').click(function(){
        $('.top-form').addClass('show');
        $('body').addClass('top-form-show');
        return false;
    });


    var granimInstance = new Granim({
        element: '#top-bg-js',
        direction: 'diagonal',
        isPausedWhenNotInView: true,
        states : {
            "default-state": {
                gradients: [                    
                    ['#73c4c4', '#3081bb'],
                    ['#7f399d', '#73c4c4'],
                    ['#3081bb', '#3081bb']
                ],
                transitionSpeed: 2000
            }
        }
    });

    $('.burger-menu-js').click(function(){
        if($('body').hasClass('menu_gamburger_opened')){
            $('body').removeClass('menu_gamburger_opened');
        } else {
            $('body').addClass('menu_gamburger_opened');
        }        
    });

    var position_top = $('.top-text-block').offset().top;
    window.onscroll = function() {
        if(window.pageYOffset >= position_top) {
            $('body').addClass('fixed');
        } else {
            $('body').removeClass('fixed');
        };
    }
});