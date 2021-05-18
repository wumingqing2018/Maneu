$(document).ready(function () {
    $('#sphere').change(function () {
        $('#sphere_msg').html($('#sphere').val())
    })
    $('#astigmatic').change(function () {
        $('#astigmatic_msg').html($('#astigmatic').val())
    })
    $('#count').change(function () {
        $('#count_msg').html($('#count').val())
    })
    $('#refraction').change(function () {
        $('#refraction_msg').html($('#refraction').val())
    })
    $('#pd').change(function () {
        $('#pd_msg').html($('#pd').val())
    })
    $("#add").change(function () {
        $('#add_msg').html($('#add').val())
    })
    $('#deviation').change(function () {
        $('#deviation_msg').html($('#deviation').val())
    })
})
