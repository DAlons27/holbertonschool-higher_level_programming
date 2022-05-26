$(document).ready(function () {
  $('div#toggle_header').click(function (e) {
    e.preventDefault();
    // $(selector).toggleClass(className);
    if ($('header').hasClass('green')) {
      $('header').removeClass('green');
      $('header').addClass('red');
    } else if ($('header').hasClass('red')) {
      $('header').removeClass('red');
      $('header').addClass('green');
    }
  });
});