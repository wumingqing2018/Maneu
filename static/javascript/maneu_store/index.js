$(function () {
    var start = moment().subtract(29, 'days');
    var end = moment();

    function forList(res) {
        $('#body').empty();
        console.log(res)
        for (i in res) {
            $('#body').append(
                "<div>\n" +
                "    <div class='col-12 row'>\n" +
                "        <div class='col-2'>\n" +
                "            <p>" + res[i]['time'] + "</p>\n" +
                "        </div>\n" +
                "        <div class='col-1'>\n" +
                "            <p>" + res[i]['name'] + "</p>\n" +
                "        </div>\n" +
                "        <div class='col-1'>\n" +
                "            <p>" + res[i]['phone'] + "</p>\n" +
                "        </div>\n" +
                "        <div class='col-7'>\n" +
                "            <p>" + res[i]['remark'] + "</p>\n" +
                "        </div>\n" +
                "        <div class='col-1'>\n" +
                "            <form method='GET' action='" + detail + "'>\n" +
                "                <input type='hidden' name='id' value=" + res[i]['id'] + ">\n" +
                "                <div class='input-group input-group-sm'>\n" +
                "                    <input type='submit' class='col-12 btn btn-primary' value='查看订单'>\n" +
                "                </div>\n" +
                "            </form>\n" +
                "        </div>\n" +
                "    </div>\n" +
                "    <hr style='color: white'>\n" +
                "</div>\n"
            )
        }
    }

    function cb(start, end) {
        $('#reportrange span').html(start.format('MMMM D, YYYY') + ' - ' + end.format('MMMM D, YYYY'));
        $.ajax({
            url: api_index,
            data: {
                start: start.format('YYYY-MM-DD 00:00:00'),
                end: end.format('YYYY-MM-DD 23:59:59'),
            },
            success: function (res) {
                forList(res.data)
            },
        });
    }

    $('#search-value').keyup(function () {
        $.ajax({
            url: api_search,
            data: {
                text: $('#search-value').val()
            },
            success: function (res) {
                forList(res.data)
            }
        })
    })

    $('#reportrange').daterangepicker({
        startDate: start, endDate: end, ranges: {
            '今天': [moment(), moment()],
            '昨天': [moment().subtract(1, 'days'), moment().subtract(1, 'days')],
            '七天内': [moment().subtract(6, 'days'), moment()],
            '三十天内': [moment().subtract(29, 'days'), moment()],
            '本月': [moment().startOf('month'), moment().endOf('month')],
            '上月': [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')]
        }
    }, cb);

    cb(start, end);
});
