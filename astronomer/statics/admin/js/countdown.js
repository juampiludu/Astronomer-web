const second = 1000,
    minute = second * 60,
    hour = minute * 60,
    day = hour * 24;

/* 21 june solar */

let countDown = new Date('Jun 21, 2020 00:00:00').getTime(),
    x = setInterval(function () {

        let now = new Date().getTime(),
            distance = countDown - now;

        document.getElementById('soljundays').innerText = Math.floor(distance / (day)),
            document.getElementById('soljunhours').innerText = Math.floor((distance % (day)) / (hour)),
            document.getElementById('soljunminutes').innerText = Math.floor((distance % (hour)) / (minute)),
            document.getElementById('soljunseconds').innerText = Math.floor((distance % (minute)) / second);

        //do something later when date is reached
        if (distance < 0) {

            $(document).ready(function () {
                $('#ul-countdown').remove();
                if (distance > -864000 && distance < 864000) {
                    $('#timedone').text("It's today!");
                } else {
                    $('#timedone').text("The event has ended");
                }
            });

        }

    }, second)

/* 14 december */

let countDown2 = new Date('Dec 14, 2020 00:00:00').getTime(),
    x2 = setInterval(function () {

        let now2 = new Date().getTime(),
            distance2 = countDown2 - now2;

        document.getElementById('decdays').innerText = Math.floor(distance2 / (day)),
            document.getElementById('dechours').innerText = Math.floor((distance2 % (day)) / (hour)),
            document.getElementById('decminutes').innerText = Math.floor((distance2 % (hour)) / (minute)),
            document.getElementById('decseconds').innerText = Math.floor((distance2 % (minute)) / second);

        //do something later when date is reached
        if (distance2 < 0) {

            $(document).ready(function () {
                $('#ul-countdown').remove();
                if (distance2 > -864000 && distance2 < 864000) {
                    $('#timedone').text("It's today!");
                } else {
                    $('#timedone').text("The event has ended");
                }
            });

        }

    }, second)

/* june lunar */

let countDown3 = new Date('Jun 5, 2020 00:00:00').getTime(),
    x3 = setInterval(function () {

        let now3 = new Date().getTime(),
            distance3 = countDown3 - now3;

        document.getElementById('lunjundays').innerText = Math.floor(distance3 / (day)),
            document.getElementById('lunjunhours').innerText = Math.floor((distance3 % (day)) / (hour)),
            document.getElementById('lunjunminutes').innerText = Math.floor((distance3 % (hour)) / (minute)),
            document.getElementById('lunjunseconds').innerText = Math.floor((distance3 % (minute)) / second);

        //do something later when date is reached
        if (distance3 < 0) {

            $(document).ready(function () {
                $('#ul-countdown').remove();
                if (distance3 > -864000 && distance3 < 864000) {
                    $('#timedone').text("It's today!");
                } else {
                    $('#timedone').text("The event has ended");
                }
            });

        }

    }, second)

/* july */

let countDown4 = new Date('Jul 5, 2020 00:00:00').getTime(),
    x4 = setInterval(function () {

        let now4 = new Date().getTime(),
            distance4 = countDown4 - now4;

        document.getElementById('juldays').innerText = Math.floor(distance4 / (day)),
            document.getElementById('julhours').innerText = Math.floor((distance4 % (day)) / (hour)),
            document.getElementById('julminutes').innerText = Math.floor((distance4 % (hour)) / (minute)),
            document.getElementById('julseconds').innerText = Math.floor((distance4 % (minute)) / second);

        //do something later when date is reached
        if (distance4 < 0) {

            $(document).ready(function () {
                $('#ul-countdown').remove();
                if (distance4 > -864000 && distance4 < 864000) {
                    $('#timedone').text("It's today!");
                } else {
                    $('#timedone').text("The event has ended");
                }
            });

        }

    }, second)

/* november */

let countDown5 = new Date('Nov 30, 2020 00:00:00').getTime(),
    x5 = setInterval(function () {

        let now5 = new Date().getTime(),
            distance5 = countDown5 - now5;

        document.getElementById('novdays').innerText = Math.floor(distance5 / (day)),
            document.getElementById('novhours').innerText = Math.floor((distance5 % (day)) / (hour)),
            document.getElementById('novminutes').innerText = Math.floor((distance5 % (hour)) / (minute)),
            document.getElementById('novseconds').innerText = Math.floor((distance5 % (minute)) / second);

        //do something later when date is reached
        if (distance5 < 0) {

            $(document).ready(function () {
                $('#ul-countdown').remove();
                if (distance5 > -864000 && distance5 < 864000) {
                    $('#timedone').text("It's today!");
                } else {
                    $('#timedone').text("The event has ended");
                }
            });

        }

    }, second)
