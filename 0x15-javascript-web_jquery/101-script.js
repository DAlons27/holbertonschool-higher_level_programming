$(document).ready(function () {
  $('div#add_item').click(function (e) {
    e.preventDefault();
    $('ul.my_list').append('<li>Item</li>');
  });
  $('div#remove_item').click(function (e) {
    e.preventDefault();
    $('ul.my_list li').last().remove();
  });
  $('div#clear_list').click(function (e) {
    e.preventDefault();
    $('ul.my_list').empty();
  });
});