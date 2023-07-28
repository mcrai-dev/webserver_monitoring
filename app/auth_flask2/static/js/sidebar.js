$(document).ready(function () {
	$("#content").attr("hidden",false);
	$("#dashboard_content").attr("hidden", true);
	$("#friends_content").attr("hidden", true);
	$("#homepage").click(function () {
		console.log("mety homepage")
		$("#content").attr("hidden",false);
		$("#dashboard_content").attr("hidden", true);
		$("#friends_content").attr("hidden", true);
	});
	$("#dashboard").click(function () {
		$("#dashboard_content").attr("hidden",false);
		$("#content").attr("hidden", true);
		$("#friends_content").attr("hidden", true);
	});
	$("#friends").click(function () {
		$("#dashboard_content").attr("hidden",true);
		$("#content").attr("hidden", true);
		$("#friends_content").attr("hidden", false);
	});

});

(function($) {
	"use strict";

	var fullHeight = function() {
		$('.js-fullheight').css('height', $(window).height());
		$(window).resize(function(){
			$('.js-fullheight').css('height', $(window).height());
		});

	};
	fullHeight();

	$('#sidebarCollapse').on('click', function () {
      $('#sidebar').toggleClass('active');
  });

})(jQuery);
