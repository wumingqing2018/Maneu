$(document).ready(function () {
    $("#c_name").blur(function(){
        var c_name = $('#c_name').val();
        if (c_name == null) {
            $('#username_error').text('请输入姓名');
        }
        else {
            $('#username_error').text('');
        }
    });
    $("#c_phone").blur(function(){
        var c_phone = $('#c_phone').val()   ;
        if (c_phone == null) {
            $('#phone_error').text('请输入电话');
        }
        else if (isNaN(c_phone)) {
            $('#phone_error').text('电话由数字构成');
        }
        else {
            $('#phone_error').text('');
        }
    });
    $('#insert').click(function () {
        $.ajax({
            url: api_order_insert,
            type: 'post',
            data: $('#order_insert').serialize(),
            success: function (res) {
                alert(res)
            }
        });
    });
});
