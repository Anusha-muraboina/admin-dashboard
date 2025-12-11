// Sales 30 Days Graph
const ctx1 = document.getElementById("salesChart");
if (ctx1) {
    new Chart(ctx1, {
        type: "line",
        data: {
            labels: ["1", "5", "10", "15", "20", "25", "30"],
            datasets: [{
                label: "Farmhouse Hyderabad",
                data: [0, 0, 0, 0, 0, 0, 0],
                borderWidth: 2
            }]
        }
    });
}

// Sales Year Graph
const ctx2 = document.getElementById("yearChart");
if (ctx2) {
    new Chart(ctx2, {
        type: "line",
        data: {
            labels: ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
            datasets: [{
                label: "Farmhouse (FY)",
                data: [0,0,0,0,0,0,0,0,0,0,0,0],
                borderWidth: 2
            }]
        }
    });
}
