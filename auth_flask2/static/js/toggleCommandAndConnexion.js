$js = jQuery.noConflict();

$js(document).ready(function () {
	$("#connexion").attr("hidden",false);
	$("#command").attr("hidden", true);

	$("#btn_command").click(function () {
		$("#command").attr("hidden",false);
		$("#connexion").attr("hidden", true);
		// $( "#btn_command" ).tabs({ active: 1 });
	});

	$("#btn_connexion").click(function () {
		$("#connexion").attr("hidden",false);
		$("#command").attr("hidden", true);
		// $( "#btn_connexion" ).tabs({ active: 0 });
	});

	// $('.nav-tabs a').click(function(){
	// 		// $(this).tab('show');
	// 		console.log('le console est = ' +$(this))
	// 		$( "#tabs" ).tabs({ active: # });
	// 	}
	// );
});