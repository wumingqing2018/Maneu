/*
提交订单JS
校验 c_name 是否符合输入要求
校验 c_phone 是否符合输入要求
*/
$(document).ready(function () {
    order_list.click(function () {
        window.location.href = api_order_list;
    })
    $("#c_name").blur(function(){
        if ($('#c_name').val() === '') {
            $('#username_error').text('请输入姓名');
        } else {
            $('#username_error').text('');
            if (c_phone.val() === '') {
                $('#insert').hide()
            } else {
                $('#insert').show()
            }
        }
    });
    c_phone.blur(function(){
        if (c_phone.val() === '') {
            $('#phone_error').text('请输入电话');
        } else if (isNaN(c_phone.val())) {
            $('#phone_error').text('电话由数字构成');
        } else {
            $('#phone_error').text('');
            if (c_name.val() === '') {
                $('#insert').hide()
            } else {
                $('#insert').show()
            }
        }
    });
    $('#insert').click(function () {
        $("#order").val('['+order+']');
        $.ajax({
            url: api_order_insert,
            type: 'POST',
            data: $('#order_insert').serialize(),
            success: function (res) {
                console.log(res)
            }
        });
    });
});
