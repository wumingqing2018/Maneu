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
    $('#insert').click(function () {
        $('#order_name').val($('#name').val())
        $('#order_time').val($('#time').val())
        $('#order_phone').val($('#phone').val())
        $('#order_remark').val($('#remark').val())

        guess = $('#guess').serializeJsonStr();
        $('#guess_form').val(guess);
        vision = $('#vision').serializeJsonStr();
        $('#vision_form').val(vision);
        product = $('#product').serializeJsonStr();
        $('#product_form').val(product);
    });
});
