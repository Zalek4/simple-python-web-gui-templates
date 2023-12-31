function getGraphData() {
    let labels;
    let results;

    $.get("/graph_01", function(data, status){
        let labels = data[0]
        let results = data[1]
        createChart(labels, results)
    });
};

// Demo chart
function createChart(labels, results) {
    data = {
        labels: labels,
    datasets: [{
        label: 'Demo Chart Data',
        data: results,
        backgroundColor: [
        'rgb(255, 99, 132)',
        'rgb(54, 162, 235)',
        'rgb(255, 205, 86)'
        ],
        hoverOffset: 4
    }]
    };
    config = {
    type: 'bar',
    data: data,
    };

    myChart = new Chart(document.getElementById('myChart'), config);
    
};

function createChartAgain() {
    var options = {
        chart: {
            type: 'line',
            width: '100%',
            height: '100%',
        },
        series: [{
            name: 'sales',
            data: [30, 40, 35, 50, 49, 60, 70, 91, 125]
        }],
        xaxis: {
            categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]
        }
    }
    
    var chart = new ApexCharts(document.querySelector("#graph_a"), options);
    
    chart.render();
};

createChartAgain();