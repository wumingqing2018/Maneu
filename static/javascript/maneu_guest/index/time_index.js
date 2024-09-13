$(function () {
    var start = moment().subtract(29, 'days');
    var end = moment();

    function cb(start, end) {
        $('#reportrange span').html(start.format('MMMM D, YYYY') + ' - ' + end.format('MMMM D, YYYY'));
        $('#body').empty();
        $.ajax({
            url: api_index,
            data: {
                star: start.format('YYYY-MM-DD 00:00:00'),
                end: end.format('YYYY-MM-DD 23:59:59')
            },
            success: function (res) {
                for (i in res) {
                    $('#body').append(
                        "                <tr>\n" +
                        "                    <td valign='middle'>\n" +
                        "                        <span>" + res[i]['time'] + "</span>\n" +
                        "                    </td>\n" +
                        "                    <td valign='middle'>\n" +
                        "                        <span>" + res[i]['name'] + "</span>\n" +
                        "                    </td>\n" +
                        "                    <td valign='middle'>\n" +
                        "                        <span>" + res[i]['phone'] + "</span>\n" +
                        "                    </td>\n" +
                        "                    <td valign='middle' colspan=\"2\">\n" +
                        "                        <span>" + res[i]['remark'] + "</span>\n" +
                        "                    </td>\n" +
                        "                    <td valign='middle' align='right'>\n" +
                        "                        <div class='col-6 row'>\n" +
                        "                            <form class='col-6'>\n" +
                        "                                <div class='col-6 input-group input-group-sm'>\n" +
                        "                                    <input type='button' class='btn btn-danger col-12' onclick='deleteBtn(this)' alt=" + res[i]['id'] + " value='删除'>\n" +
                        "                                </div>\n" +
                        "                            </form>\n" +
                        "                            <form class='col-6' method='get' action=" + api_detail + " >\n" +
                        "                                <input type='hidden' name='guess_id' value=" + res[i]['id'] + ">\n" +
                        "                                <div class='input-group input-group-sm'>\n" +
                        "                                    <input type='submit' class='btn btn-primary col-12' value='查看'>\n" +
                        "                                </div>\n" +
                        "                            </form>\n" +
                        "                        </div>\n" +
                        "                    </td>\n" +
                        "                </tr>\n"
                    )
                }
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
    }, cb);
    cb(start, end);
});
