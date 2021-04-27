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
            $('#username_error').text('');
        }
    });
    $("#c_phone").blur(function(){
        var c_phone = $('#c_phone').val();

        if (c_phone == '') {
            $('#c_phone_error').text('请输入单号');
        }
        else if (isNaN(c_phone)) {
            $('#c_phone_error').text('单号由数字构成');
        }
        else {
            $('#c_phone_error').text('');
        }
    });
    $("#frame").blur(function(){
        var frame = $('#frame').val();

        if (frame == '') {
            $('#frame_error').text('请输入单号');
        }
        else if (isNaN(frame)) {
            $('#frame_error').text('单号由数字构成');
        }
        else {
            $('#frame_error').text('');
        }
    });
    $("#r_glasses").blur(function(){
        var r_glasses = $('#r_glasses').val();

        if (r_glasses == '') {
            $('#r_glasses_error').text('请输入单号');
        }
        else if (isNaN(r_glasses)) {
            $('#r_glasses_error').text('单号由数字构成');
        }
        else {
            $('#r_glasses_error').text('');
        }
    });
    $("#r_sphere").blur(function(){
        var r_sphere = $('#r_sphere').val();

        if (r_sphere == '') {
            $('#r_sphere_error').text('请输入单号');
        }
        else if (isNaN(r_sphere)) {
            $('#r_sphere_error').text('单号由数字构成');
        }
        else {
            $('#r_sphere_error').text('');
        }
    });
    $("#r_astigmatic").blur(function(){
        var r_astigmatic = $('#r_astigmatic').val();

        if (r_astigmatic == '') {
            $('#r_astigmatic_error').text('请输入单号');
        }
        else if (isNaN(r_astigmatic)) {
            $('#r_astigmatic_error').text('单号由数字构成');
        }
        else {
            $('#r_astigmatic_error').text('');
        }
    });
    $("#r_deviation").blur(function(){
        var r_deviation = $('#r_deviation').val();

        if (r_deviation == '') {
            $('#r_deviation_error').text('请输入单号');
        }
        else if (isNaN(r_deviation)) {
            $('#r_deviation_error').text('单号由数字构成');
        }
        else {
            $('#r_deviation_error').text('');
        }
    });
    $("#r_add").blur(function(){
        var r_add = $('#r_add').val();

        if (r_add == '') {
            $('#r_add_error').text('请输入单号');
        }
        else if (isNaN(r_add)) {
            $('#r_add_error').text('单号由数字构成');
        }
        else {
            $('#r_add_error').text('');
        }
    });
    $("#r_pd").blur(function(){
        var r_pd = $('#r_pd').val();

        if (r_pd == '') {
            $('#r_pd_error').text('请输入单号');
        }
        else if (isNaN(r_pd)) {
            $('#r_pd_error').text('单号由数字构成');
        }
        else {
            $('#r_pd_error').text('');
        }
    });
    $("#l_glasses").blur(function(){
        var l_glasses = $('#l_glasses').val();

        if (l_glasses == '') {
            $('#l_glasses_error').text('请输入单号');
        }
        else if (isNaN(l_glasses)) {
            $('#l_glasses_error').text('单号由数字构成');
        }
        else {
            $('#l_glasses_error').text('');
        }
    });
    $("#l_sphere").blur(function(){
        var l_sphere = $('#l_sphere').val();

        if (l_sphere == '') {
            $('#l_sphere_error').text('请输入单号');
        }
        else if (isNaN(l_sphere)) {
            $('#l_sphere_error').text('单号由数字构成');
        }
        else {
            $('#l_sphere_error').text('');
        }
    });
    $("#l_astigmatic").blur(function(){
        var l_astigmatic = $('#l_astigmatic').val();

        if (l_astigmatic == '') {
            $('#l_astigmatic_error').text('请输入单号');
        }
        else if (isNaN(l_astigmatic)) {
            $('#l_astigmatic_error').text('单号由数字构成');
        }
        else {
            $('#l_astigmatic_error').text('');
        }
    });
    $("#l_deviation").blur(function(){
        var l_deviation = $('#l_deviation').val();

        if (l_deviation == '') {
            $('#l_deviation_error').text('请输入单号');
        }
        else if (isNaN(l_deviation)) {
            $('#l_deviation_error').text('单号由数字构成');
        }
        else {
            $('#l_deviation_error').text('');
        }
    });
    $("#l_add").blur(function(){
        var l_add = $('#l_add').val();

        if (l_add == '') {
            $('#l_add_error').text('请输入单号');
        }
        else if (isNaN(l_add)) {
            $('#l_add_error').text('单号由数字构成');
        }
        else {
            $('#l_add_error').text('');
        }
    });
    $("#l_pd").blur(function(){
        var l_pd = $('#l_pd').val();

        if (l_pd == '') {
            $('#l_pd_error').text('请输入单号');
        }
        else if (isNaN(l_pd)) {
            $('#l_pd_error').text('单号由数字构成');
        }
        else {
            $('#l_pd_error').text('');
        }
    });

})

