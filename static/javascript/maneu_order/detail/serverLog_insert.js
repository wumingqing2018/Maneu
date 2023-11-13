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
                "                    <div class=\"input-group input-group-sm\" style=\"padding-bottom: 10px\">\n" +
                "                        <span class=\"input-group-text\">{{ foo.time }}</span>\n" +
                "                        <input type=\"text\" class=\"form-control\" id=\"content\" autocomplete=\"off\" placeholder=\"售后内容\" value=\"{{ foo.content }}\">\n" +
                "                        <input type=\"button\" class=\"btn btn-primary\" value=\"更新\" onclick=\"serviceUpdate(this)\">\n" +
                "                        <input type=\"hidden\" value=\"{{ foo.id }}\">\n" +
                "                        <input type=\"button\" class=\"btn btn-primary\" value=\"删除\" onclick=\"serviceDelete(this)\">\n" +
                "                    </div>\n"
            );
        }
    })
});
