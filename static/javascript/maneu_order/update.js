$.fn.serializeJsonStr = function () {
    var o = {};
    var a = this.serializeArray();
    $.each(a, function () {
        if (o[this.name] !== undefined) {
            if (!o[this.name].push) {
                o[this.name] = [o[this.name]];
            }
            o[this.name].push(this.value || '');
        } else {
            o[this.name] = this.value || '';
        }
    });
    return JSON.stringify(o);
}


$(document).ready(function (){
    detail_order(function (data) {
        if (data === true){
            detail_guest(function (data) {
                if (data === true){
                    detail_report(function (data) {
                        console.log(data)
                    })
                }
            })
        }
    })

    $('#delete').click(function () {
        if (confirm("确定要删除记录吗？")) {
            delete_report(function (data) {
            if (data===true){
                delete_order(function (data) {
                    if (data===true){
                        window.location.href = index
                    }
                })
            }
        })
        } else {
            return false;
        }
    })
    $('#update').click(function () {
        if (confirm("确定要修改记录吗？")) {

        } else {
            return false;
        }
    })

    function detail_order(callback){
        $.ajax({
            url: order_detail,
            data: {
                'id': order_id
            },
            success: function (res){
                $('#remark').val(res.data.remark)
                $('#name').val(res.data.name)
                $('#call').val(res.data.phone)
                $('#time').val(res.data.time)
                console.log(res.data.content)
                for (var i = 0; i < res.data.content.length; i++){
                    store = $(".store:eq(" + i + ")")
                    store.find("[name='arg10']").val(res.data.content[i]['arg10'])
                    store.find("[name='arg11']").val(res.data.content[i]['arg11'])
                    store.find("[name='arg12']").val(res.data.content[i]['arg12'])
                    store.find("[name='arg13']").val(res.data.content[i]['arg13'])
                    store.find("[name='arg14']").val(res.data.content[i]['arg14'])
                }

                report_id = res.data.report_id;
                guest_id = res.data.guest_id;
                callback(true); // 第一个参数为null表示没有错误，第二个参数为请求的数据
            },
            error: function (res) {
                callback(false); // 第一个参数为null表示没有错误，第二个参数为请求的数据
            }
        })
    }
    function detail_guest(callback){
        $.ajax({
            url: guest_detail,
            data: {
                'id': guest_id
            },
            success: function (res){
                content = res.data
                console.log(content)
                $('#age').val(content.age)
                $('#dfh').val(content.dfh)
                $('#em').val(content.em)
                $('#ot').val(content.ot)
                $('#sex').val(content.sex)
                callback(true); // 第一个参数为null表示没有错误，第二个参数为请求的数据
            },
            error: function (res) {
                callback(false); // 第一个参数为null表示没有错误，第二个参数为请求的数据
            }
        })
    }
    function detail_report(callback){
        $.ajax({
            url: report_detail,
            data: {
                'id': report_id
            },
            success: function (res){
                content = JSON.parse(res.data.content)
                $('#PD').val(content.PD)
                $('#function').val(content.Function)
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
                callback(true); // 第一个参数为null表示没有错误，第二个参数为请求的数据
            },
            error: function (res) {
                callback(false); // 第一个参数为null表示没有错误，第二个参数为请求的数据
            }
        })
    }

    function delete_order(callback){
        $.ajax({
            url: order_delete,
            data: {
                'id': order_id
            },
            success: function (res){
                callback(true); // 第一个参数为null表示没有错误，第二个参数为请求的数据
            },
            error: function (res) {
                callback(false); // 第一个参数为null表示没有错误，第二个参数为请求的数据
            }
        })
    }
    function delete_report(callback){
        $.ajax({
            url: report_delete,
            data: {
                'id': report_id
            },
            success: function (res){
                callback(true); // 第一个参数为null表示没有错误，第二个参数为请求的数据
            },
            error: function (res) {
                callback(false); // 第一个参数为null表示没有错误，第二个参数为请求的数据
            }
        })
    }

    function update_order(callback){
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
                if (res.status === true){
                    callback(res.data.id); // 第一个参数为null表示没有错误，第二个参数为请求的数据
                }else {
                    callback(''); // 第一个参数为null表示没有错误，第二个参数为请求的数据
                }
            },
            error: function (res) {
                callback(''); // 第一个参数为null表示没有错误，第二个参数为请求的数据
            }
        })
    }
    function update_guest(callback){
        $.ajax({
            url: guest_api,
            method: 'GET',
            data: {
                remark: $("[name='remark']").val(),
                time: $("[name='time']").val(),
                name: $("[name='name']").val(),
                call: $("[name='call']").val(),
                age: $("[name='age']").val(),
                sex: $("[name='sex']").val(),
                DFH: $("[name='DFH']").val(),
                OT: $("[name='OT']").val(),
                EM: $("[name='EM']").val(),
            },
            success: function (res) {
                if(res.status === true){
                    alert('提交成功,返回上一页')
                    window.location.href = guest_index
                }else {
                    alert("提交失败" + res.message)
                }
            }
        })
    }
    function update_report(callback){
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
});
