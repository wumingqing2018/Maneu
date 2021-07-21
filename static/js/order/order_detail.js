 
$(document).ready(function(){
    $.ajax({
        url: api_order_detail,
        type: "GET",
        data: {order_id: order_id},
        success: function (res) {
            if (res.code === 0){
                c_name.html(res.data.c_name)
                c_time.html(res.data.c_time)
                c_phone.html(res.data.c_phone)
                remark.html(res.data.remark)
                order = jQuery.parseJSON(res.data.order)
                for (i in order){
                    content = ''
                    content += '<tr>'
                    content += '<td style="width: 9%"><span>'+ order[i]['product'] + '</span></td>'
                    content += '<td style="width: 9%"><span>'+ order[i]['brand'] +'</span></td>'
                    content += '<td style="width: 9%"><span>'+ order[i]['model'] + '</span></td>'
                    content += '<td style="width: 9%"><span>'+ order[i]['sphere'] + '</span></td>'
                    content += '<td style="width: 9%"><span>'+ order[i]['astigmatic'] + '</span></td>'
                    content += '<td style="width: 9%"><span>'+ order[i]['refraction'] + '</span></td>'
                    content += '<td style="width: 9%"><span>'+ order[i]['Around'] + '</span></td>'
                    content += '<td style="width: 9%"><span>'+ order[i]['pd'] + '</span></td>'
                    content += '<td style="width: 9%"><span>'+ order[i]['add'] + '</span></td>'
                    content += '<td style="width: 9%"><span>'+ order[i]['deviation'] + '</span></td>'
                    content += '<td style="width: 9%"><span>'+ order[i]['count'] + '</span></td>'
                    content += '</tr>'
                    $('#order_content').append(content)
                }
            }
        }
    })
    // 获取二维码
    $("#get_qr_code").click(function(){
        $.ajax({
            url: api_order_qrcode,
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
