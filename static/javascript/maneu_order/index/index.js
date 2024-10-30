$(function () {
    var start = moment().subtract(29, 'days');
    var end = moment();

    function forList(res) {
        for (i in res) {
            $('#body').append(
                "<div class='col-12 row'>\n" +
                "    <div class='col-2'>\n" +
                "        <span>" + res[i]['time'] + "</span>\n" +
                "    </div>\n" +
                "    <div class='col-1'>\n" +
                "        <span>" + res[i]['name'] + "</span>\n" +
                "    </div>\n" +
                "    <div class='col-1'>\n" +
                "        <span>" + res[i]['phone'] + "</span>\n" +
                "    </div>\n" +
                "    <div class='col-6'>\n" +
                "        <span>" + res[i]['remark'] + "</span>\n" +
                "    </div>\n" +
                "    <div class='col-2 row' align='right'>\n" +
                "        <form class='col-6'>\n" +
                "            <div class='col-12 input-group input-group-sm'>\n" +
                "                <input type='button' class='btn btn-danger col-12' onclick='deleteBtn(this)' value='删除' alt=" + res[i]['id'] + ">\n" +
                "            </div>\n" +
                "        </form>\n" +
                "        <form class='col-6' method='get' action=" + api_detail + " >\n" +
                "            <input type='hidden' name='order_id' value=" + res[i]['id'] + ">\n" +
                "            <div class='col-12 input-group input-group-sm'>\n" +
                "                <input type='submit' class='btn btn-primary col-12' value='查看'>\n" +
                "            </div>\n" +
                "        </form>\n" +
                "    </div>\n" +
                "</div>\n" +
                "<hr style='color: white'>\n"
            )
        }
    }

    function cb(start, end) {
        $('#reportrange span').html(start.format('MMMM D, YYYY') + ' - ' + end.format('MMMM D, YYYY'));
        $('#body').empty();
        $.ajax({
            url: api_index, data: {
                start: start.format('YYYY-MM-DD 00:00:00'), end: end.format('YYYY-MM-DD 23:59:59')
            }, success: function (res) {
                forList(res.data)
            },
        });
    }

    $('#search-value').keyup(function () {
        $('#body').empty()
        $.ajax({
            url: api_search, data: {
                text: $('#search-value').val()
            }, success: function (res) {
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
