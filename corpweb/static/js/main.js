/*왼쪽 서브메뉴 스크립트*/
var webLeftGnb = function(){
	$("div.left_menu ul.gnb li").mouseenter(function(){
		var indexNum = $(this).index();
	//	console.log(indexNum);
		
		$("div.left_sub_menu").css({"display":"block"});
		$("div.left_sub_menu").stop().animate({"opacity" : "1","left":"180px"},200);
		$("div.left_sub_menu ul").not( ($("div.left_sub_menu ul").eq( indexNum )) ).hide();
		$("div.left_sub_menu ul").eq( indexNum ).show();
	});

	$("div.left_menu").mouseleave(function(){
		$("div.left_sub_menu ul").hide();
		$("div.left_sub_menu").stop().animate({"opacity" : "0","left":"100px"},200);
		$("div.left_sub_menu").css({"display": "none"	});
	//	$("div.left_sub_menu").hide();
	});
}
/*왼쪽 서브메뉴 스크립트 끝*/

/*메인 슬라이드*/
var mainSlide = function(){
    var swiper = new Swiper('.main_slide', {
      slidesPerView: 1,
      loop: true,
      autoplay: {
        delay: 4500,
        disableOnInteraction: false,
      },
      pagination: {
        el: '.main_slide_pagination',
        clickable: true,
      },
    });
}
/*메인 슬라이드 끝*/

/*오른쪽메뉴 게시판 슬라이드*/

var boardSlide = function(){
    var swiper = new Swiper('.board_slide_wrap', {
      direction: 'vertical',
      slidesPerView: 1,
      loop: true,
      autoplay: {
        delay: 4500,
        disableOnInteraction: false,
      },
      navigation: {
        nextEl: 'div.board_slide_bts div.board_slide_next',
        prevEl: 'div.board_slide_bts div.board_slide_prev',
      },
    });
}
/*오른쪽메뉴 게시판 슬라이드 끝*/


/*모바일 메인 슬라이드*/
var mobileMainSlide = function(){
    var swiper = new Swiper('.m_main_slide', {
      slidesPerView: 1,
      loop: true,
      autoplay: {
        delay: 4500,
        disableOnInteraction: false,
      },
      pagination: {
        el: '.m_main_slide_pagination',
        clickable: true,
      },
    });
}
/*모바일 메인 슬라이드 끝*/

/*모바일 게시판 슬라이드*/

var mBoardSlide = function(){
    var swiper = new Swiper('.m_board_slide_wrap', {
      direction: 'vertical',
      slidesPerView: 1,
      loop: true,
      autoplay: {
        delay: 4500,
        disableOnInteraction: false,
      },
      navigation: {
        nextEl: 'div.m_board_slide_bts div.board_slide_next',
        prevEl: 'div.m_board_slide_bts div.board_slide_prev',
      },
    });
}
/*모바일 게시판 슬라이드 끝*/

$(document).ready(function(){
	webLeftGnb();
	mainSlide();
	boardSlide();
	mBoardSlide();
	mobileMainSlide();
});
