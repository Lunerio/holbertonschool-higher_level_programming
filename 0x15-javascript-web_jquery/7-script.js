let charName;
$(function () {
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data, textStatus) {
    charName = data.name;
    $('#character').text(charName);
  });
});
