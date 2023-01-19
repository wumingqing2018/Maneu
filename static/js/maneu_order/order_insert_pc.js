$('#insert').click(function () {
    Product_Orders_json = $('#Product_Orders').serializeJsonStr();
    $('#Product_Orders_json').val(Product_Orders_json);
    Vision_Solutions_json = $('#Vision_Solutions').serializeJsonStr();
    $('#Vision_Solutions_json').val(Vision_Solutions_json);
    order_json = $('#order').serializeJsonStr();
    $('#order_json').val(order_json);
})

var InputCount=1;
$("#AddMoreTextBox").click(function (e)
{
    InputCount++;
    $("#Product_Orders_TABLE").append('<tr><td class="col-8" colspan="5"> <div class="input-group input-group-sm mb-2"> <input autocomplete="off" type="text" name="arg'+ InputCount +'0" class="form-control" style="width: 12%"> <input autocomplete="off" type="text" name="arg'+ InputCount +'1" class="form-control" style="width: 12%"> <input autocomplete="off" type="text" name="arg'+ InputCount +'2" class="form-control" style="width: 12%"> <input autocomplete="off" type="text" name="arg'+ InputCount +'3" class="form-control" style="width: 52%"> <input autocomplete="off" type="text" name="arg'+ InputCount +'4" class="form-control" style="width: 12%"></div> </td></tr>');
});
$('#deleteTextBox').click(function (e) {
    $("#Product_Orders_TABLE>tr").last().remove()
})

