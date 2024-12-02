$(document).ready(function () {
    $('#insert').click(function () {
        console.log( $("#content").serializeJsonStr())
        $.ajax({
            url: api_insert,
            method: "GET",
            data: {
                time: $("#time").val(),
                name: $("#name").val(),
                phone: $("#call").val(),
                remark: $("#remark").val(),
                Function: $("[name='function']").val(),
                PD: $("[name='PD']").val(),
                OD: $("#OD").serializeJsonStr(),
                OS: $("#OS").serializeJsonStr(),
            },
            success: function (res) {
                if (res.status === true) {
                    alert("提交成功，可以继续填写")
                }else {
                    alert("提交失败，请确认数据后再次重试")
                }
            }
        })
    })
})