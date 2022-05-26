$(document).ready(function () {
  $('div#update_header').click(function (e) {
    e.preventDefault();
    $('header').html('New Header!!!');
  });
});