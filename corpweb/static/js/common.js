
/*모바일 오른쪽 서브메뉴 스크립트*/
var mobileGnb = function(){
	$(".m_gnb_bt").click(function(){
//		console.log("asd");
		$("html, body").css({"height":"100%","overflow-y":"hidden"});
		$("div.m_header div.m_sub_menu").css({"display":"block"});
		$("div.m_header div.m_sub_menu").animate({"right":"0","opacity":"1"},400);
	});

	$(".m_sub_menu_bg").click(function(){
		$("html, body").css({"height":"auto","overflow-y":"auto"});
		$("div.m_header div.m_sub_menu").animate({"right":"-30%","opacity":"0"},400);
		$("div.m_header div.m_sub_menu").fadeOut(400);
	});

	$("a.subdetailmenubt").click(function(){
		if( $(this).next(".m_subdetailmenu").css("display") == "block" ){
			$(this).removeClass("on");
			$(this).find("span").css({"transform":"rotate(0deg)"});
			$(this).next(".m_subdetailmenu").slideUp(400);		
		}else{
			$("a.subdetailmenubt span").not( $(this).find("span") ).css({"transform":"rotate(0deg)"});
			$(this).find("span").css({"transform":"rotate(90deg)"});
			$("a.subdetailmenubt").not( $(this) ).removeClass("on");
			$(this).toggleClass("on");
			$("div.m_header div.m_sub_menu ul.m_sub_menu_list > li > ul.m_subdetailmenu").not( $(this).next(".m_subdetailmenu") ).slideUp(400);
			$(this).next(".m_subdetailmenu").slideDown(400);
		}
	});

}
/*모바일 오른쪽 서브메뉴 스크립트 끝*/


$(document).ready(function(){

	window.onload = function(){
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

	mobileGnb();

});

function loading() {
	$.blockUI({
		message: '<h3>처리중 입니다.<br />잠시 기다려 주세요.</h3>'
	});	
}
