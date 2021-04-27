$(document).ready(function () {
    $.ajax({
        url: api_order_list,
        type: 'GET',
        data: {'min': min, 'max': max},
        success: function (res) {
            if (res.code === 0){
                if (res.data.length === 10){
                }
                for (i in res.data){
                    console.log(res.data[i])
                }
            } else {
                console.log(res.data)
            }
        }
    })
})