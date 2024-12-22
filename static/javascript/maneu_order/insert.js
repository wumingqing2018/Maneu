$(document).ready(function () {
    $('#insert').click(function () {
        guest_insert()
        store_insert()
        report_insert()
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

    function store_insert(){
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
            url: store,
            method: 'GET',
            data: {
                remark: $("#remark").val(),
                time: $("#time").val(),
                name: $("#name").val(),
                call: $("#call").val(),
                guest_id: guest_id,
                store: JSON.stringify(store),
            },
            success: function (res) {
                console.log(res)
            }
        })
    }

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
                    console.log(res)
                    guest_id = res.data
                } else {
                    alert("提交失败" + res.message)
                }
            }
        })
    }

    function report_insert() {
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
                time: $("#time").val(),
                name: $("#name").val(),
                call: $("#call").val(),
                remark: $("#remark").val(),
                content: JSON.stringify(content)
            },
            success: function (res) {
                console.log(res)
                if (res.status === true) {
                    console.log(res)
                                        report_id = res.data
                } else {
                    alert("提交失败，请确认数据后再次重试")
                }
            }
        })
    }
});
