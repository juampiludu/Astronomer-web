const second = 1000,
    minute = second * 60,
    hour = minute * 60,
    day = hour * 24;

/* 21 june solar */

var date = $('#solar1date').text();

let countDown = new Date(date).getTime(),
    x = setInterval(function () {

        let now = new Date().getTime(),
            distance = countDown - now;

        document.getElementById('solar1days').innerText = Math.floor(distance / (day)),
            document.getElementById('solar1hours').innerText = Math.floor((distance % (day)) / (hour)),
            document.getElementById('solar1minutes').innerText = Math.floor((distance % (hour)) / (minute)),
            document.getElementById('solar1seconds').innerText = Math.floor((distance % (minute)) / second);

        //do something later when date is reached
        if (distance < 0) {

            $(document).ready(function () {
                $('#solar1ul-countdown').remove();
                if (distance > -864000 && distance < 864000) {
                    $('#solar1timedone').text("It's today!");
                } else {
                    $('#solar1timedone').text("The event has ended");
                }
            });

        }

    }, second)

/* 14 december */

var date2 = $('#solar2date').text();

let countDown2 = new Date(date2).getTime(),
    x2 = setInterval(function () {

        let now2 = new Date().getTime(),
            distance2 = countDown2 - now2;

        document.getElementById('solar2days').innerText = Math.floor(distance2 / (day)),
            document.getElementById('solar2hours').innerText = Math.floor((distance2 % (day)) / (hour)),
            document.getElementById('solar2minutes').innerText = Math.floor((distance2 % (hour)) / (minute)),
            document.getElementById('solar2seconds').innerText = Math.floor((distance2 % (minute)) / second);

        //do something later when date is reached
        if (distance2 < 0) {

            $(document).ready(function () {
                $('#solar2ul-countdown').remove();
                if (distance2 > -864000 && distance2 < 864000) {
                    $('#solar2timedone').text("It's today!");
                } else {
                    $('#solar2timedone').text("The event has ended");
                }
            });

        }

    }, second)

/* june lunar */

var date3 = $('#lunar1date').text();

let countDown3 = new Date(date3).getTime(),
    x3 = setInterval(function () {

        let now3 = new Date().getTime(),
            distance3 = countDown3 - now3;

        document.getElementById('lunar1days').innerText = Math.floor(distance3 / (day)),
            document.getElementById('lunar1hours').innerText = Math.floor((distance3 % (day)) / (hour)),
            document.getElementById('lunar1minutes').innerText = Math.floor((distance3 % (hour)) / (minute)),
            document.getElementById('lunar1seconds').innerText = Math.floor((distance3 % (minute)) / second);

        //do something later when date is reached
        if (distance3 < 0) {

            $(document).ready(function () {
                $('#lunar1ul-countdown').remove();
                if (distance3 > -864000 && distance3 < 864000) {
                    $('#lunar1timedone').text("It's today!");
                } else {
                    $('#lunar1timedone').text("The event has ended");
                }
            });

        }

    }, second)

/* july */

var date4 = $('#lunar2date').text();

let countDown4 = new Date(date4).getTime(),
    x4 = setInterval(function () {

        let now4 = new Date().getTime(),
            distance4 = countDown4 - now4;

        document.getElementById('lunar2days').innerText = Math.floor(distance4 / (day)),
            document.getElementById('lunar2hours').innerText = Math.floor((distance4 % (day)) / (hour)),
            document.getElementById('lunar2minutes').innerText = Math.floor((distance4 % (hour)) / (minute)),
            document.getElementById('lunar2seconds').innerText = Math.floor((distance4 % (minute)) / second);

        //do something later when date is reached
        if (distance4 < 0) {

            $(document).ready(function () {
                $('#lunar2ul-countdown').remove();
                if (distance4 > -864000 && distance4 < 864000) {
                    $('#lunar2timedone').text("It's today!");
                } else {
                    $('#lunar2timedone').text("The event has ended");
                }
            });

        }

    }, second)

/* november */

var date5 = $('#lunar3date').text();

let countDown5 = new Date(date5).getTime(),
    x5 = setInterval(function () {

        let now5 = new Date().getTime(),
            distance5 = countDown5 - now5;

        document.getElementById('lunar3days').innerText = Math.floor(distance5 / (day)),
            document.getElementById('lunar3hours').innerText = Math.floor((distance5 % (day)) / (hour)),
            document.getElementById('lunar3minutes').innerText = Math.floor((distance5 % (hour)) / (minute)),
            document.getElementById('lunar3seconds').innerText = Math.floor((distance5 % (minute)) / second);

        //do something later when date is reached
        if (distance5 < 0) {

            $(document).ready(function () {
                $('#lunar3ul-countdown').remove();
                if (distance5 > -864000 && distance5 < 864000) {
                    $('#lunar3timedone').text("It's today!");
                } else {
                    $('#lunar3timedone').text("The event has ended");
                }
            });

        }

    }, second)
