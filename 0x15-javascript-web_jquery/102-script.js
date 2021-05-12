document.addEventListener('DOMContentLoaded', function () {
  $('#btn_translate').click(function () {
    const code = document.getElementById('language_code').value;
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + code;
    $.get(url, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
