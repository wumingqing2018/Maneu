$(document).ready(function () {
    report_hide()
    guest_hide()
    $('#guest_hide').click(function () {
        guest_hide()
    })
    $('#guest_show').click(function (){
        guest_show()
    })
    $('#report_hide').click(function () {
        report_hide()
    })
    $('#report_show').click(function (){
        report_show()
    })

    $('#insert').click(function () {
        guest_insert(function (data) {
            console.log(data)
            if (data.status === true){
                guest_id = data.data.id
                report_insert(guest_id,function (data) {
                    console.log(data)
                    if (data.status === true){
                        report_id = data.data.id
                        order_insert(guest_id,report_id,function (data) {
                            console.log(data)
                            if (confirm("提交成功是否继续填写？")) {
                                window.location.href = web_insert
                            } else {
                                window.location.href = web_index
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
                callback(res); // 第一个参数为null表示没有错误，第二个参数为请求的数据
            },
            error: function (res) {
                callback({'status':false, 'message': '请求出错请刷新页面'}); // 第一个参数为null表示没有错误，第二个参数为请求的数据
            }
        })
    }
    function order_insert(guest_id, report_id, callback) {
        store = []
        $(".store").each(function () {
            data = {
                arg10: $(this).find(".arg10").val(),
                arg11: $(this).find(".arg11").val(),
                arg12: $(this).find(".arg12").val(),
                arg13: $(this).find(".arg13").val(),
                arg14: $(this).find(".arg14").val(),
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
                callback(res); // 第一个参数为null表示没有错误，第二个参数为请求的数据
            },
            error: function (res) {
                callback({'status':false, 'message': '请求出错请刷新页面'}); // 第一个参数为null表示没有错误，第二个参数为请求的数据
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
                callback(res); // 第一个参数为null表示没有错误，第二个参数为请求的数据
            },
            error: function (res) {
                callback({'status':false, 'message': '请求出错请刷新页面'}); // 第一个参数为null表示没有错误，第二个参数为请求的数据
            }
        })
    }
    function report_hide() {
        $("#report_hide").hide()
        $("#report_show").show()
        $("#OD_VA").hide()
        $("#OD_PR").hide()
        $("#OD_FR").hide()
        $("#OD_AL").hide()
        $("#OD_AK").hide()
        $("#OD_AD").hide()
        $("#OD_CCT").hide()
        $("#OD_LT").hide()
        $("#OD_VT").hide()
        $("#OD_BC").hide()
        $("#OS_VA").hide()
        $("#OS_PR").hide()
        $("#OS_FR").hide()
        $("#OS_AL").hide()
        $("#OS_AK").hide()
        $("#OS_AD").hide()
        $("#OS_CCT").hide()
        $("#OS_LT").hide()
        $("#OS_VT").hide()
        $("#OS_BC").hide()
    }
    function report_show() {
        $("#report_hide").show()
        $("#report_show").hide()
        $("#OD_VA").show()
        $("#OD_PR").show()
        $("#OD_FR").show()
        $("#OD_AL").show()
        $("#OD_AK").show()
        $("#OD_AD").show()
        $("#OD_CCT").show()
        $("#OD_LT").show()
        $("#OD_VT").show()
        $("#OD_BC").show()
        $("#OS_VA").show()
        $("#OS_PR").show()
        $("#OS_FR").show()
        $("#OS_AL").show()
        $("#OS_AK").show()
        $("#OS_AD").show()
        $("#OS_CCT").show()
        $("#OS_LT").show()
        $("#OS_VT").show()
        $("#OS_BC").show()
    }
    function guest_hide() {
        $("#guest_hide").hide()
        $("#guest_show").show()
        $("#guest_content").hide()
    }
    function guest_show() {
        $("#guest_hide").show()
        $("#guest_show").hide()
        $("#guest_content").show()
    }
});
