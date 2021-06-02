
$(document).ready(function(){
    // 获取二维码
    $("#get_qr_code").click(function(){
        $.ajax({
            url: api_qr_code,
            type: 'POST',
            data: $('#qr_code').serialize(),
            success: function (res) {
                if (res.code !== 0){
                    alert(res.msg)
                }
            },
        })
    });
    // 删除订单
    $("#delete").click(function () {
        $.ajax({
            url: api_order_delete,
            type: 'POST',
            data: $('#order_delete').serialize(),
            success: function (res) {
                alert(res.msg)
            },
        });
    });
});
