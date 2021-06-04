$(document).ready(function () {
    glass_insert_show.click(function () {
        glass_show()
        $.ajax({
            url: api_glass_brand,
            type: 'GET',
            success: function (res) {
                if (res.code === 0) {
                    for (i in res.data) {
                        data = res.data[i]
                        glass_brand_select.append('<option value="' + data + '">' + data + '</option>')
                    }
                }
            }
        })
    });
    glass_insert_hide.click(function () {
        glass_hide()
        glass_model_select.find('option').remove()
        glass_sphere_select.find('option').remove()
        glass_astigmatic_select.find('option').remove()
        glass_refraction_select.find('option').remove()
        glass.val('')
    });
    glass_brand_select.change(function () {
        glass_model_select.find('option').remove()
        glass_sphere_select.find('option').remove()
        glass_astigmatic_select.find('option').remove()
        glass_refraction_select.find('option').remove()
        $.ajax({
            url: api_glass_model,
            type: 'GET',
            data: {'brand': glass_brand_select.val()},
            success: function (res) {
                if (res.code === 0){
                    glass_model_select.append('<option></option>')
                    for (i in res.data){
                        data = res.data[i]
                        glass_model_select.append('<option value="' + data + '">' + data + '</option>')
                    }
                }
            }
        })
    });
    glass_model_select.change(function () {
        glass_sphere_select.find('option').remove()
        glass_astigmatic_select.find('option').remove()
        glass_refraction_select.find('option').remove()
        $.ajax({
            url: api_glass_sphere,
            type: 'GET',
            data: {'brand': glass_brand_select.val(),
                'model': glass_model_select.val()},
            success: function (res) {
                glass_sphere_select.append('<option></option>')
                if (res.code === 0){
                    for (i in res.data){
                        data = res.data[i]
                        glass_sphere_select.append('<option value="' + data + '">' + data + '</option>')
                    }
                }
            }
        })
    });
    glass_sphere_select.change(function () {
        glass_astigmatic_select.find('option').remove()
        glass_refraction_select.find('option').remove()
        $.ajax({
            url: api_glass_astigmatic,
            type: 'GET',
            data: {'brand': glass_brand_select.val(),
                'model': glass_model_select.val(),
                'sphere': glass_sphere_select.val()
            },
            success: function (res) {
                if (res.code === 0){
                    glass_astigmatic_select.append('<option></option>')
                    for (i in res.data){
                        data = res.data[i]
                        glass_astigmatic_select.append('<option value="' + data + '">' + data + '</option>')
                    }
                }
            }
        })
    });
    glass_astigmatic_select.change(function () {
        glass_refraction_select.find('option').remove()
        $.ajax({
            url: api_glass_refraction,
            type: 'GET',
            data: {'brand': glass_brand_select.val(),
                'model': glass_model_select.val(),
                'sphere': glass_sphere_select.val(),
                'astigmatic': glass_astigmatic_select.val()},
            success: function (res) {
                if (res.code === 0){
                    glass_refraction_select.append('<option></option>')
                    for (i in res.data){
                        data = res.data[i]
                        glass_refraction_select.append('<option value="' + data + '">' + data + '</option>')
                    }
                }
            }
        })
    });
    glass_refraction_select.change(function () {
        $.ajax({
            url: api_glass_count,
            type: 'GET',
            data: {'brand': glass_brand_select.val(),
                'model': glass_model_select.val(),
                'sphere': glass_sphere_select.val(),
                'astigmatic': glass_astigmatic_select.val(),
                'refraction': glass_refraction_select.val()},
            success: function (res) {
                if (res.code===0){
                    store_id = res.data[0][0]
                    store_count = res.data[0][1]
                    glass.val(store_id)
                    $('#count').attr({'max':store_count})
                }
            }
        })
    });
    glass_insert_btn.click(function () {
        content = glass_insert.serializeJsonStr()
        order.push(content)
        order_content(content)
    });
    function glass_show() {
        /*
        点击添加镜片按钮执行以下操作 id = glass_insert_show
        显示添加镜片表格 id = glass_table
        显示取消添加按钮 id = glass_insert_hide
        隐藏添加镜片按钮 id = glass_insert_show
        清空品牌选择栏并填入空白值
         */
        glass_table.show()
        glass_insert_hide.show()
        glass_insert_show.hide()
        glass_brand_select.children('option').remove()
        glass_brand_select.append('<option></option>')
        // framework_insert_hide.click()
    }
    function glass_hide(){
        /*
        点击取消添加按钮
        隐藏添加镜片表格 id = glass_table
        隐藏取消添加按钮 id = glass_insert_hide
        显示添加镜片按钮 id = glass_insert_show
         */
        glass_insert_hide.hide()
        glass_insert_show.show()
        glass_table.hide()
    }
    function order_content (content){
        content = jQuery.parseJSON(content)
        console.log(content)
        html = ''
        html += '<tr class="yellow">'
        html += '<td>'+ content.product +'</td>'
        html += '<td>'+ content.brand +'</td>'
        html += '<td>'+ content.model +'</td>'
        html += '<td>'+ content.sphere +'</td>'
        html += '<td>'+ content.astigmatic +'</td>'
        html += '<td>'+ content.refraction +'</td>'
        html += '<td>'+ content.Around +'</td>'
        html += '<td>'+ content.pd +'</td>'
        html += '<td>'+ content.add +'</td>'
        html += '<td>'+ content.deviation +'</td>'
        html += '<td>'+ content.count +'</td>'
        html += '</tr>'
        $('#order_content').append(html)
    }

    $.fn.serializeJsonStr = function () {
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
        return JSON.stringify(o);
    }
})
