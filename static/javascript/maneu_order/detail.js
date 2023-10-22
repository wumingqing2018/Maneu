$(document).ready(function () {
    $("#function").text(maneu_vision.function);
    $("#PD").text(maneu_vision.PD);
    $("#remark").text(maneu_vision.remark);

    $("#OD_VA").text(maneu_vision.OD_VA);
    $("#OD_SPH").text(maneu_vision.OD_SPH);
    $("#OD_CYL").text(maneu_vision.OD_CYL);
    $("#OD_AX").text(maneu_vision.OD_AX);
    $("#OD_PR").text(maneu_vision.OD_PR);
    $("#OD_FR").text(maneu_vision.OD_FR);
    $("#OD_ADD").text(maneu_vision.OD_ADD);
    $("#OD_BCVA").text(maneu_vision.OD_BCVA);

    $("#OS_VA").text(maneu_vision.OD_VA);
    $("#OS_SPH").text(maneu_vision.OD_SPH);
    $("#OS_CYL").text(maneu_vision.OD_CYL);
    $("#OS_AX").text(maneu_vision.OD_AX);
    $("#OS_PR").text(maneu_vision.OD_PR);
    $("#OS_FR").text(maneu_vision.OD_FR);
    $("#OS_ADD").text(maneu_vision.OD_ADD);
    $("#OS_BCVA").text(maneu_vision.OD_BCVA);

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
