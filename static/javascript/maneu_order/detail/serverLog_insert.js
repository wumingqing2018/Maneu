$("#server_button").click(function () {
    $.ajax({
        url: service_insert,
        type: 'POST',
        data: {
            "order_id": order_id,
            "guess_id": guess_id,
            "content": $("#server_value").val(),
            "csrfmiddlewaretoken": $("[name='csrfmiddlewaretoken']").val()
        },
        success: function (res) {
            alert('添加成功');
            $('#server_list').append(
                "    <div class='col-2'>\n"+
                "        <span>"+ res['data']['time'] +"</span>\n"+
                "    </div>\n"+
                "    <div class='col-10'>\n"+
                "        <span>"+ res['data']['content'] +"</span>\n"+
                "    </div>\n"+
                "<hr style='color: white'>\n"
            );
        }
    })
});
