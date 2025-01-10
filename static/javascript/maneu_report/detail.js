
$(document).ready(function () {
    report_detail()
    $('#delete').click(report_delete)
    $('#update').click(report_update)

    function report_detail() {
        $.ajax({
            url: api_detail,
            method: 'GET',
            data: {
                id: id
            },
            success: function (res) {
                if (res.status === true) {
                    data = res.data
                    content = $.parseJSON(data.content)

                    $("#time").val(data.time)
                    $("#name").val(data.name)
                    $("#phone").val(data.phone)
                    $("#remark").val(data.remark)
                    $("#PD").val(content.PD)
                    $("#PLAN").val(content.PLAN)

                    $("#OD_VA").val(content.OD.VA)
                    $("#OD_SPH").val(content.OD.SPH)
                    $("#OD_CYL").val(content.OD.CYL)
                    $("#OD_AX").val(content.OD.AX)
                    $("#OD_PR").val(content.OD.PR)
                    $("#OD_FR").val(content.OD.FR)
                    $("#OD_ADD").val(content.OD.ADD)
                    $("#OD_AL").val(content.OD.AL)
                    $("#OD_AK").val(content.OD.AK)
                    $("#OD_AD").val(content.OD.AD)
                    $("#OD_CCT").val(content.OD.CCT)
                    $("#OD_LT").val(content.OD.LT)
                    $("#OD_VT").val(content.OD.VT)
                    $("#OD_BC").val(content.OD.BC)

                    $("#OS_VA").val(content.OS.VA)
                    $("#OS_SPH").val(content.OS.SPH)
                    $("#OS_CYL").val(content.OS.CYL)
                    $("#OS_AX").val(content.OS.AX)
                    $("#OS_PR").val(content.OS.PR)
                    $("#OS_FR").val(content.OS.FR)
                    $("#OS_ADD").val(content.OS.ADD)
                    $("#OS_AL").val(content.OS.AL)
                    $("#OS_AK").val(content.OS.AK)
                    $("#OS_AD").val(content.OS.AD)
                    $("#OS_CCT").val(content.OS.CCT)
                    $("#OS_LT").val(content.OS.LT)
                    $("#OS_VT").val(content.OS.VT)
                    $("#OS_BC").val(content.OS.BC)
                } else {
                    alert('获取订单失败，即将返回上一页。');
                    window.location.href = api_index
                }
            },
        })
    }
    function report_delete() {
        if (confirm("确定要删除吗？")) {
            $.ajax({
                url:api_delete,
                method: 'GET',
                data: {
                    id: id
                },
                success: function (res) {
                    if (res.status === true) {
                        alert('删除成功，即将返回上一页。')
                        window.location.href = api_index
                    }else {
                        alert('删除失败，请重试。')
                    }
                }
            })
        } else {
            return false;
        }
    }
    function report_update() {
        if (confirm("确定要修改吗？")) {
            content = {
                PLAN: $("#PLAN").val(),
                PD: $("#PD").val(),
                OD: {
                    'VA': $("#OD_VA").val(),
                    'SPH': $("#OD_SPH").val(),
                    'CYL': $("#OD_CYL").val(),
                    'AX': $("#OD_AX").val(),
                    'PR': $("#OD_PR").val(),
                    'FR': $("#OD_FR").val(),
                    'ADD': $("#OD_ADD").val(),
                    'AL': $("#OD_AL").val(),
                    'AK': $("#OD_AK").val(),
                    'AD': $("#OD_AD").val(),
                    'CCT': $("#OD_CCT").val(),
                    'LT': $("#OD_LT").val(),
                    'VT': $("#OD_VT").val(),
                    'BC': $("#OD_BC").val(),
                },
                OS: {
                    'VA': $("#OS_VA").val(),
                    'SPH': $("#OS_SPH").val(),
                    'CYL': $("#OS_CYL").val(),
                    'AX': $("#OS_AX").val(),
                    'PR': $("#OS_PR").val(),
                    'FR': $("#OS_FR").val(),
                    'ADD': $("#OS_ADD").val(),
                    'AL': $("#OS_AL").val(),
                    'AK': $("#OS_AK").val(),
                    'AD': $("#OS_AD").val(),
                    'CCT': $("#OS_CCT").val(),
                    'LT': $("#OS_LT").val(),
                    'VT': $("#OS_VT").val(),
                    'BC': $("#OS_BC").val(),
                },
            }
            $.ajax({
                url: api_update,
                method: "GET",
                data: {
                    report_id: id,
                    time: $("#time").val(),
                    name: $("#name").val(),
                    call: $("#call").val(),
                    remark: $("#remark").val(),
                    content: JSON.stringify(content)
                },
                success: function (res) {
                    if (res.status === true){
                        alert('更新成功')
                    }else {
                        alert('更新失败')
                    }
                },
            })
        } else {
            return false;
        }
    }
})
