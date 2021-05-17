function orderByName(){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
        }
    }
    let location = window.location.host
    xhttp.open("GET", "http://" + location + "/order_name/", true);
    xhttp.send()
}

function orderByPrice(){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
        }
    }
    let location = window.location.host
    xhttp.open("GET", "http://" + location + "/order_price/", true);
    xhttp.send()
}

function orderByStock(){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
        }
    }
    let location = window.location.host
    xhttp.open("GET", "http://" + location + "/order_stock/", true);
    xhttp.send()
}