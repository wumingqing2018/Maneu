var time = new Date();
var day = ("0" + time.getDate()).slice(-2);
var month = ("0" + (time.getMonth() + 1)).slice(-2);
var today = time.getFullYear() + "-" + (month) + "-" + (day);
$('.date_time').val(today)
