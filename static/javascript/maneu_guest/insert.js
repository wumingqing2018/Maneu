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
$(document).ready(function () {
    $("#insert").click(function () {
        $.ajax({
            url: api_insert,
            method: 'GET',
            data: {
                remark: $("[name='remark']").val(),
                time: $("[name='time']").val(),
                name: $("[name='name']").val(),
                call: $("[name='call']").val(),
                age: $("[name='age']").val(),
                sex: $("[name='sex']").val(),
                dfh: $("[name='dfh']").val(),
                ot: $("[name='ot']").val(),
                em: $("[name='em']").val(),
            },
            success: function (res) {
                if(res.status === true){
                    alert('提交成功,返回上一页')
                    window.location.href = web_index
                }else {
                    alert("提交失败" + res.message)
                }
            }
        })
    })
})