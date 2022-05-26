$(document).ready(function () {
  $('div#red_header').click(function (event) {
    event.preventDefault();
    $('header').css({ color: '#FF0000' });
  });
});