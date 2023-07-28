jSuites.calendar(document.getElementById('calendar'), {
    // 'MMM dd, YYYY HH:MM:SS' example Nov 02, 2022 12:05:55
    format: 'MMM dd, YYYY HH:MM:SS',
    time: true,
});



$j = jQuery.noConflict();

$j(document).ready(function () {

    //input mask bundle ip address
    $('#ipv4').inputmask({
        alias: "ip",
        greedy: false //The initial mask shown will be "" instead of "-____".
    });
});