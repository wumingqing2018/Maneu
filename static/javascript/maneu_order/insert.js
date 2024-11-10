$(document).ready(function (){
    $('#insert').click(function () {
        $.ajax({
            url: api_insert,
            method: 'GET',
            data: {
                name: $('#name').val(),
                time: $('#time').val(),
                call: $('#call').val(),
                guest: $('#guest').serializeJsonStr(),
                store: $('#store').serializeJsonStr(),
                report: $('#report').serializeJsonStr(),
                remark: $('#remark').val(),
            },
            success: function (res) {
                console.log(res)
            }
        })
    });
});
