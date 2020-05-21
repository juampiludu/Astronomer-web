$(document).ready(function () {

    $('.sidenav').sidenav();
    $('input#input_text').characterCounter();
    $('.modal').modal();
    $('.parallax').parallax();
    $('.collapsible').collapsible();
    $('.materialboxed').materialbox();
    M.textareaAutoResize($('#emailbody'));
    $(".mdl-spinner").fadeOut("fast");
    $(".success-help").fadeOut("fast");
    $('.fixed-action-btn').floatingActionButton();
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

$(document).on('keypress', function (e) {
    if (e.which == 13) {
        operation()
    }
});

function operation() {

    var weight = document.getElementById("input_text").value;

    if (String(weight).length == 0) {

        document.getElementById("input_text").style.borderColor = "red";
        document.getElementById("label_text").style.color = "red";

    }
    else if (parseFloat(weight) != Math.abs(weight)) {

        document.getElementById("input_text").style.borderColor = "red";
        document.getElementById("label_text").style.color = "red";

    }
    else if (String(weight).length > 20) {

    }
    else {

        document.getElementById("input_text").style.borderColor = "white";
        document.getElementById("label_text").style.color = "gray";
        var kg = weight;
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
        document.getElementById("text_earth").innerText = parseFloat(kg).toFixed(2) + " kg";

    }

}

$(function () {
    ["from", "subject", "emailbody"].forEach(function (field) {
        $("#" + field).attr("required", true);
        $("#" + field).focus(function () {
            $(".success-help").fadeOut("fast");
        });
    });

    $(".sendEmail").submit(function (e) {
        $(".mdl-spinner").fadeIn("slow").css("display", "inline-block");
        e.preventDefault();
        var from = $("#from").val();
        var to = 'lu.dev.spprt@gmail.com';
        var subject = $("#subject").val();
        var emailbody = $("#emailbody").val();
        $.ajax({
            url: "https://mybench-sendingemail.backbench.io/send",
            data: {
                from: from,
                to: to,
                subject: subject,
                emailbody: emailbody
            },
            error: function () {
                $(".mdl-spinner").fadeOut("fast");
                $(".success-help").html("An error has occurred").fadeIn("slow");
            },
            success: function (data) {
                $(".mdl-spinner").fadeOut("fast");
                ["from", "subject", "emailbody"].forEach(function (field) {
                    $("#" + field).val("");
                });
                $(".success-help").fadeIn("slow");
            },
            type: "POST"
        });
    });
});


/* navbar hide */

var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("navbar").style.top = "0";
  } else {
    document.getElementById("navbar").style.top = "-65px";
  }
  prevScrollpos = currentScrollPos;
}

/* up button */

var btnUp = $('#up-button');

$(window).scroll(function() {
    if ($(window).scrollTop() > 300) {
        btnUp.addClass('show');
    } else {
        btnUp.removeClass('show');
    }
});

btnUp.on('click', function(e) {
    e.preventDefault();
    $('html, body').animate({scrollTop:0}, '300');
});