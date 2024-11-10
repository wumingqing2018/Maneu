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
                console.log('d')
            }
        })
    })
})