$(function () {
    var start = moment().subtract(29, 'days');
    var end = moment();

    function cb(start, end) {
        $('#reportrange span').html(start.format('MMMM D, YYYY') + ' - ' + end.format('MMMM D, YYYY'));
        $('#body').empty();
        $.ajax({
            url: api_index,
            data: {
                star: start.format('YYYY-MM-DD'),
                end: end.format('YYYY-MM-DD')
            },
            success: function (res){
                console.log(res)
            },
        });
    }

    $('#reportrange').daterangepicker({
            startDate: start,
            endDate: end,
            ranges: {
                '今天': [moment(), moment()],
                '昨天': [moment().subtract(1, 'days'), moment().subtract(1, 'days')],
                '七天内': [moment().subtract(6, 'days'), moment()],
                '三十天内': [moment().subtract(29, 'days'), moment()],
                '本月': [moment().startOf('month'), moment().endOf('month')],
                '上月': [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')]
            }
        },
        cb);
    cb(start, end);
});
