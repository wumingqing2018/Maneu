$(document).ready(function () {
    $('#insert').click(function () {
        guest_insert(function (data) {
            if (data.status === true){
                console.log(data.data.id)
                report_insert(data.data.id,function (data) {
                    if (data.status === true){
                        window.location.href = index_api
                    }else {
                        alert(data.message)
                    }
                })
            }else {
                alert(data.message)
            }
        });
    })

    function guest_insert(callback) {
        $.ajax({
            url: guest_api,
            method: "GET",
            data: {
                time: $("#time").val(),
                name: $("#name").val(),
                call: $("#call").val(),
            },
            success: function (res) {
                callback(res); // 第一个参数为null表示没有错误，第二个参数为请求的数据
            },
            error: function (res) {
                callback(false); // 第一个参数为null表示没有错误，第二个参数为请求的数据
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
                callback(false); // 第一个参数为null表示没有错误，第二个参数为请求的数据
            }
        })
    }
})