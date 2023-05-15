
$(document).ready(function () {
    $("#OD_SPH").text(maneu_vision.OD_SPH);
    $("#OD_CYL").text(maneu_vision.OD_CYL);
    $("#OD_AX").text(maneu_vision.OD_AX);
    $("#OD_PR").text(maneu_vision.OD_PR);
    $("#OD_FR").text(maneu_vision.OD_FR);
    $("#OD_ADD").text(maneu_vision.OD_ADD);
    $("#OD_BCVA").text(maneu_vision.OD_BCVA);
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
            "            <tr>\n" +
            "                <td colspan='2'>\n" +
            "                    <span>"+ maneu_store['arg'+i+'0']+"</span>\n" +
            "                </td>\n" +
            "                <td colspan='2'>\n" +
            "                    <span>"+ maneu_store['arg'+i+'1']+"</span>\n" +
            "                </td>\n" +
            "                <td colspan='2'>\n" +
            "                    <span>"+ maneu_store['arg'+i+'2']+"</span>\n" +
            "                </td>\n" +
            "                <td colspan='2'>\n" +
            "                    <span>"+ maneu_store['arg'+i+'3']+"</span>\n" +
            "                </td>\n" +
            "                <td>\n" +
            "                    <span>"+ maneu_store['arg'+i+'4']+"</span>\n" +
            "                </td>\n" +
            "            </tr>\n")
    }
    $('.submit').click(function () {
        $(this).parent().parent().parent().parent().hide()
        $.ajax({
            url: service_delete,
            type: 'GET',
            data: {'server_id': $(this).attr('rel')},
            success: function (res) {
                $(this).parent().parent().parent().parent().hide()
            }
        })
    })
})
