$(document).ready(function () {
    detail_report(function (data) {
        console.log(data)
        guest_id = data.data.guest_id
        if (data.status === true) {
            detail_guest(function (data) {
                console.log(data)
            })
        }
    })
    $('#delete').click(function () {
        if (confirm("确定要删除记录吗？")) {
            delete_report(function (data) {
                if (data === true) {
                    delete_order(function (data) {
                        if (data === true) {
                            alert('删除成功')
                            window.location.href = index
                        } else {
                            alert(data.message)
                        }
                    })
                } else {
                    alert(data.message)
                }
            })
        } else {
            return false;
        }
    })
    $('#update').click(function () {
        if (confirm("确定要修改记录吗？")) {
            update_guest(function (data) {
                if (data.status === true) {
                    update_report(function (data) {
                                if (data.status === true) {
                                    alert('修改成功')
                                } else {
                                    alert(data.message)
                                }
                    })
                } else {
                    alert(data.message)
                }
            })
        } else {
            return false;
        }
    })


    function detail_guest(callback) {
        $.ajax({
            url: guest_detail,
            data: {
                'id': guest_id
            },
            success: function (res) {
                content = res.data
                $('#name').val(content.name)
                $('#call').val(content.phone)
                $('#age').val(content.age)
                $('#DFH').val(content.dfh)
                $('#EM').val(content.em)
                $('#OT').val(content.ot)
                $('#sex').val(content.sex)
                callback(res); // 第一个参数为null表示没有错误，第二个参数为请求的数据
            },
            error: function (res) {
                callback(false); // 第一个参数为null表示没有错误，第二个参数为请求的数据
            }
        })
    }

    function detail_report(callback) {
        $.ajax({
            url: report_detail,
            data: {
                'id': report_id
            },
            success: function (res) {
                $('#time').val(res.data.time)
                content = JSON.parse(res.data.content)
                $('#PD').val(content.PD)
                $('#PLAN').val(content.PLAN)
                $('#OD_AD').val(content.OD.AD)
                $('#OD_ADD').val(content.OD.ADD)
                $('#OD_AK').val(content.OD.AK)
                $('#OD_AL').val(content.OD.AL)
                $('#OD_BC').val(content.OD.BC)
                $('#OD_CCT').val(content.OD.CCT)
                $('#OD_CYL').val(content.OD.CYL)
                $('#OD_FR').val(content.OD.FR)
                $('#OD_LT').val(content.OD.LT)
                $('#OD_PR').val(content.OD.PR)
                $('#OD_SPH').val(content.OD.SPH)
                $('#OD_VA').val(content.OD.VA)
                $('#OD_VT').val(content.OD.VT)

                $('#OS_AD').val(content.OS.AD)
                $('#OS_ADD').val(content.OS.ADD)
                $('#OS_AK').val(content.OS.AK)
                $('#OS_AL').val(content.OS.AL)
                $('#OS_BC').val(content.OS.BC)
                $('#OS_CCT').val(content.OS.CCT)
                $('#OS_CYL').val(content.OS.CYL)
                $('#OS_FR').val(content.OS.FR)
                $('#OS_LT').val(content.OS.LT)
                $('#OS_PR').val(content.OS.PR)
                $('#OS_SPH').val(content.OS.SPH)
                $('#OS_VA').val(content.OS.VA)
                $('#OS_VT').val(content.OS.VT)
                callback(res); // 第一个参数为null表示没有错误，第二个参数为请求的数据
            },
            error: function (res) {
                callback(false); // 第一个参数为null表示没有错误，第二个参数为请求的数据
            }
        })
    }

    function delete_report(callback) {
        $.ajax({
            url: report_delete,
            data: {
                'id': report_id
            },
            success: function (res) {
                callback(res)
            },
            error: function () {
                callback({"status": false, 'message': 'order,网络出错'})
            }
        })
    }

    function update_guest(callback) {
        $.ajax({
            url: guest_update,
            method: 'GET',
            data: {
                guest_id: guest_id,
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
                callback(res)
            },
            error: function () {
                callback({"status": false, 'message': 'guest,网络出错'})
            }
        })
    }

    function update_report(callback) {
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
            url: report_update,
            method: "GET",
            data: {
                report_id: report_id,
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
                callback({"status": false, 'message': 'report,网络出错'})
            }
        })
    }
});
