function getYear(){
    let year = new Date().getFullYear();
    let footSpan = document.getElementById('info');
    footSpan.innerHTML = '<i  class="fa fa-male" ></i> ' + 'Divino ' + year ;
}