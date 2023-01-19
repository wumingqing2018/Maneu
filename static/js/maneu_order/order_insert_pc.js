$('#insert').click(function () {
    Product_Orders_json = $('#Product_Orders').serializeJsonStr();
    $('#Product_Orders_json').val(Product_Orders_json);
    Vision_Solutions_json = $('#Vision_Solutions').serializeJsonStr();
    $('#Vision_Solutions_json').val(Vision_Solutions_json);
    order_json = $('#order').serializeJsonStr();
    $('#order_json').val(order_json);
})
