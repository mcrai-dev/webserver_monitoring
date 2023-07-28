        // ==========================for the realtime
        `use strict`;
        function refreshTime() {
            const timeDisplay = document.getElementById("time");
            const dateString = new Date().toLocaleString();
            const formattedString = dateString.replace(", ", " - ");
            timeDisplay.textContent = formattedString;
            var timeNowToUseForChart = formattedString;
        }
        setInterval(refreshTime, 1000);