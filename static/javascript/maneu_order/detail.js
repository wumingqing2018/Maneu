$(document).ready(function () {
    $("#function").val(maneu_vision.function);
    $("#PD").val(maneu_vision.PD);
    $("#remark").val(maneu_vision.remark);

    $("#OD_VA").val(maneu_vision.OD_VA);
    $("#OD_SPH").val(maneu_vision.OD_SPH);
    $("#OD_CYL").val(maneu_vision.OD_CYL);
    $("#OD_AX").val(maneu_vision.OD_AX);
    $("#OD_PR").val(maneu_vision.OD_PR);
    $("#OD_FR").val(maneu_vision.OD_FR);
    $("#OD_ADD").val(maneu_vision.OD_ADD);
    $("#OD_BCVA").val(maneu_vision.OD_BCVA);

    $("#OS_VA").val(maneu_vision.OD_VA);
    $("#OS_SPH").val(maneu_vision.OD_SPH);
    $("#OS_CYL").val(maneu_vision.OD_CYL);
    $("#OS_AX").val(maneu_vision.OD_AX);
    $("#OS_PR").val(maneu_vision.OD_PR);
    $("#OS_FR").val(maneu_vision.OD_FR);
    $("#OS_ADD").val(maneu_vision.OD_ADD);
    $("#OS_BCVA").val(maneu_vision.OD_BCVA);

    upline = Object.keys(maneu_store).length / 5
    for (i = 1; i <= upline; i++) {
        $('#store_table').append(
            "<tr>\n" +
            "    <td colspan='2'>\n" +
            "        <span>" + maneu_store['arg' + i + '0'] + "</span>\n" +
            "    </td>\n" +
            "    <td colspan='2'>\n" +
            "        <span>" + maneu_store['arg' + i + '1'] + "</span>\n" +
            "    </td>\n" +
            "    <td colspan='2'>\n" +
            "        <span>" + maneu_store['arg' + i + '2'] + "</span>\n" +
            "    </td>\n" +
            "    <td colspan='2'>\n" +
            "        <span>" + maneu_store['arg' + i + '3'] + "</span>\n" +
            "    </td>\n" +
            "    <td>\n" +
            "        <span>" + maneu_store['arg' + i + '4'] + "</span>\n" +
            "    </td>\n" +
            "</tr>\n")
    }
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
                $("#server_list").empty();
                $('#server_list').prepend(
                    "<tr>\n"+
                    "    <td width='10%'>\n"+
                    "        <span>"+ res['data']['time'] +"</span>\n"+
                    "    </>\n"+
                    "    <td width='90%'>\n"+
                    "        <span>"+ res['data']['content'] +"</span>\n"+
                    "    </>\n"+
                    "</tr>\n"
                );
            }
        })
    });
})
