$(document).ready(function () {
    $('#insert').click(function () {
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
                'BCVA': $("#OD_BC").val(),
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
                'BCVA': $("#OS_BC").val(),
            },
        }
        $.ajax({
            url: api_insert,
            method: "GET",
            data: {
                time: $("#time").val(),
                name: $("#name").val(),
                call: $("#call").val(),
                remark: $("#remark").val(),
                content: JSON.stringify(content)
            },
            success: function (res) {
                if (res.status === true) {
                    alert("提交成功，可以继续填写")
                } else {
                    alert("提交失败，请确认数据后再次重试")
                }
            }
        })
    })
})