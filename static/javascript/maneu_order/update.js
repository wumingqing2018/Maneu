$(document).ready(function () {
    $("input[name='OD_VA']").val(vision.OD_VA)
    $("input[name='OD_SPH']").val(vision.OD_SPH)
    $("input[name='OD_CYL']").val(vision.OD_CYL)
    $("input[name='OD_AX']").val(vision.OD_AX)
    $("input[name='OD_PR']").val(vision.OD_PR)
    $("input[name='OD_FR']").val(vision.OD_FR)
    $("input[name='OD_ADD']").val(vision.OD_ADD)
    $("input[name='OD_BCVA']").val(vision.OD_BCVA)
    $("input[name='OS_VA']").val(vision.OS_VA)
    $("input[name='OS_SPH']").val(vision.OS_SPH)
    $("input[name='OS_CYL']").val(vision.OS_CYL)
    $("input[name='OS_AX']").val(vision.OS_AX)
    $("input[name='OS_PR']").val(vision.OS_PR)
    $("input[name='OS_FR']").val(vision.OS_FR)
    $("input[name='OS_ADD']").val(vision.OS_ADD)
    $("input[name='OS_BCVA']").val(vision.OS_BCVA)
    $("input[name='PD']").val(vision.PD)
    $("input[name='remark']").val(vision.remark)
    $("input[name='function']").val(vision.function)

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
