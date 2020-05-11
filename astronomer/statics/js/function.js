$(document).ready(function () {

    $('.sidenav').sidenav();
    $('input#input_text').characterCounter();
    $('.modal').modal();
    $('.parallax').parallax();
    $('.collapsible').collapsible();
    /*$('.tooltipped').tooltip();*/
    M.updateTextFields();

});

const earth = 9.807;
const moon = 1.62;
const mercury = 3.7;
const venus = 8.87;
const mars = 3.711;
const jupiter = 24.79;
const saturn = 10.44;
const uranus = 8.87;
const neptune = 11.15;
const pluto = 0.62;

function operation() {

    var kg = document.getElementById("input_text").value;
    var op1 = (parseFloat(kg) * mercury) / earth;
    var op2 = (parseFloat(kg) * venus) / earth;
    var op3 = (parseFloat(kg) * moon) / earth;
    var op4 = (parseFloat(kg) * mars) / earth;
    var op5 = (parseFloat(kg) * jupiter) / earth;
    var op6 = (parseFloat(kg) * saturn) / earth;
    var op7 = (parseFloat(kg) * uranus) / earth;
    var op8 = (parseFloat(kg) * neptune) / earth;
    var op9 = (parseFloat(kg) * pluto) / earth;
    document.getElementById("text_mercury").innerText = op1.toFixed(2) + " kg";
    document.getElementById("text_venus").innerText = op2.toFixed(2) + " kg";
    document.getElementById("text_moon").innerText = op3.toFixed(2) + " kg";
    document.getElementById("text_mars").innerText = op4.toFixed(2) + " kg";
    document.getElementById("text_jupiter").innerText = op5.toFixed(2) + " kg";
    document.getElementById("text_saturn").innerText = op6.toFixed(2) + " kg";
    document.getElementById("text_uranus").innerText = op7.toFixed(2) + " kg";
    document.getElementById("text_neptune").innerText = op8.toFixed(2) + " kg";
    document.getElementById("text_pluto").innerText = op9.toFixed(2) + " kg";
    document.getElementById("text_earth").innerText = kg + " kg";

}

var btn = $("#weight_button")

function disableButton() {

    if (String(document.getElementById("input_text").value).length > 20) {
        btn.attr("disabled", "disabled");
    }

}

function enableButton() {

    if (String(document.getElementById("input_text").value).length <= 20) {
        btn.removeAttr("disabled");
    }

}
