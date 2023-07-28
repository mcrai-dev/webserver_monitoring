var Yvalue = ""; //this variable is used to get the value from server to Plot Yvalue
var Y2value = ""; //this variable is used to get the value from server to Plot Yvalue2
var cpu ="";
var temperature = "";


// TO START COUNTDOWN
var countDownDate = "";
function checkboxFunction() {
    var checkBox = document.getElementById("flexCheckDefault");
    if (checkBox.checked == true) {
        start_countDown();
    } else if (checkBox.checked == false) {
        countDownDate = new Date().getTime();

    }
}
function start_countDown() {
    // get the data in input field
    document.getElementById("calendar").value;
    document.getElementById("countDownText").value;
    // var countdownText is set to show the date from date picker
    $('#countDownText').text(document.getElementById("calendar").value).css('color', 'springgreen').show();

    // Set the date we're counting down to
    countDownDate = new Date(document.getElementById("calendar").value).getTime();

    // Update the count down every 1 second
    var x = setInterval(function () {
        // Get today's date and time
        var now = new Date().getTime();

        // Find the distance between now and the count down date
        var distance = countDownDate - now;

        // Time calculations for days, hours, minutes and seconds
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // If the count down is over, write some text 
        if (distance < 0) {
            clearInterval(x);
            $('#countDownText').text("EXPIRED").css('color', 'gray').show();
            document.getElementById("countDownText").innerHTML = "EXPIRED";
            uncheck();
        }
    }, 1000);
}

// uncheck automatically the checkbox
function uncheck() {
    document.getElementById('flexCheckDefault').checked = false;
}

//  get the calendar date et send it to the server
$('#flexCheckDefault').click(function (e) {
    if ($('#flexCheckDefault').is(":checked")) {
        var date_and_time = $("#calendar").val();
        $.ajax({
            data: {
                code: "timeBrut",
                timeBrut: date_and_time,
            },
            type: 'POST',
            url: '/profile'
        }).done(function (data) {
            console.log("time is sent ")
        });
        e.preventDefault();
    }
});

// to send IP Data on server
$("#ip_request").on('submit', function (e) {
if($('#ipv4').val() === ""){
alert("IP not set")
}else{
    
    $('#ip_state_output').text("Checking...").css('color', 'black').show();
    $("#loadingText").text("Checking...").css('color', 'black').show();
    $("#loadingImage").attr("src","../static/Eclipse-1s-48px.svg");
    $("#overlay").show();
    $("#loadingPopup").show();
    $.ajax({
        data: {
            code: 'ip_check',
            ip_Address: $('#ipv4').val(),
        },
        // contentType: 'application/JSON',
        type: 'POST',
        url: '/profile'
    }).done(function (data) {
        $("#loadingText").text(data.out)

         setTimeout(function() {
            $("#overlay").hide();
            $("#loadingPopup").hide();
          }, 3000);

        if (data.out == ' Connected.') {
            $('#ip_state_output').text(data.out).css('color', 'springgreen').show();
            $("#loadingImage").attr("src","../static/CLIPLY_372103860_CHECK_MARK_400px.gif");
        } else {
            $('#ip_state_output').text(data.out).css('color', 'tomato').show();
            $("#loadingImage").attr("src","../static/icons8_warning_90px.png");
        }

        $("#color_mode").prop('checked', true);
        $('#countDownText').text(data.out)
    });
}
    e.preventDefault();

});


// this function is used for the function toggleTarget()
// it is useful to block the toggle if the select form is not set before clicking the toggle
var device_selected = ""
function selectedItem() {
    (device_form === "Choose device") ? alert("device is not selected !") : device_selected = $('#device_form').find(":selected").val()
}
// to toggle data if 
function toggleTarget() {
    var currentDateTime = new Date()
    var datetime = currentDateTime.getDate() + '/' + currentDateTime.getMonth() + '/' + currentDateTime.getFullYear() + ' ' + currentDateTime.getHours() + ':' + currentDateTime.getMinutes() + ':' + currentDateTime.getSeconds()
    if ($('#checkbox_target').is(":checked")) {
        selectedItem()
        //console.log(device_selected)
        $.ajax({
            data: {
                code: "toggle",
                keywords: 'turn_on',
                time: datetime,
                cible: device_selected,
            },
            type: 'POST',
            url: '/profile'
        }).done(function (data) {
            //console.log("toggle is sent ")
            $('#toggle_checkbox_label').text(data.next_state)
        });
    } else {
        //console.log('the toggle is off')
        $.ajax({
            data: {
                code: "toggle",
                keywords: 'turn_off',
                time: datetime,
                cible: device_selected,
            },
            type: 'POST',
            url: '/profile'
        }).done(function (data) {
            //console.log("toggle is sent ")
            $('#toggle_checkbox_label').text(data.next_state)
        });
    }
}

// this function is executed asynchronusly to get the data from the server to the interface
var fetch = setInterval(function () {
    // fetch data from server to Yvalue plot
    fetchData();
}, 1000);
function executeAsync(func) {
    setTimeout(func, 0);
}

function fetchData() {
    executeAsync(function () { 
        $.ajax({
            data: {
                code: "data_plot",
                keywords: 'get',
            },
            type: 'POST',
            url: '/profile'
        }).done(function (data) {
            // Yvalue = data.next_state
            brute = data.data_bute
            word = brute.split('#');
            Yvalue = word[0]
            Y2value = word[1]
            active_rebour = word[2]
            cpu = word[3]
            temperature = word[4]
            $('#cpu').text(cpu)
            $('#temperature').text(temperature)
            $('#current').text(Y2value)
            $('#voltage').text(Yvalue)
            $('#countDownText').text(active_rebour)
        });
    });
}
// for realtime plot
function rand() {
    return Math.random();
}

var time = new Date();

var trace1 = {
    x: [],
    y: [],
    mode: 'lines',
    name: 'Current',
    fill: 'tonexty',
    type: 'scatter',
    line: {
        color: '#80CAF6'
    }
}

var trace2 = {
    x: [],
    y: [],
    xaxis: 'x2',
    yaxis: 'y2',
    mode: 'lines',
    name: 'Tension',
    fill: 'tonexty',
    type: 'scatter',
    line: { color: '#DF56F1' }
};

var layout = {
    width: 800,
    height: 400,
    font: {
        family: 'Roboto, sans-serif',
        size: 14,
        // color: '#7f7f7f'
        color: '#4f4f4f'
    },
    xaxis: {
        type: 'date',
        domain: [0, 1],
        showticklabels: false
    },
    // yaxis: { domain: [0.6, 1], range: [0, 300], text: 'values' },
    yaxis: { domain: [0.6, 1], text: 'values' },
    xaxis2: {
        type: 'date',
        anchor: 'y2',
        domain: [0, 1]
    },
    yaxis2: {
        anchor: 'x2',
        domain: [0, 0.4]
    },
}
var config = {
    displayModeBar: true,
    displaylogo: false,
    scrollZoom: true,
    responsive: true
};
var data = [trace1, trace2];

Plotly.plot('graph', data, layout, config);

var cnt = 0;

var interval = setInterval(function () {

    var time = new Date();

    var update = {
        x: [[time], [time]],
        // y: [[rand()], [rand()]]
        y: [[Yvalue], [Y2value]]
    }

    Plotly.extendTraces('graph', update, [0, 1])

    if (cnt === 100) clearInterval(interval);
}, 1000);
