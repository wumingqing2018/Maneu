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
        var c_name = $('#c_name').val();
        if (c_name === '') {
            $('#username_error').text('请输入姓名');
        } else {
            $('#username_error').text('');
        }
    });
    c_phone.blur(function(){
        c_phone_val = c_phone.val();
        if (c_phone_val === '') {
            $('#phone_error').text('请输入电话');
        } else if (isNaN(c_phone_val)) {
            $('#phone_error').text('电话由数字构成');
        } else {
            $('#phone_error').text('');
        }
    });
    $('#insert').click(function () {
        $("#order").val(order);
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
