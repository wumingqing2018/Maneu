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
        guess_form = $('#guess_form').serializeJsonStr();
        subjective_form = $('#subjective_form').serializeJsonStr();
        $("#guess").val(guess_form);
        $("#subjective").val(subjective_form);
    })
})