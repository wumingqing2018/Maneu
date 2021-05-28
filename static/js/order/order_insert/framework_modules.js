/*
添加镜框相关js模块
 */
$(document).ready(function () {
    framework_insert_show.click(function () {
        framework_show()
        $.ajax({
            url: api_framework_store_brand,
            type: 'GET',
            success: function (res) {
                if (res.code === 0){
                    for (i in res.data){
                        data = res.data[i]
                        framework_brand_select.append('<option value="' + data + '">' + data + '</option>')
                    }
                }
            }
        })
    });
    framework_insert_hide.click(function () {
        framework_hide()
    });
    framework_brand_select.change(function () {
        framework_model_select.find('option').remove()
        framework_model_select.append('<option></option>')
        $.ajax({
            url: api_framework_store_model,
            type: 'GET',
            data: {'brand': framework_brand_select.val()},
            success: function (res) {
                if (res.code === 0){
                    for (i in res.data){
                        data = res.data[i]
                        framework_model_select.append('<option value="' + data + '">' + data + '</option>')
                    }
                }
            }
        })
    });
    framework_model_select.change(function () {
        $.ajax({
            url: api_framework_store_count,
            type: 'GET',
            data: {'brand': framework_brand_select.val(), 'model': framework_model_select.val()},
            success: function (res) {
                if (res.code === 0){
                    framework.val(res.data)
                }
            }
        })
    });
    framework_insert_btn.click(function () {
        framework_hide()
        order.push($('#framework_insert').serializeObject())
        console.log($('#framework_insert').serializeObject())
    });
    $.fn.serializeObject = function() {
        var o = {};
        var a = this.serializeArray();
        $.each(a, function() {
            if (o[this.name] !== undefined) {
                if (!o[this.name].push) {
                    o[this.name] = [o[this.name]];
                }
                o[this.name].push(this.value || '');
            } else {
                o[this.name] = this.value || '';
            }
        });
        return o;
    };
    function framework_show() {
        /*
        添加镜框表格 id=framework_table
        添加镜框按钮 id=framework_insert_show
        取消添加按钮 id=framework_insert_hide
        清空品牌选择栏并添加空白栏
        清空型号选择栏并添加空白栏
         */
        framework_table.show()
        framework_insert_show.hide()
        framework_insert_hide.show()
        framework_brand_select.children('option').remove()
        framework_brand_select.append('<option></option>')
        framework_model_select.children('option').remove()
        framework_model_select.append('<option></option>')
    }
    function framework_hide() {
        /*
        添加镜框表格 id=framework_table
        添加镜框按钮 id=framework_insert_show
        取消添加按钮 id=framework_insert_hide
         */
        framework_table.hide()
        framework_insert_show.show()
        framework_insert_hide.hide()
    }
})
