$(document).ready(function (){
    $("#c_name").blur(function(){
        var c_name = $('#c_name').val();
        if (c_name == '') {
            $('#username_error').text('请输入单号');
        }
        else if (isNaN(c_name)) {
            $('#username_error').text('单号由数字构成');
        }
        else {
            alert(c_name);
        }
    });
    $("#c_name").focus(function(){
        var c_name = $('#c_name').val();
        if (c_name == '') {
            $('#username_error').text('请输入单号');
        }
        else if (isNaN(c_name)) {
            $('#username_error').text('单号由数字构成');
        }
        else {
            alert(c_name);
        }
    })
})
