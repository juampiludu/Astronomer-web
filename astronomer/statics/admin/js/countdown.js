downCount("solar1");
downCount("solar2");
downCount("lunar1");
downCount("lunar2");
downCount("lunar3");

function downCount(solorlunid) {
  const second = 1000,
    minute = second * 60,
    hour = minute * 60,
    day = hour * 24;

  var date = $("#" + solorlunid + "date").text();

  let countDown = new Date(date).getTime(),
    x = setInterval(function () {
      let now = new Date().getTime(),
        distance = countDown - now;

      (document.getElementById(solorlunid + "days").innerText = Math.floor(
        distance / day
      )),
        (document.getElementById(solorlunid + "hours").innerText = Math.floor(
          (distance % day) / hour
        )),
        (document.getElementById(solorlunid + "minutes").innerText = Math.floor(
          (distance % hour) / minute
        )),
        (document.getElementById(solorlunid + "seconds").innerText = Math.floor(
          (distance % minute) / second
        ));

      if (distance < 0) {
        $(document).ready(function () {
          $("#" + solorlunid + "ul-countdown").remove();
          if (distance > -864000 && distance < 864000) {
            $("#" + solorlunid + "timedone").text("It's today!");
          } else {
            $("#" + solorlunid + "timedone").text("The event has ended");
          }
        });
      }
    }, second);
}
