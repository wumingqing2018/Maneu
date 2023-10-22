$(function() {
    var start =moment().subtract(29, 'days');
    var end =moment();
    function cb(start, end) {
        $('#reportrange span').html(start.format('MMMM D, YYYY') +' - '+end.format('MMMM D, YYYY'));
        $('#body').empty();
        $.ajax({
            url: api_index,
            data: {
                star: start.format('YYYY-MM-DD'),
                end: end.format('YYYY-MM-DD')
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
                        "                    <td valign='middle'>\n" +
                        "                        <span>999</span>\n" +
                        "                    </td>\n" +
                        "                    <td valign='middle' align='right'>\n" +
                        "                        <div class='col-6 row'>\n" +
                        "                            <form class='col-6'>\n" +
                        "                                <div class='col-6 input-group input-group-sm'>\n" +
                        "                                    <input type='button' class='btn btn-danger col-12' onclick='deleteBtn(this)' alt=" + res[i]['id'] + " value='删除'>\n" +
                        "                                </div>\n" +
                        "                            </form>\n" +
                        "                            <form class='col-6' method='get' action=" + api_detail + " >\n" +
                        "                                <input type='hidden' name='order_id' value=" + res[i]['id'] + ">\n" +
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
            'Today': [moment(), moment()],
            'Yesterday': [moment().subtract(1, 'days'), moment().subtract(1, 'days')],
            'Last 7 Days': [moment().subtract(6, 'days'), moment()],
            'Last 30 Days': [moment().subtract(29, 'days'), moment()],
            'This Month': [moment().startOf('month'), moment().endOf('month')],
            'Last Month': [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')]
        }
    }, cb);
    cb(start, end);
});
