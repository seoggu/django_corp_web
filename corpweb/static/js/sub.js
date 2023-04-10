/*서브페이지 GNB 스크립트*/
var sub_webLeftGnb = function(){
    $("div.left_menu ul.gnb li").mouseenter(function(){
        var indexNum = $(this).index();
        $("div.left_sub_menu ul").not( ($("div.left_sub_menu ul").eq( indexNum )) ).hide();
        $("div.left_sub_menu ul").eq( indexNum ).show();
    });

}
/*서브페이지 GNB 스크립트 끝*/


/* 웹 오른쪽 스크롤메뉴들 스크립트*/
var scrollQuickMenu = function(){
    $(window).scroll(function( ){   //스크롤이 움직일때마다 이벤트 발생
        var position = $(window).scrollTop(); // 현재 스크롤바의 위치값을 반환합니다.
        $( "div.scroll_quick_menu_wrap" ).stop().animate({top:position+"px"}, 400); //해당 오브젝트 위치값 재설정
    });
}
/* 웹 오른쪽 스크롤메뉴들 스크립트 끝*/

/* 웹 오른쪽 하단 상단으로 스크롤버튼 스크립트*/
var scTopBt = function(){
    $("div.sc_top").click(function(){
        $( 'html, body' ).animate( { scrollTop : 0 }, 400 );
        return false;
    });
}
/* 웹 오른쪽 하단 상단으로 스크롤버튼 스크립트 끝*/

/*인사말 높이 같게 스크립트*/

$(window).resize(function(){
    var window_w = $(window).outerWidth();
    if( window_w >= 1020){
        var all_h_same = $("div.page_contents").outerHeight();
        $(".subpage_wrap").css({"height":all_h_same+"px"});
        $("div.page_wrap").css({"height":all_h_same+"px"});
    }else if( window_w < 1019){
        $(".subpage_wrap").css({"height":"auto"});
        $("div.page_wrap").css({"height":"auto"});
    }
});


var sameHeight = function(){
//	console.log( h_all );
//	console.log( win_w );
    var win_w = $(window).outerWidth();
    var h_all = $("div.page_contents").outerHeight();
    if( win_w >= 1020){
        $(".subpage_wrap").css({"height":h_all+"px"});
        $("div.page_wrap").css({"height":h_all+"px"});
    }else if( win_w < 1019){
        $(".subpage_wrap").css({"height":"auto"});
        $("div.page_wrap").css({"height":"auto"});
    }
}

/*인사말 높이 같게 스크립트 끝*/

/*모바일 탭메뉴 게시판 슬라이드*/
var tabboxSlide = function(){
    var swiper = new Swiper('.pr_tabbox_slide', {
        slidesPerView: 'auto',
//      loop: true,
        navigation: {
            nextEl: 'a.move_bt_right',
            prevEl: 'a.move_bt_left',
        },
    });
}
/*모바일 탭메뉴 게시판 슬라이드 끝*/

/*모바일 테이블 스크립트*/
var mTableView = function(){
    $("div.m_pd_info_tablebox h4").click(function(){
        $("div.m_pd_info_tablebox h4").not( $(this) ).removeClass("on");
        $(this).toggleClass("on");
        $("div.m_pd_infobox").not( $(this).next("div.m_pd_infobox") ).slideUp(400);
        $(this).next("div.m_pd_infobox").slideToggle(400);
    });
}
/*모바일 테이블 스크립트 끝*/


$(document).ready(function(){
    sameHeight();
    tabboxSlide();
    mTableView();
});