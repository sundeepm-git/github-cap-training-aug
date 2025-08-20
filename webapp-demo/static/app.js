// When the page loads, add a click handler to #btnHello.
// On click: fetch("/api/hello"), parse JSON, pretty-print it into #output.
// Handle errors by showing the message in #output.

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("btnHello").addEventListener("click", function() {
        fetch("/api/hello")
            .then(response => response.json())
            .then(data => {
                document.getElementById("output").textContent = JSON.stringify(data, null, 2);
            })
            .catch(error => {
                document.getElementById("output").textContent = "Error: " + error.message;
            });
    });

    // Add: fetch ISO timestamp from /api/time and display it
    const btnTime = document.getElementById("btnTime");
    if (btnTime) {
        btnTime.addEventListener("click", function() {
            fetch("/api/time")
                .then(response => response.json())
                .then(data => {
                    document.getElementById("output").textContent = data.timestamp;
                })
                .catch(error => {
                    document.getElementById("output").textContent = "Error: " + error.message;
                });
        });
    }

    
});

