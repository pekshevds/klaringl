/*
Author       : Theme-Family
Template Name: Kabir - Logistic & Moving Company Website Template
Version      : 1.0
*/
(function($) {
    "use strict";
	
	
		/*PRELOADER JS*/
			$('#atf-loader').delay(1500).fadeOut(500);
		/*END PRELOADER JS*/

		
		//  Sidebar Js
		$(".atf_sidebar-toggle-btn").on("click", function () {
			$(".atf_sidebar__area").addClass("sidebar-opened");
			$(".atf_body-overlay").addClass("opened");
		});
		$(".atf_sidebar__close-btn").on("click", function () {
			$(".atf_sidebar__area").removeClass("sidebar-opened");
			$(".atf_body-overlay").removeClass("opened");
		});
		
		 // Toggle Js
		$(".atf_body-overlay").on("click", function () {
			$(".atf_sidebar__area").removeClass("sidebar-opened");
			$(".atf_body-overlay").removeClass("opened");
		});
	
		/* --------------------------------------------------------
		 Toogle Search
		-------------------------------------------------------- */
		// Handle click on toggle search button
		$('.header-search').on('click', function() {
			$('.header-search, .header-search-form').toggleClass('search-open');
			return false;
		});
	
		// Active Slick Nav 			
		$('#main-menu').slicknav({
			label: '',
			duration: 1000,
			easingOpen: "easeOutBounce", //available with jQuery UI
			prependTo:'#mobile_menu',
			closeOnClick: true,
			easingClose:"swing", 
			easingOpen:"swing", 
			openedSymbol: "&#9660;",
			closedSymbol: "&#9658;" 	
		});	
		
		
		/*START MENU JS*/
		if ($(window).scrollTop() > 200) {
              $('.fixed-top').addClass('menu-bg');
          } else {
              $('.fixed-top').removeClass('menu-bg');
          }
			$(window).on('scroll', function(){
				if ( $(window).scrollTop() > 70 ) {
					$('.site-navigation, .header-white, .header').addClass('navbar-fixed');
				} else {
					$('.site-navigation, .header-white, .header').removeClass('navbar-fixed');
				}
			});		  
		/*END MENU JS*/
        
		//**================= Sticky =====================**//
  
		  $(window).on('scroll', function() {
			if ($(window).scrollTop() > 50) {
				$('.navbar-expand-md').addClass('menu-bg');
				$('.atf-back-to-top').addClass('open');
			} else {
				$('.atf-header-area').removeClass('menu-bg');
				$('.atf-back-to-top').removeClass('open');
			}
		  });
		 
		  
		//**===================Scroll UP ===================**//

			if ($('.atf-back-to-top').length) {
			  $(".atf-back-to-top").on('click', function () {
				var target = $(this).attr('data-targets');
				// animate
				$('html, body').animate({
				  scrollTop: $(target).offset().top
				}, 1000);

			  });
			}	
		//**===================Scroll UP ===================**//
		
		
		// swiper slider
			if ($(".atf-swiper__slider").length) {
			  $(".atf-swiper__slider").each(function () {
				let elm = $(this);
				let options = elm.data("swiper-options");
				let thmSwiperSlider = new Swiper(elm, options);
			  });
			}
		

			
		/* --------------------------------------------------------
           Service Slider
        --------------------------------------------------------- */
        $('.atf__service-slider-active').slick({
            arrows: true,
            dots: false,
            infinite: true,
            speed: 300,
            slidesToShow: 3,
            slidesToScroll: 1,
            prevArrow: '<a class="slick-prev"><i class="fas fa-arrow-left" alt="Arrow Icon"></i></a>',
            nextArrow: '<a class="slick-next"><i class="fas fa-arrow-right" alt="Arrow Icon"></i></a>',
            responsive: [
                {
                    breakpoint: 1200,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 992,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 768,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 1,
						arrows: false,
						dots: true,
                    }
                },
                {
                    breakpoint: 580,
                    settings: {
                        arrows: false,
                        dots: true,
                        slidesToShow: 1,
                        slidesToScroll: 1
                    }
                }
            ]
        });
		
			
	/*--------------------------------------------------------------
		Counter
      --------------------------------------------------------------*/	
			$('.counter-value').counterUp({
			delay: 10,
			time: 1000
		});
			
		
		/*Start gallery Design*/
		
			$('.atf__gallery-slider-active').slick({
            arrows: true,
            dots: false,
            infinite: true,
            speed: 300,
            slidesToShow: 4,
            slidesToScroll: 1,
            prevArrow: '<a class="slick-prev"><i class="fas fa-arrow-left" alt="Arrow Icon"></i></a>',
            nextArrow: '<a class="slick-next"><i class="fas fa-arrow-right" alt="Arrow Icon"></i></a>',
            responsive: [
                {
                    breakpoint: 1200,
                    settings: {
                        slidesToShow: 4,
                        slidesToScroll: 1,
                        arrows: false,
                        dots: true
                    }
                },
                {
                    breakpoint: 992,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 1,
                        arrows: false,
                        dots: true
                    }
                },
                {
                    breakpoint: 768,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 1,
                        arrows: false,
                        dots: true
                    }
                },
                {
                    breakpoint: 575,
                    settings: {
                        arrows: false,
                        dots: true,
                        slidesToShow: 1,
                        slidesToScroll: 1
                    }
                }
            ]
        });
			

		/*END gallery Design*/
			
			
		/*Start Testimonials LOGO*/
		
			$('#atf-testimonial-slider').owlCarousel({
				margin:5,
				autoplay:false,
				items: 3,
				loop:true,
				nav:false,
				responsive:{
					0:{
						items:1
					},
					600:{
						items:1
					},
					992:{
						items:2
					}
				}
			})

		/*END Testimonials LOGO*/
			
		/*Start Blog Design*/
			$('.atf_blog-slider-one-active').slick({
            arrows: true,
            dots: false,
            infinite: true,
            speed: 300,
            slidesToShow: 3,
            slidesToScroll: 1,
            prevArrow: '<a class="slick-prev"><i class="fas fa-arrow-left" alt="Arrow Icon"></i></a>',
            nextArrow: '<a class="slick-next"><i class="fas fa-arrow-right" alt="Arrow Icon"></i></a>',
            responsive: [
                {
                    breakpoint: 1200,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 1,
                        arrows: false,
                        dots: true
                    }
                },
                {
                    breakpoint: 992,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 1,
                        arrows: false,
                        dots: true
                    }
                },
                {
                    breakpoint: 768,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 1,
                        arrows: false,
                        dots: true
                    }
                },
                {
                    breakpoint: 580,
                    settings: {
                        arrows: false,
                        dots: true,
                        slidesToShow: 1,
                        slidesToScroll: 1
                    }
                }
            ]
        });

		/*END Blog Design*/
		
		/*START PARTNER LOGO*/
			$('.atf-brand-active').owlCarousel({
				margin:5,
				autoplay:true,
				items: 3,
				loop:true,
				nav:false,
				responsive:{
					0:{
						items:1
					},
					600:{
						items:3
					},
					1000:{
						items:5
					}
				}
			})
			/*END PARTNER LOGO*/
			

		/* --------------------------------------------------------
			 LightCase jQuery Active
		--------------------------------------------------------- */
			$('a[data-rel^=lightcase]').lightcase({
				transition: 'elastic', /* none, fade, fadeInline, elastic, scrollTop, scrollRight, scrollBottom, scrollLeft, scrollHorizontal and scrollVertical */
				swipe: true,
				maxWidth: 1170,
				maxHeight: 600,
			});
		
		/* --------------------------------------------------------
             Mailchamp
        --------------------------------------------------------- */

		$('#mc-form').ajaxChimp({
			url: 'https://gmail.us10.list-manage.com/subscribe/post?u=c9af266402a277062d0d7cee0&amp;id=1211fda42f'
			/* Replace Your AjaxChimp Subscription Link */
		}); 
		
		/* --------------------------------------------------------
				 Nice Select
			--------------------------------------------------------- */
			// $('select').niceSelect();
			
		/*START ANIMATION JS*/
		  AOS.init();
		/*END ANIMATION JS*/
		

		
})(jQuery);