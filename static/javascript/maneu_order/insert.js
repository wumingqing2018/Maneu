$(document).ready(function () {
    $('#insert').click(function () {
        store = []
        $(".store").each(function () {
            data = {
                arg10: $(this).find("[name='arg10']").val(),
                arg11: $(this).find("[name='arg11']").val(),
                arg12: $(this).find("[name='arg12']").val(),
                arg13: $(this).find("[name='arg13']").val(),
                arg14: $(this).find("[name='arg14']").val(),
            };
            store.push(data)
        })
        $.ajax({
            url: order_api,
            method: 'GET',
            data: {
                remark: $("#remark").val(),
                time: $("#time").val(),
                name: $("#name").val(),
                call: $("#call").val(),
                guest_id: guest_id,
                vision_id: vision_id,
                store: JSON.stringify(store),
            }
        })
    });

    function store_insert(){
        store = []
        $(".store").each(function () {
            data = {
                arg10: $(this).find("[name='arg10']").val(),
                arg11: $(this).find("[name='arg11']").val(),
                arg12: $(this).find("[name='arg12']").val(),
                arg13: $(this).find("[name='arg13']").val(),
                arg14: $(this).find("[name='arg14']").val(),
            };
            store.push(data)
        })
        $.ajax({
            url: order_api,
            method: 'GET',
            data: {
                remark: $("#remark").val(),
                time: $("#time").val(),
                name: $("#name").val(),
                call: $("#call").val(),
                guest_id: guest_id,
                vision_id: vision_id,
                store: JSON.stringify(store),
            },
            success: function (res) {

            }
        })
    }

    function guest_insert() {
        $.ajax({
            url: guest_api,
            method: 'GET',
            data: {
                remark: $("#remark").val(),
                time: $("#time").val(),
                name: $("#name").val(),
                call: $("#call").val(),
                age: $("#age").val(),
                sex: $("#sex").val(),
                DFH: $("#DFH").val(),
                OT: $("#OT").val(),
                EM: $("#EM").val(),
            },
            success: function (res) {
                if (res.status === true) {
                    alert('提交成功,返回上一页')
                    window.location.href = web_index
                } else {
                    alert("提交失败" + res.message)
                }
            }
        })
    }

    function report_insert() {
        $.ajax({
            url: report_api,
            method: "GET",
            data: {
                Function: $("#function").val(),
                time: $("#time").val(),
                name: $("#name").val(),
                phone: $("#call").val(),
                remark: $("#remark").val(),
                PD: $("#PD").val(),
                OD: $("#OD").serializeJsonStr(),
                OS: $("#OS").serializeJsonStr(),
            },
            success: function (res) {
                if (res.status === true) {
                    alert("提交成功，可以继续填写")
                } else {
                    alert("提交失败，请确认数据后再次重试")
                }
            }
        })
    }


});
$('#store_add').click(function () {
    $("#store").append(
        "<div class='vertical1 col-10 row store'>\n" +
        "    <div class='col-11'>\n" +
        "        <div class='input-group input-group-sm'>\n" +
        "            <input autocomplete='off' type='text' name='arg10' class='form-control product1'\n" +
        "                   placeholder='类别'>\n" +
        "            <input autocomplete='off' type='text' name='arg11' class='form-control product1'\n" +
        "                   placeholder='品牌'>\n" +
        "            <input autocomplete='off' type='text' name='arg12' class='form-control product1'\n" +
        "                   placeholder='型号'>\n" +
        "            <input autocomplete='off' type='text' name='arg13' class='form-control product2'\n" +
        "                   placeholder='参数'>\n" +
        "            <input autocomplete='off' type='text' name='arg14' class='form-control product3'\n" +
        "                   placeholder='价格'>\n" +
        "        </div>\n" +
        "    </div>\n" +
        "    <div class='col-1'>\n" +
        "        <a class='col-1' onclick='store_remove()'>移除</a>\n" +
        "    </div>\n" +
        "</div>\n"
    )
})
function store_remove () {
    this.remove();
}
