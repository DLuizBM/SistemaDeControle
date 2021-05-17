function getFieldCep(){
    let cep = document.getElementById('id_zipcode');
    return cep.value
}

function fillAddressFields(response){
    document.getElementById('id_address').value = response.logradouro;
    document.getElementById('id_district').value = response.bairro;
    document.getElementById('id_city').value = response.localidade;
    document.getElementById('id_state').value = response.uf;
}

function getAddressFields() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            let response = JSON.parse(xhttp.responseText)
            fillAddressFields(response)
        }
    }
    xhttp.open("GET", "http://viacep.com.br/ws/" + getFieldCep() + "/json/", true);
    xhttp.send()
}