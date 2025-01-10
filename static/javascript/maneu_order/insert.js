$(document).ready(function () {
    $('#insert').click(function () {
        guest_insert(function (data) {
            if (data.status === true){
                guest_id = data.data.id
                console.log(guest_id)
                report_insert(guest_id,function (data) {
                    if (data.status === true){
                        report_id = data.data.id
                        console.log(report_id)
                        order_insert(guest_id,report_id,function (data) {
                            order_id = data.data.id
                            console.log(order_id)
                            if (confirm("提交成功是否继续填写？")) {
                                window.location.href = insert_web
                            } else {
                                window.location.href = index_web
                            }
                        })
                    }else {
                        alert('提交失败，错误信息：'+data.message)
                    }
                })
            }else {
                alert('提交失败，错误信息：'+data.message)
            }
        });
    });

    function order_insert(guest_id, report_id, callback) {
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
                content: JSON.stringify(store),
                remark: $("#remark").val(),
                time: $("#time").val(),
                name: $("#name").val(),
                call: $("#call").val(),
                guest_id: guest_id,
                report_id: report_id,
            },
            success: function (res) {
                console.log(res)
                if (res.status === true){
                    callback(res.data.id); // 第一个参数为null表示没有错误，第二个参数为请求的数据
                }else {
                    callback(null); // 第一个参数为null表示没有错误，第二个参数为请求的数据
                }
            },
            error: function (res) {
                callback(null); // 第一个参数为null表示没有错误，第二个参数为请求的数据
            }
        })
    }
    function guest_insert(callback) {
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
                console.log(res)
                if (res.status === true){
                    callback(res.data.id); // 第一个参数为null表示没有错误，第二个参数为请求的数据
                }else {
                    callback(null); // 第一个参数为null表示没有错误，第二个参数为请求的数据
                }
            },
            error: function (res) {
                callback(null); // 第一个参数为null表示没有错误，第二个参数为请求的数据
            }
        })
    }
    function report_insert(guest_id, callback) {
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
            url: report_api,
            method: "GET",
            data: {
                guest_id: guest_id,
                time: $("#time").val(),
                name: $("#name").val(),
                call: $("#call").val(),
                remark: $("#remark").val(),
                content: JSON.stringify(content)
            },
            success: function (res) {
                console.log(res)
                if (res.status === true){
                    callback(res.data.id); // 第一个参数为null表示没有错误，第二个参数为请求的数据
                }else {
                    callback(null); // 第一个参数为null表示没有错误，第二个参数为请求的数据
                }
            },
            error: function (res) {
                callback(null); // 第一个参数为null表示没有错误，第二个参数为请求的数据
            }
        })
    }
});
