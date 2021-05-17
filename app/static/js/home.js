function plotGraphic(response) {
    var getGraphic = document.getElementById("graphic");
    var names = response.names;
    var stock = response.stock;

    var productsChart = new Chart(getGraphic, {
        type: 'bar',
        data: {
            labels: names,
            datasets: [{
                label: 'Produtos',
                data: stock,
                backgroundColor: [
                    'rgba(250, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 2
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });
}

function getProductData(){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            let response = JSON.parse(xhttp.responseText)
            plotGraphic(response)
        }
    }
    let location = window.location.host
    xhttp.open("GET", "http://" + location + "/graphicdata", true);
    xhttp.send()
}