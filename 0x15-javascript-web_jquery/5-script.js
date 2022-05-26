$(document).ready(function () {
  $('div#add_item').click(function (e) {
    e.preventDefault();
    $('ul.my_list').append('<li>Item</li>');
  });
});