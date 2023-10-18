function LoadContent(res) {
    for (i in res){
        $('#body').append(
            "                <tr>\n" +
            "                    <td valign='middle'>\n" +
            "                        <span>"+ res[i]['time'] +"</span>\n" +
            "                    </td>\n" +
            "                    <td valign='middle'>\n" +
            "                        <span>"+ res[i]['name'] +"</span>\n" +
            "                    </td>\n" +
            "                    <td valign='middle'>\n" +
            "                        <span>"+ res[i]['phone'] +"</span>\n" +
            "                    </td>\n" +
            "                    <td valign='middle'>\n" +
            "                        <span>999</span>\n" +
            "                    </td>\n" +
            "                    <td valign='middle' align='right'>\n" +
            "                        <div class='col-6 row'>\n" +
            "                            <form class='col-6'>\n" +
            "                                <div class='col-6 input-group input-group-sm'>\n" +
            "                                    <input type='button' class='btn btn-danger col-12' onclick='deleteBtn(this)' alt="+ res[i]['id'] +" value='删除'>\n" +
            "                                </div>\n" +
            "                            </form>\n" +
            "                            <form class='col-6' method='get' action="+ api_detail +" >\n" +
            "                                <input type='hidden' name='order_id' value="+ res[i]['id'] +">\n" +
            "                                <div class='input-group input-group-sm'>\n" +
            "                                    <input type='submit' class='btn btn-primary col-12' value='查看'>\n" +
            "                                </div>\n" +
            "                            </form>\n" +
            "                        </div>\n" +
            "                    </td>\n" +
            "                </tr>\n"
        )
    }
}
function deleteBtn(obj){
    if (confirm("您确定要删除吗？")) {
        $.ajax({
            url: api_delete,
            type: 'GET',
            data: {
                order_id :obj.alt,
            },
            success: function (res) {
                obj.parentElement.parentElement.parentElement.parentElement.parentElement.remove()
            }
        })
    } else {
        return false;
    }
}
$(function() {
    $.ajax({
        url: api_index,
        data: {
            star: today,
            end: today,
        },
        success: function (res){
            LoadContent(res);
        }
    });
    $('input[name="daterange"]').daterangepicker({
        opens:'center',
        locale:{format:'YYYY-MM-DD'}
    }, function(start, end, label) {
        $('#body').empty()
        $.ajax({
            url: api_index,
            data: {
                star: start.format('YYYY-MM-DD'),
                end: end.format('YYYY-MM-DD')
            },
            success: function (res){
                LoadContent(res);
            }
        })
    });
    $('input[name="search-value"]').keyup(function () {
        $('#body').empty()
        $.ajax({
            url: api_search,
            data: {
                text: $('input[name="search-value"]').val()
            },
            success: function (res){
                LoadContent(res);
            }
        })
    })
});
