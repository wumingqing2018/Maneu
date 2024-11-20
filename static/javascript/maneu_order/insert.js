$(document).ready(function () {
    $('#insert').click(function () {
        store = []
        $(".store").each(function () {
            data = {
                arg10: $(this).find("[name='arg10']").val(),
                arg11: $(this).find("[name='arg11']").val(),
                arg12: $(this).find("[name='arg12']").val(),
                arg13: $(this).find("[name='arg13']").val(),
                arg14: $(this).find("[name='arg14']").val(),
            };
            store.push(data)
        })
        $.ajax({
            url: order_api,
            method: 'GET',
            data: {
                remark: $("#remark").val(),
                time: $("#time").val(),
                name: $("#name").val(),
                call: $("#call").val(),
                guest_id: guest_id,
                vision_id: vision_id,
                store: JSON.stringify(store),
            }
        })
    });

    function guest_insert() {
        $.ajax({
            url: guest_api,
            method: 'GET',
            data: {
                remark: $("#remark").val(),
                time: $("#time").val(),
                name: $("#name").val(),
                call: $("#call").val(),
                age: $("#age").val(),
                sex: $("#sex").val(),
                DFH: $("#DFH").val(),
                OT: $("#OT").val(),
                EM: $("#EM").val(),
            },
            success: function (res) {
                if (res.status === true) {
                    alert('提交成功,返回上一页')
                    window.location.href = web_index
                } else {
                    alert("提交失败" + res.message)
                }
            }
        })
    }

    function report_insert() {
        $.ajax({
            url: report_api,
            method: "GET",
            data: {
                Function: $("#function").val(),
                time: $("#time").val(),
                name: $("#name").val(),
                phone: $("#call").val(),
                remark: $("#remark").val(),
                PD: $("#PD").val(),
                OD: $("#OD").serializeJsonStr(),
                OS: $("#OS").serializeJsonStr(),
            },
            success: function (res) {
                if (res.status === true) {
                    alert("提交成功，可以继续填写")
                } else {
                    alert("提交失败，请确认数据后再次重试")
                }
            }
        })
    }
});
