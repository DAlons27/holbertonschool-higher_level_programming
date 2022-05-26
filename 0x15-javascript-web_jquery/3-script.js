$(document).ready(function () {
  $('div#red_header').click(function (e) {
    e.preventDefault();
    $('header').addClass('red');
  });
});