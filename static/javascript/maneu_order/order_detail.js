
$(document).ready(function () {
    $("#OD_VA").text(maneu_vision.OD_VA);
    $("#OD_SPH").text(maneu_vision.OD_SPH);
    $("#OD_CYL").text(maneu_vision.OD_CYL);
    $("#OD_AX").text(maneu_vision.OD_AX);
    $("#OD_PR").text(maneu_vision.OD_PR);
    $("#OD_FR").text(maneu_vision.OD_FR);
    $("#OD_ADD").text(maneu_vision.OD_ADD);
    $("#OD_BCVA").text(maneu_vision.OD_BCVA);
    $("#OS_VA").text(maneu_vision.OS_VA);
    $("#OS_SPH").text(maneu_vision.OS_SPH);
    $("#OS_CYL").text(maneu_vision.OS_CYL);
    $("#OS_AX").text(maneu_vision.OS_AX);
    $("#OS_PR").text(maneu_vision.OS_PR);
    $("#OS_FR").text(maneu_vision.OS_FR);
    $("#OS_ADD").text(maneu_vision.OS_ADD);
    $("#OS_BCVA").text(maneu_vision.OS_BCVA);
    $("#PD").text(maneu_vision.PD);
    $("#remark").text(maneu_vision.remark);
    $("#function").text(maneu_vision.function);
    upline = Object.keys(maneu_store).length/5
    for (i = 1; i <= upline; i++) {
        $('#store_table').append(
            "<tr>\n" +
            "    <td colspan='2'>\n" +
            "        <span>"+ maneu_store['arg'+i+'0']+"</span>\n" +
            "    </td>\n" +
            "    <td colspan='2'>\n" +
            "        <span>"+ maneu_store['arg'+i+'1']+"</span>\n" +
            "    </td>\n" +
            "    <td colspan='2'>\n" +
            "        <span>"+ maneu_store['arg'+i+'2']+"</span>\n" +
            "    </td>\n" +
            "    <td colspan='2'>\n" +
            "        <span>"+ maneu_store['arg'+i+'3']+"</span>\n" +
            "    </td>\n" +
            "    <td>\n" +
            "        <span>"+ maneu_store['arg'+i+'4']+"</span>\n" +
            "    </td>\n" +
            "</tr>\n")
    }
    $('.submit').click(function () {
        $(this).parent().parent().parent().hide()
        $.ajax({
            url: service_delete,
            type: 'GET',
            data: {'server_id': $(this).attr('rel')},
            success: function (res) {
            }
        })
    })
    $('#serverInsertButton').click(function () {
        content = $('#serverInsert').serializeJsonStr()
        csrf_token = $('[name="csrfmiddlewaretoken"]').val();

        $.ajax({
            url: serverInsertUrl,
            type: 'POST',
            data: {
                'csrfmiddlewaretoken': csrf_token,
                'content': content
            },
            success: function (res) {
                $('#serverTable').prepend(
                    "<tr>\n" +
                    "    <td>\n" +
                    "        <span>"+ res.data.time +"</span>\n" +
                    "    </td>\n" +
                    "    <td>\n" +
                    "        <span>"+ res.data.content +"</span>\n" +
                    "    </td>\n" +
                    "    <td>\n" +
                    "        <div class='col-6 offset-6 input-group input-group-sm'>\n" +
                    "            <input type='button' class='btn btn-danger delete submit' value='删除' rel="+ res.data.id +">\n" +
                    "        </div>" +
                    "    </td>\n" +
                    "</tr>\n"
                )
            }
        })
    })
})
