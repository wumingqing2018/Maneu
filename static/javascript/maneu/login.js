$(document).ready(function () {
    $("#sendsms-btn").click(function () {
        $.ajax({
            url: sendsms,
            method: 'GET',
            data: {
                call: $("#call").val(),
            },
            success: function (res) {
                if (res.status === true) {
                    $("#msg").text("")
                } else {
                    $("#msg").text("发送短信失败" + res.message)
                }
            }
        })
    })
    $("#login-btn").click(function () {
        $.ajax({
            url: login_verify,
            method: 'GET',
            data: {
                call: $("#call").val(),
                code: $("#code").val()
            },
            success: function (res) {
                if (res.status === true) {
                    window.location.href = maneu_order_index
                } else {
                    $("#msg").text(res.message)
                }
            },
        })
    })
})