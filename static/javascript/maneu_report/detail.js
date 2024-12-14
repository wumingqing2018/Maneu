$(document).ready(function () {
    report_detail();
    $('#delete').click(report_delete)
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
                    console.log(content)
                    $("#time").text(data.time)
                    $("#name").text(data.name)
                    $("#call").text(data.phone)
                    $("#remark").text(data.remark)
                    $("#PD").text(content.PD)
                    $("#function").text(content.Function)
                    $("#OD>.VA").text(content.OD.VA)
                    $("#OD>.SPH").text(content.OD.SPH)
                    $("#OD>.CYL").text(content.OD.CYL)
                    $("#OD>.AX").text(content.OD.AX)
                    $("#OD>.PR").text(content.OD.PR)
                    $("#OD>.FR").text(content.OD.FR)
                    $("#OD>.ADD").text(content.OD.ADD)
                    $("#OD>.AL").text(content.OD.AL)
                    $("#OD>.AK").text(content.OD.AK)
                    $("#OD>.AD").text(content.OD.AD)
                    $("#OD>.CCT").text(content.OD.CCT)
                    $("#OD>.LT").text(content.OD.LT)
                    $("#OD>.VT").text(content.OD.VT)
                    $("#OD>.BC").text(content.OD.BC)


                    $("#OS>.VA").text(content.OS.VA)
                    $("#OS>.SPH").text(content.OS.SPH)
                    $("#OS>.CYL").text(content.OS.CYL)
                    $("#OS>.AX").text(content.OS.AX)
                    $("#OS>.PR").text(content.OS.PR)
                    $("#OS>.FR").text(content.OS.FR)
                    $("#OS>.ADD").text(content.OS.ADD)
                    $("#OS>.AL").text(content.OS.AL)
                    $("#OS>.AK").text(content.OS.AK)
                    $("#OS>.AD").text(content.OS.AD)
                    $("#OS>.CCT").text(content.OS.CCT)
                    $("#OS>.LT").text(content.OS.LT)
                    $("#OS>.VT").text(content.OS.VT)
                    $("#OS>.BC").text(content.OS.BC)
                } else {
                    alert('查看订单失败，即将返回上一页。');
                    history.back()
                }
            },
        })
    }
    function report_delete() {
        $.ajax({
            url:api_delete,
            method: 'GET',
            data: {
                id: id
            },
            success: function (res) {
                console.log(res)
                if (res.status === true) {
                    alert('删除成功，即将返回上一页。')
                    history.back()
                }else {
                    alert('删除失败，请重试。')
                }
            }
        })
    }
})
