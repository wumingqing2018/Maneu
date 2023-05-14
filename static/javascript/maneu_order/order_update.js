$(document).ready(function () {
    $("input[name='OD_VA']").val(vision.OD_VA)
    $("input[name='OD_SPH']").val(vision.OD_SPH)
    $("input[name='OD_CYL']").val(vision.OD_CYL)
    $("input[name='OD_AX']").val(vision.OD_AX)
    $("input[name='OD_PR']").val(vision.OD_PR)
    $("input[name='OD_FR']").val(vision.OD_FR)
    $("input[name='OD_ADD']").val(vision.OD_ADD)
    $("input[name='OD_BCVA']").val(vision.OD_BCVA)
    $("input[name='OS_VA']").val(vision.OS_VA)
    $("input[name='OS_SPH']").val(vision.OS_SPH)
    $("input[name='OS_CYL']").val(vision.OS_CYL)
    $("input[name='OS_AX']").val(vision.OS_AX)
    $("input[name='OS_PR']").val(vision.OS_PR)
    $("input[name='OS_FR']").val(vision.OS_FR)
    $("input[name='OS_ADD']").val(vision.OS_ADD)
    $("input[name='OS_BCVA']").val(vision.OS_BCVA)
    $("input[name='PD']").val(vision.PD)
    $("input[name='remark']").val(vision.remark)
    $("input[name='function']").val(vision.function)

    for (StoreInput= 0; StoreInput < InputCount; StoreInput++){
        console.log('arg'+StoreInput.toString()+'0', store['arg'+StoreInput.toString()+'0'])
        $("#Product_Orders_TABLE").append(
            '    <div class="input-group input-group-sm mb-2">\n' +
            '        <input autocomplete="off" type="text" name="arg'+StoreInput.toString()+'0" class="form-control" style="width: 12%" placeholder="类别" value='+store['arg'+StoreInput.toString()+'0']+'>\n' +
            '        <input autocomplete="off" type="text" name="arg'+StoreInput.toString()+'1" class="form-control" style="width: 12%" placeholder="品牌" value='+store['arg'+StoreInput.toString()+'1']+'>\n' +
            '        <input autocomplete="off" type="text" name="arg'+StoreInput.toString()+'2" class="form-control" style="width: 12%" placeholder="型号" value='+store['arg'+StoreInput.toString()+'2']+'>\n' +
            '        <input autocomplete="off" type="text" name="arg'+StoreInput.toString()+'3" class="form-control" style="width: 52%" placeholder="参数" value='+store['arg'+StoreInput.toString()+'3']+'>\n' +
            '        <input autocomplete="off" type="text" name="arg'+StoreInput.toString()+'4" class="form-control" style="width: 12%" placeholder="价格" value='+store['arg'+StoreInput.toString()+'4']+'>\n' +
            '    </div>\n' +
            '</div>\n');
    }

    $("#AddMoreTextBox").click(function (e) {
        $("#Product_Orders_TABLE").append(
            '    <div class="input-group input-group-sm mb-2">\n' +
            '        <input autocomplete="off" type="text" name="arg'+InputCount+'0" class="form-control" style="width: 12%" placeholder="类别">\n' +
            '        <input autocomplete="off" type="text" name="arg'+InputCount+'1" class="form-control" style="width: 12%" placeholder="品牌">\n' +
            '        <input autocomplete="off" type="text" name="arg'+InputCount+'2" class="form-control" style="width: 12%" placeholder="型号">\n' +
            '        <input autocomplete="off" type="text" name="arg'+InputCount+'3" class="form-control" style="width: 52%" placeholder="参数">\n' +
            '        <input autocomplete="off" type="text" name="arg'+InputCount+'4" class="form-control" style="width: 12%" placeholder="价格">\n' +
            '    </div>\n' +
            '</div>\n');
        InputCount++;
    });
    $('#DeleteTextBox').click(function (e) {
        if (InputCount >1){
            InputCount = InputCount-1;
            $("#Product_Orders_TABLE>div").last().remove()
        }
    })
    $('#insert').click(function () {
        Product_Orders_json = $('#Product_Orders').serializeJsonStr();
        $('#Product_Orders_json').val(Product_Orders_json);
        Vision_Solutions_json = $('#Vision_Solutions').serializeJsonStr();
        $('#Vision_Solutions_json').val(Vision_Solutions_json);
        order_json = $('#order').serializeJsonStr();
        $('#order_json').val(order_json);
    })
    $('#Vision_Solutions_showbutton').click(function () {
            $('#Vision_Solutions_showbutton').attr('style', 'display: none')
            $('#Vision_Solutions_hidebutton').attr('style', 'display: block')
            $(".Vision_Solutions").attr('style', 'display: block')
        }
    )
    $('#Vision_Solutions_hidebutton').click(function () {
            $('#Vision_Solutions_hidebutton').attr('style', 'display: none');
            $('#Vision_Solutions_showbutton').attr('style', 'display: block');
            $(".Vision_Solutions").attr('style', 'display: none');
            $("#Vision_Solutions")[0].reset();
        }
    )
    $('#Store_showbutton').click(function () {
            $('#Store_showbutton').attr('style', 'display: none')
            $('#Store_hidebutton').attr('style', 'display: block')
            $(".Store").attr('style', 'display: block')
        }
    )
    $('#Store_hidebutton').click(function () {
            $('#Store_hidebutton').attr('style', 'display: none');
            $('#Store_showbutton').attr('style', 'display: block');
            $(".Store").attr('style', 'display: none');
            $("#Store")[0].reset();
        }
    )
});
