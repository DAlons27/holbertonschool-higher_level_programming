$(document).ready(function () {
  $('input#btn_translate').click(function (e) {
    e.preventDefault();
    const lang = $('input#language_code').val();
    const URL = 'https://fourtonfish.com/hellosalut/?lang=' + lang;
    $.get(URL, function (data) {
      $('div#hello').html(data.hello);
    });
  });
  $('input#language_code').keypress(function (e) {
    if (e.which === 13) {
      $('input#btn_translate').click();
    }
  });
});