$(document).ready(function (){
    $('#insert').click(function () {
        $.ajax({
            url: api_insert,
            method: 'GET',
            data: {
                name: $('#name').val(),
                time: $('#time').val(),
                call: $('#call').val(),
                remark: $('#remark').val(),
                guest: $('#guest').serializeJsonStr(),
                store: $('#store').serializeJsonStr(),
                report: $('#report').serializeJsonStr(),
            },
            success: function (res) {
                console.log(res)
            }
        })
    });
});
