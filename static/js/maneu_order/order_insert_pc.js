$(document).ready(function () {
    var InputCount=1;
    $("#AddMoreTextBox").click(function (e)
    {
        InputCount++;
        $("#Product_Orders_TABLE").append('    <div class="input-group input-group-sm mb-2">\n' +
            '        <input autocomplete="off" type="text" name="arg'+InputCount+'0" class="form-control" style="width: 12%">\n' +
            '        <input autocomplete="off" type="text" name="arg'+InputCount+'1" class="form-control" style="width: 12%">\n' +
            '        <input autocomplete="off" type="text" name="arg'+InputCount+'2" class="form-control" style="width: 12%">\n' +
            '        <input autocomplete="off" type="text" name="arg'+InputCount+'3" class="form-control" style="width: 52%">\n' +
            '        <input autocomplete="off" type="text" name="arg'+InputCount+'4" class="form-control" style="width: 12%">\n' +
            '    </div>\n' +
            '</div>\n');
    });
    $('#DeleteTextBox').click(function (e) {
        $("#Product_Orders_TABLE>div").last().remove()
    })
    $('#insert').click(function () {
        Product_Orders_json = $('#Product_Orders').serializeJsonStr();
        $('#Product_Orders_json').val(Product_Orders_json);
        Vision_Solutions_json = $('#Vision_Solutions').serializeJsonStr();
        $('#Vision_Solutions_json').val(Vision_Solutions_json);
        order_json = $('#order').serializeJsonStr();
        $('#order_json').val(order_json);
    })
});
